from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Amazon logo
driver.find_element(By.CSS_SELECTOR,'.a-icon')
# Create account
driver.find_element(By.CSS_SELECTOR,'.a-spacing-small')
# Your name field
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name')
# Mobile number or email field
driver.find_element(By.CSS_SELECTOR,'#ap_email')
# Password field
driver.find_element(By.CSS_SELECTOR,'#ap_password')
# Re-enter password field
driver.find_element(By.CSS_SELECTOR,'#ap_password_check')
# Continue button
driver.find_element(By.CSS_SELECTOR,'#continue')
# Conditions of Use
driver.find_element(By.CSS_SELECTOR,"#legalTextRow [href*='condition']")
# Privacy Notice
driver.find_element(By.CSS_SELECTOR,"#legalTextRow [href*='privacy']")
# Sign in
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis")