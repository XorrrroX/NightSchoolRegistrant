import os
import time
import base64
import ddddocr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib
import sched

def getscImg():
    img_base64 = driver.execute_script("""
    var ele = arguments[0];
    var cnv = document.createElement('canvas');
    cnv.width = ele.width; cnv.height = ele.height;
    cnv.getContext('2d').drawImage(ele, 0, 0);
    return cnv.toDataURL('image/jpeg').substring(22);    
    """, driver.find_element(By.XPATH, "/html/body/div[2]/div/span/img"))
    return img_base64

def saveImg(img):
    with open("captcha_login.png", 'wb') as image:
        image.write(base64.b64decode(img))
    return
def getscAnswer():
    ocr = ddddocr.DdddOcr()
    with open("captcha_login.png", 'rb') as f:
        img_bytes = f.read()
    res = ocr.classification(img_bytes)
    return res

service = Service(executable_path=r'D:\NightSchoolSigner\chromedriver-win64\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service,options = options)
driver.implicitly_wait(10)
driver.get("https://2www.tcssh.tc.edu.tw/nightschool/index.html")
driver.implicitly_wait(10)
q = driver.find_element(By.ID, 'a_login_student')
q.send_keys(Keys.TAB)
q.send_keys(Keys.ENTER)
q = driver.find_element(By.ID, 'txt_student_id')
name = input()
q.send_keys(name)
q = driver.find_element(By.ID, 'txt_student_password')
pw = input()
q.send_keys(pw)
q = driver.find_element(By.ID, 'txt_student_sc')
time.sleep(1)
img = getscImg()
saveImg(img)
answer = getscAnswer()
q.send_keys(answer)
q = driver.find_element(By.ID, 'but_student_login')
q.click()
def register():
    p = driver.find_element(By.XPATH, '/html/body/div/div[2]/ul/li[3]')
    p.click()
    p = driver.find_element(By.XPATH, '//*[@id="check_book"]')
    p.click()
    p = driver.find_element(By.XPATH, '/html/body/div/div[3]/div[5]/div[2]/div/button')
    p.click()
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    return

schedule = sched.scheduler(time.time, time.sleep)
schedule.enterabs(time.mktime(time.strptime('2023-10-06 00:01:00', '%Y-%m-%d %H:%M:%S')), 0, register, ())
schedule.run()


