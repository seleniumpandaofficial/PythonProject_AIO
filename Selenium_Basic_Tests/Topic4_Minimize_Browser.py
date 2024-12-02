import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")
time.sleep(5)
driver.minimize_window()