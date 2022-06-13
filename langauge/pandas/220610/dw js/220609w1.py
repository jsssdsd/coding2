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

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# from  selenium import webdriver
# import time as t
# from selenium.webdriver.common.by import By

fsong = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



data1=read_csv("l12020.csv",encoding='UTF-8')
data2=read_csv("l12021.csv",encoding='UTF-8')
print(data1)
print(type(data1))

def addappen(x):
    return x+50

a=data1['순위']
aval=a.values
print(aval)
result=data2['순위'].apply(addappen)

data2['순위']= data2['순위'].replace(aval.tolist(),result)  #(a,b) a> b로 바꾼다.
df= merge(data1,data2,how='outer')
print(df)
df.to_csv('lMel.csv')

data_all=read_csv("lMel.csv",encoding='utf-8')



while True:
    search=input("검색 년도 입력:")
    if search=="2020":
        data = read_csv("l12020.csv", encoding='utf-8')

        while search:
            rank = input("순위검색 or 가수검색:")
            if rank=="순위":
                inprk = input("순위입력")
                try:
                    result0 = data1.loc[data['순위'] ==int(inprk)]
                    print(result0)
                    break
                except:
                    print("50이하의 숫자를 입력하세요.")
                    continue
            elif rank=="가수":
                InpS = input("가수입력")
                try:
                    result0 = data1.loc[data['가수명'] == InpS]
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
        data2 = read_csv("l12021.csv", encoding='utf-8')

        while search:
            rank = input("순위검색 or 가수검색:")
            if rank == "순위":
                inprk = input("순위입력")
                try:
                    result0 = data2.loc[data2['순위'] == int(inprk)]
                    print(result0)
                    break
                except:
                    print("50이하의 숫자를 입력해주세요 .")
                    continue
            elif rank == "가수":
                InpS = input("가수입력")
                try:
                    result0 = data2.loc[data2['가수명'] == InpS]
                    print(result0)
                    break
                except:
                    print("잘못 입력하셨습니다.")
                    continue
            else:
                print("잘못 입력하셨습니다. 2020년이나  2021년을 입력해주세요.")
                print("*" * 200)
                continue
    else:
        print("잘못 입력하셨습니다. 2020 or 2021을 입력해주세요.")
        print("*"*200)
        continue