import os
import glob
import shutil

from projinfo import ProjectInfo
from xmlutil import xmlUtil




class FileUtil(ProjectInfo, xmlUtil):
    """
    A class of functions used for finding files, copying to target directories, and
    linking SEGY files.
    """


    def __init__(self, job_num, line_name, area,
        src_path, target_path, target_home, master):
        #self.uid = uid removed dependency on uid
        self.job_num = job_num
        self.line_name = line_name
        self.area = area
        self.src_path = src_path
        self.target_path = target_path
        self.target_home = target_home
        self.master = master

    def __str__(self):
        return (ProjectInfo.__str__() + "Src Path: %s, Target Path: %s, \
            Target home: %s, Master: %s ") % (str(src_path), str(target_path),
            str(target_home), str(master))

    def __repr__(self):
        return str(self)

    def copy_master(self, master, target_path):
        """use shutil.copytree() this will check if dir exists.
        if dir exists, this wont work.
        if dir does not exist, then everything will be copied from src to dst
        """
        print "master is %s     " % master
        print 'copying master flow to %s ' % target_path
        try:
            shutil.copytree(master, target_path, symlinks=True)
        # directories are the same
        except shutil.Error as err:
            print 'Master flow not copied. Error: %s ' % err
        # any other error saying that the directory doesnt exist
        except OSError as err:
            print 'Master flow not copied. Error: %s ' % err

    def create_new_project(self):
        """simply calls copy_master(), where copy_master() will create the
        new project directory with copytree().

        input:
            copy_master_function - a call to copy_master()

        output:
            creation of new project directory with master flow files copied in

        NOTE:
            1. This could have been implemented in one function, say make_new_proj(),
            which could have used shutil.copytree(). We chose to split into two
            functions copy_master() and create_new_project() to improve
            readability of the code.
            2. This function is replacing newproj.py
        """
        self.copy_master(self.master, self.target_path)

    def find_files(self, file_str):
        """function to find certain files within a directory, and place them
        in a list with their absolute paths.

        input:
            self - instance of FileUtil
            file_str - str; name or partial name of files to search for.
                    Will search with a regular expression, any filename
                    with a string matching files.

        output:
            files_found - list; containing the absolute path of the files found
            n_files - int; number of files found
        """
        files_found = []
        for files in glob.glob(self.src_path + '/*' + file_str + '*'):
            files_found.append(files)
        n_files = len(files_found)
        print "%i \t field_qc files found" % n_files
        return files_found, n_files

    def link_fieldsegy_to_fieldqc(self, n_files, src_files, target_segy, target_dsk):
        """this function should link field.SEGY disks in the SeisUp project
        to the appropriate field_qc.sgy files in the /d1 database.

        input:
            self - instance of FileUtil
            n_files - int; number of .sgy files to be linked
            src_files - list of strings; points to the source files to be linked to
            target_segy - str; target field.SEGY file
            target_dsk -  str; target field.SEGY.dsk

        output:
            builds a symbolic link from the src_file to the target_file
        """
        # first we remove any .SEGY files from the SeisUp project so that
        #   our symlink can target a new .SEGY file.
        for SEGY_files in os.listdir(self.target_path):
            SEGY_files = os.path.join(self.target_path, SEGY_files)
            if SEGY_files.endswith('SEGY'):
                os.remove(SEGY_files)
        # now create the sym link for each of the src_files a.k.a. field_qc files
        target_segy_files = []
        if n_files == 1:
            print "symlinking %s \t --> \t %s " % (src_files[0], target_segy)
            os.symlink(src_files[0], target_segy)
            target_segy_files.append(target_segy)
        elif n_files > 1:
            # link first file as field.SEGY
            print "symlinking %s \t --> \t %s " % (src_files[0], target_segy)
            os.symlink(src_files[0], target_segy)
            target_segy_files.append(target_segy)
            # link other files as field#.SEGY starting with index 1 in src_files
            n = 1
            for SEGY_files in src_files[1:]:
                target_segy = os.path.join(self.target_path, "field%i.SEGY" % n)
                #target_dsk_new = os.path.join(self.target_path, "field%i.SEGY.dsk" % n)
                print "symlinking %s \t --> \t %s.SEGY " % (src_files[n], target_segy)
                # shutil.copy2(target_dsk, target_dsk_new)
                os.symlink(src_files[n], target_segy)
                target_segy_files.append(target_segy)
                n += 1
        linked_files = target_segy_files
        return linked_files

    def station_to_home(self):
        """This function copies the station.prn file from a projects
        d1 jobs directory to the users mnt home directory so that
        the file will be in the defaulted directory for the
        import matrix dialog in SeisUp.

        input:
            self - instance of FileUtil

        output:
            an overwritten copy of station.prn in the users /mnt/home directory.
        """
        # deal with station.prn first
        sta = os.path.join(self.src_path, 'station.prn')
        shutil.copy2(sta, self.target_home)
        print '\nstation.prn copied to your \'mnt\' home directory '
        #now handle the allstations case
        allsta_list = glob.glob(os.path.join(self.src_path, '*allstation*.sp1'))
        if allsta_list:
            for files in allsta_list:
                old = files.split('/')[-1]
                new = 'AllStation.sp1'
                shutil.copy2(files, os.path.join(self.target_home, new))
            print '\nAllStations.sp1 copied to your \'mnt\' home directory '

    def copy_area_DB(self, area_path, line_info_xml):
        """method to copy a SeisUp non-existant areas DB into the areas
        SeisUp directory when the new area is created.

        input:
            self - instance of FileUtil
            area_path - str; path to area being created.
            line_info_xml - str; path to the LineInfo.xml file for a project

        output: appropriate DB copied into newly created area.

        NOTE: this function should be called after 'self.create_new_project'
        which makes intermediate directories (including SeisUp non-existant areas)
        while creating a new project.
        """
        DB_path = '/mnt/gz4/home/supProjectCreator_data/usr/area_DBs/'
        xu = xmlUtil()
        xu.read_project(line_info_xml)
        project = xu.project
        project = project.replace(' ', '_')
        print 'Copying area DB for %s to newly created area %s' % (project, self.area)
        shutil.copy2(DB_path + project, area_path + '/DB')

    def openKMZ(self):

        googEarth = glob.glob(os.path.join(self.src_path, '*.kmz'))[0]
        googEarth = os.path.abspath(googEarth)
        os.system('open %s' % googEarth)
        os.system('open /mnt/gz4/home/supProjectCreator_data/arkomaVEL.kmz')

    def flatIrons(self):
        os.system('bash  ~/FlatIrons.command')
