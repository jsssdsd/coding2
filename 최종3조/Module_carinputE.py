# 내차 견적 모듈...

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
yb1=[]
p1=[]
we1=[]
ct=[]
cl=[]

d1= d1[1:]
myc1=[]
myc2=[]
CarIdex={}
mycarex=0
eslist=[]
usey=[]
carkNation=[]
caroNation=[]
x1=[]
a1=[]
l2=[]
class car1: #카의 항목 클래스화
    def __init__(self,carN,carEx,carybene,carPri,carWEneg,carTyp,carLink):
        self.N=carN
        self.E=carEx
        self.b=carybene
        self.p=carPri
        self.WE=carWEneg
        self.ct=carTyp
        self.cl=carLink

for i in range(len(d1)):  #데이터 전처리
    d1[i]= d1[i].replace('\t', ',')
    d1[i] = d1[i].replace('\n', '')
    d1[i]= d1[i].split(',')

for i in range(len(d1)):
    # l2.append(car1(
    l1.append(car1(d1[i][0],d1[i][1],d1[i][2],d1[i][3],d1[i][4],d1[i][5],d1[i][6]))
    n1.append(l1[i].N)
    e1.append(l1[i].E)
    yb1.append(l1[i].b)
    p1.append(l1[i].p)
    we1.append(l1[i].WE)
    ct.append(l1[i].ct)
    cl.append(l1[i].cl)
    CarIdex[n1[i]]= [e1[i],yb1[i],p1[i],we1[i],ct[i],cl[i]]

stringTemp=""

file2= open("차량가액.txt",'r',encoding='UTF-8')
d2= file2.readlines()


class CplusP1: #차량가액
    def __init__(self,Uyear,carkNation,caroNation):
        self.UY= Uyear
        self.CN= carkNation
        self.CN = caroNation

for i in range(len(d2)):
    d2[i]= d2[i].replace('\t', ',')
    d2[i] = d2[i].replace('\n', '')
    d2[i] = d2[i].replace('년', '')
    d2[i] = d2[i].replace('미만','')
    d2[i] = d2[i].split(',')
usey=(d2[0][1:])
carkNation=(d2[1][1:])
caroNation=(d2[2][1:])
lcplus=[]
lcplus=d2
lcplus2=[]
escar=[]
c=365

for i in range(len(d2)):
    lcplus2.append(CplusP1(d2[0][1:],d2[1][1:],d2[2][1:]))

cou=0
listresules=[]

def taxcal(cname,Uyear):
    global cou
    global a1
    while True:
        global escar
        escar.clear()
        global c
        global p1
        for i in range(len(d1)):
            # l2.append(car1(
            l1.append(car1(d1[i][0], d1[i][1], d1[i][2], d1[i][3], d1[i][4], d1[i][5], d1[i][6]))
            n1.append(l1[i].N)
            e1.append(l1[i].E)
            yb1.append(l1[i].b)
            p1.append(l1[i].p)
            we1.append(l1[i].WE)
            ct.append(l1[i].ct)
            cl.append(l1[i].cl)
            CarIdex[n1[i]] = [e1[i], yb1[i], p1[i], we1[i], ct[i], cl[i]]
        if cname in n1:
            # if (int(Uyear)) < int(usey[i])*c and int(Uyear)>= int(usey[i])*c:
            if Uyear < c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[0]), 3)
            elif Uyear >= c and Uyear < 2 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[1]), 3)
                a1= CarIdex[cname][2]
            elif Uyear >= 2 * c and Uyear < 3 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[2]), 3)
            elif Uyear >= 3 * c and Uyear < 4 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[3]), 3)
            elif Uyear >= 4 * c and Uyear < 5 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[4]), 3)
            elif Uyear >= 5 * c and Uyear < 6 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[5]), 3)
            elif Uyear >= 6 * c and Uyear < 7 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[6]), 3)
            elif Uyear >= 7 * c and Uyear < 8 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[7]), 3)
            elif Uyear >= 8 * c and Uyear < 9 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[8]), 3)
            elif Uyear >= 9 * c and Uyear < 10 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[9]), 3)
            elif Uyear >= 10 * c and Uyear < 11 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[10]), 3)
            elif Uyear >= 11 * c and Uyear < 12 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[11]), 3)
            elif Uyear >= 12 * c and Uyear < 13 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[12]), 3)
            elif Uyear >= 13 * c and Uyear < 14 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[13]), 3)
            elif Uyear >= 14 * c and Uyear < 15 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[14]), 3)
            elif Uyear >= 15 * c:
                CarIdex[cname][2] = int(CarIdex[cname][2]) * round(float(carkNation[15]), 3)
            CarIdex[cname][2] = round(CarIdex[cname][2],2)
            escar.append(cname)
            escar.append(CarIdex[cname][:-1])
            escar.append(Uyear)
            x1.append(cname)
            return escar
        else:
            escar.clear()

def taxcalres():
    global escar
    global c
    global p1

    return escar.clear()

def useyreset(cname,Uyear):  #나눈값만큼 다시 곱해주면 원상복귀다.
    global escar
    escar.append(cname)
    escar.append(CarIdex[cname][:-1])
    escar.append(Uyear)
    return escar
def cleancaridex():
    open("자동차 목록.txt", 'r', encoding='UTF-8')
    global list_1
    global list_2
    global list_3
    global list_4
    list_1 = []
    list_2 = []
    list_3 = []
    list_4=[]
    for i in open("자동차 목록.txt",'r',encoding='UTF-8').readlines():
        if "차량명" in i:
            continue
        else:
            list_1.append(i)
    for i in list_1:
        temp = i.replace('\n', '')
        list_2.append(temp)
    for i in list_2:
        list_3.append(i.split('\t'))
    for i in list_3:
        list_4.append(i[0])
        return list_4



def escarout():
    return escar

def cleandata(x):
    global n1
    global ye1
    open("자동차 목록.txt", 'r', encoding='UTF-8')
    global list_1
    global list_2
    global list_3
    global list_4
    global list_5
    list_1 = []
    list_2 = []
    list_3 = []
    list_4=[]
    list_5=[]
    for i in open("자동차 목록.txt",'r',encoding='UTF-8').readlines():
        if "차량명" in i:
            continue
        else:
            list_1.append(i)
    for i in list_1:
        temp = i.replace('\n', '')
        list_2.append(temp)
    for i in list_2:
        list_3.append(i.split('\t'))
    for i in list_3:
        list_4.append(i[0])

    if x== n1:
        return n1
    elif x == e1:
        return e1
    elif x == yb1:
        return yb1
    elif x == p1:
        return p1
    elif x == we1:
        return we1

def cleandatacarlist():
    global list_1
    global list_2
    global list_3
    global list_4
    global list_5
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    for i in open("자동차 목록.txt",'r',encoding='UTF-8').readlines():
        if "차량명" in i:
            continue
        else:
            list_1.append(i)
    for i in list_1:
        temp = i.replace('\n', '')
        list_2.append(temp)
    for i in list_2:
        list_3.append(i.split('\t'))
    for i in list_3:
        list_4.append(i[0])
    return list_3
def cleandatacarlist2(): #이름 출력
    global list_1
    global list_2
    global list_3
    global list_4
    global list_5
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    for i in open("자동차 목록.txt",'r',encoding='UTF-8').readlines():
        if "차량명" in i:
            continue
        else:
            list_1.append(i)
    for i in list_1:
        temp = i.replace('\n', '')
        list_2.append(temp)
    for i in list_2:
        list_3.append(i.split('\t'))
    for i in list_3:
        list_4.append(i[0])
    return list_4
