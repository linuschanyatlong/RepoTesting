// CopyRight Notice @1234
import os, sys

count = 0
unclassified = 0
yearinput = input('Year of CopyRight notice: ')
path = '/Users/connectar/Desktop/RepoTesting' 
dirs = os.listdir( path )
print('dirs: ' + str(dirs))
for i in range (0,len(dirs)):
	sfile = str(dirs[i]).split('.')[ -1 ]
	print('sfile: ' + str(sfile))
	if sfile == 'c':	#class CStyle()
		os.chdir(path)
		src=open(dirs[i],"r")