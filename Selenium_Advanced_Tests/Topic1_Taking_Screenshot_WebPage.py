import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.fullscreen_window()
time.sleep(1)
driver.maximize_window()
driver.get("https://openweathermap.org/")

driver.save_screenshot("C:\\Users\\autom\\PycharmProjects\\pythonProject1\\screenshots\\Webpage.png")
driver.get_screenshot_as_file("C:\\Users\\autom\\PycharmProjects\\pythonProject1\\screenshots\\Webpage1.png")