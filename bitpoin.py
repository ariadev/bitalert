import time
import sys
from selenium import webdriver
from playsound import playsound
from colorama import Fore

SYMBOL = 'BTCUSDT'
print('enter your UP_TARGET:')
UP_TARGET = float(input())
print('you entered ' + str(UP_TARGET) + ' as your UP_TARGET')
UP_STATUS = 0

print('enter your DOWN_TARGET:')
DOWN_TARGET = float(input())
print('you entered ' + str(DOWN_TARGET) + ' as your DOWN_TARGET')
DOWN_STATUS = 0

PREVIUS_PRICE = 0

# Windows webdriver
# driver = webdriver.Chrome('./chromedriver')

# Linux webdriver
driver = webdriver.Chrome('./chromedriver-linux')

driver.get('https://www.tradingview.com/symbols/'+SYMBOL+'/')
result = driver.find_elements_by_class_name('tabValue-3iOTI9jm')


def play_sound(duration):
    for i in range(duration):
        playsound('./sound.mp3')
        time.sleep(1)


def remove_last_line():
    sys.stdout.write("\033[F")  # Cursor up one line
    sys.stdout.write("\033[K")  # Cursor up one line


def check_stats_of_price(price):
    global PREVIUS_PRICE

    if PREVIUS_PRICE != 0 and price > PREVIUS_PRICE:
        print(Fore.GREEN + 'PRICE GOES UP | ' + str(price))
        remove_last_line()

    if PREVIUS_PRICE != 0 and price < PREVIUS_PRICE:
        print(Fore.RED + 'PRICE GOES DOWN | ' + str(price))
        remove_last_line()


def money_tracking():
    global UP_STATUS
    global DOWN_STATUS
    global PREVIUS_PRICE

    while True:
        PREVIUS_PRICE = float(result[1].text)
        time.sleep(1)

        check_stats_of_price(float(result[1].text))

        if UP_STATUS == 0:
            if float(result[1].text) >= UP_TARGET:
                play_sound(5)
                UP_STATUS = 1

        if DOWN_STATUS == 0:
            if float(result[1].text) <= DOWN_TARGET:
                play_sound(5)
                DOWN_STATUS = 1


if __name__ == "__main__":
    money_tracking()
