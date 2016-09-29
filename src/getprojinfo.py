import sys

"""
authors:
    Chris Branca
    Cory Robinson
"""

def get_ids():
	uidNum = raw_input('What is the UID?   ')
	jobNum = raw_input('What is the Job number?   ')
	lineNum = raw_input('What is the line number?  ')
	area = jobNum.split('-')[0]
	return uidNum, jobNum, lineNum, area

def get_master():
    """
    output:
        string of directory path to master flow to use
    """
    masters = {'smwt' : ['SEIMAX MASTERS - WestTX',
    '/mnt/gz4/seisup-beta2d/usr/SEIMAX\ MASTERS/WestTX'],
    'crwt' : ['cRob - westTexas', '/mnt/gz4/seisup-beta2d/usr/cRob/westTexas'],
    'cbm' : ['cbranca master', '/mnt/gz4/seisup-beta2d/usr/example/cbr']}
    print '\n Master flows available:	'
    print 'Enter the key for the master flow would you like to copy? \n'
    print 'KEY \t MASTER FLOW'
    for key, value in masters.iteritems():
        print key, '\t', value[0]
    master_flow = raw_input()
    if master_flow in masters.keys():
        print 'got it!'
    else:
        print
        print 'Key not found, please try again. '
        master_flow_again = raw_input()
        if master_flow_again in masters:
            master_flow = master_flow_again
            print 'got it!'
        else:
            sys.exit('Master flow not recognized. Aborting.')
    return masters.get(master_flow)[1]