from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

x = open("learn2.txt").read().splitlines()
for line in x:
	if len(line) > 0 :
		print line
		driver = webdriver.Chrome(executable_path = "/home/shriram/Downloads/chromedriver")
		driver.set_window_size(2048,1280)
		driver.get(line)
#button = driver.find_element_by_id('vjs_video_3_html5_api')
		try:
			driver.find_element_by_link_text("Download (3 files)").click()
		except NoSuchElementException:
			driver.find_element_by_link_text("Download (2 files)").click()
time.sleep(1200)


#button.click()
