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
UserName.send_keys("Admin")
time.sleep(5)

Password = driver.find_element(By.CSS_SELECTOR,
                               '#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(3) > div > div:nth-child(2) > input')
Password.send_keys("admin123")
time.sleep(5)

LoginButton = driver.find_element(By.CSS_SELECTOR,
                                  '#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button')
# locate the login button and click it
LoginButton.click()
time.sleep(5)

# Find the element
AdminButton = driver.find_element(By.CSS_SELECTOR,
                                  '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a')
AdminButton.click()
time.sleep(5)

Pim_Button = driver.find_element(By.CSS_SELECTOR,
                                 '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a')
Pim_Button.click()
time.sleep(5)


Leave_Button = driver.find_element(By.CSS_SELECTOR,
                                   '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(4) > a')

Leave_Button.click()
time.sleep(5)

Time_Button = driver.find_element(By.CSS_SELECTOR,
                                  '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(4) > a')
Time_Button.click()
time.sleep(5)

Recruitment_Button = driver.find_element(By.CSS_SELECTOR,
                                         '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(5) > a > span')
Recruitment_Button.click()
time.sleep(5)


MyInfo_Button = driver.find_element(By.CSS_SELECTOR,
                                    '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(6) > a > span')
Recruitment_Button.click()
time.sleep(5)

Performance_Button = driver.find_element(By.CSS_SELECTOR,
                                         '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(7) > a > span')
Performance_Button.click()
time.sleep(5)

Dashboard_Button = driver.find_element(By.CSS_SELECTOR,
                                       '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(8) > a > span')
Dashboard_Button.click()
time.sleep(5)

Directory_Button = driver.find_element(By.CSS_SELECTOR
                                       '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(9) > a > span')
Directory_Button.click()
time.sleep(5)

Maintenance_Button = driver.find_element(By.CSS_SELECTOR,
                                         '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(10) > a > span')
Maintenance_Button.click()
time.sleep(5)

Claim_Button = driver.find_element(By.CSS_SELECTOR,
                                   '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(11) > a')
Claim_Button.click()
time.sleep(5)

Buzz_Button = driver.find_element(By.CSS_SELECTOR
                                  '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(12) > a')
Buzz_Button.click()
time.sleep(5)


# Close the browser
driver.quit()
