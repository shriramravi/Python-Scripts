import xlrd
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import glob
import os
from moviepy.editor import VideoFileClip

def download(i):
	print(sheet.cell_value(i, 10)) 
	driver = webdriver.Chrome(executable_path = "/home/shriram/Downloads/chromedriver")
	driver.set_window_size(2048,1280)
	driver.get(sheet.cell_value(i,10))
#button = driver.find_element_by_id('vjs_video_3_html5_api')
	try:
		driver.find_element_by_link_text("Download (3 files)").click()
	except NoSuchElementException:
		driver.find_element_by_link_text("Download (2 files)").click()
	time.sleep(240)
	list_of_files = glob.glob('/home/shriram/Downloads/*') # * means all if need specific format then *.csv
	latest_file = max(list_of_files, key=os.path.getctime)
	print(latest_file)
	os.rename(latest_file,'Fly.mp4')
	clip = VideoFileClip("Fly.mp4").subclip(2400,2425)
	clip.to_videofile("Kunsh.mp4", codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')
	

loc="./test_mama.xlsx"
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
sheet.cell_value(0, 0) 
  
for i in range(1,sheet.nrows): 
    download(i)

