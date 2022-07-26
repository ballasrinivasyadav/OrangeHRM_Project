from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element_by_id("autosuggest").send_keys("Ind")


countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

# for country in countries:
#     if country.text == "India":
#         country.click()
#         break

driver.quit()
