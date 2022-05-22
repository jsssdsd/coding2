import tkinter as tk
from tkinter import *
import mecrosel_mod2 as mm2
from selenium import webdriver

from selenium.webdriver.common.by import By
import time as t
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

win = Tk()
win.title('매크로 프로그램')

win.geometry("840x440")  # 창의 사이즈
win.resizable(True, True)  # 창의 사이즈 변경 여부 속성 지정\
framefirst = Frame(win)
framefirst.pack()
framesecond = Frame(win)
framesecond.pack()
c = 0
listB = ''
url1 = ''
cE=0
libl1=[]
libl2=[]
libl3=[]
libl4=[]
txtl=''
Lsc1=[]
Lsc2=[]
tu1=()
tu2=()
# elem1=''
da11=''
da22=''
da33=''
da44=''
d5=[]
da55=[]
Ldc=0
# result=driver.find_element_by_id('id')
# print(result.text)
# driver.find_element(By.CLASS_NAME, txt2.get())

# 키보드 이벤트, 마우스 이벤트, 요소찾기 이벤트, url 가져오기 이벤트, 지우기 이벤트, (크롬드라이버 변경)
def InputURLpage():
    global pro
    global txt1
    global url1
    pro = Toplevel(win)
    pro.title("URL 입력창")  # 창의 타이틀명
    pro.geometry("500x100")  # 창의 사이즈
    frame2 = tk.Frame(pro)
    frame2.pack()

    lbl2 = Label(frame2, text="URL입력")
    lbl2.grid(row=1, column=0)
    txt1 = Entry(frame2)
    txt1.grid(row=1, column=1)
    txt1.bind("<Return>", txt1.get())
    url1 = txt1.get()
    btn = Button(frame2, text="OK", width=15, command=OKURL)
    btn.grid(row=2, column=1)
    pro.mainloop()
    win.mainloop()


#
# def ResultEle():
#     if answer1.get() == 0:
#         print(crolD.find_element(By.CLASS_NAME, txt2).get())
#         return crolD.find_element(By.CLASS_NAME, txt2.get())
#     elif answer1.get() == 1:
#         print(crolD.find_element(By.XPATH, txt2.get()))
#         return crolD.find_element(By.XPATH, txt2.get())
#     elif answer1.get() == 2:
#         print(crolD.find_element(By.ID, txt2.get()))
#         return crolD.find_element(By.ID, txt2.get())


import datetime

def doScrollDown(whileSeconds):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=whileSeconds)
    while True:
        crolD.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        t.sleep(1)
        if datetime.datetime.now() > end:
            break

def OKURL():
    listbox.insert(0, "1.URL : %s" % txt1.get())
    pro.withdraw()


def InputElement():
    global pro2
    global txt2
    global answer1
    global cE
    pro2 = Toplevel(win)
    pro2.title("요소값 입력창")  # 창의 타이틀명
    pro2.geometry("500x300")  # 창의 사이즈
    answer1 = tk.IntVar()
    Rad1 = tk.Radiobutton(pro2, text="class_name", variable=answer1, value=0)
    Rad1.grid(row=0, column=1, sticky="w")
    Rad2 = tk.Radiobutton(pro2, text="xpath", variable=answer1, value=1)
    Rad2.grid(row=1, column=1, sticky="w")
    Rad3 = tk.Radiobutton(pro2, text="id", variable=answer1, value=2)
    Rad3.grid(row=2, column=1, sticky="w")
    txt2 = Entry(pro2)
    txt2.grid(row=3, column=1)
    txt2.bind("<Return>", txt2.get())

    def ADDElement():
        global c
        c = c + 1
        listbox2.insert(c, "2.PATH값 : %s" % txt2.get())


    def DELElement():
        global c
        c = c - 1
        listbox2.delete(END)

    def ADELElement():
        global c
        c = 0
        listbox2.delete(0, END)

    def LCELElement():
        global listB
        global c
        global cE
        listB = (listbox2.get(0, END))
        print(len(listB))
        for i in range(len(listB)):
            listbox.insert(END, (listbox2.get(i)))
        # print(listB)
        cE=c
        c = 0
        print(listbox.get(0))
        print(cE)

        # pro.withdraw()
        pro2.withdraw()

    btntax = tk.Button(pro2, text="추가하기", command=ADDElement)
    btntax.grid(row=4, column=1)
    btntax = tk.Button(pro2, text="삭제하기", command=DELElement)
    btntax.grid(row=5, column=1)
    btntax = tk.Button(pro2, text="전체삭제", command=ADELElement)
    btntax.grid(row=6, column=1)
    btntax = tk.Button(pro2, text="완료", command=LCELElement)
    btntax.grid(row=6, column=3)
    lbl2 = Label(pro2, text="요소리스트")
    lbl2.grid(row=2, column=7)
    # listbox2 = Listbox(pro2, selectmode='extended', height=5, width=30)
    # listbox2.grid(row=3, column=7)
    listbox2 = Listbox(pro2, selectmode='extended', height=5, width=30)
    listbox2.grid(row=3, column=7)
    pro2.mainloop()
    win.mainloop()

#
# def OKElement():
#     listbox.insert(END, "2.요소값 : %s" % txt2.get())
#     listbox.config()
#     pro2.withdraw()


def InputSearch():
    global pro3
    global txtsearch
    global txtsearchpath
    pro3 = Toplevel(win)
    pro3.title("검색 기능")  # 창의 타이틀명
    pro3.geometry("500x300")  # 창의 사이즈

    lbl1 = Label(pro3, text="검색창 PATH값")
    lbl1.grid(row=0, column=0)
    lbl2 = Label(pro3, text="검색어")
    lbl2.grid(row=1, column=0)
    txtsearchpath = Entry(pro3)
    txtsearchpath.grid(row=0, column=1)
    txtsearchpath.bind("<Return>", txtsearchpath.get())  #검색 PATH
    txtsearch = Entry(pro3)
    txtsearch.grid(row=1, column=1)
    txtsearch.bind("<Return>", txtsearch.get())   #검색어 ...
    # btntax = tk.Button(pro3, text="검색", command=OKSearch)
    # btntax.grid(row=2, column=1)

    def ADDElement():
        global c
        print(txtsearchpath.get())
        if txtsearchpath.get() == '':
            c = c + 1
            listbox2.insert(c + 1, "4.검색어 : %s" % txtsearch.get())
            # listbox2.insert(c, "3.검색창 PATH값 : %s" % txtsearchpath.get())
            # listbox2.insert(c, "3.검색창 PATH값 : %s / 4.검색어 : %s" % (txtsearchpath.get(), txtsearch.get()))
        elif txtsearch.get() == '':
            c = c + 1
            listbox2.insert(c, "3.검색창 PATH값 : %s" % txtsearchpath.get())
            # listbox2.insert(c + 1, "4.검색어 : %s" % txtsearch.get())

        else:
            c = c + 2
            listbox2.insert(c, "3.검색창 PATH값 : %s" % txtsearchpath.get())
            listbox2.insert(c + 1, "4.검색어 : %s" % txtsearch.get())
            # listbox2.insert(c, "3.검색창 PATH값 : %s / 4.검색어 : %s" % (txtsearchpath.get(), txtsearch.get()))

    def DELElement():
        global c
        c = c - 1
        listbox2.delete(END)

    def ADELElement():
        global c
        c = 0
        listbox2.delete(0, END)

    def LCELElement():
        global c
        global cE
        global listB
        listB = (listbox2.get(0, END))
        print(len(listB))
        for i in range(len(listB)):
            listbox.insert(END, (listbox2.get(i)))  # 검색이니까
        # print(listB)
        cE = c
        c = 0

        pro3.destroy()

    btntax = tk.Button(pro3, text="추가하기", command=ADDElement)
    btntax.grid(row=4, column=1)
    btntax = tk.Button(pro3, text="삭제하기", command=DELElement)
    btntax.grid(row=5, column=1)
    btntax = tk.Button(pro3, text="전체삭제", command=ADELElement)
    btntax.grid(row=6, column=1)
    btntax = tk.Button(pro3, text="완료", command=LCELElement)
    btntax.grid(row=6, column=3)
    lbl2 = Label(pro3, text="검색리스트")
    lbl2.grid(row=2, column=7)
    listbox2 = Listbox(pro3, selectmode='extended', height=5, width=30)
    listbox2.grid(row=3, column=7)
    pro3.mainloop()
    win.mainloop()


def OKSearch():
    listbox.insert(END, "3.검색창 PATH값 : %s / 4.검색어 : %s" % (txtsearchpath.get(), txtsearch.get()))
    # listbox.insert(END, "4.검색어 : %s" % txtsearch.get())
    pro3.withdraw()

def CollectData():
    global pro4
    global txtDP1
    global txtDP2
    pro4 = Toplevel(win)
    pro4.title("데이터 수집")  # 창의 타이틀명
    pro4.geometry("500x300")  # 창의 사이즈

    lbl1 = Label(pro4, text="예시데이터 PATH값 1")
    lbl1.grid(row=0, column=0)
    lbl2 = Label(pro4, text="예시데이터 PATH값 2")
    lbl2.grid(row=1, column=0)
    txtDP1 = Entry(pro4)
    txtDP1.grid(row=0, column=1)
    txtDP1.bind("<Return>", txtDP1.get())
    txtDP2 = Entry(pro4)
    txtDP2.grid(row=1, column=1)
    txtDP2.bind("<Return>", txtDP2.get())
    btntax = tk.Button(pro4, text="데이터 추출", command=OKData)
    btntax.grid(row=2, column=1)
    pro4.mainloop()
    win.mainloop()


def OKData():
    global c
    global cE
    global listB
    # listbox.insert(END, "5.데이터 수집 PATH값 1 : %s / 6.데이터 수집 PATH값 2: %s" % (txtDP1.get(), txtDP2.get()))

    listbox.insert(END, "5.데이터 수집 PATH값 1 : %s" % txtDP1.get())
    listbox.insert(END, "6.데이터 수집 PATH값 2 : %s" % txtDP2.get())
    # listB = (listbox2.get(0, END))
    # print(len(listB))
    # for i in range(len(listB)):
    #     listbox.insert(END, (txtDP1.get(i), txtDP2.get(i)))
    pro4.withdraw()

def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + ""
    return result.strip()

def Delete():
    listbox.delete(END)

def ALLDelete():
    listbox.delete(0, END)


def final():
    global crolD
    global a
    global c
    global libl1
    global libl2
    global libl3
    global libl4
    global txtl
    global tu1
    global tu2
    global Lsc1
    global Lsc2
    global elem1
    global da11
    global da22
    global da33
    global da44
    global sc3
    global d5
    global df1
    global df2


    # Traverse the tuple returned by
    # curselection method and print
    # corresponding value(s) in the listbox
    # print("요소체크박스", ResultEle())
    # for i in range(listbox.size()):
    listbox.select_set(0)
    listbox.event_generate("<<ListboxSelect>>")

    if listbox.get(0) == "1.URL : %s" % txt1.get():
        crolD = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        url = txt1.get()
        crolD.get(url)
        t.sleep(1)

        d1 = txt1.get()
        # # mm2.deldata()
        # mm2.inpelement(d1, '', '', '','')

        print("리스트박스값",listbox.get(0,END))  # listbox.get(1)은 두번째값 소환 0부터시작
        print(listbox.size())

        # listbox2.get(0,END)

        for i in range(listbox.size()):
            print("i값",i)
            # print("2.PATH값 : %s" % listbox.get(1))
            print(str(listbox.get(1)))
            # if 1<=i<cE+1: #요소 , 검색 크롤러 실행
            # listbox.get(i + 1)
            if '2.PATH값' in str(listbox.get(i)) :
                print("listbox i값:", str(listbox.get(i)))  #전처리 뒤의 PATH값만 따온다.
                libl1= listbox.get(i) #튜블 리스트화
                libl2= libl1[10:]
                print("libl2값",libl2)
                txtl= libl2
                print("txtl값",txtl)
                # txt2.get= str(listbox.get(i+1))  #@@@@@앞에 문자르 빼고 삽입한다.
                txt2.get =txtl

                a = crolD.find_element(By.XPATH, txt2.get)
                print("a의값",a)
                a.click()
                t.sleep(1.5)

                # d2 = listbox.get(i)
                d2=txtl
                da22=txtl
                # mm2.deldata()
                mm2.inpelement(d1,d2,'','','')

            elif '3.검색창' in str(listbox.get(i)):
                # print("resultEle의값", ResultEle())
                # driver(driver.current_url)
                # print(txt2.get(i+1))
                # txtsearchpath.get() = 검색PATH
                # txtsearch.get()) = 검색 값

                print("listbox i값:", str(listbox.get(i)))  # 전처리!  뒤의 PATH값만 따온다.

                libl1 = listbox.get(i)  # 튜블 리스트화
                libl2 = libl1[14:]     #검색창 PATH

                print("libl2값", libl2)
                txtl = libl2
                print("txtl값", txtl)
                # txt2.get= str(listbox.get(i+1))  #@@@@@앞에 문자르 빼고 삽입한다.
                txtsearchpath.get = txtl

                sc3 = txtsearchpath.get
                t.sleep(1.5)
                # txtsearchpath.get = listbox.get(i)  #검색 경로를 바꿔준다 내 리스트에 목록으로

                # txtsearch.get = listbox.get(i) ##검색값을 바꿔준다 내 리스트에 목록으로
                #     elem = driver.find_element(By.XPATH, txtsearchpath.get())
                #     elem.send_keys(txtsearch.get())
                #     elem.send_keys(Keys.RETURN)
                # print("a의값", a)
                # a.click()

                # crolD.get(crolD.current_url)
                # print(crolD.current_url)
                da33 = txtl
                da3 = txtl
                # mm2.deldata()
                mm2.inpelement(d1, '', da33, '','') # url, ele, scPATH, SCip, DA

            elif '4.검색어' in str(listbox.get(i)):
                # print("resultEle의값", ResultEle())
                # driver(driver.current_url)
                # print(txt2.get(i+1))
                # txtsearchpath.get() = 검색PATH
                # txtsearch.get()) = 검색 값

                print("listbox i값:", str(listbox.get(i)))  # 전처리!  뒤의 PATH값만 따온다.
                libl1 = listbox.get(i)  # 튜블 리스트화
                libl2 = libl1[8:]     #검색창 PATH
                print("libl2값", libl2)
                txtl = libl2
                print("txtl값", txtl)
                # txt2.get= str(listbox.get(i+1))  #@@@@@앞에 문자르 빼고 삽입한다.
                txtsearchpath.get = sc3
                print("txtsearchpath값", txtsearchpath.get)

                txtsearch = txtl
                elem = crolD.find_element(By.XPATH, txtsearchpath.get)
                elem.send_keys(str(txtsearch)) #문자열로 바꿔줘야 입력가능한다 !! str 겟값을 넣지않는이유 xpath같은 형태데이터가아니라 그냥 문자열이므로!!
                elem.send_keys(Keys.RETURN)
                # print(elem)
                #     elem = driver.find_element(By.XPATH, txtsearchpath.get())
                #     elem.send_keys(txtsearch.get())
                #     elem.send_keys(Keys.RETURN)
                t.sleep(3)
                # crolD.get(crolD.current_url)
                # print(crolD.current_url)
                da44 = txtl
                mm2.inpelement(d1, da22, da33, da44,'')

            elif '스크롤내리기' in str(listbox.get(i)):
                global da55
                global d5
                global Ldc

                last_height = crolD.execute_script("return document.body.scrollHeight")
                crolD.execute_script('window.scrollTo(0, document.body.scrollHeight);') #끝까지 내리기
                doScrollDown(2)
                # webdriver.ActionChains(crolD).scroll(0, 0, 0, 100000000, origin=url).perform()
                print("스크롤높이", last_height)
                t.sleep(1)
                # t.sleep(SCROLL_PAUSE_SEC)
                # 스크롤 다운 후 스크롤 높이 다시 가져옴
                new_height = crolD.execute_script("return document.body.scrollHeight")
                print(new_height)
                if new_height == last_height:
                    break
                last_height = new_height

                # crolD.execute_script("scrollbot.scrollTo(0, document.body.scrollHeight);") #스크롤 봇끝까지내리기
                # webdriver.ActionChains(x).scroll(0, 0, 0, 100000000, origin=element).perform()  # 창안의 스크롤맨아래내리기
                # element = crolD.find_element(By.ID, "aside_coin")  # webdriver.ActionChains.scroll()
                # # x.switch_to.window(element) #프레임변경

            elif '5.데이터 수집' in str(listbox.get(i)):
                global da55
                global d5
                global Ldc
            # elif listbox.get(i) == "5.데이터 수집 PATH값 1 : %s / 6.데이터 수집 PATH값 2: %s" % (txtDP1.get(), txtDP2.get()):
            #     crolD.get(crolD.current_url)
                print("listbox i값:", str(listbox.get(i)))  # 전처리!  뒤의 PATH값만 따온다.
                print("listbox i+1값:", str(listbox.get(i+1)))
                libl1 = listbox.get(i)  # 튜블 리스트화
                libl2 = libl1[19:]  # 검색창 PATH
                print("libl2값", libl2)
                # txtl = libl2
                df1=libl2

                libl3 = listbox.get(i+1)  # 튜블 리스트화
                libl4 = libl3[19:]  # 검색창 PATH
                print("libl4값", libl4)
                df2=libl4

                # txt2.get= str(listbox.get(i+1))  #@@@@@앞에 문자르 빼고 삽입한다.
                txtDP1= df1
                txtDP2 = df2
                #전처리해줘야함 ... 그리고 수집 1,2칸을 나눠줘야함
                lista = []
                listb = []
                print("txtDP1값 txtDP2값",txtDP1, txtDP2)
                for i in range(len(txtDP1)):
                    if txtDP1[i] == txtDP2[i]:
                        lista.append(txtDP1[i])
                    elif txtDP1[i] != txtDP2[i]:
                        listb.append(txtDP1[i:len(txtDP1)])
                        break
                # for i in range(len(txtDP1.get)):
                #     if txtDP1.get()[i] == txtDP2.get[i]:
                #         lista.append(txtDP1.get[i])
                #     elif txtDP1.get[i] != txtDP2.get[i]:
                #         listb.append(txtDP1.get[i:len(txtDP1.get)])
                #         break
                print("리스트a", lista)
                print("리스트b", listb)
                result1 = listToString(lista)
                result2 = listToString(listb)
                print("리스트a",lista)
                print("리스트b",listb)
                print("result1:",result1,"result2:",result2)
                for xpath2 in range(1, 100000000000):
                    try:

                        xpath100 = result1 + str(xpath2) + result2[1:]
                        # print("xpath100",xpath100)
                        LO= crolD.find_element(By.XPATH, xpath100).text
                        # la= (str(xpath2), ": %s" % crolD.find_element(By.XPATH, xpath100).text)

                        la = str(xpath2+(Ldc))+": %s" %LO
                        print(la)
                        d5.append(la)
                        # mm2.inpelement(d1, da22, da33, da44, '')
                        # mm2.LDATA(d5)
                    except:
                        Ldc = xpath2-1
                        print("데이터 수집 완료")
                        break
                mm2.inpelement(d1, da22, da33, da44, '')
                mm2.LDATA(d5)
                t.sleep(5)
    #
    # else:
    #         print("데이터수집완료")


def save():
    # d1 = driver.find_element(By.XPATH, xpath100).text
    # mm2.inpelement('', '', d1)
    import os.path
    path = "element.txt"
    print(save)
    if not os.path.isfile(path):
        f = open('element.txt', 'w')

def load():
    print(load)
def scroldown():
    listbox.insert(END,"스크롤내리기")
    # x.switch_to.window(element)
    # x.execute_script("scrollbot.scrollTo(0, document.body.scrollHeight);") #끝까지내리기
    #
    # element = x.find_element(By.ID, "aside_coin")  # webdriver.ActionChains.scroll()
    # # x.switch_to.window(element)
    # # x.execute_script("scrollbot.scrollTo(0, document.body.scrollHeight);") #끝까지내리기
    # webdriver.ActionChains(x).scroll(0, 0, 0, 100000000, origin=element).perform()  # 맨아래내리기



# listbox = Listbox(win, selectmode='extended', height=10, width=100) 다중선택


listbox = Listbox(win, selectmode='single', height=10, width=100)
listbox.pack()

btn1 = tk.Button(framefirst, width=25, height=10, text="URL입력", font=("bold", 10, "bold"), fg="white",
                 bg="mediumturquoise", command=InputURLpage)
btn1.grid(row=3, column=3)
btn2 = tk.Button(framefirst, width=25, height=10, text="요소입력", font=("bold", 10, "bold"), fg="white",
                 bg="cornflowerblue", command=InputElement)
btn2.grid(row=3, column=4)
btn4 = tk.Button(framefirst, width=25, height=10, text="검색값입력", font=("bold", 10, "bold"), fg="white",
                 bg="mediumslateblue", command=InputSearch)
btn4.grid(row=3, column=5)
btn3 = tk.Button(framefirst, width=25, height=10, text="데이터수집", font=("bold", 10, "bold"), fg="white",
                 bg="mediumpurple", command=CollectData)
btn3.grid(row=3, column=6)

lbl0 = Label(win, text="")
lbl0.pack()
btn2 = tk.Button(win, text="불러오기", command=load)
# btn2.place(x=50,y=100)
btn2.pack(side='right')
btn1 = tk.Button(win, text="저장", command=save)
# btn1.place(x=50,y=100)
btn1.pack(side='right')
btn1 = tk.Button(win, text="페이지스크롤내리기", command=scroldown)
# btn1.place(x=50,y=100)
btn1.pack(side='left')

btnOUTPUT = tk.Button(win, text="출력", command=final)
btnOUTPUT.pack()
btnreset = tk.Button(win, text="초기화", command=Delete)
btnreset.pack()
btnADEL = tk.Button(win, text="allDEL", command=ALLDelete)
btnADEL.pack()
win.mainloop()