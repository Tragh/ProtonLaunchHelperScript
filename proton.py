#!/usr/bin/python3
import glob
import sys
import os
import re

# CONFIG SECTION - EDIT THESE PATHS

proton_builds_folder=os.path.expanduser("~/.steam/steam/steamapps/common/")
cdatas_folder=os.path.expanduser("~/.proton_cdatas_folder/")

# END OF CONFIG SECTION


#function no longer used...
def get_group(ex,s):
	m=re.search(ex, s)
	if m and m.group(1):
		return m.group(1)
	else:
		print(f"match error looking for \n{ex}\nin\n{s}")

def get_selection_numeric(array,question):
	print(question)
	for i in range(0, len(array)):
		print("   "+str(i+1)+") "+array[i])
	answer=input()
	if answer not in "123456789":
		print("exiting..")
		exit()
	index=int(answer)-1
	if index >= len(array):
		print("index out of range")
		exit()
	return array[index]


if not os.path.isdir(cdatas_folder):
	print(f"The cdatas folder \" {cdatas_folder} \" doesn't exist, create it?")
	if input("[Y/n]") in ["Y", "y", ""]:
		os.mkdir(cdatas_folder)
	else:
		print("Cannot procede without cdatas folder")
		exit()


exes=glob.glob("*.exe")
exes.append("* custom command")
exe=get_selection_numeric(exes, "Select exe to run with Proton")

proton_builds=[x for x in glob.glob(proton_builds_folder+"/*") if os.path.isfile(os.path.join(x,"proton"))]
proton_builds.sort(reverse=True)
proton_build=get_selection_numeric(proton_builds, "Select which Proton build to use")

cdatas_folder_specific=os.path.join(cdatas_folder,os.path.split(proton_build)[1])

if not os.path.isdir(cdatas_folder_specific):
	print(f"This proton's cdatas folder \" {cdatas_folder_specific} \" doesn't exist, create it?")
	if input("[Y/n]") in ["Y", "y", ""]:
		os.mkdir(cdatas_folder_specific)
	else:
		print("Cannot procede without proton's cdatas folder")
		exit()

print(f'looking for cdatas in "{cdatas_folder_specific}"')
cdatas=glob.glob(cdatas_folder_specific+"/*")
cdatas.sort()
cdatas.append("* create new cdata folder")
cdata=get_selection_numeric(cdatas, "Select cdata to use with Proton")

if cdata=="* create new cdata folder":
	new_folder=os.path.join(cdatas_folder_specific,input("Please enter folder name: "))
	print(f"Create \" {new_folder} \"?")
	if input("[Y/n]") in ["Y", "y", ""]:
		os.mkdir(new_folder)
		cdata=new_folder
	else:
		print("Cannot procede.")
		exit()



#runstring=f"STEAM_COMPAT_DATA_PATH=\"{cdata}\" \"{proton_build}/proton\" run \"" + exe+"\""
param=""
if exe=="* custom command":
	exe=input("Please enter custom command: ")
	param=input("Please enter custom parameter: ")
runstring=f"STEAM_COMPAT_DATA_PATH=\"{cdata}\" STEAM_COMPAT_CLIENT_INSTALL_PATH=\"~/.local/share/Steam\" \"{proton_build}/proton\" run \"" + exe+"\""
if param != "":
	runstring=runstring+" \""+param+"\""
print(runstring)
os.system(runstring)
