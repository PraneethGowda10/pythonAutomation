from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome driver using Selenium Manager (built-in)
driver = webdriver.Chrome()

# Use absolute file path and convert to proper file URL
driver.get("https://www.google.com/")

driver.maximize_window()

element = driver.find_element(By.ID, "APjFqb")


element.send_keys("Hello World")

driver.close()
