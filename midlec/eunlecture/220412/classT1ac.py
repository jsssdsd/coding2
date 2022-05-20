# 클래스변수는 공용.
# 바뀌지않는값 클래스변수 , 안의 기능값 객체변수, 객체안의 세부기능 메서드.

# 문제1 #은행계좌 account
# 속성: 예금주명/잔액/은행/계좌번호/
# 1. 공통속성: 클래스 변수
# 2.객체속성: 객체변수

# 기능: 입금/출금/잔액확인
# 생성자 메서드 구현

class account:
    clvar="계좌정보"
    def __init__(self,name,bal,bank,accnum):   #1
        self.name= name
        self.bal=bal
        self.bank=bank
        self.accnum=accnum
    def inM(self,m): #입금
        self.bal+=m
        return self.bal
    def outM(self,m):  #출금
        self.bal-=m
        return self.bal
    def checkBal(self): #잔액
        print(self.bal)

h1=account('학생',10000,'농협',1234567890)  #2   #1를 #2로 풀어씀. 출력을위해서....self =h1
print(h1.clvar)
print(h1.name)
print(h1.bank)
print(h1.accnum)
print(h1.bal)
h1.inM(30000)
print(h1.bal)
h2=account('학생1',10000,'농협',1234567890)
print("="*100)

def addH(n,bal,bank,accnum):
    global listx
    print(type(n))
    print(type(bal))
    print(type(bank))
    print(type(account))
    listx.append(account(n,bal,bank,accnum))

listx=[]

while True:
    mode= input("1.추가 2종료")
    if mode=='1':
        name =input("이름")
        bal = int(input("잔액"))
        bank = input("은행")
        accnum = int(input("계좌번호"))
        addH(name,bal,bank,accnum)
    else:
        break

for i in range(len(listx)):
    print(listx[i].clvar)
    print(listx[i].name)
    print(listx[i].bal)
    print(('='*20))

for n in range(len(listx)):
    globals()['no_{}'.format(n)]= listx[n]
print(no_1)


listx=[5,5,5,6,6,6]

for n in range(len(listx)):
    globals()['no_{}'.format(n)]= listx[n] # globals()[이름{} .format(횟수)]= linstx[n] 넣을 공간.{}= format.~~
print(no_3)