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

# open the url
driver.get('https://www.target.com/')
# Click the Sign in button
driver.find_element(By.LINK_TEXT, "Sign in").click()
# Click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']//span[text()='Sign in']").click()

sleep(3)


driver.find_element(By.ID, "username").send_keys("nooko4@yahoo.com")
driver.find_element(By.ID, "password").send_keys("Bless4ever")
driver.find_element(By.ID, "login").click()

sleep(10)



