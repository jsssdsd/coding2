import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
import module as m

path = './userlist'
userlist=os.listdir(path)

font_path = "C:/Windows/Fonts/malgun.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font)
barcolors=['indianred','sandybrown','gold','lightgreen','powderblue','cornflowerblue','mediumpurple','pink']

def makenamedata():
    namelist=[]
    for u in userlist:
        if u[2].isdigit():
            namelist.append(u[:2])
        else:
            namelist.append(u[:3])
    return namelist

def makenumdata():
    import re
    numlist=[]
    for i in userlist:
        num = re.compile(r'\d\d\d\d')
        result2 = re.findall(num,i)
        numlist.append(result2[0])
    return numlist

namedata=makenamedata()[1:]
numdata=makenumdata()[1:]

#사용자 리스트 익명화
def anonymity():
    xlist=[]
    for u in userlist:
        u=u.replace(u[2],'*') #익명
        xlist.append(u[:3])
    return xlist[1:]

#모든 사용자의 출석부 리스트 만드는 함수
def total_rollbook():
    Alist=[]
    for i in range(len(namedata)):
        Alist.append(m.rollbook(namedata[i],numdata[i]))
    return Alist

#'userlist'디렉토리의 모든 출석부 리스트
rlist=total_rollbook()

#사용자별 출석일 리스트
def total_Adays():
    y_data_Adays=[]
    for i in rlist:
        r=m.Adays(i)
        y_data_Adays.append(r)
    return y_data_Adays

x_data = anonymity()  # x축, 사용자 이름
y_data = total_Adays()  # y축, 사용자별 출석일
x= np.arange(len(x_data))  # 주어진 범위와 간격에 따라 균일한 값을 갖는 어레이를 반환
y = np.arange(0, 96, 5)
plt.figure('Attendance')
plt.title('수강생별 출석일')
plt.xticks(x, label=x_data)  # .xticks(x축 눈금 레이블, label=x축 데이터)
plt.xlabel('총 출석일: 95일')
plt.ylim([0, 95])
plt.yticks(y, label=y_data)
plt.ylabel('출석 일수')
plt.grid(True, axis='y', alpha=0.5)
for i in range(1, len(x_data) + 1):
    plt.text(i - 1, y_data[i - 1], y_data[i - 1], ha='center', size=8)
plt.bar(x_data, y_data, color=barcolors, width=0.5)
plt.show()