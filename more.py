# Author: Liuyu
# Email: yuliu314@gmail.com
# Description: 'more' unix command
# Version: 1.0
# Time: 2013,9,2 20:30
# Option: The reason I add "<&2" after "stty ..." is to redirect stdin 
#	   	  to stdout, it can solve the problem "stty: stdin isn't a terminal"

import os
import sys

def see_more(f):
	while True:
		os.system("stty -icanon <&2") # input a character without enter
		c = f.read(1)
		os.system("stty icanon <&2")
		if c == 'q':
			return 0
		elif c == ' ':
			return 24
		else:
			return 1

def do_more(filename):
	std = 0
	f_tty = file("/dev/tty", 'r')
	if f_tty == None:
		sys.exit()
	if filename == "std":
		std = 1
	else:
		f = file(filename, 'r')
		os.system("stty -echo <&2") # input a character without echo
	numLines = 0
	while True:
		if std == 1:
			line = sys.stdin.readline()
		else:
			line = f.readline()
		if numLines == 24:
			reply = see_more(f_tty)
			if reply == 0:
				os.system("stty echo <&2")
				break
			numLines = numLines - reply
		if len(line) == 0:
			os.system("stty echo <&2")
			break
		numLines = numLines + 1
		print line,
	if std == 0:
		f.close()

if len(sys.argv) == 1:
	try:
		do_more("std")
	finally:
		os.system("stty echo <&2")
		os.system("stty icanon <&2")
elif sys.argv[1].startswith('-'):
	option = sys.argv[1][1:]
	if option == 'help':
		print "Usage: more [file...]"
else:
	if not os.path.exists(sys.argv[1]):
		print "%s: No such file or directory" %sys.argv[1]
	else:
		try:
			do_more(sys.argv[1])
		finally:
			os.system("stty echo <&2")
			os.system("stty icanon <&2")
