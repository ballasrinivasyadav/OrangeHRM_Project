from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Shetty")
driver.find_element_by_id("exampleCheck1").click()
#select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)
driver.find_element_by_xpath("//input[@name='email']").send_keys("Sweety")
driver.find_element_by_css_selector("input[type='submit']").click()
message = driver.find_element_by_class_name("alert-success").text

assert "sucess" in message