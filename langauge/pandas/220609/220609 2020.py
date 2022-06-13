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



f= open("l2020.csv",'w',encoding='UTF-8')
# f.write("2020년"+"\n")
f.write("순위,곡명,가수명,좋아요"+"\n")

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
    f.write(str(xpathn)+','+LO1+','+LO2+','+LO3+"\n")
f.write("\n")
f.close()
# while (True):
#     pass


data=read_csv("l2020.csv",encoding='UTF-8')
print(type(data))


import matplotlib.pyplot as plt
import numpy as np
font1={'family':'serif',
       'color':'b',
       'weight':'bold',
       'size':20
}

a= data.value_counts('가수명').head(5) #head 몇순위 까지 출력하는지 입력
print(a)
print(a[1],a[2],a[3])
print(a.head(2))
ai= a.index
am= a.idxmax()
print(ai[1])
print("가장 많이 순위에 등재된 가수: ",am)
print("가수별 순위에 몇번 등재됐는가?: %s" %data.value_counts('가수명'))


# print(a.loc[1])
# list(my_dataframe.columns.values)  # 열 헤더만 (제목)출력

plt.rcParams["font.family"]='Malgun Gothic'

aciN=[ai[0],ai[1],ai[2],ai[3],ai[4]] # 행 가수명
value=[a[0],a[1],a[2],a[3],a[4]]  #수치 순위등재 횟수.
colors=['#221121','#b2c1f2','#fa2cf2','#1111f2','#1313f2','#1312f2']
plt.ylim([0,10])
plt.bar(aciN,value,color=colors)   #바에 x,y값지정

# a= a1[0] ,a1[1], a1[2] +" 교통사고수 "
a= "가수 top50차트등재순위 "
plt.title(a)
plt.ylabel("건수")
plt.xlabel("분류")
plt.show()
