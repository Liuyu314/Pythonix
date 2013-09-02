# Author: Liuyu
# Email: yuliu314@gmail.com
# Description: 'cat' unix command
# Version: 1.0
# Time: 2013,9,2 8:43
# Option: Default:cat
#         cat -n file.txt #show line number
#         cat file.txt

import sys
import os

def showContent(f, option):
	n = 1;
	while True:
		line = f.readline()
		if len(line) == 0:
			break
		if option == 'n':
			print "%6d" %n,
			n = n + 1
		print " %s" %line,

option = None
if len(sys.argv) == 1:
	while True:
		line = raw_input()
		print line
else:
	for i in sys.argv[1:]:
		if i.startswith('-'):
			option = i[1:]
		else:
			if not os.path.exists(i):
				print "cat: %s: No such file or directory" %i
				sys.exit()
			f = file(i, 'r')
			break
	showContent(f, option)
	f.close
