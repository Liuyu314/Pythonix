# Author: Liuyu
# Email: yuliu314@gmail.com
# Description: 'ls' unix command
# Version: 1.0
# Time: 2013,9,1 23:36
# Option: Unfinished function: Output format, ls -a, ls -l

import os
import sys

def showList(curPath, showHide = 0):
	step = 0
	for i in os.listdir(curPath):
		print "%-15s" %i,

if len(sys.argv) == 1:
	curPath = os.getcwd()
	showList(curPath)
elif sys.argv[1].startswith('-'):
	option = sys.argv[1][1:]
	if option == 'a':
		showHide = 1
	if option == 'help':
		print "usage: ls [-a] [file...]"
		sys.exit()
else:
	curPath = sys.argv[1]
	showList(curPath)
