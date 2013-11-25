#!/usr/bin/python

import contant
import os
import sys
import signal

def execute(args):

	"""
	The execute create a new process for the command
	Input: args (list)
	"""

	try:
		pid = os.fork()
		if pid == 0:
			signal.signal(signal.SIGINT, signal.SIG_DFL)
			signal.signal(signal.SIGINT, signal.SIG_DFL)
			try:
				os.execvp(args[0], args)
			except OSError, e:
				print "-bash: %s: command not found" %args[0]
		else:
			os.wait()[0]
	except OSError, e:
		pass
	#line = sys.stdin.readline().split()

def pysh():
	"""
	The pysh is the main function.

	Feature1: Ctr-C can kill the child process but cannot kill the parent process.
	Feature2: command like "ps;ls;pwd" can be executed.
	"""
	while True:
		signal.signal(signal.SIGINT, signal.SIG_IGN)
		signal.signal(signal.SIGQUIT, signal.SIG_IGN)
		args = []
		line = raw_input('pysh$ ').split()
		while line == []:
			line = raw_input('pysh$ ').split()

		for arg in line:
			if arg.find(';') != -1:
				arg_tmp = arg.replace(';', " ; ").split()
				for i in arg_tmp:
					args.append(i)
			else:
				args.append(arg)
		args.append(';')
		#for j in args:
		#	print j
		arg_handle = []
		for j in args:
			if j == ';':
				execute(arg_handle)
				arg_handle = []
			else:
				arg_handle.append(j)



if __name__ == '__main__':
	pysh()
