from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions();
options.add_argument("--disable-notifications");

driver = webdriver.Chrome('./chromedriver.exe') 
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.facebook.com/")
email_emt = driver.find_element_by_id("email")
email_emt.send_keys("username")
password_emt = driver.find_elements_by_id("pass")[0]
password_emt.send_keys("password")
submit_btn_emt = driver.find_elements_by_id("loginbutton")[0]
submit_btn_emt.click()
parentElement = driver.find_elements_by_id("universalNav")[0]
childElement = parentElement.find_elements_by_tag_name("ul")[0]
cchildElement = childElement.find_elements_by_tag_name("li")[1]
anchorElement = cchildElement.find_elements_by_tag_name("a")[0]
anchorElement.send_keys("\n")
time.sleep(2)
parentElement = driver.find_element_by_xpath("//div[@aria-label='New message']")
textbox_element = parentElement.find_elements_by_class_name("notranslate")[0]
textbox_element.send_keys("SENT BY SELENIUM!!!\n")
