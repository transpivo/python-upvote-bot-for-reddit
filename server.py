import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import os

folder_path = "cookie"
files = os.listdir(folder_path)

for file in files:
    driver = webdriver.Firefox()
    driver.maximize_window() 
    file_path = os.path.join(folder_path, file) # Получаем полный путь к файлу
    with open(file_path, 'r') as file:
        cookies = json.load(file)
    driver.get('https://reddit.com')
            # загрукза куков
    for cookie in cookies:
            name = cookie['name']
            value = cookie['value']
            driver.add_cookie({'name' : name, 'value' : value})

    driver.refresh()