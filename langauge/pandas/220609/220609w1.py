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


data=read_csv("l2020.csv",encoding='utf-8')
data1=read_csv("l2021.csv",encoding='utf-8')
a=data1['순위'] #순위값의 밸류만 뽑음.
aval=a.values
print('aval',aval)

def plus(x):
    return x+50

result=data1['순위'].apply(plus)
data1['순위']= data1['순위'].replace(aval.tolist(),result) #t순위를 50에서 100으로 증가 apply 로 판다스  csv문서에 함수를 적용시킨다!!!!
df= merge(data,data1,how='outer')
print(df)
df.to_csv('melon_all.csv')

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
                    result0 = data1.loc[data1['순위'] == int(InputRank)]
                    print(result0)
                    break
                except:
                    print("50이하의 숫자를 입력하세요.")
                    continue
            elif rank == "가수":
                InputSinger = input("가수입력")
                try:
                    result0 = data1.loc[data1['가수명'] == InputSinger]
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

