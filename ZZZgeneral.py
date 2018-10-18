import os, sys

# Open a file
#path = "RepoTesting"
yearinput=input('Year of CopyRight notice: ')
dirs = os.listdir()
for i in range (0,len(dirs)-1):
	sfile = str(dirs[i]).split('.')[ -1 ]
	#print(sfile)
	if sfile == 'c':
		#class CStyle()
		src=open(dirs[i],"r")
		fline="#c language testing \n"    #Prepending string
		oline=src.readlines() #Here, we prepend the string we want to on first line
		oline.insert(0,fline)
		src.close()
		src=open(dirs[i],"w")  #We again open the file in WRITE mode 
		src.writelines(oline)
		src.close()
	elif sfile == 'java':
		src=open(dirs[i],"r")
		fline="//java testing \n"    #Prepending string
		oline=src.readlines() #Here, we prepend the string we want to on first line
		oline.insert(0,fline)
		src.close()
		src=open(dirs[i],"w")  #We again open the file in WRITE mode 
		src.writelines(oline)
		src.close()
	elif sfile == 'py':
		src=open(dirs[i],"r")
		fline="#py testing \n"    #Prepending string
		oline=src.readlines() #Here, we prepend the string we want to on first line
		oline.insert(0,fline)
		src.close()
		src=open(dirs[i],"w")  #We again open the file in WRITE mode 
		src.writelines(oline)
		src.close()
	elif sfile == 'txt':
		src=open(dirs[i],"r")
		fline="# This is copyright notice @" + str(yearinput)   #Prepending string
		oline=src.readlines() #Here, we prepend the string we want to on first line
		oline.insert(0,fline)
		src.close()
		src=open(dirs[i],"w")  #We again open the file in WRITE mode 
		src.writelines(oline)
		src.close()
		#else unclassified = []
		#unclassified.append(dirs[i]):
		#print(unclassified)	#把變數x塞到list的最後面