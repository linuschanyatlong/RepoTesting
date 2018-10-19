import os, sys

count = 0
unclassified = 0
yearinput = input('Year of CopyRight notice: ')
path = '/Users/connectar/Desktop/Fablead' 
dirs = os.listdir( path )
for i in range (0,len(dirs)):
	sfile = str(dirs[i]).split('.')[ -1 ]
	os.chdir(path)
	if sfile == 'c':	#class CStyle()
		src=open(dirs[i],"r")
		fline="// Copyright Notce @	"  + str(yearinput) + "\n" #Prepending string
		oline=src.readlines() #Here, we prepend the string we want to on first line
		oline.insert(0,fline)
		src.close()
		src=open(dirs[i],"w")  #We again open the file in WRITE mode 
		src.writelines(oline)
		src.close()
		count += 1
	elif sfile == 'java':
		src=open(dirs[i],"r")
		fline="//java testing CopyRight Notice @" + str(yearinput) + "\n"  #Prepending string
		oline=src.readlines() #Here, we prepend the string we want to on first line
		oline.insert(0,fline)
		src.close()
		src=open(dirs[i],"w")  #We again open the file in WRITE mode 
		src.writelines(oline)
		src.close()
		count += 1
	elif sfile == 'py':
		src=open(dirs[i],"r")
		fline="#py testing CopyRight Notice @ " + str(yearinput) + "\n"  #Prepending string
		oline=src.readlines() #Here, we prepend the string we want to on first line
		oline.insert(0,fline)
		src.close()
		src=open(dirs[i],"w")  #We again open the file in WRITE mode 
		src.writelines(oline)
		src.close()
		count += 1
	elif sfile == 'txt':
		src=open(dirs[i],"r")
		fline="<<This is copyright notice @" + str(yearinput) + ">> \n"   #Prepending string
		oline=src.readlines() #Here, we prepend the string we want to on first line
		oline.insert(0,fline)
		src.close()
		src=open(dirs[i],"w")  #We again open the file in WRITE mode 
		src.writelines(oline)
		src.close()
		count += 1
	else:
		unclassified += 1
sumcu = count + unclassified
print('Total files in folder: ' + str(len(dirs)))
print('Classified: ' + str(count))
print('Unclassified: ' + str(unclassified))
print('Sum of Classified and Unclassified: ' + str(sumcu))