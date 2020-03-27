from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard

options = webdriver.ChromeOptions();
options.add_argument("--disable-notifications");

driver = webdriver.Chrome('./chromedriver.exe') 
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://play.typeracer.com/")
time.sleep(3)
keyboard.press_and_release('ctrl+alt+i')
time.sleep(12)
gameView = driver.find_elements_by_class_name("gameView")[0];
inputPanel = gameView.find_elements_by_class_name("inputPanel")[0]
textToInput = inputPanel.find_element_by_tag_name("tr")
textToInput = textToInput.find_element_by_tag_name("td")
textToInput = textToInput.find_element_by_tag_name("tbody")
textToInput = textToInput.find_element_by_tag_name("tr")
textToInput = textToInput.find_element_by_tag_name("td")
textToInput = textToInput.find_element_by_tag_name("div")
textToInput = textToInput.find_element_by_tag_name("div")
textToInput = textToInput.find_elements_by_tag_name("span")
text = ""
for i in range(len(textToInput)):
    if (i == 1):
        if (len(textToInput) % 2 == 0):
            text = text + textToInput[i].text
            continue
        else:
            text = text + textToInput[i].text + " "
            continue
    text = text + textToInput[i].text
time.sleep(2)
for i in text:
    if (i == " "):
        keyboard.press_and_release('space')
    else:
        keyboard.write(i)
    time.sleep(0.05)
