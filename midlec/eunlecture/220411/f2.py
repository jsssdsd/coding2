import time as t
print(t.time())
#UTC 시간을 기준으로 얼마나 경과
#UTC 협정 세계 표준시 1970년 1월 1일 0시 0분 0초

#초단위
#실수 형태

print(t.localtime())
print(t.localtime())
#연도 월 일 시간 분 초 요일 등 형태로 표현하는 함수

#struct time

print(t.asctime(t.localtime())) #asctime
print(type(t.asctime(t.localtime())))

print(t.ctime())


print(t.strftime('%p',t.localtime()))

print(t.strftime('%S',t.localtime()))

#a 요일
#A 요일 풀네임

#b 달 줄임말
#B 달 풀네임
#d 날짜
#H 시간
#M 분
#S 초
#p pm am 오전 후
#Y 년

#W 요일  월~ 일 1~7

for i in range(5):

    print(i)
    t.sleep(0.0010)  # 텀을 준다. input은 입력할때까지 계속이지만 t.sleep은 초가 지날때까지 홀딩



import  calendar as c
print(c.calendar(2022,10))

print(c.weekday(2015,1,1))

print(c.monthrange(2022,10))  #0~6  월~ 일  출력된다.  숫자로 요일에 따라

import random as rd
for i in range(100):
    print(rd.random())



#random 모듈의 random 함수
#0.0~  1.0 사이의 실수 형태 난수 생성.


listx=[]
for i in range(100000):
    listx.append(int(rd.random()*11)+20)
print("xxxxxxxxxxxxxxx")
print(max(listx))