import time
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
URL ='https://www.facebook.com/marketplace/105756796124329/vehicles?minPrice=2024&maxPrice=100000&maxMileage=200000&maxYear=2023&minMileage=20000&minYear=1995&topLevelVehicleType=car_truck&exact=false'
driver = webdriver.Chrome()
driver.get(URL)
SCROLL_PAUSE_TIME = 10
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
time.sleep(15)
results = driver.find_element(By.XPATH,'//*[@id="facebook"]/body')
output=results.text
with open('facebookcars.txt', 'w', encoding='utf-8') as f:
    for line in output:
        f.write(line)





