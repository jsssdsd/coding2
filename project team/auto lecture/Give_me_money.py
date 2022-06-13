import tkinter as tk
import time as t
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
from selenium.webdriver import ActionChains

option=webdriver.ChromeOptions()
option.headless=False
driver=webdriver.Chrome("chromedriver.exe", options=option)
driver.get('https://mcea.metiscloud.kr/')
driver.maximize_window()
driver.implicitly_wait(30)
t.sleep(2)

 #귀찮으면 인풋 빼고 그냥 문자열로 아이디 적어주세요.
 #마찬가지


#로그인
IDwin=driver.find_element_by_css_selector('#panel > div.page1 > div > div > table > tbody > tr > td > div > div.page_login_input_id > input')
IDwin.click()
pyautogui.write('ehdwls8533') #혹시 너무 빠르게 입력해서 메크로로 인식한다면 interval=0.25 속성값에 넣어주세요.
t.sleep(1)
PWwin=driver.find_element_by_css_selector('#panel > div.page1 > div > div > table > tbody > tr > td > div > div.page_login_input_pw > input[type=password]')
PWwin.click()
pyautogui.write('Ghktxld314?')
t.sleep(1)
Login=driver.find_element_by_css_selector('#panel > div.page1 > div > div > table > tbody > tr > td > div > div.button_black.page_login_input_login')
Login.click()
t.sleep(2)

#로그인 하자마자 나오는 창입니다. 아래 괄호에 아직 안들은 부분 CSS셀렉션 따서 넣어주시면 됩니다.

test1=driver.find_element_by_css_selector('#my_course > div:nth-child(2) > div.box_right > div.tbody_course > div:nth-child(2) > div.name')
test1.click()
t.sleep(2)

#한 번 더 들어가면 됩니다.  아래 괄호에 아직 안들은 부분 CSS셀렉션 따서 넣어주시면 됩니다.

test2=driver.find_element_by_css_selector('#l_classroom_page > div.div_table > div.div_table_tbody > div:nth-child(8) > div:nth-child(1) > div.div_td.open.pc_show > div')
test2.click()









#range 안에는 다음을 눌러야 하는 횟수 적어주시면 되는데 그냥 while문으로 바꿔도 될 것 같습니다. (끝내는 부분에 대한 코드는 없어요)
while True:
    t.sleep(5)
    driver.switch_to.frame(
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div/div/iframe'))
    driver.switch_to.frame(driver.find_element_by_xpath(('/html/body/iframe')))
    play_btn=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/p[3]')
    play_btn.click()

    print(driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div[3]/ul/li[3]').text)
    print(type(driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div[3]/ul/li[3]').text))
    sleeptime=driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div[3]/ul/li[3]').text
    sleepmin=sleeptime[0:2]
    print('분',sleepmin)
    sleepmin_sec=int(sleepmin)*60
    sleepsec=int(sleeptime[3:5])
    print('초',sleepsec)
    sumsleep=sleepmin_sec+sleepsec

    t.sleep(sumsleep)
    print('t.sleep완료')
    t.sleep(4)

    print(driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div').value_of_css_property('width')) #1000px이 되면 다음 누르게 해야 함
    print(type(driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div').value_of_css_property('width'))) #1000px이 되면 다음 누르게 해야 함

    if driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div').value_of_css_property('width')=='1000px':
        print('끝난 것 확인')
        driver.switch_to.default_content()
        driver.switch_to.default_content()
        next_btn=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/span[3]')
        next_btn.click()
        t.sleep(3)
    elif driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div[2]/div/div/div[2]/div').value_of_css_property('width')!='1000px':
        print('안끝났는데 걍 넘어감',i)
        driver.switch_to.default_content()
        driver.switch_to.default_content()
        next_btn=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[2]/div/span[3]')
        next_btn.click()
        t.sleep(3)
    else:
        pass


    # driver.switch_to.default_content()
    # driver.switch_to.default_content()
    # next_btn=driver.find_element_by_xpath('#wrapper > div.page1.play > div > div > div.play_container > div.play_nav > div > img.right.nav_right_btn')
    # next_btn.click()
    #
