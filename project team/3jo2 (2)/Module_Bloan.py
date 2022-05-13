# 대출값 계산.


import os.path #path경로를 가져오기 위한 모듈
path= "taxcal.py"
os.path.isfile(path) #path변수에 저장되어 있는 파일이 존재하는지 여부
#...데이터 파일 불러오기
file1=open("자동차 목록.txt",'r',encoding='UTF-8')

d1=file1.readlines()
d2=list(d1)

def cleandatacarBlist():
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
print(cleandatacarBlist())
#


com=[]  #할부개월, 거치기간 ,할부금리 ,할부원금, 선수금 , 할부원금페이백, 선수금페이백, 사은품
class carLone: #카의 대출항목 클래스화
    def __init__(self,loanMonth,notinterestday,interestrate,installpricipal,advancedpayment,
                 installPpayback,advancedpaymentPB,bonusmoney):
        self.LM=loanMonth #할부개월
        self.NID=notinterestday #거치기간
        self.IR=interestrate #할부금리
        self.IPL=installpricipal #할부원금
        self.AP=advancedpayment #선수금
        self.IPB=installPpayback #할부원금 페이백
        self.APB=advancedpaymentPB #선수금 페이백
        self.BM = bonusmoney #사은품

# 1. 원리금 균등(분할) 상환식
# interRSum,RealinterRSum,Realinterate  #이자 합계,실납부 이자 , 실질 금리(년))
# def lonecal(loanMonth,notinterestday,interestrate,installpricipal,advancedpayment,  #이자 합계,실납부 이자 , 실질 금리(년))
#                  installPpayback1,advancedpaymentPB1,bonusmoney,interRSum,RealinterRSum,Realinterate ):

# 1. 계산식.
# a= 대출받을 원금
# b= 대출에 대한 이자 (연이자율(연이율) /12)
# 분모 : (1+b)n승 -1
# 분자 : ab(1+b)n승     최종  ab(1+b)n승 / (1+b)n승 -1  매달 지불 실질할부금.
LoanRec=[]

##   (할부개월, 거치기간 ,할부금리 ,할부원금, 선수금 , 할부원금페이백, 선수금페이백, 사은품)
def loanMonthSM(loanMonth,notinterestday,interestrate,installpricipal,advancedpayment,
                 installPpayback1,advancedpaymentPB1,bonusmoney ):
    global b
    global LoanRec
    # l1.append(car1(d1[i][0], d1[i][1], d1[i][2], d1[i][3], d1[i][4], d1[i][5], d1[i][6]))
    LoanRec.clear()
    LoanRec.append(carLone(loanMonth,notinterestday,interestrate,installpricipal,advancedpayment,
                 installPpayback1,advancedpaymentPB1,bonusmoney))
    print(LoanRec)
    # loanMonthSM1 =round(int(installpricipal)/ int(loanMonth),2)  #기초 식 :월할부 납부액결과 #할부원금 /개월
    b =round((float(interestrate)/12)*0.01, 5)
    installpricipal = int(installpricipal)-int(installPpayback1)
    loanMonthSMMot = round(((float(b+1) ** (float(loanMonth))) -1),5)   #분모
    loanMonthSMson = round(((float(installpricipal)*b) * float(float(b+1) ** float(loanMonth))),5)         #분자
    loanMonthSM1= round((float(loanMonthSMson)/ float(loanMonthSMMot))*10000 ) #만단위니까 만을 나눠준다.
    print(b, loanMonthSMMot,loanMonthSMson)
    # print("b+1의 n승", round((b+1) ** (int(loanMonth)),5))
    # print("결과값",loanMonthSM1)
    return loanMonthSM1

def installPpaybackR(loanMonth,notinterestday,interestrate,installpricipal,advancedpayment,
                 installPpayback1,advancedpaymentPB1,bonusmoney ):
    installPpaybackR1 = round(installpricipal / (0.01 * (installPpayback1)))    #실납부 이자
    return installPpaybackR


# CalResult.append(loanMonthSM1,installPpaybackR1)

# 2. 원금 균등분할 상환식








# 3. 만기일시  상환식
