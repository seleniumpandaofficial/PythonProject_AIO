import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo")
driver.find_element(By.LINK_TEXT, "My Account").click()
driver.find_element(By.LINK_TEXT, "Login").click()
driver.find_element(By.ID, "input-email").send_keys("seelniumpanda@gmail.com")
driver.find_element(By.ID, "input-password").send_keys("Selenium@123")
driver.find_element(By.CSS_SELECTOR, "input.btn.btn-primary").click()
time.sleep(10)
