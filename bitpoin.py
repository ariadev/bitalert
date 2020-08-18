import time
from selenium import webdriver
from playsound import playsound

driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.tradingview.com/symbols/BTCUSDT/')
result = driver.find_elements_by_class_name('tabValue-3iOTI9jm')
target = 12000
status = 0


def play_sound(duration):
    for i in range(int(duration)):
        playsound('./sound.mp3')
        time.sleep(1)


while True:
    if status == 0:
        if float(result[1].text) >= target:
            play_sound(5)
            status = 1

    time.sleep(1)
