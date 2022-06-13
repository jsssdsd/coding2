import tkinter as tk
from tkinter import *

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time as t
from selenium import webdriver
from matplotlib import font_manager, rc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#한글 깨짐문제 해결 메소드
from matplotlib import font_manager, rc
import pandas as pd
from pandas import *
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# from  selenium import webdriver
# import time as t
# from selenium.webdriver.common.by import By



a=0
fsong = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url ="https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2020"
fsong.get(url)
t.sleep(1)

fsong.execute_script('window.scrollTo(0, document.body.scrollHeight);') #스크롤 내리기

xpath1="/html/body/div/div[3]/div/div/div[4]/div/div[2]/div[1]/form/table/tbody/tr["
xpath3="]/td[4]/div/div/div[1]/span/strong/a"
xpath4="/html/body/div/div[3]/div/div/div[4]/div/div[2]/div[1]/form/table/tbody/tr["
xpath5="]/td[4]/div/div/div[2]/div[1]/a"
xpath6="/html/body/div/div[3]/div/div/div[4]/div/div[2]/div[1]/form/table/tbody/tr["
xpath7="]/td[5]/div/button/span[2]"

result1 = "/html/body/div/div[3]/div/div/div[4]/div/div[2]/div[1]/form/table/tbody/tr["
result2 = "]"



f= open("l1.csv",'w',encoding='UTF-8')
# f.write("2020년"+"\n")
f.write("곡명, 가수명, 좋아요,"+"\n")

for xpathn in range(1, 51):
    xpath100 = xpath1 + str(xpathn) + xpath3
    LO1 = fsong.find_element(By.XPATH, xpath100).text.replace(",","")
    print(LO1)


    xpath100 = xpath4 + str(xpathn) + xpath5
    LO2 = fsong.find_element(By.XPATH, xpath100).text.replace(",","")
    print(LO2)

    xpath100 = xpath6 + str(xpathn) + xpath7
    LO3 = fsong.find_element(By.XPATH, xpath100).text.replace(",","")
    print(LO3)
    f.write(LO1+','+LO2+','+LO3+"\n")
f.write("\n")

# f = pd.read_csv("l1.csv",  encoding='utf-8')
# csvWriter = csv.writer(f)
# csvWriter.writerow(LO3)
# for xpath2 in range(1, 50):
#     result1 ="/html/body/div[2]/div[3]/div/div/div[4]/div/div[2]/div[1]/form/table/tbody/tr["
#     result2 ="]/td[4]/div/div"
#     xpath100 = result1 + str(xpath2) + result2
#     LO = crolD.find_element(By.XPATH, xpath100).text


#
#
# fsong.find_element_by_xpath("/html/body/div/div[3]/div/div/div[3]/div[3]/button[2]").click()
# t.sleep(1)
# # fsong.switch_to.frame("window")
#
# fsong.execute_script('window.scrollTo(0, document.body.scrollHeight);')


# f.write("2021년"+"\n")
# f.write("곡명, 가수명, 좋아요,"+"\n")
#
# for xpathn in range(1, 51):
#     xpath100 = xpath1 + str(xpathn) + xpath3
#     LO1 = fsong.find_element(By.XPATH, xpath100).text.replace(",","")
#     print(LO1)
#
#     xpath100 = xpath4 + str(xpathn) + xpath5
#     LO2 = fsong.find_element(By.XPATH, xpath100).text.replace(",","")
#     print(LO2)
#
#     xpath100 = xpath6 + str(xpathn) + xpath7
#     LO3 = fsong.find_element(By.XPATH, xpath100).text.replace(",","")
#     print(LO3)
#     f.write(LO1+','+LO2+','+LO3+"\n")
# f.write("\n")
# f.close()
# while (True):
#     pass


data=read_csv("l1.csv",encoding='UTF-8')
print(data)
print(type(data))


while True:
    search=input("검색 년 입력:")
    if search=="2020":
        data = read_csv("l2020.csv", encoding='utf-8')
        while search:
            rank = input("순위검색 or 가수검색:")
            if rank=="순위":
                InputRank = input("순위입력")
                try:
                    result0 = data.loc[data['순위'] ==int(InputRank)]
                    print(result0)
                    break
                except:
                    print("50이하의 숫자를 입력하세요.")
                    continue
            elif rank=="가수":
                InputSinger = input("가수입력")
                try:
                    result0 = data.loc[data['가수명'] == InputSinger]
                    print(result0)
                    break
                except:
                    print("50이하의 숫자를 입력하세요.")
                    continue
            else:
                print("잘못 입력하셨습니다. 2020 or 2021을 입력해주세요.")
                print("*" * 200)
                continue
    elif search=="2021":
        data1 = read_csv("l2021.csv", encoding='utf-8')
        while search:
            rank = input("순위검색 or 가수검색:")
            if rank == "순위":
                InputRank = input("순위입력")
                try:
                    result0 = data.loc[data['순위'] == int(InputRank)]
                    print(result0)
                    break
                except:
                    print("50이하의 숫자를 입력하세요.")
                    continue
            elif rank == "가수":
                InputSinger = input("가수입력")
                try:
                    result0 = data.loc[data['가수명'] == InputSinger]
                    print(result0)
                    break
                except:
                    print("잘못 입력하셨습니다.")
                    continue
            else:
                print("잘못 입력하셨습니다. 2020 or 2021을 입력해주세요.")
                print("*" * 200)
                continue
    else:
        print("잘못 입력하셨습니다. 2020 or 2021을 입력해주세요.")
        print("*"*200)
        continue

