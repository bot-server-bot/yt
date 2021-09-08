from selenium import webdriver
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)


no_of_driver = 10
url = "https://youtu.be/1B-5I2oBuf8"
time_to_refresh = 30
drivers = []

for i in range(no_of_driver):
    drivers.append(driver)
    drivers[i].get(url)
while True:
    time.sleep(time_to_refresh)
    for i in range(no_of_driver):
        drivers[i].refresh()
