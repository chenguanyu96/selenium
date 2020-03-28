from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import keyboard
import string
from random import randint
from random import sample

numOfMistakes = randint(1, 4)
options = webdriver.ChromeOptions();
options.add_argument("--disable-notifications");

driver = webdriver.Chrome('./chromedriver.exe') 
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://play.typeracer.com/")
time.sleep(3)
keyboard.press_and_release('ctrl+alt+o')
time.sleep(3)
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
posOfMistakes = []
for i in range(len(textToInput)):
    if (i == 1):
        if (len(textToInput) % 2 == 0):
            if (textToInput[i].text[0] in string.punctuation):
                text = text + textToInput[i].text
            else:
                text = text + " " + textToInput[i].text
            continue
        else:
            if (textToInput[i+1].text[0] in string.punctuation):
                text = text + textToInput[i].text
            else:
                text = text + textToInput[i].text + " "
            continue
    text = text + textToInput[i].text
time.sleep(2)
for i in range(numOfMistakes):
    tempPos = randint(0, len(text)-1)
    while (tempPos in posOfMistakes):
        tempPos = randint(0, len(text)-1)
    posOfMistakes.append(tempPos)
for i in range(len(text)):
    if (text[i] == " "):
        keyboard.press_and_release('space')
    else:
        keyboard.write(text[i])
        if (i in posOfMistakes):
            numOfWLetters = randint(1,3)
            keyboard.write("".join(sample(string.ascii_letters, numOfWLetters)))
            time.sleep(1)
            for i in range(numOfWLetters):
                keyboard.press_and_release('backspace')
    time.sleep(0.05)
