import os
import sys

def create_new_line_dir(area, line_name):
    """
    input:
        area - string output by get_ids()
        line_name - string output by get_ids()
    """
    # check if area exists
    usr_path = os.path.expanduser('/mnt/gz4/seisup-beta2d/usr/')
    area_path = os.path.join(usr_path, area)
    line_path = os.path.join(area_path, line_name)
    if not os.path.exists(area_path):
        try:
            print 'The area %s doesn\'t exist. ' % area
            print ' Would you like to create it here? '
            print '(yes/no)'
            mkdir_choice = raw_input()
            if mkdir_choice == 'y' or 'yes':
                print '\Creating new area # %s ' % area
                # mkdir is probably safer than makedirs
                os.mkdir(area_path)
            elif mkdir_choice == 'n' or  'no':
                sys.exit('Maybe you should create the area with SeisUP.')
        except OSError as exc:  # guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    # now check if line number exists, if not then create it
    if not os.path.exists(line_path):
        try:
            print '\n Creating new line # %s ' % line_name
            os.mkdir(line_path)
        except OSError as exc:  #guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    return line_path