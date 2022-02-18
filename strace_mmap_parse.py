#!/usr/bin/env python

import sys,re

parse_file=''

pid=0
threads=0

strace_reg='strace: Process (\d+) attached with (\d+) threads'
mmap_reg='mmap(\S+, (\d+),'

def mmap_parse(l):
	print(l)

def parse_file(fh):
	while 1:
		line=fh.readline()

		if not line:
			break
		
		mmap_parse(line)

	close(fh)		
	print("Finish Parse File!!!")

def get_file_handle(f_name):
	with open(f_name,'r') as f:
		line=fh.readline()
		if not line:
			print("!!!Error!!! File is NULL!")
			sys.exit(0)

		pid,threads=re.match(strace_reg,line)
		print("Threads: "+str(threads))
		return f	

if __name__ == '__main__':
	if sys.argv[1]:
		parse_file=sys.argv[1]

	print("Parse file: "+parse_file)
	f_handle = get_file_handle(parse_file)

	parse_file(f_handle)
	
