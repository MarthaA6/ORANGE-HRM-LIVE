from selenium import webdriver
import time


# Initialize the Chrome WebDriver using WebDriver manager
driver = webdriver.Chrome()

# Open a website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(10)

# Close the browser
driver.quit()


