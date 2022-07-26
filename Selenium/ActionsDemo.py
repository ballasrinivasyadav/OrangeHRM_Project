
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()
action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()
action.double_click(driver.find_element_by_id("double-click")).perform()
Alert = driver.switch_to.alert

assert "You double clicked me!!!, You got to be kidding me" == Alert.text
Alert.accept()