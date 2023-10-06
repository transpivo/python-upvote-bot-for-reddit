import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
import random
import os
url = input('линк на пост который нужно поднять : ')
count_up = int(input('количество апвоутов : ')) 
index = 0 # пересчет апвоутов
def upvote(files_c, proxy):
    print('proxy : ' + proxy)
    options = Options()
    options.add_argument(f'--proxy-server={proxy}')

    driver = webdriver.Firefox(options = options)

    driver.maximize_window() 
        # чтение куков
    with open(files_c, 'r') as file:
        cookies = json.load(file)

    driver.get('https://reddit.com')
        # загрукза куков
    for cookie in cookies:
        name = cookie['name']
        value = cookie['value']
        driver.add_cookie({'name' : name, 'value' : value})

    driver.get(url)
    wait = WebDriverWait(driver, 15) # закрыть pop-up
    # проверка на наличие pop-up'a выбора интереса. 
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/div/div/header/div/div[2]/button")))
        elements = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[4]/div/div/div/header/div/div[2]/button")
        elements.click()
    except:
        wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/button[1]")))
        
        upvote = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div[3]/div[1]/div/div[1]/div/button[1]")
        upvote.click()
        time.sleep(5)
        driver.quit()

folder_path = "cookie"
folder_path_proxy1 = "proxy"
files_p = os.listdir(folder_path_proxy1)
files_c = os.listdir(folder_path)
proxy_arr = []
for file_p in files_p:
        file_path_proxy = os.path.join(folder_path_proxy1, file_p)
        with open(file_path_proxy, 'r') as file:
            proxy = file.readlines()
            proxy_arr.extend(proxy)        


for file_c in files_c:
    file_path = os.path.join(folder_path, file_c) # Получаем полный путь к файлу
    proxy_df = random.randint(0,len(proxy_arr) - 1)
    upvote(file_path, proxy_arr[proxy_df])
    index += 1 
    # проверка равен ли апвот по счету нужному нам количеству.
    if index == count_up:
        print('апвоуты поставил.')
        break




