from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C://Users//Srinivas//PycharmProjects//Udemy//Selenium//Drivers//chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
ChildWindow = driver.window_handles[1]
driver.switch_to.window(ChildWindow)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])

assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
