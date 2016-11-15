import os
import cPickle as pickle
from projinfo import ProjectInfo
from xmlutil import xmlUtil




class PickleUtil(xmlUtil):

    def __init__(self, master_flows, pickle_jar):
        self.master_flows = master_flows
        self.pickle_jar = pickle_jar
        self.cb_items = None
        self.xu = xmlUtil()
        self.xu.xml_tree(master_flows)
        self.xu.read_xml_to_dict()
        self.master_dict = self.xu.master_dict

    def master_list_for_combobox(self):
        """This method prepares a list of items to place into the combobox
        on the gui.

        input:
            self - instance of ProjectInfo

        output:
            cb_items - list of strings for the combobox
        """
        self.cb_items = []
        for key, value in self.master_dict.iteritems():
            self.cb_items.append(key + ': ' + value[0])

    def pickle_dump(self):
        """Method to dump combobox list and master flow dictionary to the
        pickle jar.

        input:
            self - instance of PickleUtil
            #xml - str; path to xml file

        ouput:
            dumped objects to pickle_jar
        """
        self.master_list_for_combobox()
        with open(self.pickle_jar, 'wb') as f:
            pickle.dump(self.cb_items, f)
            pickle.dump(self.master_dict, f)

if __name__ == '__main__':
    # these are the global masters and pickles NOT LOCAL USERS
    data_base = '/mnt/gz4/home/supProjectCreator_data'
    master_flows = os.path.join(data_base, 'masters', 'global', 'master_flows.xml')
    pickle_jar = os.path.join(data_base, 'pickles', 'global', 'pickle_jar')
    #master_flows = '/mnt/gz4/home/supProjectCreator_data/master_flows.xml'
    #pickle_jar = '/mnt/gz4/home/supProjectCreator_data/pickle_jar'
    pu = PickleUtil(master_flows, pickle_jar)
    pu.master_list_for_combobox()
    cb_items = pu.cb_items
    pu.pickle_dump()

    # with open(pickle_jar, 'rb') as g:
    #     cb = pickle.load(g)
    #     msd = pickle.load(g)
    #
    # print cb
    # print 'sorted cb ==  ', sorted(cb)
    # print msd
