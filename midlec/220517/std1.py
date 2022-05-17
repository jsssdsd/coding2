from  selenium import webdriver
import time as t
from selenium.webdriver.common.by import By

# x= webdriver.ChromeOptions()
# x.add_argument("headless")
# x.add_argument('window-size = 1920x1080')
# browser = webdriver.Chrome("chromedriver.exe", options=x)
# browser.get("https://www.melon.com/")


# 모듈

x= webdriver.Chrome("chromedriver.exe")

def start(mode,url):


    if mode=="시작":
        x.get(url)
    if mode =="시간":
        t.sleep(a)