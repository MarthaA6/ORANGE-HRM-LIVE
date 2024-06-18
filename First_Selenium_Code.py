from selenium import webdriver
import time

from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

# Initialize the Chrome WebDriver using WebDriver manager
driver = webdriver.Chrome()

# Open a website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)

# LOGIN PAGE
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

# ADMIN PAGE ----------------------------------------------------------------------------------------------------------
# Find the element
AdminButton = driver.find_element(By.CSS_SELECTOR,
                                  '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a')
AdminButton.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 1 USER MANAGEMENT SUB-BUTTON ----------------------------------------------------------------------------------------
UserManagement1_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
UserManagement1_Button.click()
time.sleep(5)

# 1 USER MANAGEMENT DROP-DOWN ARROW
Users1_Button = driver.find_element(By.XPATH,
                                    '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li')
Users1_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 1 JOBS SUB-BUTTON ---------------------------------------------------------------------------------------------------
Jobs1_Button = driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
Jobs1_Button.click()
time.sleep(5)

# 1 JOB TITLES DROP-DOWN ARROW
JobsTitles_DropDown = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]')
JobsTitles_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 2 JOBS SUB-BUTTON----------------------------------------------------------------------------------------------------
Jobs2_Button = driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
Jobs2_Button.click()
time.sleep(5)

# 2 PAY GRADES DROP-DOWN ARROW
PayGrades_DropDown = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]')
PayGrades_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 3 JOBS SUB-BUTTON ---------------------------------------------------------------------------------------------------
Jobs3_Button = driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
Jobs3_Button.click()
time.sleep(5)

# 3 EMPLOYMENT STATUS DROP-DOWN
EmploymentStatus_DropDown = driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]')
EmploymentStatus_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 4 JOBS SUB-BUTTON----------------------------------------------------------------------------------------------------
Jobs4_Button = driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
Jobs4_Button.click()
time.sleep(5)

# 4 JOB CATEGORIES DROP-DOWN
JobCategories_DropDown = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]')
JobCategories_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 5 JOBS SUB-BUTTON ---------------------------------------------------------------------------------------------------
Jobs5_Button = driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
Jobs5_Button.click()
time.sleep(5)

# 5 WORK SHIFT DROP-DOWN ARROW
WorkShift_DropDown = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[5]')
WorkShift_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 1 ORGANIZATIONS SUB-BUTTON-------------------------------------------------------------------------------------------
Organizations1_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span')
Organizations1_Button.click()
time.sleep(5)

# 1 GENERAL INFORMATION DROP-DOWN
GeneralInformation_DropDown = driver.find_element(By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]/a')
GeneralInformation_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 2 ORGANIZATIONS SUB-BUTTON-------------------------------------------------------------------------------------------
Organizations2_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span')
Organizations2_Button.click()
time.sleep(5)

# 2 LOCATION DROP-DOWN
Locations_DropDown = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]/a')
Locations_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 3 ORGANIZATIONS SUB-BUTTON-------------------------------------------------------------------------------------------
Organizations3_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span')
Organizations3_Button.click()
time.sleep(5)

# 3 STRUCTURE DROP-DOWN
Structure_DropDown = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]/a')
Structure_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 1 QUALIFICATIONS SUB-BUTTON------------------------------------------------------------------------------------------
Qualifications1_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
Qualifications1_Button.click()
time.sleep(5)

# 1 SKILLS DROP-DOWN ARROW
Skills_DropDown = driver.find_element(By.XPATH,
                                      '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]')
Skills_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 2 QUALIFICATIONS SUB-BUTTON------------------------------------------------------------------------------------------
Qualifications2_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
Qualifications2_Button.click()
time.sleep(5)

# 2 EDUCATION DROP-DOWN ARROW
Education_DropDown = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]/a')
Education_DropDown.click()
time.sleep(5)

# 3 QUALIFICATIONS SUB-BUTTON------------------------------------------------------------------------------------------
Qualifications3_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
Qualifications3_Button.click()
time.sleep(5)

# 3 LICENSES DROP-DOWN ARROW
Licenses_DropDown = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[3]')
Licenses_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 4 QUALIFICATIONS SUB-BUTTON------------------------------------------------------------------------------------------
Qualifications4_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
Qualifications4_Button.click()
time.sleep(5)

# 4 LANGUAGES DROP-DOWN ARROW
Languages_DropDown = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[4]/a')
Languages_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 5 QUALIFICATIONS SUB-BUTTON------------------------------------------------------------------------------------------
Qualification5_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
Qualification5_Button.click()
time.sleep(5)

# 5 MEMBERSHIPS DROP-DOWN ARROW
Memberships_DropDown = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[5]/a')
Memberships_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# NATIONALITIES BUTTON ------------------------------------------------------------------------------------------------
Nationalities_Button = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
Nationalities_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# CORPORATE BRANDING BUTTON -------------------------------------------------------------------------------------------
CorporateBranding_Button = driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]')
CorporateBranding_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 1 CONFIGURATION SUB-BUTTON ---------------------------------------------------------------------------------------------------
Configuration1_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
Configuration1_Button.click()
time.sleep(5)

# 1 EMAIL CONFIGURATION DROP-DOWN ARROW
EmailConfiguration_DropDown = driver.find_element(By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[1]')
EmailConfiguration_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 2 CONFIGURATION SUB-BUTTON ------------------------------------------------------------------------------------------
Configuration2_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
Configuration2_Button.click()
time.sleep(5)

# 2 EMAIL SUBSCRIPTIONS  DROP-DOWN ARROW
EmailSubscriptions_DropDown = driver.find_element(By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[2]')
EmailSubscriptions_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 3 CONFIGURATION PAGE --------------------------------------------------------------------------------------------------
Configuration3_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
Configuration3_Button.click()
time.sleep(5)

# 3 LOCALIZATION DROP-DOWN ARROW
Localization_DropDown = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[3]')
Localization_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 4 CONFIGURATION SUB-BUTTON ---------------------------------------------------------------------------------------------------
Configuration4_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
Configuration4_Button.click()
time.sleep(5)

# 4 LANGUAGE PACKAGES CROP-DOWN ARROW
LanguagePackages_DropDown = driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[4]')
LanguagePackages_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 5 CONFIGURATION SUB-BUTTON ------------------------------------------------------------------------------------------------
Configuration5_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
Configuration5_Button.click()
time.sleep(5)

# 5 MODULES DROP-DOWN ARROW
Modules_DropDown = driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[5]')
Modules_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 6 CONFIGURATION SUB-BUTTON -------------------------------------------------------------------------------------------------
Configuration6_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
Configuration6_Button.click()
time.sleep(5)

# 6 SOCIAL MEDIA AUTHENTICATION DROP-DOWN ARROW
SocialMediaAuthentication_DropDown = driver.find_element(By.XPATH,
                                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[6]')
SocialMediaAuthentication_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 7 CONFIGURATION SUB-BUTTON ------------------------------------------------------------------------------------------------
Configuration7_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
Configuration7_Button.click()
time.sleep(5)

# 7 REGISTER OAUTH CLIENT DROP-DOWN ARROW
RegisterOAuthClient_DropDown = driver.find_element(By.XPATH,
                                                   '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[7]')
RegisterOAuthClient_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# # 8 CONFIGURATION SUB-BUTTON ----------------------------------------------------------------------------------------------
Configuration8_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
Configuration8_Button.click()
time.sleep(5)

# 8LDAP CONFIGURATION DROP-DOWN ARROW
LDAPConfiguration_DropDown = driver.find_element(By.XPATH,
                                                 '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/ul/li[8]')
LDAPConfiguration_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# PIM PAGE ------------------------------------------------------------------------------------------------------------
Pim_Button = driver.find_element(By.CSS_SELECTOR,
                                 '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a')
Pim_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 11 CONFIGURATION SUB-BUTTON -----------------------------------------------------------------------------------------
Configuration11_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Configuration11_Button.click()
time.sleep(5)

# 11 OPTIONAL FIELDS DROP DOWN ARROW
OptionalFields_DropDown = driver.find_element(By.XPATH,
                                              '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]')
OptionalFields_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 22 CONFIGURATION SUB-BUTTON -----------------------------------------------------------------------------------------
Configuration22_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Configuration22_Button.click()
time.sleep(5)

# 22 CUSTOM FIELDS DROP-DOWN ARROW
CustomFields_DropDown = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]')
CustomFields_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 33 CONFIGURATION SUB-BUTTON -----------------------------------------------------------------------------------------
Configuration33_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Configuration33_Button.click()
time.sleep(5)

# 33 DATA IMPORT DROPDOWN ARROW
DataImport_DropDown = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[3]')
DataImport_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 44 CONFIGURATION SUB-BUTTON -----------------------------------------------------------------------------------------
Configuration44_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Configuration44_Button.click()
time.sleep(5)

# 44 REPORTING METHODS DROP-DOWN ARROW
ReportingMethods_DropDown = driver.find_element(By.XPATH,
                                                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[4]')
ReportingMethods_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 55 CONFIGURATION SUB-BUTTON -----------------------------------------------------------------------------------------
Configuration55_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Configuration55_Button.click()
time.sleep(5)

# 55 TERMINATION REASONS DROP-DOWN ARROW
TerminationReasons_DropDown = driver.find_element(By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[5]')
TerminationReasons_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# EMPLOYEE LIST SUB-BUTTON --------------------------------------------------------------------------------------------------
EmployeeList_Button = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
EmployeeList_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# ADD EMPLOYEE SUB-BUTTON ---------------------------------------------------------------------------------------------------
AddEmployee_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
AddEmployee_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# REPORTS SUB-BUTTON --------------------------------------------------------------------------------------------------------
Reports_Button = driver.find.element(By.XPATH,
                                     '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
Reports_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# LEAVE PAGE ----------------------------------------------------------------------------------------------------------
Leave_Button = driver.find_element(By.CSS_SELECTOR,
                                   '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(3) > a')
Leave_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# APPLY SUB-BUTTON ----------------------------------------------------------------------------------------------------------
Apply_Button = driver.find_element(By.XPATH,
                                   '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Apply_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# MY LEAVE SUB-BUTTON ---------------------------------------------------------------------------------------------------
MyLeave_Button = driver.find_element(By.XPATH,
                                     '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
MyLeave_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 1 ENTITLEMENTS SUB-BUTTON -------------------------------------------------------------------------------------------
Entitlements1_Button = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
Entitlements1_Button.click()
time.sleep(5)

# ADD ENTITLEMENTS DROP-DOWN ARROW
AddEntitlements_DropDown = driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]')
AddEntitlements_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 2 ENTITLEMENTS SUB-BUTTON -------------------------------------------------------------------------------------------
Entitlements2_Button = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
Entitlements2_Button.click()
time.sleep(5)

# EMPLOYEE ENTITLEMENTS DROP-DOWN ARROW
EmployeeEntitlements_DropDown = driver.find_element(By.XPATH,
                                                    '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]')
EmployeeEntitlements_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 3 ENTITLEMENTS SUB-BUTTON -------------------------------------------------------------------------------------------
Entitlements3_Button = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
Entitlements3_Button.click()
time.sleep(5)

# MY ENTITLEMENTS DROP-DOWN ARROW
MyEntitlements_DropDown = driver.find_element(By.XPATH,
                                              '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]')
MyEntitlements_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# REPORTS SUB-BUTTON --------------------------------------------------------------------------------------------------
Reports1_Button = driver.find_element(By.XPATH,
                                      '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
Reports1_Button.click()
time.sleep(5)

# LEAVE ENTITLEMENTS AND USAGE REPORTS DROP-DOWN ARROW
LeaveEntitlementsAndUsageReports_DropDown = driver.find_element(By.XPATH,
                                                                '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]')
LeaveEntitlementsAndUsageReports_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# REPORTS SUB-BUTTON --------------------------------------------------------------------------------------------------
Reports1_Button = driver.find_element(By.XPATH,
                                      '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
Reports1_Button.click()
time.sleep(5)

# MY LEAVE ENTITLEMENTS AND USAGE REPORTS DROP-DOWN ARROW
MyLeaveEntitlementsAndUsageReports_DropDown = driver.find_element(By.XPATH,
                                                                  '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]')
MyLeaveEntitlementsAndUsageReports_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 1 CONFIGURE SUB-BUTTON ----------------------------------------------------------------------------------------------
Configure1_Button = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
Configure1_Button.click()
time.sleep(5)

# 1 LEAVE PERIOD DROP-DOWN ARROW
LeavePeriod_DropDown = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/li[1]')
LeavePeriod_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 2 CONFIGURE SUB-BUTTON ----------------------------------------------------------------------------------------------
Configure2_Button = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
Configure2_Button.click()
time.sleep(5)

# 2 LEAVE TYPES DROP-DOWN ARROW
LeaveTypes_DropDown = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/li[2]')
LeaveTypes_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 3 CONFIGURE SUB-BUTTON ----------------------------------------------------------------------------------------------
Configure3_Button = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
Configure3_Button.click()
time.sleep(5)

# 3 WORK WEEK DROP-DOWN ARROW
WorkWeek_DropDown = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/li[3]')
WorkWeek_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 4 CONFIGURE SUB-BUTTON ----------------------------------------------------------------------------------------------
Configure4_Button = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
Configure4_Button.click()
time.sleep(5)

# 5 HOLIDAYS DROP-DOWN ARROW
Holidays_DropDown = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/li[4]')
Holidays_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# LEAVE LIST SUB-BUTTON -----------------------------------------------------------------------------------------------------
LeaveList_Button = driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]')
LeaveList_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# ASSIGN LEAVE SUB-BUTTON ---------------------------------------------------------------------------------------------------
AssignLeave_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]')
AssignLeave_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# TIME PAGE -----------------------------------------------------------------------------------------------------------
Time_Button = driver.find_element(By.CSS_SELECTOR,
                                  '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(4) > a')
Time_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 1 TIME SHEETS SUB BUTTON --------------------------------------------------------------------------------------------
TimeSheets1_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
TimeSheets1_Button.click()
time.sleep(5)

# MY TIME SHEETS DROP-DOWN ARROW
MyTimeSheets_DropDown = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]')
MyTimeSheets_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 2 TIME SHEETS SUB-BUTTON --------------------------------------------------------------------------------------------
TimeSheets2_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
TimeSheets2_Button.click()
time.sleep(5)

# EMPLOYEE TIME SHEETS DROP-DOWN ARROW
EmployeeTimeSheets_DropDown = driver.find_element(By.XPATH,
                                                  '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]')
EmployeeTimeSheets_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 1 ATTENDANCE SUB-BUTTON ---------------------------------------------------------------------------------------------------
Attendance1_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
Attendance1_Button.click()
time.sleep(5)

# 1 MY RECORDS DROP-DOWN ARROW
MyRecords_DropDown = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]')
MyRecords_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 2 ATTENDANCE SUB-BUTTON ---------------------------------------------------------------------------------------------------
Attendance2_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
Attendance2_Button.click()
time.sleep(5)

# 2 PUNCH IN/OUT DROP-DOWN ARROW
PunchInOut_DropDown = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]')
PunchInOut_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 3 ATTENDANCE SUB-BUTTON ---------------------------------------------------------------------------------------------------
Attendance3_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
Attendance3_Button.click()
time.sleep(5)

# 3 EMPLOYEE RECORDS DROP-DOWN ARROW
EmployeeRecords_DropDown = driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]')
EmploymentStatus_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 4 ATTENDANCE SUB-BUTTON ---------------------------------------------------------------------------------------------------
Attendance4_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
Attendance4_Button.click()
time.sleep(5)

# 4 CONFIGURATION DROP-DOWN ARROW
Configuration_DropDown = driver.find_element(By.XPATH,
                                             '')
Configuration_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 11 REPORTS SUB-BUTTON ---------------------------------------------------------------------------------------------------
Reports11_Button = driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul')
Reports11_Button.click()
time.sleep(5)

# 11 PROJECT REPORTS DROP-DOWN ARROW
ProjectReports_DropDown = driver.find_element(By.XPATH,
                                              '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]')
ProjectReports_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 22 REPORTS SUB-BUTTON ---------------------------------------------------------------------------------------------------
Reports22_Button = driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul')
Reports22_Button.click()
time.sleep(5)

# 22 EMPLOYEE REPORTS DROP-DOWN ARROW
EmployeeReports_DropDown = driver.find_element(By.XPATH,
                                               '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]')
EmployeeEntitlements_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 33 REPORTS SUB-BUTTON --------------------------------------------------------------------------------------------------
Reports33_Button = driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul')
Reports33_Button.click()
time.sleep(5)

# ATTENDANCE SUMMARY DROP-DOWN ARROW
AttendanceSummary_DropDown = driver.find_element(By.XPATH,
                                                 '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]')
AttendanceSummary_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 1 PROJECT INFO SUB-BUTTON ---------------------------------------------------------------------------------------------------
ProjectInfo1_Button = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
ProjectInfo1_Button.click()
time.sleep(5)

# CUSTOMERS DROP-DOWN ARROW
Customers_DropDown = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]')
Customers_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 2 PROJECT INFO SUB-BUTTON ---------------------------------------------------------------------------------------------------
ProjectInfo2_Button = driver.find_element(By.XPATH,
                                          '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
ProjectInfo2_Button.click()
time.sleep(5)

# PROJECTS DROP-DOWN ARROW
Projects_DropDown = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[2]')
Projects_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# RECRUITMENT PAGE --------------------------------------------------------------------------------------------------
Recruitment_Button = driver.find_element(By.CSS_SELECTOR,
                                         '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(5) > a > span')
Recruitment_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# CANDIDATES SUB-BUTTON --------------------------------------------------------------------------------------------------
Candidates_Button = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Candidates_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# VACANCIES SUB-BUTTON ---------------------------------------------------------------------------------------------------
Vacancies_Button = driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
Vacancies_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# MY INFO PAGE ------------------------------------------------------------------------------------------------------
MyInfo_Button = driver.find_element(By.CSS_SELECTOR,
                                    '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(6) > a')
MyInfo_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# PERFORMANCE PAGE --------------------------------------------------------------------------------------------------
Performance_Button = driver.find_element(By.CSS_SELECTOR,
                                         '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(7) > a')
Performance_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 11 CONFIGURE SUB-BUTTON --------------------------------------------------------------------------------------------------
Configure11_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Configure11_Button.click()
time.sleep(5)

# 11 KPIs TRACKER DROP-DOWN ARROW
KPIsTracker_DropDown = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]')
KPIsTracker_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 22 CONFIGURE SUB-BUTTON ---------------------------------------------------------------------------------------------------
Configure22_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Configure22_Button.click()
time.sleep(5)

# TRACKERS DROP-DOWN ARROW
Tracker_DropDown = driver.find_element(By.XPATH,
                                       '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]')
Tracker_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# MANAGE REVIEWS SUB-BUTTON # ---------------------------------------------------------------------------------------------------
ManageReviews_Button = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
ManageReviews_Button.click()
time.sleep(5)

# MANAGE REVIEWS DROP-DOWN ARROW
ManageReviews_DropDown = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]')
ManageReviews_DropDown.click()
time.sleep(5)
# ---------------------------------------------------------------------------------------------------

# MANAGE REVIEWS SUB-BUTTON # ---------------------------------------------------------------------------------------------------
ManageReviews_Button = driver.find_element(By.XPATH,
                                           '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
ManageReviews_Button.click()
time.sleep(5)

# MY REVIEWS DROP-DOWN ARROW
MyReviews_DropDown = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]')
MyReviews_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# MANAGE REVIEWS DROP-DOWN ARROW ---------------------------------------------------------------------------------------------------
ManageReviews_DropDown = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]')
ManageReviews_DropDown.click()
time.sleep(5)

# EMPLOYEE REVIEWS SUB-BUTTON
EmployeeReviews_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[3]')
EmployeeReviews_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# MY TRACKERS PAGE ---------------------------------------------------------------------------------------------------
MyTrackers_Button = driver.find_element(By.XPATH,
                                        '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
MyTrackers_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# EMPLOYEE TRACKERS PAGE ---------------------------------------------------------------------------------------------------
EmployeeTrackers_Button = driver.find_element(By.XPATH,
                                              '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
EmployeeTrackers_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# DASHBOARD PAGE ----------------------------------------------------------------------------------------------------
Dashboard_Button = driver.find_element(By.CSS_SELECTOR,
                                       '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(8) > a')
Dashboard_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# DIRECTORY PAGE ----------------------------------------------------------------------------------------------------
Directory_Button = driver.find_element(By.CSS_SELECTOR,
                                       '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(9) > a')
Directory_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# MAINTENANCE PAGE --------------------------------------------------------------------------------------------------
Maintenance_Button = driver.find_element(By.CSS_SELECTOR,
                                         '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(10) > a > span')
Maintenance_Button.click()
time.sleep(5)
Cancel_Button = driver.find_element(By.CSS_SELECTOR,
                                    '#app > div.orangehrm-admin-access-container > div.orangehrm-card-container > form > div.orangehrm-admin-access-button-container > button.oxd-button.oxd-button--large.oxd-button--ghost.orangehrm-admin-access-button')
Cancel_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# CLAIM PAGE --------------------------------------------------------------------------------------------------------
Claim_Button = driver.find_element(By.CSS_SELECTOR,
                                   '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(11) > a')
Claim_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 01 CONFIGURATION SUB-BUTTON ---------------------------------------------------------------------------------------------------
Configuration01_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Configuration01_Button.click()
time.sleep(5)

# 01 EVENTS DROP-DOWN ARROW
Events_DropDown = driver.find_element(By.XPATH,
                                      '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[1]')
Events_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# 02 CONFIGURATION SUB-BUTTON ---------------------------------------------------------------------------------------------------

Configuration02_Button = driver.find_element(By.XPATH,
                                             '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]')
Configuration02_Button.click()
time.sleep(5)

# EXPENSE TYPES DROP-DOWN ARROW
ExpenseTypes_DropDown = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li[2]')
ExpenseTypes_DropDown.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# SUBMIT CLAIM SUB-BUTTON ---------------------------------------------------------------------------------------------------
SubmitClaim_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]')
SubmitClaim_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# MY CLAIMS SUB-BUTTON ---------------------------------------------------------------------------------------------------
MyClaims_Button = driver.find_element(By.XPATH,
                                      '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')
MyClaims_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# EMPLOYEE CLAIMS SUB-BUTTON ---------------------------------------------------------------------------------------------------
EmployeeClaims_Button = driver.find_element(By.XPATH,
                                            '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]')
EmployeeClaims_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------

# ASSIGN CLAIM SUB-BUTTON ---------------------------------------------------------------------------------------------------
AssignClaim_Button = driver.find_element(By.XPATH,
                                         '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]')
AssignClaim_Button.click()
time.sleep(5)

# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------

# BUZZ PAGE ---------------------------------------------------------------------------------------------------------
Buzz_Button = driver.find_element(By.CSS_SELECTOR,
                                  '#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(12) > a > span')
Buzz_Button.click()
time.sleep(5)

# Close the browser
driver.quit()
