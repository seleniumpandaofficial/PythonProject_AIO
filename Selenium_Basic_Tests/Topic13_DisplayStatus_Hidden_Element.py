from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com")

HomePageTitle = driver.title
HomePageCurrentURL = driver.current_url
print(HomePageTitle)
print(HomePageCurrentURL)

hiddenButton = driver.find_element(By.ID, "hbutton")
if hiddenButton.is_displayed():
    print("diplayed")
else:
    print("not displayed")