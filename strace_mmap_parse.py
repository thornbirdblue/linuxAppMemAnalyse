#!/usr/bin/env python

import sys,re
import pandas as pd

file_name=''

threads=0

strace_reg='strace: Process \d+ attached with (\d+) threads'

pid_reg='\[pid\s+(\d+)\]'
time_reg='\d{2}:\d{2}:\d{2}.\d{6}'
mmap_reg='mmap\(\S+, (\d+),'

mmap=dict()

def mmap_parse(l):
	r=re.match(pid_reg,l)
	if r!=None:
		pid=r.group(1)

		r=re.search(time_reg,l)
		if r!=None:
			time=r.group(0)

		r=re.search(mmap_reg,l)
		if r!=None:
			mmap_len =r.group(1)
			
			if pid in mmap:
				mmap[pid]+=int(mmap_len)
			else:
				mmap[pid]=int(mmap_len)

def parse_file(fh):
	while 1:
		line=fh.readline()

		if not line:
			break
		
		mmap_parse(line)

	fh.close()		
	print("Finish Parse File!!!")

	df=pd.DataFrame.from_dict(mmap.orient='index').T
	print(df)
	df.to_excel("parse.xlsx",index=False)
	print(df.apply(lambda x:x.sum(),axis=1))

def get_file_handle(f_name):
	f=open(f_name,'r')
	line=fh.readline()
	if not line:
		print("!!!Error!!! File is NULL!")
		sys.exit(0)

	r=re.match(strace_reg,line)
	if r!=None:
		threads=r.group(1)
		print("Threads: "+str(threads))
		return f	

if __name__ == '__main__':
	if sys.argv[1]:
		parse_file=sys.argv[1]

	print("Parse file: "+parse_file)
	f_handle = get_file_handle(parse_file)

	parse_file(f_handle)
	
