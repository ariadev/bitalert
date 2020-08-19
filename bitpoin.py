import time
import sys
from selenium import webdriver
from playsound import playsound

SYMBOL = 'BTCUSDT'
print('enter your target:')
TARGET = float(input())
print('you entered ' + str(TARGET) + ' as your target')
STATUS = 0
PREVIUS_PRICE = 0

# Windows webdriver
driver = webdriver.Chrome('./chromedriver')

# Linux webdriver
# driver = webdriver.Chrome('./chromedriver-linux')

driver.get('https://www.tradingview.com/symbols/'+SYMBOL+'/')
result = driver.find_elements_by_class_name('tabValue-3iOTI9jm')


def play_sound(duration):
    for i in range(duration):
        playsound('./sound.mp3')
        time.sleep(1)


def remove_last_line():
    sys.stdout.write("\033[F") # Cursor up one line
    sys.stdout.write("\033[K") # Cursor up one line


def check_stats_of_price(price):
    global PREVIUS_PRICE

    if price > PREVIUS_PRICE and PREVIUS_PRICE != 0:
        print('PRICE GOES UP')
        remove_last_line()

    if price < PREVIUS_PRICE and PREVIUS_PRICE != 0:
        print('PRICE GOES DOWN')
        remove_last_line()


def money_tracking():
    global STATUS
    global PREVIUS_PRICE

    while True:
        PREVIUS_PRICE = float(result[1].text)
        time.sleep(1)

        check_stats_of_price(float(result[1].text))

        if STATUS == 0:
            if float(result[1].text) >= TARGET:
                play_sound(5)
                STATUS = 1


if __name__ == "__main__":
    money_tracking()
