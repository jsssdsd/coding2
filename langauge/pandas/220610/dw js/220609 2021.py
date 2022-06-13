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
url ="https://www.melon.com/chart/age/index.htm?chartType=YE&chartGenre=KPOP&chartDate=2021"
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



f= open("l12021.csv",'w',encoding='UTF-8')
# f.write("2021년"+"\n")
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

import matplotlib.pyplot as plt
import numpy as np
font1={'family':'serif',
       'color':'b',
       'weight':'bold',
       'size':20
}
data=read_csv("l12021.csv",encoding='UTF-8')

plt.rcParams["font.family"]='Malgun Gothic'
ac= data.value_counts('가수명')
print("2021년 가수별 랭킹에 등재된 횟수",ac)
am =data.value_counts('가수명').idxmax()
print("2021년 가수별 랭킹에 가장많이 등재된 가수: ",am)
ami=data.value_counts('가수명').head(5)

av=data.value_counts('가수명')[0]

print("1등빈번도",av)
print(ami)
print(ami[0],ami[1])

x=np.arange(5)
print(x)
values=np.array(ami[0:].tolist())
print(values)


amq =data.value_counts('가수명').head().index
print("amq출력",amq,a)

aciN=[amq[0],amq[1],amq[2],amq[3],amq[4]]
value=[ami[0],ami[1],ami[2],ami[3],ami[4]]
colors=['#ba0128','#141362','#331322','#2a1ff2','#dda3d2','#c3b2a2']
plt.ylim([0,10])
plt.bar(aciN,value,color=colors)   #바에 x,y값지정

plt.title(a)
plt.ylabel("건수")
plt.xlabel("분류")
plt.show()
