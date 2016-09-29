import getprojinfo as gpinfo 
import newproj as npj 
import copyandlink as cnl 

if __name__ == "__main__":
	uidNum, jobNum, lineNum, area = gpinfo.get_ids()
	master = gpinfo.get_master()
	new_line = npj.create_new_line_dir(area, lineNum)
	copy_master = cnl.copy_master_files_to_line(master, area, lineNum)
	link = cnl.link_fieldsegy_to_fieldqc(area, jobNum, lineNum, uidNum)