import os
import sys

def showList(curPath):
	step = 0
	for i in os.listdir(curPath):
		if step == 8:
			print 
			step = 0
		else:
			print "%-15s" %i,
			step = step + 1





if len(sys.argv) == 1:
	curPath = os.getcwd()
	showList(curPath)
else:
	curPath = sys.argv[1]
	showList(curPath)

