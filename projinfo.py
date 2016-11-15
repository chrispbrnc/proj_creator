import os
import sys
import xml.etree.cElementTree as ET
from glob import glob
from xmlutil import xmlUtil



class ProjectInfo(xmlUtil):
    """This class defines methods intended to get user input of
    key information about new projects that will be used in the
    copying and linking of files for the new project creation.
    """

    def __init__(self):
        self.uid = ""
        self.job_num = ""
        self.line_num = ""
        self.area = ""
        self.master = ""
        self.mnt_path = ""
        self.d1_path = ""
        xu = xmlUtil()
        self.master_dict = xu.master_dict

    def __str__(self):
        return ("UID: %s, Job Number: %s, Line Number: %s, Area: %s, \
            Master Flow: %s, mnt Path: %s, d1 Path: %s ") % (str(self.uid),
            str(self.job_num), str(self.line_num), str(self.area), str(self.master),
            str(self.mnt_path), str(self.d1_path))

    def __repr__(self):
        return str(self)

    def get_ids(self):
        """
        Method to get raw input regarding new project ID numbers
        and names.

        input:
            self - ProjectInfo instance

        output:
            # removed from output: self.uid - str; UID number
            self.job_num - str; Job number
            self.line_num - str; Line number
            self.area = area - str; area
        """
        while True:
            #uid = raw_input('What is the UID?       ')
            job_num = raw_input('What is the Job Number?        ')
            line_num = raw_input('What is the line number?  ')
            area = job_num.split('-')[0]
            if job_num == "" or line_num == "":     # uid == "" or
                print "\nOops, you missed one! Let's try this again.    "
            else:
                break
        #self.uid = uid
        self.job_num = job_num
        self.line_num = line_num.upper() # user can input lower or uppercase
        self.area = area

    def mnt_project_path(self, mnt_base):
        """This method should output a string path in the /mnt/gz4 directory
        to the new project being created

        input:
            self - ProjectInfo instance
            area - str; line area
            line_num - str; line number (case insensitive)

        output:
            self.mnt_path - str; mnt directory path to new project
        """
        mnt_base = os.path.expanduser(mnt_base)
        self.mnt_path = os.path.join(mnt_base, self.area, self.line_num.upper())

    def d1_project_path(self, d1_base):
        """This method should output a string path in jobs directory of the
        /d1 directory.

        input:
            self - ProjectInfo instance
            area - str; line area
            job_num - str; job number

        output:
            self.d1_path - str; d1 directory path to project's jobs directory
        """
        d1_base = os.path.expanduser(d1_base)
        #self.d1_path = os.path.join(d1_base, self.area, self.job_num + '_' +
        #    self.line_num.lower() + '__' + self.uid)
        d1_path_list = glob(os.path.join(d1_base, self.area, self.job_num +
            '_' + self.line_num.lower() + '*'))
        if d1_path_list == []:
            self.d1_path = ""
            self.uid = ""
        else:
            self.d1_path = d1_path_list[0]
            self.uid = self.d1_path.split('__')[1]

    # def xml_master(self, xml):
    #     """Method reads the xml file with master flow info as a tree, and
    #     creates a dictionary with appropriate info.
    #
    #     input:
    #         self - instance of ProjectInfo
    #         xml - file path to xml file
    #
    #     output:
    #         self.master_dict - instance var; dictionary of master flows with
    #             structure {key : [SeisupArea - SeisupLine, mnt_path]}
    #     """
    #     tree = ET.parse(xml)
    #     root = tree.getroot()
    #     elem_list = []
    #     elem_dict = {}
    #     for elem in root:
    #         elem_list.append(list(elem))
    #     for elem in elem_list:
    #         elem_dict[elem[0].text] = [elem[1].text, elem[2].text]
    #     self.master_dict = elem_dict

    def master_list_for_combobox(self):
        """This method prepares a list of items to place into the combobox
        on the gui.

        input:
            self - instance of ProjectInfo

        output:
            cb_items - list of strings for the combobox
        """
        cb_list = []
        for key, value in self.master_dict.iteritems():
            cb_list.append(key + ' : ' + value[0])
        self.cb_items = cb_list

    def get_master(self):
        """Method to get the master flow to be used as input from the,
        and output the path to the master flow.

        input:
            self - ProjectInfo instance

        output:
            self.master - str; path to the master flow

        TODO:
            1. (DONE) create XML file with master flows and read them into
            this function.
            2. if user inputs a master flow that doesnt exist in the XML
            file, give option for user to add the master flow.
            3. once the XML master file is complete, change the for loop
            to a switch case.
        """
        print '\n Master flows available:   '
        print 'Enter the key for the master flow would you like to copy? \n'
        print 'KEY \t MASTER FLOW'
        for key, value in self.master_dict.iteritems():
            print key, '\t', value[0]
        while True:
            master_flow = raw_input('\n')
            if master_flow not in self.master_dict.keys():
                print '\nKey not found, please try again. '
            else:
                break
        self.master = os.path.expanduser(self.master_dict.get(master_flow)[1])
