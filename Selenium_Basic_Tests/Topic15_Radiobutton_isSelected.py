from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")


MaleRadioButton = driver.find_element(By.XPATH, "//input[@id = 'radio1']")
print(MaleRadioButton.is_selected())

if MaleRadioButton.is_enabled():
    MaleRadioButton.click()
else:
    print("Radio button is not enabled")

print(MaleRadioButton.is_selected())