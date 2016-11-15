import os

from projinfo import ProjectInfo




class Checker(ProjectInfo):
    def __init__(self, ProjectInfo):
        self.mnt_path = ProjectInfo.mnt_path
        self.d1_path = ProjectInfo.d1_path
        self.area = ProjectInfo.area
        self.job_num = ProjectInfo.job_num
        self.line_num = ProjectInfo.line_num
        #self.uid = ProjectInfo.uid     removed dependency on uid

    def mnt_check_area(self, mnt_base):
        """Method to check whether the area's directory has been created in
        SeisUP yet.

        input:
            self - ProjectInfo instance

        output:
            boolean - True if area is found
        """
        return os.path.isdir(os.path.join(mnt_base, self.area))

    def mnt_check_line_name(self):
        """Method to check whether the line number entered has been created already

        input:
            self - ProjectInfo instance

        output:
            boolean - True if line number is found
        """
        return os.path.isdir(self.mnt_path)

    def d1_check_path(self):
        """Method to check if the directory pointed to by d1_project_path exists

        input:
            self - instance of ProjectInfo

        output:
            boolean - True if the d1_path is a directory
        """
        return os.path.isdir(self.d1_path)

    def d1_check_area(self, d1_base):
        """Method to check whether the area's directory has been created in
        SeisUP yet.

        input:
            self - ProjectInfo instance

        output:
            boolean - True if area is found
        """
        return os.path.isdir(os.path.join(d1_base, self.area))

    def d1_check_job_num(self, d1_base):
        """Method to check whether the job number entered exists in the /d1 directory

        input:
            self - ProjectInfo instance

        output:
            boolean - True if job number is found
        """
        area_path = os.path.join(d1_base, self.area)
        job_num_str = self.job_num
        if any(x.startswith(job_num_str) for x in os.listdir(area_path)):
            return True
        else:
            return False

    def d1_check_line_num(self, d1_base):
        """Method to check whether the line number entered exists in the /d1 directory

        input:
            self - ProjectInfo instance

        output:
            boolean - True if line number is found
        """
        area_path = os.path.join(d1_base, self.area)
        line_str = self.line_num.lower()
        if any(line_str in x for x in os.listdir(area_path)):
            return True
        else:
            return False

    def d1_check_uid(self, d1_base):
        """Method to check whether the uid number entered was found in the
        /d1 directory. This has same affect as check_line_name.

        input:
            self - ProjectInfo instance

        output:
            boolean - True if uid number is found
        """
        area_path = os.path.join(d1_base, self.area)
        uid_str = self.uid
        if any(x.endswith(uid_str) for x in os.listdir(area_path)):
            return True
        else:
            return False
