import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
action = ActionChains(driver)
menu = driver.find_element_by_css_selector("#mousehover")
action.move_to_element(menu).perform()
ChildMenu = driver.find_element_by_link_text("Top").click()
action.move_to_element(ChildMenu).perform()
