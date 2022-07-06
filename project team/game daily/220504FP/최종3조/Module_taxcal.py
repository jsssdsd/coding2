# 자동차 세액 계산 module

import os.path #path경로를 가져오기 위한 모듈
path= "taxcal.py"
os.path.isfile(path) #path변수에 저장되어 있는 파일이 존재하는지 여부
#...데이터 파일 불러오기
file1=open("자동차 목록.txt",'r',encoding='UTF-8')

d1=file1.readlines()
d2=list(d1)
l1=[]
n1=[]
e1=[]
b1=[]
p1=[]
we1=[]
d1= d1[1:]
myc1=[]
myc2=[]
CarIdex={}
mycarex=0


class car1: #카의 항목 클래스화
    def __init__(self,carN,carEx,carybene,carPri,carWEneg):
        self.N=carN
        self.E=carEx
        self.b=carybene
        self.p=carPri
        self.WE=carWEneg

    # def taxcal(self):
    #     self.

for i in range(len(d1)):
    d1[i]= d1[i].replace('\t', ',')
    d1[i] = d1[i].replace('\n', '')
    d1[i]= d1[i].split(',')

for i in range(len(d1)):
    l1.append(car1(d1[i][0],d1[i][1],d1[i][2],d1[i][3],d1[i][4]))
    n1.append(l1[i].N)
    e1.append(l1[i].E)
    b1.append(l1[i].b)
    p1.append(l1[i].p)
    we1.append(l1[i].WE)
    CarIdex[n1[i]]= [e1[i],b1[i],p1[i],we1[i]]

stringTemp=""


def alonecarlist(): #단일메뉴에 메뉴판출력
    global CarIdex
    for i in list(CarIdex):
        return list(CarIdex).index(i)+1, i, "배기량:",CarIdex[i][0]

def texcal(car,ty):
    global myc1
    global CarIdex
    global mycarex
    global stringTemp
    alonecarlist()
    if car in CarIdex:
        myc1.append(car)
        myc1.append(CarIdex[car])
        if ty==0:
            if int(myc1[1][0])<=1000:
                mycarex = int(myc1[1][0])*18
                return mycarex
            elif 1000<int(myc1[1][0])<=1600:
                mycarex = int(myc1[1][0])*18
                return mycarex
            elif 1600<int(myc1[1][0])<=2000:
                mycarex = int(myc1[1][0])*19
                return mycarex
            elif 2000<int(myc1[1][0])<=2500:
                mycarex = int(myc1[1][0])*19
                return mycarex
            elif int(myc1[1][0])>=2500:
                mycarex = int(myc1[1][0])*24
                return mycarex
        elif ty==1:
            if int(myc1[1][0])<=1000:
                mycarex = int(myc1[1][0])*80
                return mycarex
            elif 1000<int(myc1[1][0])<=1600:
                mycarex = int(myc1[1][0])*140
                return mycarex
            elif 1600<int(myc1[1][0])<=2000:
                mycarex = int(myc1[1][0])*200
                return mycarex
            ################################
            elif 2000<int(myc1[1][0])<=2500:
                mycarex = int(myc1[1][0])*260
                return mycarex
            elif 2500<=int(myc1[1][0]):
                mycarex = int(myc1[1][0])*320
                return mycarex
        else:
            return "잘못입력함"





