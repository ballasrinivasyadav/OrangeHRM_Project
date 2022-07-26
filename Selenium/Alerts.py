# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome("C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
# driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.find_element_by_css_selector("#name").send_keys("option3")
# driver.find_element_by_id("alertbtn").click()
# alert = driver.switch_to.alert
# print(alert.text)
# alert.accept()

# In otherway to validate our alerts test cases:

from selenium import webdriver
from selenium.webdriver.common.by import By
validateText = "option3"
driver = webdriver.Chrome("C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element_by_css_selector("#name").send_keys("validateText ")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()

# for to cancel the pop ups....
alert.dismiss()