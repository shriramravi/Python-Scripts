from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import glob
import os
import xlrd
import datetime
from moviepy.editor import VideoFileClip

dt = str(datetime.datetime.now())
nochild=0
loc="./6-7_CAR_B2.xlsx"
loc1=0
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 

#download zoom video and crop
def download(m):
	print(sheet.cell_value(m, 3)) 
	driver = webdriver.Chrome(executable_path = "/home/shriram/Downloads/chromedriver")
	driver.set_window_size(2048,1280)
	driver.get(sheet.cell_value(m,3))
#button = driver.find_element_by_id('vjs_video_3_html5_api')
	try:
		driver.find_element_by_link_text("Download (4 files)").click()
	except NoSuchElementException:
		driver.find_element_by_link_text("Download (2 files)").click()
	time.sleep(240)	
	list_of_files = glob.glob('/home/shriram/Downloads/*') # * means all if need specific format then *.csv
	latest_file = max(list_of_files, key=os.path.getctime)
	_, filename = os.path.split(latest_file)
	return latest_file


#convert time string to seconds
def get_sec(time_str):
    """Get Seconds from time."""
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)
  
# For row 0 and column 0 
task=[]
sheet.cell_value(0, 0) 

# Get number of children and task cells
for row in range(0,sheet.nrows):
	if len(sheet.cell_value(row,2))>0 and row>=7:
		print(sheet.cell_value(row,2))
		task.append(row)
	else:
		loc=row;

for row in range(7,sheet.nrows):
	try:
		if(sheet.cell_value(row,0).is_integer()):
			loc1+=1
		print(sheet.cell_value(row,0))
	except AttributeError:
		print("Error ended")
print(loc1+7)
loc2 = loc1+7
print(loc2)
		

i=task[0]
j=0
if(len(task)>1):
	nochild = task[1] - task[0]
else:
	nochild = loc - 7	




print(task)
print(nochild)

m=0;
print(sheet.cell_value(7,16))
print(sheet.cell_value(7,17))
print(sheet.cell_value(7,16))
print(sheet.cell_value(7,17))
print(m)

while  m < (len(task)-1):
	if len(sheet.cell_value(task[m],3)) == 0:
		m+=1
		continue
	else:
		x = download(task[m])
# Get all time stamps for a task and clip provided the next task exists
		i = task[m]
		print(i)
		while i < (task[m+1]):
			print(sheet.cell_value(i,16))
			print(sheet.cell_value(i,17))
			if sheet.cell_value(i,16) == 0:
				i+=1
				continue
			clip = VideoFileClip(x).subclip(sheet.cell_value(i,16),sheet.cell_value(i,17))
			clip.to_videofile(str(sheet.cell_value(i,1))+"_"+str(sheet.cell_value(i,4))+"_"+str(sheet.cell_value(1,1))+str(sheet.cell_value(i,15)) +".mp4", codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
			print("The"+str(i)+"th cropping is done")
			i+=1
		m+=1
# Exits when there is no further task 
# When m is at the last task we iterate as many times as the number of children
if m == len(task)-1:
	if len(sheet.cell_value(task[m],3)) == 0:
		exit()
	else:
		x = download(task[m])
# Get all time stamps for a task and clip
		i = task[m]
		print(i)
		while i < (loc2):
			print(sheet.cell_value(i,16))
			print(sheet.cell_value(i,17))
			if sheet.cell_value(i,16) == 0:
				i+=1
				continue
			clip = VideoFileClip(x).subclip(sheet.cell_value(i,16),sheet.cell_value(i,17))
			clip.to_videofile(str(sheet.cell_value(i,1))+"_"+str(sheet.cell_value(i,4))+"_"+str(sheet.cell_value(1,1))+str(sheet.cell_value(i,15)) +".mp4", codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
			print("The"+str(i)+"th cropping is done")
			i+=1
		m+=1











	



