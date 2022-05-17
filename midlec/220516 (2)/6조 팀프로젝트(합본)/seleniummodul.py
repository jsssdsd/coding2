import os
import webbrowser
import time as t
from selenium import webdriver
# 병원 목록 모듈
listH=[]
def Hsearch():
    global listH
    #웹페이지 연결

    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('window-size=1920x1080')
    import time as t
    browser=webdriver.Chrome("chromedriver.exe",options=options)
    browser.get("https://map.naver.com/v5/search/%EB%8F%99%EB%AC%BC%EB%B3%91%EC%9B%90")

    #내 위치 입력
    t.sleep(2)
    my_lctn=browser.find_element_by_class_name("btn_location")
    my_lctn.click()

    #내 위치에서 검색
    t.sleep(2)
    Mlsrch=browser.find_element_by_class_name("btn_text")
    Mlsrch.click()

    # 크롤링하기
    # 프레임 안에 들어가기
    browser.switch_to.frame('searchIframe')
    t.sleep(2)

    # 프레임안에 있는 정보가져오기
    # 주소 전처리



    clinics = browser.find_elements_by_css_selector('li._22p-O._2NEjP')

    #전체 정보 가져온거(전처리 안된거)
    clinic_infos = []
    for clinic in clinics:
        clinic_infos.append(clinic.text)


    #병원 전처리
    names = []
    for clinic_info in clinic_infos:
        name = clinic_info.split('\n')[0][0:-4]
        if name == '':
            name = clinic_info.split('\n')[2][0:-4]
        names.append(name)


    # 영업시간 전처리
    times = []
    for clinic_info in clinic_infos:
        if len(clinic_info.split('\n')) == 7:  # 클리닉 정보를 줄바꿈한 위치가 7개라면
            time = clinic_info.split('\n')[3] #클리닉 정보를 줄바뚬한 위치 3번째에서 \n을 지워라.
        elif len(clinic_info.split('\n')) == 5:
            time = clinic_info.split('\n')[1]
        elif len(clinic_info.split('\n')) == 4:
            time = '정보없음'
        times.append(time)


    #주소 전처리
    adrs=[]
    for clinic_info in clinic_infos:
        if len(clinic_info.split('\n'))==7:
            adr=clinic_info.split('\n')[4]
        elif len(clinic_info.split('\n'))==5:
            adr=clinic_info.split('\n')[2]
        elif len(clinic_info.split('\n'))==4:
            adr=clinic_info.split('\n')[1]
        adrs.append(adr)



    with open("Hlist.txt", 'w', encoding='utf-8') as tgl:
        i=0
        while i<len(clinic_infos):
            x = names[i]+ '\t' + times[i] + '\t' + adrs[i] + '\n'
            tgl.write(x)
            i += 1



    H_infor = open("Hlist.txt", 'r', encoding='utf-8')
    HI = H_infor.readlines()


    for i in range(len(HI)):
        listH1=[]
        HI[i]=HI[i].replace("\n", "").split('\t')
        listH1.append((HI[i]))
        listH.append(listH1)
#Hsearch()





# #회원가입 모듈
def signin():


    import os.path
    path="회원정보.txt"
    if os.path.isfile(path):
        pass
    else:

        infor="아이디\t비밀번호\t이름\t성별\t닉네임\t신뢰도\t평가받은횟수\n"
        list = open("회원정보.txt", 'w', encoding='utf-8')
        list.write(infor)

        list.close()


# # 회원가입 중복확인 모듈
def signinSuc(ID, PW, Name, sex, NName):
    Ulist=open("회원정보.txt",'r',encoding='utf-8')
    Ulist=Ulist.readlines()

    del Ulist[0]
    for i in range(len(Ulist)):
        Ulist[i]=Ulist[i].replace("\n","")
        Ulist[i]=Ulist[i].split("\t")

    firI=[]
    secPW=[]
    thrnick = []
    for i in range(len(Ulist)):
        fir=Ulist[i][0]
        sec=Ulist[i][1]
        thr=Ulist[i][4]
        thrnick.append(thr)
        secPW.append(sec)
        firI.append(fir)

    if ID not in firI and NName not in thrnick:
        UL=open('회원정보.txt','a',encoding="utf-8")
        UL.write(ID +"\t"+PW+"\t"+Name+"\t"+sex+"\t"+NName+'\t'+'0'+'\t'+'0'+'\n')

# 정보수정
# 수정할 회원정보 가져오기
def edit(ID,NPW,NN):
    Ueditlist = open("회원정보.txt", 'r', encoding='utf-8')
    Uedit = Ueditlist.readlines()

    for i in range(len(Uedit)):
        Uedit[i] = Uedit[i].replace("\n", "")
        Uedit[i] = Uedit[i].split('\t')

    #필터링 후 작성
    Ueditlist = open("회원정보.txt", 'w', encoding='utf-8')
    for i in range(len(Uedit)):
        if ID == Uedit[i][0]:
            Uedit[i][1] = NPW # 새로운 변수 (새 비밀번호)
            Uedit[i][4] = NN # 새로운 변수 (새로운 닉네임)
        Ueditlist.write(Uedit[i][0]+'\t'+Uedit[i][1]+'\t'+Uedit[i][2]+'\t'+Uedit[i][3]+'\t'+Uedit[i][4]+'\t'+Uedit[i][5]+'\t'+Uedit[i][6]+'\n')

def delfromlist(eeer, nn):
    newinf = ''
    with open("%s.txt" % eeer, 'r', encoding='UTF-8') as list:
        lr = list.readlines()
        for i in range(len(lr)):
            lr[i] = lr[i].split()
        for i in lr[:]:
            if nn in i:
                lr.remove(i)
        for i in range(len(lr)):
            lr[i] = lr[i][0] + ' ' + lr[i][1] + '\n'
        result = ''.join(map(str, lr))
        newinf += result
    with open("%s.txt" % eeer, 'w', encoding='UTF-8') as list:
        list.write(newinf)


# 회원탈퇴
def Udel(ID, nn):
    path = os.getcwd()
    Del_list=open("회원정보.txt","r",encoding="utf-8")
    Dlist=Del_list.readlines()
    del_list=[]
    for i in range(len(Dlist)):
        Dlist[i]=Dlist[i].replace("\n","")
        del_list.append(Dlist[i].split("\t"))

    del_L= open("회원정보.txt", 'w', encoding='utf-8')
    for i in range(len(del_list)):
        if ID==del_list[i][0]:
            continue

        del_L.write(del_list[i][0]+'\t'+del_list[i][1]+'\t'+del_list[i][2]+'\t'+del_list[i][3]+'\t'+del_list[i][4]+'\t'+del_list[i][5]+'\t'+del_list[i][5]+'\n')
    del_L.close()

    file_n = os.listdir(path)
    for i in file_n:
        if i.endswith(" %s 댓글 목록.txt" % nn):  #해당 계정이 작성한 게시글의 댓글 파일 삭제
            os.remove(i)
        if i.endswith('댓글 목록'):  #해당 계정이 작성한 타 게시글의 댓글 삭제
            newlist = ''
            dellist = ''
            with open("%s" % i, 'r', encoding='UTF-8') as list:
                content = list.readlines()
                for m in content:
                    if nn in m:
                        content.remove(m)
                for o in content:
                    o = o.strip('\n')
                    o = o.strip('\t')
                    dellist += o + '\n'
                print(dellist)
                result = ''.join(map(str, dellist))
                newlist += result
                print(newlist)
            with open("%s" % i, 'w', encoding='UTF-8') as list:
                list.write(newlist)
        if i.endswith("%s.txt" % nn):  #해당 계정이 작성한 게시글 파일 삭제
            os.remove(i)
    delfromlist("구인게시글목록", nn)
    delfromlist("구직게시글목록", nn)






# 기능특성상 딕셔너리에 넣고 형준이한테 코드넘김
# def login():
#     ULIST = open('회원정보.txt', 'r', encoding="utf-8")
#     ULIST=ULIST.readlines()
#     del ULIST[0]
#     for i in range(len(ULIST)):
#         ULIST[i]=ULIST[i].replace('\n','')
#         ULIST[i]=ULIST[i].split('\t')
#     print(ULIST)
#
#     logdic={}
#     for i in range(len(ULIST)):
#         IDkey=ULIST[i][0]
#         PWvalue=ULIST[i][1]
#         logdic[IDkey]=PWvalue
#     print(logdic)

def changeNN(ID, NN):
    newinfo = ""
    with open("회원정보.txt", 'r', encoding='UTF-8') as info:
        infolist = info.readlines()
        del infolist[0]
        for i in range(len(infolist)):
            infolist[i] = infolist[i].replace('\n', '')
            infolist[i] = infolist[i].split('\t')

        nnlist = []  # 닉네임 리스트

        for i in range(len(infolist)):  # 회원 정보 리스트의 갯수를 하나씩 꺼내라
            nnlist.append(infolist[i][4])  # 닉네임 리스트에 닉네임 위치만 넣어라
        if NN not in nnlist and NN != '':  # 새로운 닉네임이 닉네임 리스트에 없고 새로운 닉네임이 빈 문자열과 같지 않으면
            for i in range(len(infolist)):  # 회원 정보 리스트의 갯수를 하나씩 꺼내라
                if ID in infolist[i]:  # 나의 아이디가 회원 정보 리스트가 안에 있으면
                    infolist[i][4] = '%s' % NN  # 새로운 닉네임을 그 위치에 덮어 씌워라
        elif NN == '' and NN in nnlist:  # 새로운 닉네임이 빈 문자열과 같거나 닉네임이 닉네임 리스트 안에 있으면
            pass  # 다음 줄로 넘어가라

        for i in range(len(infolist)):
            infolist[i] = infolist[i][0] + '\t' + infolist[i][1] + '\t' + infolist[i][2] + '\t' + \
                          infolist[i][3] + '\t' + infolist[i][4] + '\t' + infolist[i][5] + '\t' + \
                          infolist[i][6] + '\n'

        result = ''.join(map(str, infolist))
        newinfo += result

    with open("회원정보.txt", 'w', encoding='UTF-8') as changeinfo:
        changeinfo.write("아이디\t비밀번호\t이름\t성별\t닉네임\t신뢰도\t평가받은횟수\n")
        changeinfo.write(newinfo)



def changeinfoPW(ID, NPW): #패스워드 변경
    newinfo = ""
    with open("회원정보.txt", 'r', encoding='UTF-8') as info:
        infolist = info.readlines()
        del infolist[0]
        for i in range(len(infolist)):
            infolist[i] = infolist[i].replace('\n','')
            infolist[i] = infolist[i].split('\t')



        if NPW!="": #빈 칸 아닐 때 새로운 비번으로 씌우기
            for i in range(len(infolist)):
                if ID in infolist[i]:
                    infolist[i][1]='%s' % NPW
        else: #그외 입력하거나 빈칸인 경우 원본 그대로 쓰기
            pass

        for i in range(len(infolist)):
            infolist[i] = infolist[i][0] + '\t' + infolist[i][1] + '\t' + infolist[i][2] + '\t' + \
            infolist[i][3] + '\t' + infolist[i][4] + '\t'+infolist[i][5] + '\t' + infolist[i][6] + '\n'


        result = ''.join(map(str, infolist))
        newinfo += result
    with open("회원정보.txt", 'w', encoding='UTF-8') as changeinfo:
        changeinfo.write("아이디\t비밀번호\t이름\t성별\t닉네임\t신뢰도\t평가받은횟수\n")
        changeinfo.write(newinfo)


import requests
import pandas as pd
import numpy as np
import folium
from folium.plugins import MiniMap

def elec_location(region,page_num):
    url = 'https://dapi.kakao.com/v2/local/search/keyword.json'
    params = {'query': region,'page': page_num}
    ## region에는  검색명이 들어갈 것임
    ## page_num은 1~3이 입력될 건데, 한 페이지 당 검색목록이 최대 15개임.
    ## 만약 page_num이 4이상이 되면 3페이지랑 같은 15개의 결과 값을 가져옴. 그래서 1~3만 쓰는 것임

    headers = {"Authorization": "KakaoAK 0501ad7d30c60a29bb293c856dec54f8"}
    ##카카오 API

    places = requests.get(url, params=params, headers=headers).json()['documents']
    total = requests.get(url, params=params, headers=headers).json()['meta']['total_count']
    ## ['meta']['total_count']은 내가 '성산일출봉 전기충전소'를 검색했을 때, 나오는 총 결과 값.
    ## ['meta']['total_count']이 45보다 크면 45개만 가져오게 됨

    if total > 45:
        print(total,'개 중 45개 데이터밖에 가져오지 못했습니다!')
    else :
        print('모든 데이터를 가져왔습니다!')
    return places





def elec_info(places):## 이 함수는 위 함수 결과 값(1 ~ 45개) 하나하나 분리해서 저장할 것임
    X = []
    Y = []
    stores = []
    road_address = []
    place_url = []
    ID = []
    for place in places:
        X.append(float(place['x']))
        Y.append(float(place['y']))
        stores.append(place['place_name'])
        road_address.append(place['road_address_name'])
        place_url.append(place['place_url'])
        ID.append(place['id'])
    # 1번 결과 값 안에는 1번 충전소 이름, 위도, 경도, 전화번호, 도로명 주소 등이 있는데 각각 배열에 저장

    ar = np.array([ID,stores, X, Y, road_address,place_url]).T
    df = pd.DataFrame(ar, columns = ['ID','stores', 'X', 'Y','road_address','place_url'])
    ## 병원 ID, 충전소 이름, 위도, 경도, 도로명주소, 사이트주소를 저장할 것임
    return df



def keywords(location_name):## 여러개의 키워드를 검색할 때 사용할 함수임
## location_name에는 ['대전 서구 둔산동 쿨펫동물병원]처럼 배열이 입력
    df = None
    for loca in location_name:
        for page in range(1,4):
            local_name = elec_location(loca, page)
            local_elec_info = elec_info(local_name)

            if df is None:
                df = local_elec_info
            elif local_elec_info is None:
                continue
            else:
                df = pd.concat([df, local_elec_info],join='outer', ignore_index = True)
    return df



def make_map(dfs):
    # 지도 생성하기
    m = folium.Map(location=[36.3542446,127.3754091],zoom_start=14)   # 기준좌표: 제주어딘가로 내가 대충 설정

    # 미니맵 추가하기
    minimap = MiniMap()
    m.add_child(minimap)

    # 마커 추가하기
    for i in range(len(dfs)):
        folium.Marker([df['Y'][i],df['X'][i]],tooltip=dfs['stores'][i],popup=dfs['place_url'][i],).add_to(m)
    m.save('map123.html')
    webbrowser.open('map123.html')

## 여기 두 개 키워드처럼 가까운 거리에 있는 키워드를 입력하면
## 중복해서 동물를 검색할 가능성이 아주 놓기 때문에
## drop_duplicates를 해주고 인덱스 리셋을 해준다
def hh(chHname):
    global df
    Hlist = list(chHname[0])
    strH = ''.join(chHname[0])
    chHname=strH.strip('\t')
    if chHname:
        location = [Hlist[2] + ' ' + Hlist[0]]
        df = keywords(location)
        df = df.drop_duplicates(['ID'])
        df = df.reset_index()
        make_map(df)
