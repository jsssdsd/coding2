




#sel stdy #6조 기본코드 복사본.



import os
import webbrowser
import time as t
from selenium import webdriver
# 병원 목록 모듈
listH=[]
def Hsearch():
    global listH
    #웹페이지 연결

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('window-size=1920x1080')
    import time as t
    browser=webdriver.Chrome("chromedriver.exe",options=options)
    browser.get("https://map.naver.com/v5/search/%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90")

    #내 위치 입력
    t.sleep(2)
    my_lctn=browser.find_element_by_class_name("btn_location")
    my_lctn.click()

    #내 위치에서 검색
    t.sleep(2)
    Mlsrch=browser.find_element_by_class_name("btn_text")
    Mlsrch.click()

    # 크롤링하기
    # 프레임 안에 들어가기
    browser.switch_to.frame('searchIframe')
    t.sleep(2)

    # 프레임안에 있는 정보가져오기
    # 주소 전처리