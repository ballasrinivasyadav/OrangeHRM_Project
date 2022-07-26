import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
#driver = webdriver.GeckoDriver(executable_path="C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//geckodriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_css_selector("[name='name']").send_keys("Srinivas")
driver.find_element_by_css_selector("[name='email']").send_keys("Shetty")
driver.find_element_by_id("exampleCheck1").click()
sel = Select(driver.find_element_by_id("exampleFormControlSelect1"))
sel.select_by_visible_text("Male")
driver.find_element_by_xpath("//input[@class='btn btn-success']").click()
alertText = driver.find_element_by_css_selector("[class*='alert-success']").text
assert ("Success" in alertText)
print(alertText)




