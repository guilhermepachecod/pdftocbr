#!/usr/bin/python
#apt install python python-pip poppler-utils
#apt install rar 
#pip install pdf2image
#pip install pathlib
from pdf2image import convert_from_path
from glob import glob
import os
import shutil

def namefile(page,folder):
	files_list = glob(os.path.join(folder, '*.jpg'))
	print len(files_list)
	return folder +"/"+ str(len(files_list)+1) + ".jpg"
def makemydir(newfolder):
	try:
		os.makedirs(newfolder)
	except OSError:
		pass
def makemyrarfile(folder):
	try:
		print('rar a '+folder+'.cbr '+folder)
		os.system('rar a "converted/'+folder+'.cbr" "'+folder+'"')
	except OSError:
		pass
def removerarfolder(folder):
	try:
		shutil.rmtree(folder)
	except OSError:
		pass	
def convertfiles(files):
	print files
	folder = files.split(".")[0].split("/")[1]
	print folder
	makemydir(folder)  	
	pages = convert_from_path(files,100)
	for page in pages:
		page.save(namefile(page,folder), 'JPEG')
	makemyrarfile(folder)
	removerarfolder(folder)
	
hq_list = glob(os.path.join("convert/", '*.pdf'))
for files in hq_list:
	convertfiles(files)

