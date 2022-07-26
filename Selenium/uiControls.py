from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
check_boxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(check_boxes))
for checkbox in check_boxes:

    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()

radiobottons = driver.find_elements_by_name("radioButton")
radiobottons[2].click()
assert radiobottons[2].is_selected()
assert print(driver.find_element_by_id("displayed-text").is_displayed())
driver.find_element_by_id("hide-textbox").click()
assert not print(driver.find_element_by_id("displayed-text").is_displayed())



driver.quit()
