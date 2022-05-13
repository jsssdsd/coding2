#모듈을 돌릴 때 필요한 함수, 변수, 딕셔너리를 모아놓은 파일.
import datetime as dt
import os
import shutil
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

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

#날짜 파일 리스트 만들기
def makedlist():
    with open('날짜.txt', 'r', encoding='UTF-8') as d:
            dlist=[]
            dtemp = d.readlines()
            for i in range(len(dtemp)):
                    dtemp[i]=dtemp[i].replace('\n','')
                    dlist.append(dtemp[i])
    return dlist

#날짜 파일 리스트(dlist)
dlist=makedlist()

#시간표 상위 출력 메시지
ttforward='★[빅데이터 UI 전문가] 비전공자를 위한 빅데이터 UI & 프론트엔드 웹개발자'+\
        '\n'+'수강 기간: 22.03.15~22.08.03 (월~금, 09:10~18:00)'

#수업 시간
fulltime='09:10~18:00'
early='09:10~13:00'

#원격 수업일 리스트(remotedays)
remotedays=[
'22-03-25(금)',
'22-04-01(금)',
'22-04-08(금)',
'22-04-15(금)',
'22-04-23(토)',
'22-04-30(토)',
'22-05-05(목)',
'22-05-21(토)',
'22-05-28(토)',
'22-06-01(수)',
'22-06-06(월)',
'22-06-11(토)']

#수업날짜별 딕셔너리 만들기
def dateDict(list):
        lesson={}
        for j in list:
                if '22-08-03(수)' in j:
                        lesson['22-08-03(수)']=early
                elif j in remotedays:
                        lesson[j]='원격수업일'
                else:
                        lesson[j]=fulltime
        return lesson

#시간표 모듈에 써먹을 딕셔너리(timetable)
timetable=dateDict(dlist)

#원격수업일을 뺀 리스트 만들기
def makeclist():
        clist=[]
        for i in dlist:
               if i not in remotedays:
                       clist.append(i)
        return clist

#원격수업일을 뺀 리스트(clist)
clist=makeclist()

#실제 총 수업일(totaldays=95)
totaldays=len(clist)

#요일 리스트(weekdays)
weekdays = ['(일)','(월)','(화)','(수)','(목)','(금)','(토)']

#오늘 날짜 뒤에 요일 붙이기
def Today():
        result=''
        result=dt.datetime.today().strftime("%Y-%m-%d")+weekdays[int(dt.datetime.today().strftime("%w"))]
        return result[2:]

#원하는 날짜에 요일 붙이기
def Date():
        day=input('수정을 원하는 날짜(mmdd):')
        result=''
        m=int(day[0:2])
        d=int(day[2:4])
        day=dt.datetime(2022,m,d).strftime("%Y-%m-%d")
        result=day+weekdays[int(dt.datetime(2022,m,d).strftime("%w"))]
        return result[2:]

#함수0. 사용자 폴더 생성(dirname=userlist)
def make_folder(dirname):
    try:
        os.makedirs(dirname)
        #파일이 하나도 없으면 아래 함수가 작동되지 않아 허위 파일 하나 생성
        sample=open('./userlist/sample0000.txt','w',encoding='utf-8')
        sample.close()
        if __name__ == '__main__':
            print('폴더 생성')
    except OSError:
        if not os.path.isdir(dirname):
            pass
make_folder('userlist')
make_folder('notetodo')

#함수1. 중복 사용자 검색(user_search)
def user_search(name,num):
    while True:
        if len(num)==4 and num.isdigit():
            for i in os.listdir('userlist'):
                if name+num+'.txt' not in i:
                    if __name__=='__main__':
                        print('계정 없음')
                        break
                else:
                    if __name__ == '__main__':
                        print('이미 존재하는 사용자')
            break
        else:
            if __name__=='__main__':
                print('잘못 입력, 다시 입력')
                break

#함수2. 사용자 추가 및 개인별 출결 파일 생성(계정 생성)(add_user)
def add_user(name,num):
    user=open('./userlist/'+name+num+'.txt','a',encoding='UTF-8')
    note=open('./notetodo/note_'+name+num+'.txt', 'a', encoding='UTF-8')
    todo=open('./notetodo/todo_'+name+num+'.txt', 'a', encoding='UTF-8')
    user.close()
    note.close()
    todo.close()

#함수3. 사용자 개인별 파일 삭제(계정 삭제)(delete_user)
#함수 실행 전 사전 경고 필요(복구 불가)
def delete_user(name,num):
    open('./userlist/'+name+num+'.txt','a',encoding='UTF-8')
    os.remove('./userlist/'+name+num+'.txt')
    open('./notetodo/note_'+name+num+'.txt', 'a', encoding='UTF-8')
    os.remove('./notetodo/note_'+name+num+'.txt')
    open('./notetodo/todo_'+name+num+'.txt','a',encoding='UTF-8')
    os.remove('./notetodo/todo_'+name+num+'.txt')

#함수4. 이름 변경(개명)/전화번호 변경(replace_info)
def replace_info(name,num):
    before=input('수정할 이름 or 전화번호 뒤 4자리: ')
    after='' #변경할 문자열
    if before.isalpha() or before=='이름':
        after=input('변경할 이름: ')
        shutil.move('./userlist/'+name+num+'.txt','./userlist/'+after+num+'.txt')
    elif before.isdigit() and len(before)==4:
        after=input('변경할 전화번호 뒤 4자리): ')
        shutil.move('./userlist/'+name+num+ '.txt','./userlist/'+name+after+'.txt')

#함수 바인딩
add=lambda:[make_folder('userlist'),user_search(),add_user()] #사용자 추가
delete=lambda:[make_folder('userlist'),user_search(),delete_user()] #사용자 삭제
replace=lambda:[make_folder('userlist'),user_search(),replace_info()] #사용자 정보 수정(=파일명 변경)

#<시간표(스케줄) 조회 모듈>
date=timetable.keys() #요일이 포함된 날짜(timetable 딕셔너리의 key값)
value=timetable.values() #수업시간 혹은 원격수업일(timetable 딕셔너리의 value값)

#전체 스케줄(시간표) 리스트(result)
result=list(zip(date,value)) #위 둘을 합쳐놓은 튜플의 리스트

#함수1. 월별 스케줄 리스트(monthly_timetable)
def monthly_timetable(mm):
    result_m=[]
    for i in result:
        if mm[0] in i[0][3] and mm[1] in i[0][4]:
            result_m.append(i)
    return result_m
#print(monthly_timetable(input('원하는 달(mm):')))

#함수2. 특정 날짜 스케줄(daily_timetable)
def daily_timetable(mmdd):
    mmdd=str(mmdd)
    result_d=[]
    for i in result:
        if mmdd[0] in i[0][3] and mmdd[1] in i[0][4] and mmdd[2] in i[0][6] and mmdd[3] in i[0][7]:
            result_d.append(i)
    return result_d
#print(daily_timetable(input('보고 싶은 날짜(mmdd):')))

#<출결 관리 모듈>
#pandas,numpy,pip,matplotlib 설치 (Settings-Project-Python Interpreter)
#매개변수가 있는 함수를 command: lambda 사용

#함수1. 당일 입실/퇴실 체크(todaycheck)
def todaycheck(name,num):
    option=input('입실 or 퇴실:')
    present=dt.datetime.today().strftime("%H:%M")
    with open('./userlist/'+name+num+'.txt','r',encoding='UTF-8') as user:
        line=user.readlines()
    if option=='입실':
        checkin=open('./userlist/'+name+num+'.txt','a',encoding='UTF-8')
        checkin.writelines(Today()+'\t'+ present)
        checkin.close()
    elif option=='퇴실':
        if Today() in line[-1]:
            checkout = open('./userlist/'+name+num+'.txt','a',encoding='UTF-8')
            checkout.writelines('-'+present+'\n')
            checkout.close()
        else:
            if __name__ == '__main__':
                print('입실 시간 없음, 추가 필요')

#함수2. 근태 사후 추가/수정(aftercheck)
def aftercheck(name,num):
    day=Date()
    option= input('입실,퇴실시간 있음(출석)/결석/공결:')
    new_line=''
    if option == '결석':
        new_line = day + '\t' + '결석' + '\n'
    elif option == '공결':
        new_line = day + '\t' + '공결' + '\n'
    elif option == '출석':
        checkin = input('입실시간 숫자 네 자리(24h):')
        checkout = input('퇴실시간 숫자 네 자리(24h):')
        new_line = day + '\t' + checkin[0:2] + ':' + checkin[2:] + '-' + checkout[0:2] + ':' + checkout[2:] + '\n'
    with open('./userlist/'+name+num+'.txt','r+',encoding='UTF-8') as f:
        lines = []
        for line in f:
            if (line.startswith(day)):
                lines = lines +[new_line]
            else:
                lines = lines + [line]
    f=open('./userlist/'+name+num+'.txt','w+',encoding='UTF-8')
    f.seek(0)
    f.writelines(lines)
    f.truncate()
    f.close()

#함수3. 출석부 날짜순 정렬(sortdata)
def sortdata(name,num):
    old = open('./userlist/'+name+num+'.txt', 'r', encoding='utf-8')
    oldlist = old.readlines()
    newlist = list(set(oldlist))
    newlist.sort()
    old.close()
    with open('./userlist/'+name+num+'.txt', 'w+', encoding='utf-8') as new:
        for i in newlist:
            new.writelines(i)

#함수4. 출석부 리스트(rollbook)
def rollbook(name,num):
    result=[]
    with open('./userlist/'+name+num+'.txt','r',encoding='UTF-8') as user:
        u=user.readlines()
        for i in range(len(u)):
            u[i]=u[i].replace('\n','')
            u[i]=u[i].replace('\t',' ')
            result.append(u[i])
    return result

#파이썬에서 print 메서드는 string 타입만 +를 사용한 출력 가능
#그 외 모두 콤마를 사용하여 출력해야 오류가 없다


#함수5. 월간 출석부 리스트(monthly_rollbook)
def monthly_rollbook(name,num,mm):
    mm=str(mm)
    result_m=[]
    with open('./userlist/'+name+num+'.txt','r',encoding='UTF-8') as user:
        u=user.readlines()
    for i in range(len(u)):
        if mm[0] in u[i][3] and mm[1] in u[i][4]:
            result_m.append(u[i])
    return result_m

#함수6. 월별 훈련수당 계산(cal_allowance)
#기준이 실제와 달라 계산 결과와 실제 수령액에는 차이가 있습니다
#하루 5500원(교통비 2500+식비 3000)
def cal_allowance(mm):
    mm=str(mm)
    mlist=monthly_timetable(mm)
    alist=monthly_rollbook(mm)
    calculate=[]
    temp=[]
    extradays=len(mlist)-len(alist)
    starttime = dt.datetime.strptime('9:21', "%H:%M")
    endtime = dt.datetime.strptime('17:49', "%H:%M")
    for s in alist:
        if s[12:17]=='결석\n' or s[12:17]=='공결\n':
            print(s[0:11],'결석으로 인해 수당 미지급')
        else:
            checkin = dt.datetime.strptime(s[12:17],"%H:%M")
            checkout = dt.datetime.strptime(s[18:23],"%H:%M")
            lateness = bool(starttime >= checkin)  # 지각(True)
            earlyleave = bool(endtime <= checkout)  # 조퇴(True)
            interval=str(checkout - checkin)[0]
            if int(interval)< 4:
                    print(s[0:11], '4시간 미만으로 인한 결석, 수당 미지급')
            elif 4<=int(interval)<8:
                if lateness==False:
                    calculate.append(s)
                    temp.append(s)
                    print(s[0:11], '지각, 3번마다 하루치 수당 미지급')
                elif earlyleave==False:
                    calculate.append(s)
                    temp.append(s)
                    print(s[0:11], '조퇴, 3번마다 하루치 수당 미지급')
            else:
                calculate.append(s)
                print(s[0:11], '정상 출석, 수당 지급')
    threeout=len(temp)//3
    return (len(calculate)-threeout+extradays)*5500

#함수7-1. 지금까지 출석한 일수(Adays)
def Adays(Alist):
    absent = []
    for s in Alist:
        if  s[12:17]=='결석' or s[12:17]=='결석\n':
            absent.append(s)
        elif  s[12:17]=='공결' or s[12:17]=='공결\n':
            pass
        else:
            checkin = dt.datetime.strptime(s[12:17], "%H:%M")
            checkout = dt.datetime.strptime(s[18:23], "%H:%M")
            interval = str(checkout - checkin)[0]
            if int(interval)<4:
                absent.append(s)
    return len(Alist)-len(absent)

#전체 출석률 계산
def cal_totalArate(name,num):
    Alist=rollbook(name,num)
    absent=[]
    for s in Alist:
        if s[12:17]=='결석' or s[12:17]=='결석\n':
            absent.append(s)
        elif  s[12:17]=='공결' or s[12:17]=='공결\n':
            pass
        else:
            checkin = dt.datetime.strptime(s[12:17], "%H:%M")
            checkout = dt.datetime.strptime(s[18:23], "%H:%M")
            interval = str(checkout - checkin)[0]
            if int(interval)<4:
                absent.append(s)
    t=len(Alist)
    a=len(absent)
    return round(((t-a)/totaldays)*100)

#월별 출석률 계산
def cal_monthlyArate(name,num,mm):
    Alist=monthly_rollbook(name,num,mm)
    absent=[]
    for s in Alist:
        if s[12:17]=='결석' or s[12:17]=='결석\n':
            absent.append(s)
        elif  s[12:17]=='공결' or s[12:17]=='공결\n':
            pass
        else:
            checkin = dt.datetime.strptime(s[12:17], "%H:%M")
            checkout = dt.datetime.strptime(s[18:23], "%H:%M")
            interval = str(checkout - checkin)[0]
            if int(interval)<4:
                absent.append(s)
    t=len(Alist)
    a=len(absent)
    return round(((t-a)/t)*100)

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
        Alist.append(rollbook(namedata[i],numdata[i]))
    return Alist

#'userlist'디렉토리의 모든 출석부 리스트
rlist=total_rollbook()

#사용자별 출석일 리스트
def total_Adays():
    y_data_Adays=[]
    for i in rlist:
        r=Adays(i)
        y_data_Adays.append(r)
    return y_data_Adays

#사용자별 출석일 비교 그래프
def compare_Adays():
    x_data = anonymity()  # x축, 사용자 이름
    y_data = total_Adays()  # y축, 사용자별 출석일
    x=np.arange(len(x_data))  # 주어진 범위와 간격에 따라 균일한 값을 갖는 어레이를 반환
    y=np.arange(0,96,5)
    plt.figure('Attendance')
    plt.title('수강생별 출석일')
    plt.xticks(x, label=x_data)  # .xticks(x축 눈금 레이블, label=x축 데이터)
    plt.xlabel('총 출석일: 95일')
    plt.ylim([0,95])
    plt.yticks(y, label=y_data)
    plt.ylabel('출석 일수')
    plt.grid(True, axis='y', alpha=0.5)
    for i in range(1, len(x_data) + 1):
        plt.text(i - 1, y_data[i - 1], y_data[i - 1], ha='center', size=8)
    plt.bar(x_data, y_data, color=barcolors, width=0.5)
    plt.show()

'''
#시간 남으면 할 거
#1.여러 날짜 한 번에 수정
#2.주간 출석부 조회
#일요일이나 월요일 기준으로 나누기, 리스트 분할
#3.18시 이후 퇴실 했을 때 시간계산 제외법
'''