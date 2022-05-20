#전처리문제 2 풀이

file_c= open('근로소득세.txt','r',encoding='UTF-8')
# rawlist=file_c.readlines()
# print(rawlist)
# print(len(rawlist))
# print("=" *100)
# x=list_all[0].replace('\t', '')
# print(x)
# y =rawlist[0].split('\t')


rawdata=file_c.readlines()
print(rawdata)
list_Temp=[]

for m in range(len(rawdata)):
    x= rawdata[m].split('\t')
    print(x)
    for i in range(len(x)):
        if x[i] and x[i]!="\n": # 여기서 x[i] 인덱싱한 자료를 다시 넣엇기때문에  listTemp는 그냥 1차원리스트이다.
            list_Temp.append(x[i])

print("리스트템프",list_Temp)

def changeX(x,y=''):     #\n를 공백으로 바꿈.
    for i in range(len(list_Temp)):  #list는 len와  range 를 결합해서 for반복에 사용가능 for은 list사용X
            if '\n' in list_Temp[i]:
                list_Temp[i] = list_Temp[i].replace(x, y)


changeX('\n')
print(list_Temp)


def changec(x, y="0"):
    for i in range(len(list_Temp)):  # list는 len와  range 를 결합해서 for반복에 사용가능 for은 list사용X
        if '-' in list_Temp[i]:
            list_Temp[i] = list_Temp[i].replace(x, y)


changec('-')
print(list_Temp)

#
# for m in (range(len(list_Temp[i]))):
#     if '\n' in list_Temp[i][m]:
#         list_Temp[i][m]=list_Temp[i][m].replace(x,y)



























# def Ssplit(sraw, lraw): #1번문제  자기가 원하는 행 출력 1~5행  2~3행
#     list_res= []
#     for i in range(len(rawlist)):
#         if sraw<= lraw:
#             list_res.append(rawlist[sraw:lraw]) #append로 가상의 리스트에 내가 넣을 값을 삽입해준다. 1.기본 기초 리스트를 ㅁ나든다.
#         return list_res
#
# print(Ssplit(0,3))












# def replacewhat(start, raw,Fromwhat, Towhat=''):  #시작 로우(행) ~를 (from)~로 바꿈 towhat..
#     # start =input("시작줄")
#     list_res=[]
#     for i in range(len(raw)):
#         if Fromwhat not in raw[i]:
#             pass
#         else:
#             while Fromwhat in raw[i]:
#                 raw[i]= raw[i].replace(Fromwhat,Towhat)
#                 if start>=0:
#                     list_res.append(rawlist[start:])
#
#     return list_res
#
# # def sliceraw(raw,what):
#
# rawlist=replacewhat(3,rawlist,'\n','')
# rawlist=replacewhat(0,rawlist,'-','0')
#
# print(rawlist)
#
# for i in range(len(rawlist)):
#     rawlist[i]=rawlist[i].split('\t')
# print(rawlist)
#
#
# dicta= {}
# for i in range(len(rawlist)):
#     dicta[rawlist[i][0]]= rawlist[i][2:]
# print(dicta)
#
#
#
#
# # # list_res= replacewhat(rawlist,'\n')
# # print(rawlist)
# # replacewhat(1)
