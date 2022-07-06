file=open("자동차 목록.txt",'r',encoding='UTF-8')
list_all=file.readlines()

def nocar():
    return "감히 차 살 생각하지 말고 걸어다니세요."
def allcar():
    return "돈이 흘러 넘칩니다. 아무거나 사고싶은차 사세요."

def Range(m):
    lista=[]
    for i in list_3:
        if m <= int(i[3]) < (m+1000):
            lista.append(i[0])
    return lista

def Rangeover(m):
    lista=[]
    for i in list_3:
        if m <= int(i[3]) < (m+10000):
            lista.append(i[0])
    return lista

def WealthRange(x):
    global carlist
    carlist=[]
    if 2400>x:
        nocar()
    elif 2400<=x<3400:
        return Range(1000)
    elif 3400<=x<4400:
        return Range(2000)
    elif 4400<=x<5400:
        return Range(3000)
    elif 5400<=x<6400:
        return Range(4000)
    elif 6400<=x<7400:
        return Range(5000)
    elif 7400<=x<8400:
        return Range(6000)
    elif 8400 <= x < 9400:
        return Range(7000)
    elif 9400<=x<10400:
        return Range(8000)
    elif 10400 <= x < 11400:
        return Range(9000)
    elif 11400 <= x < 12400:
        return Rangeover(10000)
    elif 12400 <= x < 13400:
        return Rangeover(20000)
    elif x >= 13400:
        allcar()

def cleandata():
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

def RecommendCar(name,wealth,pay,debt):
    global wealthrangex
    wealthrangex=pay*12+(wealth/10)-(debt/10)
    cleandata()
    return WealthRange(wealthrangex)
#RecommendCar("dd",150,100,0)

def cleandatareturn():
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

def cleandatareturn2():
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
    return list_3


if __name__=="__main__":

    while True:
        pass