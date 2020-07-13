from selenium import webdriver

driver = webdriver.Chrome(executable_path = "/home/shriram/Downloads/chromedriver")
driver.set_window_size(2048,1280)
executor_url = driver.command_executor._url
session_id = driver.session_id
driver.get("https://zoom.us/recording")

print session_id
print executor_url


driver2 = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
driver2.set_window_size(2048,1280)
driver2.session_id = session_id
driver2.get("https://zoom.us/recording")
print driver2.current_url