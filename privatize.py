import os
import shutil




class Privatize(object):
    def __init__(self):
        self.username = os.path.expanduser('~').split('/')[2]
        self.data_base = os.path.expanduser('/mnt/gz4/home/supProjectCreator_data')
        self.global_master_path = os.path.join(self.data_base, 'masters',
                                        'global', 'master_flows.xml')
        self.global_pickle_path = os.path.join(self.data_base, 'pickles',
                                        'global', 'pickle_jar')
        self.user_master_dir = os.path.join(self.data_base, 'masters',
                                            self.username)
        self.user_pickle_dir = os.path.join(self.data_base, 'pickles',
                                            self.username)


    def public_master_to_private(self):
        """method to copy the global master_flows.xml to a private one
        in a users data directory.

        input:
            self

        output:
            masters/global/master_flows.xml copied to
            masters/username/master_flows.xml

        NOTE: this should only copy the global master flow if the .xml file
        does not exist in the masters/username/ directory.
        """
        user_master_file = os.path.join(self.user_master_dir, 'master_flows.xml')
        if not os.path.exists(user_master_file):
            os.makedirs(self.user_master_dir)
            shutil.copy2(self.global_master_path, user_master_file)
        else:
            pass

    def public_pickle_to_private(self):
        """method to copy the global master_flows.xml to a private one
        in a users data directory.

        input:
            self

        output:
            pickles/global/master_flows.xml copied to
            pickles/username/master_flows.xml

        NOTE: this should only copy the global pickle jar if the file
        does not already exist in the pickles/username/ directory.
        """
        user_pickle_file = os.path.join(self.user_pickle_dir, 'pickle_jar')
        if not os.path.exists(user_pickle_file):
            os.makedirs(self.user_pickle_dir)
            shutil.copy2(self.global_pickle_path, user_pickle_file)
        else:
            pass
