from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver using WebDriver manager
driver = webdriver.Chrome()

# Open a website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)


# locate the username and password field
UserName = driver.find_element(By.CSS_SELECTOR,
                               '#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(2) > div > div:nth-child(2) > input')
time.sleep(5)
Password = driver.find_element(By.CSS_SELECTOR,
                               '#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(3) > div > div:nth-child(2) > input')
time.sleep(5)
LoginButton = driver.find_element(By.CSS_SELECTOR,
                                  '#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button')
time.sleep(5)


# Enter your credentials
UserName.send_keys("Admin")
Password.send_keys("admin123")


# locate the login button and click it
LoginButton.click()


time.sleep(10)

# Close the browser
driver.quit()
