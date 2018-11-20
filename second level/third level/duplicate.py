// CopyRight Notice @1234
# CopyRight Notice @ Jimmy haha
# CopyRight Notice @ happy to get iphone
# CopyRight Notice @ r23r23
# CopyRight Notice @ 12312
# CopyRight Notice @ 1323
# CopyRight Notice @ 123123
# CopyRight Notice @ 123
# CopyRight Notice @ 12312
# CopyRight Notice @ 21312
# CopyRight Notice @ 123
# CopyRight Notice @ 3123
# CopyRight Notice @ 123
# CopyRight Notice @ 213
# CopyRight Notice @ 123
# CopyRight Notice @ 12312
# CopyRight Notice @ 1232
# CopyRight Notice @ 123123
# CopyRight Notice @ 123
# CopyRight Notice @ 3333
# CopyRight Notice @ 123
# CopyRight Notice @ 1234
# CopyRight Notice @ mouse testing
# CopyRight Notice @ 1234546
# CopyRight Notice @ 123456
#py testing CopyRight Notice @ 1234
#py testing CopyRight Notice @ This is a coffee
#py testing CopyRight Notice @ 1234
#py testing CopyRight Notice @ 1234
import os, sys, csv, re

count = 0
unclassified = 0
numfiles = 0
success_list = []
fail_list = []
repoinput = input('Input Repo folder Name: ')
yearinput = input('Year of CopyRight notice: ')
outpath = '/Users/connectar/Desktop'
path = '/Users/connectar/Desktop/RepoTesting'
file_list = []
inpath = []
for root, dirs, files in os.walk(path):
	inpath.append(root)
exlist = ['/Users/connectar/Desktop/RepoTesting\\.git']
blacklist = re.compile('|'.join([re.escape(word) for word in exlist]))
inpath = [word for word in inpath if not blacklist.search(word)]
#print(inpath)
for j in range (0, len(inpath)):
	root, dirs, files = next(os.walk(inpath[j]))
	numfiles += len(files)
	#dirs = os.listdir(inpath[j])
	for i in range (0,len(files)):
		sfile = str(files[i]).split('.')[ -1 ]
		os.chdir(inpath[j])
		if sfile == 'c':	# CStyle()
			src=open(files[i],"r")
			fline="// Copyright Notce @	"  + str(yearinput) + "\n" #Prepending string
			oline=src.readlines() #Here, we prepend the string we want to on first line
			oline.insert(0,fline)
			src.close()
			src=open(files[i],"w")  #We again open the file in WRITE mode 
			src.writelines(oline)
			src.close()
			count += 1
			success_list.append(str(files[i]))
		elif sfile == 'java': #JavaStyle
			src=open(files[i],"r")
			fline="//java testing CopyRight Notice @" + str(yearinput) + "\n"  #Prepending string
			oline=src.readlines() #Here, we prepend the string we want to on first line
			oline.insert(0,fline)
			src.close()
			src=open(files[i],"w")  #We again open the file in WRITE mode 
			src.writelines(oline)
			src.close()
			count += 1
			success_list.append(str(files[i]))
		elif sfile == 'php': #phpStyle
			src=open(files[i],"r")
			fline="//Php testing CopyRight Notice @" + str(yearinput) + "\n"  #Prepending string
			oline=src.readlines() #Here, we prepend the string we want to on first line
			oline.insert(0,fline)
			src.close()
			src=open(files[i],"w")  #We again open the file in WRITE mode 
			src.writelines(oline)
			src.close()
			count += 1
			success_list.append(str(files[i]))
		elif sfile == 'py': #phytonStyle
			src=open(files[i],"r")
			fline="#py testing CopyRight Notice @ " + str(yearinput) + "\n"  #Prepending string
			oline=src.readlines() #Here, we prepend the string we want to on first line
			oline.insert(0,fline)
			src.close()
			src=open(files[i],"w")  #We again open the file in WRITE mode 
			src.writelines(oline)
			src.close()
			count += 1
			success_list.append(str(files[i]))
		elif sfile == 'txt': #txtStyle
			src=open(files[i],"r")
			fline="<<This is copyright notice @" + str(yearinput) + ">> \n"   #Prepending string
			oline=src.readlines() #Here, we prepend the string we want to on first line
			oline.insert(0,fline)
			src.close()
			src=open(files[i],"w")  #We again open the file in WRITE mode 
			src.writelines(oline)
			src.close()
			count += 1
			success_list.append(str(files[i]))
		elif sfile == 'xml': #XMLStyle
			src=open(files[i],"r")
			fline="<!--This is copyright notice @" + str(yearinput) + "--> \n"   #Prepending string
			oline=src.readlines() #Here, we prepend the string we want to on first line
			oline.insert(0,fline)
			src.close()
			src=open(files[i],"w")  #We again open the file in WRITE mode 
			src.writelines(oline)
			src.close()
			count += 1
			success_list.append(str(files[i]))
		elif sfile == 'html': #XMLStyle
			src=open(files[i],"r")
			fline="<!--This is copyright notice @" + str(yearinput) + "--> \n"   #Prepending string
			oline=src.readlines() #Here, we prepend the string we want to on first line
			oline.insert(0,fline)
			src.close()
			src=open(files[i],"w")  #We again open the file in WRITE mode 
			src.writelines(oline)
			src.close()
			count += 1
			success_list.append(str(files[i]))
		else:
			unclassified += 1
			fail_list.append(str(files[i]))
os.chdir(outpath)
with open('Repo_Summary.csv', 'a', newline='') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow([repoinput, 'Total no.'])
	writer.writerow(['Classified', str(count),success_list])
	writer.writerow(['Unclassified', str(unclassified),fail_list]) 
sumcu = count + unclassified
print('Classified: ' + str(count))
print('Unclassified: ' + str(unclassified))
print('Sum of Classified and Unclassified: ' + str(sumcu))
print('Total files in folder: ' + str(numfiles))