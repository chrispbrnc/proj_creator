import os
import glob
import shutil



def copy_master_files_to_line(master, area, line):
    """
    input:
        master - string output by get_master
        area - string output by get_ids()
        line - string output by get_ids()
    """
    usr_path = os.path.expanduser('/mnt/gz4/seisup-beta2d/usr')
    line_path = os.path.join(usr_path, area, line)
    mstr = os.path.expanduser(master)
    print 'copying master flow to %s ' % line_path
    print "master is %s     " % mstr
    #shutil.copytree(mstr, line_path)
    for file_name in os.listdir(mstr):
        file_name_full = os.path.expanduser(os.path.join(mstr, file_name))
        if os.path.isdir(file_name_full):
            print "copying directory %s to %s  " % (file_name_full, line)
            shutil.copytree(file_name_full, os.path.join(line_path, file_name))
        else:
            print "copying file %s to %s  " % (file_name, line)
            shutil.copy2(file_name_full, line_path)

def link_fieldsegy_to_fieldqc(area, job_number, line_name, uid):
    """
    make this symlink to a field_qc file instead of copy it.
    fix to make safer, and generic for whatever master is being used
    now it only works for master flow crwt
    """
    field_segy = 'field.SEGY'
    base4sgy = os.path.expanduser('/d1/gc/jobs/')
    mnt_base = os.path.expanduser('/mnt/gz4/seisup-beta2d/usr/')
    mnt_line = os.path.join(mnt_base, area, line_name)
    mnt_field_segy = os.path.join(mnt_line, field_segy)
    area_path = os.path.join(base4sgy, area)
    line_path = glob.glob(area_path + '/*' + uid)[0]
    # now find the field_qc file(s)
    field_qc_files = []
    for file_name in glob.glob(line_path + '/*field_qc*.sgy'):
        field_qc_files.append(file_name)
    num_field_qc_files = len(field_qc_files)
    print "%i field_qc files \n " % num_field_qc_files
    # check for any .SEGY files and rm them
    for SEGY_files in os.listdir(mnt_line):
        SEGY_files = os.path.join(mnt_line, SEGY_files)
        if SEGY_files.endswith('.SEGY'):
            os.remove(SEGY_files)
    # now link the field_qc files to field.SEGYlink_fieldsegy_to_fieldqc(area, job_number, line_name, uid)
    file_num = 1    # assuming indexing started at 0
    for files in field_qc_files:
        if field_qc_files[0]:
            print "symlinking %s \t --> \t %s/field.SEGY" %  (files, mnt_line)
            os.symlink(files, mnt_field_segy)
        else:
            print "symlinking %s to %sfield.SEGY" %  (files, mnt_line)
            os.symlink(files, mnt_line + "field%i.SEGY" % file_num)
            os.copy2(mnt_line + "field.SEGY.dsk", mnt_line + "field%i.SEGY.dsk" % file_num)
            file_num += 1