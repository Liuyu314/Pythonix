# Author:  UesrName
# Email:  UesrEmail
# Time: 2013,09,08 13:31:22
# Description:
# Version:
# Option:

import os
import sys

def do_wc(filename, opt_lines, opt_words, opt_types):
	if not os.path.exists(filename):
		print "wc: %s: open: No such file or directroy"
	else:
		lines = 0
		words = 0
		types = 0
		f = open(filename, 'r')
		while True:
			cnt = f.readline()
			if len(cnt) == 0:
				break
			if opt_lines == 1:
				lines += + 1
			if opt_types == 1:
				types += len(cnt)
			if opt_words == 1:
				tmp = cnt.split(' ')
				words += len(tmp)

		if opt_lines == 1:
			print "%8d" %lines,
		if opt_words == 1:
			print "%7d" %words,
		if opt_types == 1:
			print "%7d" %types,
		print filename
		
		return lines, words, types
				
if len(sys.argv) == 1:
	print "Missing file"
else:
	opt_words = 0
	opt_types = 0
	opt_lines = 0
	location = 0
	for i in sys.argv[1:]:
		if i.startswith('--'):
			if i[2:] == "help":
				print "Usage: wc [-lcw] [file...]"
				sys.exit()
			else:
				print "wc: illegal option -- -"
				sys.exit()
		elif i.startswith('-'):
			location = location + 1
			for opt in i[1:]:
				if opt == 'w':
					opt_words = 1
				elif opt == 'c':
					opt_types = 1
				elif opt == 'l':
					opt_lines = 1
				else:
					print "wc: illegal option -- -%c" %opt
		else:	
			lines_total = 0
			types_total = 0
			words_total = 0
			file_num = 0
			break
	if location == len(sys.argv):
		print "Missiong files"
		sys.exit()
	if location == 0:
		opt_lines = 1
		opt_words = 1
		opt_types = 1
	for i in sys.argv[location + 1:]:
		file_num += 1
		re_wc = do_wc(i, opt_lines, opt_words, opt_types)
		print re_wc[0], re_wc[1], re_wc[2]
		lines_total += re_wc[0]
		words_total += re_wc[1]
		types_total += re_wc[2]
	if file_num == 1:
		sys.exit()
	else:
		if opt_lines == 1:
			print "%8d" %lines_total,
		if opt_words == 1:
			print "%8d" %words_total,
		if opt_types == 1:
			print "%8d" %types_total,
		print "      total" 
