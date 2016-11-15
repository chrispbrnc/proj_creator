import os
import sys
import xml.etree.cElementTree as ET
from xml.dom import minidom




class xmlUtil(object):
    """The xml file used in this class has the following form
            <masters>
              <owner name="pmiatech">
                <key>smwt</key>
                <supName>SEIMAX MASTERS - WestTX</supName>
                <path>/mnt/gz4/seisup-beta2d/usr/SEIMAX_MASTERS/WestTX</path>
              </owner>
            </masters>
    """

    def __init__(self):
        self.master_dict = None
        self.cb_items = None
        self.tree = None
        self.user = None
        self.new_xml = None
        self.project = None

    def xml_tree(self, xml, xml_user):
        """Reads in an xml file and stores in a tree structure.

        input:
            self - instance of xmlUtil
            xml - file path to xml file

        output:
            returns the class instance self.tree
        """
        self.tree = ET.parse(xml)
        self.tree_user = ET.parse(xml_user)

    def read_xml_to_dict(self):
        """Method reads the xml file with master flow info as a tree, and
        creates a dictionary with appropriate info.

        input:
            self - instance of ProjectInfo

        output:
            self.master_dict - instance var; dictionary of master flows with
                structure {key : [SeisupArea - SeisupLine, mnt_path]}
        """
        root = self.tree.getroot()
        elem_list = []
        elem_dict = {}
        for elem in root:
            elem_list.append(list(elem))
        for elem in elem_list:
            elem_dict[elem[0].text] = [elem[1].text, elem[2].text]
        self.master_dict = elem_dict


        root2 = self.tree_user.getroot()
        elem_list2 = []
        elem_dict2 = {}
        for elem in root2:
            elem_list2.append(list(elem))
        for elem in elem_list2:
            elem_dict2[elem[0].text] = [elem[1].text, elem[2].text]
        self.master_dict_user = elem_dict2

        self.master_dict.update(self.master_dict_user)



    def read_project(self, li_xml):
        """method to get the SPOS project name from LineInfo.xml

        input:
            self - instance of xmlUtil
            li_xml - str; path to the LineInfo.xml file (project dependant)

        output:
            self.project - str; class instance variable of the project name
        """
        li_tree = ET.parse(li_xml)
        li_root = li_tree.getroot()
        for child in li_root.iter():
            if child.tag == 'PROJECT':
                self.project = child.text.strip()

    def get_user(self):
        """Method to get the username from their home directory path
        """
        user_path = os.path.expanduser('~')
        self.user = user_path.split('/')[2]

    def indent(self, elem, level=0):
        """Method to nicely indent xml tags for xml file to be written
        """
        i = "\n" + level*"  "
        j = "\n" + (level-1)*"  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                self.indent(subelem, level+1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = j
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = j
        return elem

    def add_master_xml(self, key, area, line):
        """Method to add new xml data to an existing xml file.

        input:
            self - instance of xmlUtil
            key - str; presumably 4 letter key for users master flow
            area - str; SeisUp area for a users master flow
            line - str; SeisUp line name for a users master flow

        output:
            new_xml - class instance for an xml data object with new data
        """
        base_path = os.path.expanduser('/mnt/gz4/seisup-beta2d/usr')
        root = self.tree.getroot()
        owner = ET.Element('owner')
        if area == 'SEIMAX MASTERS':
            owner.set('name', 'pmiatech')
        else:
            owner.set('name', self.user)
        root.append(owner)
        m_key = ET.SubElement(owner, 'key')
        m_key.text = key
        supname = ET.SubElement(owner, 'supName')
        supname.text = area + ' - ' + line
        path = ET.SubElement(owner, 'path')
        path.text = os.path.join(base_path, area.replace(" ", "_"),
            line.replace(" ", "_"))
        self.indent(root, level=1)
        self.new_xml = ET.tostring(root)

    def write_xml(self, xml):
        """Method to write out new xml data to an existing xml file.

        input:
            self - instance of xmlUtil
            xml - file path to xml file

        output:
            xml - file being overwritten with new xml data

        NOTE: This will simply overwrite line-by-line an existing xml file
        with both existing and new xml data. This should be fine for such a
        small xml file, but if the xml file ever grows to be quite large, then
        we should change this to only append new data to the file.
        """
        with open (xml, 'w') as f:
            f.write(self.new_xml)
