from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
import time
from utils import *

data = File_Interact('data.txt').read_file_list()
list_keyword = File_Interact('keyword.txt').read_file_list()

options  = webdriver.ChromeOptions()
user_data_path = f'{data[0]}'
options.add_argument('--remote-debugging-port=9222')
options.add_argument(f'user-data-dir={user_data_path}')
options.add_argument(f'profile-directory={data[1]}')
driver = webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=options)

while True:
    try:
        driver.get('https://www.ebay.com/')
        keyword = list_keyword[random.randint(0,len(list_keyword)-1)]
        print('keyword: ',keyword)
        # input key word
        WebDriverWait(driver , 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[aria-label="Search for anything"]')))
        driver.find_elements_by_css_selector('input[aria-label="Search for anything"]')[0].send_keys(keyword)
        #click tim kiem
        WebDriverWait(driver , 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="submit"]')))
        driver.find_elements_by_css_selector('input[type="submit"]')[0].click()
        # get_link sp
        WebDriverWait(driver , 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'ul[class="srp-results srp-list clearfix"]')))
        js = '''return document.querySelectorAll('a[class="s-item__link"]').length'''
        len_sp = driver.execute_script(js)
        len_sp_review = random.randint(3,5)
        list_link = []
        for i in range(2,len_sp_review+3):
            js = f'''return document.querySelectorAll('a[class="s-item__link"]')[{i}].href'''
            link = driver.execute_script(js)
            list_link.append(link)

        for i in range(len(list_link)):
            try:
                driver.get(list_link[i])
                print(list_link[i])
                #click xem anh
                WebDriverWait(driver , 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[id="vi-img-overlay--trans"]')))
                driver.find_elements_by_css_selector('div[id="vi-img-overlay--trans"]')[0].click()

                for j in range(30):
                    js = '''return document.querySelectorAll('ul[class="lst icon"]').length'''
                    len_icon = driver.execute_script(js)
                    if len_icon>1:
                        break
                    else:
                        time.sleep(2)

                js = '''return document.querySelectorAll('ul[class="lst icon"]')[1].querySelectorAll('button[class="pic pic1"]').length'''
                len_img = driver.execute_script(js)
                for i in range(len_img):
                    try:
                        js = f'''document.querySelectorAll('ul[class="lst icon"]')[1].querySelectorAll('button[class="pic pic1"]')[{i}].click()'''
                        driver.execute_script(js)
                        time.sleep(random.randint(10,20))
                    except:
                        time.sleep(random.randint(10,20))
                        continue

                #close image tab
                js = '''document.querySelectorAll('div[id="viEnlargeImgLayer"]')[0].querySelectorAll('button[aria-label="Close modal dialog"]')[0].click()'''
                driver.execute_script(js)
                Y = 0
                # scroll
                while True:
                    Y += 100
                    print(Y)
                    driver.execute_script(f"window.scrollTo(0, {Y})")
                    if Y == 6500:
                        break
                    else:
                        time.sleep(random.randint(3,5))

                # click anh
                try:
                    js = '''return document.querySelectorAll('img[class="reviews-thumbnail"]').length'''
                    len_img_click = driver.execute_script(js)       
                except:
                    pass
                print('len image: ',len_img_click)
                if len_img_click != 0:
                    for i in range(len_img_click):
                        try:
                            js = f'''document.querySelectorAll('img[class="reviews-thumbnail"]')[{i}].click()'''
                            driver.execute_script(js)
                            time.sleep(random.randint(10,20))
                        except:
                            pass
                        try:
                            WebDriverWait(driver , 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[class="reviews-thumbnail"]')))
                        except:
                            pass
                        try:
                            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                        except:
                            pass

                time_sleep = random.randint(150,200)
                print('time_sleep: ',time_sleep)
                Y = 0

                for i in range(int(time_sleep/2)):
                    Y += 50
                    driver.execute_script(f"window.scrollTo(0, {Y})")
                    print(Y)
                    time.sleep(2)

                Y += 500
                for i in range(int(time_sleep/2)):
                    Y -= 50
                    driver.execute_script(f"window.scrollTo(0, {Y})")
                    time.sleep(2)
            except:
                print('Link Fail!')
    except:
        print('NEXT KEYWORD!')