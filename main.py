from selenium import webdriver
import time

no_of_driver = 10
url = "https://youtu.be/1B-5I2oBuf8"
time_to_refresh = 30
drivers = []

for i in range(no_of_driver):
    drivers.append(webdriver.Chrome(executable_path='driver/chromedriver'))
    drivers[i].get(url)
while True:
    time.sleep(time_to_refresh)
    for i in range(no_of_driver):
        drivers[i].refresh()