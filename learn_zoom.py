from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import glob
import os
import xlrd
import datetime
dt = str(datetime.datetime.now())

def download(i):
	print(sheet.cell_value(i, 0)) 
	driver = webdriver.Chrome(executable_path = "/home/shriram/Downloads/chromedriver")
	driver.set_window_size(2048,1280)
	driver.get(sheet.cell_value(i,0))
#button = driver.find_element_by_id('vjs_video_3_html5_api')
	try:
		driver.find_element_by_link_text("Download (3 files)").click()
	except NoSuchElementException:
		driver.find_element_by_link_text("Download (2 files)").click()
	if(sheet.cell_value(i,1)<200):
		time.sleep(60)
	elif(sheet.cell_value(i,1)<400):
		time.sleep(120)
	elif(sheet.cell_value(i,1)>400):
		time.sleep(240)	
	list_of_files = glob.glob('/home/shriram/Downloads/*') # * means all if need specific format then *.csv
	latest_file = max(list_of_files, key=os.path.getctime)
	_, filename = os.path.split(latest_file)
	print(filename)
	if "Ignite" in filename:
		os.rename(latest_file,'/home/shriram/Videos/Ignite/'+filename)
	elif "Explore" in filename:
		os.rename(latest_file,'/home/shriram/Videos/Explore/'+filename)
	elif "Workshop" in filename:
		os.rename(latest_file,'/home/shriram/Videos/Workshop/'+filename)
	else:
		os.rename(latest_file,'/home/shriram/Videos/'+filename)



loc="./learn2.xlsx"
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0) 
  
for i in range(0,sheet.nrows): 
    download(i)
time.sleep(600)