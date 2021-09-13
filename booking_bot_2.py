from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import timedelta, date

currentDate = date.today() + timedelta(days=4)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://form.jotform.com/211996172097263")

tower = driver.find_element_by_id("input_34")
tower.click()
tower.send_keys(Keys.ARROW_DOWN)

unit = driver.find_element_by_id("input_35")
unit.send_keys("1708")

first = driver.find_element_by_id("first_29")
first.send_keys("Ray")

last = driver.find_element_by_id("last_29")
last.send_keys("Hao")

email = driver.find_element_by_id("input_30")
email.send_keys("ray.ray.hao@gmail.com")

phone1 = driver.find_element_by_id("input_31_area")
phone1.send_keys("613")

phone2 = driver.find_element_by_id("input_31_phone")
phone2.send_keys("415-2975")

system = driver.find_element_by_id("input_43_0")
system.click()

datePicker = driver.find_element_by_xpath("//div[@data-value='" + str(currentDate) + "']")
datePicker.click()

timePicker = driver.find_element_by_xpath("//div[@data-value='" + str(currentDate) + " 9:00 AM']")
timePicker.click()

covid1 = driver.find_element_by_id("input_47")
covid1.click()
covid1.send_keys(Keys.ARROW_DOWN)
covid1.send_keys(Keys.ARROW_DOWN)

covid1 = driver.find_element_by_id("input_48")
covid1.click()
covid1.send_keys(Keys.ARROW_DOWN)
covid1.send_keys(Keys.ARROW_DOWN)

covid1 = driver.find_element_by_id("input_49")
covid1.click()
covid1.send_keys(Keys.ARROW_DOWN)
covid1.send_keys(Keys.ARROW_DOWN)

covid1 = driver.find_element_by_id("input_50")
covid1.click()
covid1.send_keys(Keys.ARROW_DOWN)
covid1.send_keys(Keys.ARROW_DOWN)

#submit = driver.find_element_by_id("input_1")
#submit.click()

#driver.quit()
