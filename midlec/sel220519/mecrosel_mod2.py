
# 요소 저장 함수
import os
import datetime as dt
from datetime import datetime
print(os.listdir(os.getcwd()))
t1 = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print(t1)
a=[]
x=[]
q=''
def mkelement(): #메모장 생성
    if str(os.listdir(os.getcwd())) not in "element.txt":
        f = open("element.txt", 'w', encoding="UTF8")
        f.close()


# ckelements()
# 요소 저장
def inpelement(url,element,SCpath,SCip,dt):
    t1 = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    import os.path
    path="element.txt"
    if os.path.isfile(path):
        f = open("element.txt", 'a', encoding="UTF8")
        f.write("기록시각: " + str(t1) )
        f.write(" url값: " + str(url) )
        f.write(" element값: " + str(element) )
        f.write(" 검색PATH값: " + str(SCpath) )
        f.write(" 검색어: " + str(SCip))
        f.write(" 데이터값: " + str(dt) + "\n\n")
        # t1 = 0
        f.close()
    else:
        f = open("element.txt", 'w', encoding="UTF8")
        f.write("기록시각: " +str(t1 ) )
        f.write(" url값: " + str(url) )
        f.write("element값: " + str(element) )
        f.write(" input값: " + str(input))
        f.write(" 데이터값: "+str(dt)+ "\n\n")
        # t1 = 0
        f.close()
# print(inpelement(4,3,3,3))

def deldata(): #파일 삭제
    import os.path
    path = "element.txt"
    if os.path.isfile(path):
        os.remove(path)
    else:
        print("not exist")



def rdelement(x):
    f = open("element.txt", 'r', encoding="UTF8")
    x= f.readlines()
    print(x)
    return x

# def rdelement():
#     inpelement()
#     a =f.readlines()
#     print(a)
# mkelement()
# inpelement('2321234234\n fewfwef \n ewfwefwe')
# rdelement(x)


#
# # #회원가입 모듈
# def signin():
#
#
#     import os.path
#     path="회원정보.txt"
#     if os.path.isfile(path):
#         pass
#     else:
#
#         infor="아이디\t비밀번호\t이름\t성별\t닉네임\t신뢰도\t평가받은횟수\n"
#         list = open("회원정보.txt", 'w', encoding='utf-8')
#         list.write(infor)
#
#         list.close()
#
#
# # # 회원가입 중복확인 모듈
# def signinSuc(ID, PW, Name, sex, NName):
#     Ulist=open("회원정보.txt",'r',encoding='utf-8')
#     Ulist=Ulist.readlines()
#
#     del Ulist[0]
#     for i in range(len(Ulist)):
#         Ulist[i]=Ulist[i].replace("\n","")
#         Ulist[i]=Ulist[i].split("\t")
#
#     firI=[]
#     secPW=[]
#     thrnick = []
#     for i in range(len(Ulist)):
#         fir=Ulist[i][0]
#         sec=Ulist[i][1]
#         thr=Ulist[i][4]
#         thrnick.append(thr)
#         secPW.append(sec)
#         firI.append(fir)
#
#     if ID not in firI and NName not in thrnick:
#         UL=open('회원정보.txt','a',encoding="utf-8")
#         UL.write(ID +"\t"+PW+"\t"+Name+"\t"+sex+"\t"+NName+'\t'+'0'+'\t'+'0'+'\n')
#
# # 정보수정
# # 수정할 회원정보 가져오기
# def edit(ID,NPW,NN):
#     Ueditlist = open("회원정보.txt", 'r', encoding='utf-8')
#     Uedit = Ueditlist.readlines()
#
#     for i in range(len(Uedit)):
#         Uedit[i] = Uedit[i].replace("\n", "")
#         Uedit[i] = Uedit[i].split('\t')
#
#     #필터링 후 작성
#     Ueditlist = open("회원정보.txt", 'w', encoding='utf-8')
#     for i in range(len(Uedit)):
#         if ID == Uedit[i][0]:
#             Uedit[i][1] = NPW # 새로운 변수 (새 비밀번호)
#             Uedit[i][4] = NN # 새로운 변수 (새로운 닉네임)
#         Ueditlist.write(Uedit[i][0]+'\t'+Uedit[i][1]+'\t'+Uedit[i][2]+'\t'+Uedit[i][3]+'\t'+Uedit[i][4]+'\t'+Uedit[i][5]+'\t'+Uedit[i][6]+'\n')
#
# def delfromlist(eeer, nn):
#     newinf = ''
#     with open("%s.txt" % eeer, 'r', encoding='UTF-8') as list:
#         lr = list.readlines()
#         for i in range(len(lr)):
#             lr[i] = lr[i].split()
#         for i in lr[:]:
#             if nn in i:
#                 lr.remove(i)
#         for i in range(len(lr)):
#             lr[i] = lr[i][0] + ' ' + lr[i][1] + '\n'
#         result = ''.join(map(str, lr))
#         newinf += result
#     with open("%s.txt" % eeer, 'w', encoding='UTF-8') as list:
#         list.write(newinf)
#
#
# # 회원탈퇴
# def Udel(ID, nn):
#     path = os.getcwd()
#     Del_list=open("회원정보.txt","r",encoding="utf-8")
#     Dlist=Del_list.readlines()
#     del_list=[]
#     for i in range(len(Dlist)):
#         Dlist[i]=Dlist[i].replace("\n","")
#         del_list.append(Dlist[i].split("\t"))
#
#     del_L= open("회원정보.txt", 'w', encoding='utf-8')
#     for i in range(len(del_list)):
#         if ID==del_list[i][0]:
#             continue
#
#         del_L.write(del_list[i][0]+'\t'+del_list[i][1]+'\t'+del_list[i][2]+'\t'+del_list[i][3]+'\t'+del_list[i][4]+'\t'+del_list[i][5]+'\t'+del_list[i][5]+'\n')
#     del_L.close()
#
#     file_n = os.listdir(path)
#     for i in file_n:
#         if i.endswith(" %s 댓글 목록.txt" % nn):  #해당 계정이 작성한 게시글의 댓글 파일 삭제
#             os.remove(i)
#         if i.endswith('댓글 목록'):  #해당 계정이 작성한 타 게시글의 댓글 삭제
#             newlist = ''
#             dellist = ''
#             with open("%s" % i, 'r', encoding='UTF-8') as list:
#                 content = list.readlines()
#                 for m in content:
#                     if nn in m:
#                         content.remove(m)
#                 for o in content:
#                     o = o.strip('\n')
#                     o = o.strip('\t')
#                     dellist += o + '\n'
#                 print(dellist)
#                 result = ''.join(map(str, dellist))
#                 newlist += result
#                 print(newlist)
#             with open("%s" % i, 'w', encoding='UTF-8') as list:
#                 list.write(newlist)
#         if i.endswith("%s.txt" % nn):  #해당 계정이 작성한 게시글 파일 삭제
#             os.remove(i)
#     delfromlist("구인게시글목록", nn)
#     delfromlist("구직게시글목록", nn)
