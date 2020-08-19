import time
from selenium import webdriver
from playsound import playsound

# Windows webdriver
# driver = webdriver.Chrome('./chromedriver')

# Linux webdriver
driver = webdriver.Chrome('./chromedriver-linux')

SYMBOL = 'BTCUSDT'
TARGET = 11796
STATUS = 0

driver.get('https://www.tradingview.com/symbols/'+SYMBOL+'/')

result = driver.find_elements_by_class_name('tabValue-3iOTI9jm')


def play_sound(duration):
    for i in range(duration):
        playsound('./sound.mp3')
        time.sleep(1)


while True:
    if STATUS == 0:
        if float(result[1].text) >= TARGET:
            play_sound(5)
            STATUS = 1

    time.sleep(1)
