import random as rd

# random.shuffle()

#랜덤 조짜기
file_c =open('sample.txt','r',encoding='UTF-8')
rfile=list(file_c.readlines())
print(rfile)

for i in range(len(rfile)):
    rfile[i]= rfile[i].split(",")
    print(rfile)
for i in range(len(rfile)):
        for m in range(len(rfile[i])):
            if '\t' in rfile[i][m]:
                rfile[i][m] = rfile[i][m].replace('\t',',')
for i in range(len(rfile)):
        for m in range(len(rfile[i])):
            if '\t' in rfile[i][m]:
                rfile[i][m] = rfile[i][m].split('\t')
for i in range(len(rfile)):
    for m in range(len(rfile[i])):
        if '\n' in rfile[i][m]:
            rfile[i][m] = rfile[i][m].replace('\n','')
revise2=rfile[i]
print(rfile)
for i in range(len(rfile)):
    for m in range(len(rfile[i])):
        rfile[i][m] = rfile[i][m].split(',')
        print(rfile[i][m])

revise1=rfile[i]

# revise1=rfile


# rd.shuffle(x)


class RDteam:
    clvar="팀원 정보"
    global revise1
    def __init__(self, name, male, score, mbti):   #1
        self.name= name
        self.male=male
        self.count=score
        self.mbti=mbti
    def randompp(self):
        pass





    #     class account:
    #         clvar = "계좌정보"
    #         def __init__(self, name, bal, bank, accnum):  # 1
    #             self.name = name
    #             self.bal = bal
    #             self.bank = bank
    #             self.accnum = accnum
    #
    #         def inM(self, m):  # 입금
    #             self.bal += m
    #             return self.bal
    #
    #         def outM(self, m):  # 출금
    #             self.bal -= m
    #             return self.bal
    #
    #         def checkBal(self):  # 잔액
    #             print(self.bal)
print("nnnnnnnnnnnnnnnnnnnnnnnn")
print(rfile)
#이름 성별 점수 mbti

# for i in range(len(revise2)):
s1= RDteam(revise1[0][1],revise1[0][2],revise1[0][3],revise1[0][4])

print(s1.name)
print(s1.male)
print(s1.score)
print(s1.mbti)


# h1= account('학생',10000,'농협',1234567890)  #2   #1를 #2로 풀어씀. 출력을위해서....self =h1
# print(h1.clvar)
# print(h1.name)
# print(h1.bank)
# print(h1.accnum)
# print(h1.bal)
# h1.inM(30000)
# print(h1.bal)
# h2=account('학생1',10000,'농협',1234567890)
# print("="*100)
#
# def addH(n,bal,bank,accnum):
#     global listx
#     print(type(n))
#     print(type(bal))
#     print(type(bank))
#     print(type(account))
#     listx.append(account(n,bal,bank,accnum))
#
# listx=[]
#
# while True:
#     mode= input("1.추가 2종료")
#     if mode=='1':
#         name =input("이름")
#         bal = int(input("잔액"))
#         bank = input("은행")
#         accnum = int(input("계좌번호"))
#         addH(name,bal,bank,accnum)
#     else:
#         break
#
# for i in range(len(listx)):
#     print(listx[i].clvar)
#     print(listx[i].name)
#     print(listx[i].bal)
#     print(('='*20))
#
# for n in range(len(listx)):
#     globals()['no_{}'.format(n)]= listx[n]
# print(no_1)
#
#
# listx=[5,5,5,6,6,6]
#
# for n in range(len(listx)):
#     globals()['no_{}'.format(n)]= listx[n] # globals()[이름{} .format(횟수)]= linstx[n] 넣을 공간.{}= format.~~
# print(no_3)

