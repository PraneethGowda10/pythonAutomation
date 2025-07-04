from selenium import webdriver
import os

# Initialize Chrome driver using Selenium Manager (built-in)
driver = webdriver.Chrome()

# Use absolute file path and convert to proper file URL
driver.get("https://www.google.com/")

driver.maximize_window()

driver.quit()
