from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path = "/home/shriram/Downloads/chromedriver")
driver.set_window_size(2048,1280)
driver.get("https://zoom.us/recording")
#button = driver.find_element_by_id('vjs_video_3_html5_api')
driver.implicitly_wait(20)
index = 0 
while True:
	a = driver.find_elements_by_class_name("btn-group")
	print a 
	a[index].click()
	time.sleep(10)
	mama = driver.find_element_by_css_selector("dropdown-menu")
	mama[1].click()
	index+=1
	time.sleep(10)

#button.click()
