import tkinter as tk
from tkinter import *
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time as t
win = Tk()
win.title('매크로 프로그램')

win.geometry("840x400") #창의 사이즈
win.resizable(True,True) #창의 사이즈 변경 여부 속성 지정\
framefirst=Frame(win)
framefirst.pack()
framesecond=Frame(win)
framesecond.pack()






#키보드 이벤트, 마우스 이벤트, 요소찾기 이벤트, url 가져오기 이벤트, 지우기 이벤트, (크롬드라이버 변경)
def InputURLpage():
    global pro
    global txt1
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
    btn = Button(frame2, text="OK", width=15, command=OKURL)
    btn.grid(row=2, column=1)
    pro.mainloop()
    win.mainloop()
def OKURL():
    listbox.insert(0, "1.URL : %s" % txt1.get())
    pro.withdraw()

def InputElement():
    global pro2
    global txt2
    global answer1
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
    btntax = tk.Button(pro2, text="적용하기", command=OKElement)
    btntax.grid(row=4, column=1)
    pro2.mainloop()
    win.mainloop()
def ResultEle():
    if answer1.get() == 0:
        return driver.find_element(By.CLASS_NAME, txt2.get())
    elif answer1.get() == 1:
        return driver.find_element(By.XPATH, txt2.get())
    elif answer1.get() == 2:
        return driver.find_element(By.ID, txt2.get())
def OKElement():
    listbox.insert(END, "2.요소값 : %s" % txt2.get())
    listbox.config()
    pro2.withdraw()

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
    txtsearchpath.bind("<Return>", txtsearchpath.get())
    txtsearch = Entry(pro3)
    txtsearch.grid(row=1, column=1)
    txtsearch.bind("<Return>", txtsearch.get())
    btntax = tk.Button(pro3, text="검색", command=OKSearch)
    btntax.grid(row=2, column=1)
    pro3.mainloop()
    win.mainloop()
def OKSearch():
    listbox.insert(END, "3.검색창 PATH값 : %s / 4.검색어 : %s" % (txtsearchpath.get(),txtsearch.get()))
    #listbox.insert(END, "4.검색어 : %s" % txtsearch.get())
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
    txtDP1= Entry(pro4)
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
    listbox.insert(END, "5.데이터 수집 PATH값 1 : %s / 6.데이터 수집 PATH값 2: %s" % (txtDP1.get(),txtDP2.get()))
    #listbox.insert(END, "6.데이터 수집 PATH값 2: %s" % txtDP2.get())
    pro4.withdraw()

def listToString(str_list):
    result = ""
    for s in str_list:
        result += s + ""
    return result.strip()
def Delete():
    listbox.delete(END)

def final():
    global driver
    global a
    # Traverse the tuple returned by
    # curselection method and print
    # corresponding value(s) in the listbox
    driver = webdriver.Chrome("chromedriver.exe")
    url = txt1.get()
    driver.get(url)
    t.sleep(5)

    for i in range(1, listbox.size()):
        driver.get(driver.current_url)
        listbox.select_set(i)
        listbox.event_generate("<<ListboxSelect>>")
        try:
            if listbox.get(i) == "2.요소값 : %s" % txt2.get():
                a = ResultEle()
                a.click()
                t.sleep(5)
                driver.get(driver.current_url)
                print(driver.current_url)
            elif listbox.get(i) == "3.검색창 PATH값 : %s / 4.검색어 : %s" % (txtsearchpath.get(), txtsearch.get()):
                driver.get(driver.current_url)
                elem = driver.find_element(By.XPATH, txtsearchpath.get())
                elem.send_keys(txtsearch.get())
                elem.send_keys(Keys.RETURN)
                t.sleep(5)
            elif listbox.get(i) == "5.데이터 수집 PATH값 1 : %s / 6.데이터 수집 PATH값 2: %s" % (txtDP1.get(), txtDP2.get()):
                driver.get(driver.current_url)
                lista = []
                listb = []
                for i in range(len(txtDP1.get())):
                    if txtDP1.get()[i] == txtDP2.get()[i]:
                        lista.append(txtDP1.get()[i])
                    elif txtDP1.get()[i] != txtDP2.get()[i]:
                        listb.append(txtDP1.get()[i:len(txtDP1.get())])
                        break
                result1 = listToString(lista)
                result2 = listToString(listb)
                for xpath2 in range(1, 100000000000):
                    try:
                        xpath100 = result1 + str(xpath2) + result2[1:]
                        print(str(xpath2), ": %s" % driver.find_element(By.XPATH, xpath100).text)
                    except:
                        print("데이터 수집 완료")
                        break
        except:
            try:
                if listbox.get(i) == "3.검색창 PATH값 : %s / 4.검색어 : %s" % (txtsearchpath.get(), txtsearch.get()):
                    driver.get(driver.current_url)
                    elem = driver.find_element(By.XPATH, txtsearchpath.get())
                    elem.send_keys(txtsearch.get())
                    elem.send_keys(Keys.RETURN)
                    t.sleep(5)
                elif listbox.get(i) == "5.데이터 수집 PATH값 1 : %s / 6.데이터 수집 PATH값 2: %s" % (txtDP1.get(), txtDP2.get()):
                    driver.get(driver.current_url)
                    lista = []
                    listb = []
                    for i in range(len(txtDP1.get())):
                        if txtDP1.get()[i] == txtDP2.get()[i]:
                            lista.append(txtDP1.get()[i])
                        elif txtDP1.get()[i] != txtDP2.get()[i]:
                            listb.append(txtDP1.get()[i:len(txtDP1.get())])
                            break
                    result1 = listToString(lista)
                    result2 = listToString(listb)
                    for xpath2 in range(1, 100000000000):
                        try:
                            xpath100 = result1 + str(xpath2) + result2[1:]
                            print(str(xpath2), ": %s" % driver.find_element(By.XPATH, xpath100).text)
                        except:
                            print("데이터 수집 완료")
                            break
            except:
                try:
                    if listbox.get(i) == "2.요소값 : %s" % txt2.get():
                        driver.get(driver.current_url)
                        a = ResultEle()
                        a.click()
                        t.sleep(5)
                        driver.get(driver.current_url)
                        print(driver.current_url)
                    elif listbox.get(i) == "5.데이터 수집 PATH값 1 : %s / 6.데이터 수집 PATH값 2: %s" % (
                    txtDP1.get(), txtDP2.get()):
                        driver.get(driver.current_url)
                        lista = []
                        listb = []
                        for i in range(len(txtDP1.get())):
                            if txtDP1.get()[i] == txtDP2.get()[i]:
                                lista.append(txtDP1.get()[i])
                            elif txtDP1.get()[i] != txtDP2.get()[i]:
                                listb.append(txtDP1.get()[i:len(txtDP1.get())])
                                break
                        result1 = listToString(lista)
                        result2 = listToString(listb)
                        for xpath2 in range(1, 100000000000):
                            try:
                                xpath100 = result1 + str(xpath2) + result2[1:]
                                print(str(xpath2), ": %s" % driver.find_element(By.XPATH, xpath100).text)
                            except:
                                print("데이터 수집 완료")
                                break
                except:
                    try:
                        if listbox.get(i) == "2.요소값 : %s" % txt2.get():
                            driver.get(driver.current_url)
                            a = ResultEle()
                            a.click()
                            t.sleep(5)
                            driver.get(driver.current_url)
                            print(driver.current_url)
                        elif listbox.get(i) == "3.검색창 PATH값 : %s / 4.검색어 : %s" % (txtsearchpath.get(), txtsearch.get()):
                            driver.get(driver.current_url)
                            elem = driver.find_element(By.XPATH, txtsearchpath.get())
                            elem.send_keys(txtsearch.get())
                            elem.send_keys(Keys.RETURN)
                            t.sleep(5)
                    except:
                        try:
                            if listbox.get(i) == "2.요소값 : %s" % txt2.get():
                                driver.get(driver.current_url)
                                a = ResultEle()
                                a.click()
                                t.sleep(5)
                                driver.get(driver.current_url)
                                print(driver.current_url)
                        except:
                            try:
                                if listbox.get(i) == "3.검색창 PATH값 : %s / 4.검색어 : %s" % (
                                        txtsearchpath.get(), txtsearch.get()):
                                    driver.get(driver.current_url)
                                    elem = driver.find_element(By.XPATH, txtsearchpath.get())
                                    elem.send_keys(txtsearch.get())
                                    elem.send_keys(Keys.RETURN)
                                    t.sleep(5)
                            except:
                                try:
                                    if listbox.get(i) == "5.데이터 수집 PATH값 1 : %s / 6.데이터 수집 PATH값 2: %s" % (
                                            txtDP1.get(), txtDP2.get()):
                                        driver.get(driver.current_url)
                                        lista = []
                                        listb = []
                                        for i in range(len(txtDP1.get())):
                                            if txtDP1.get()[i] == txtDP2.get()[i]:
                                                lista.append(txtDP1.get()[i])
                                            elif txtDP1.get()[i] != txtDP2.get()[i]:
                                                listb.append(txtDP1.get()[i:len(txtDP1.get())])
                                                break
                                        result1 = listToString(lista)
                                        result2 = listToString(listb)
                                        for xpath2 in range(1, 100000000000):
                                            try:
                                                xpath100 = result1 + str(xpath2) + result2[1:]
                                                print(str(xpath2),
                                                      ": %s" % driver.find_element(By.XPATH, xpath100).text)
                                            except:
                                                print("데이터 수집 완료")
                                                break
                                except:
                                    print("끝")
                                    break
            #listbox.delete(0)



listbox = Listbox(win, selectmode='single', height=10, width=100)
listbox.pack()

btn1=tk.Button(framefirst,width=25,height=10,text="URL입력",font=("bold",10,"bold"),fg="white",bg="mediumturquoise",command=InputURLpage)
btn1.grid(row=3, column=3)
btn2=tk.Button(framefirst,width=25,height=10,text="요소입력",font=("bold",10,"bold"),fg="white",bg="cornflowerblue", command=InputElement)
btn2.grid(row=3, column=4)
btn4=tk.Button(framefirst,width=25,height=10,text="검색값입력",font=("bold",10,"bold"),fg="white",bg="mediumslateblue",command=InputSearch)
btn4.grid(row=3, column=5)
btn3=tk.Button(framefirst,width=25,height=10,text="데이터수집",font=("bold",10,"bold"),fg="white",bg="mediumpurple",command=CollectData)
btn3.grid(row=3, column=6)

lbl0 = Label(win, text="")
lbl0.pack()

btnOUTPUT=tk.Button(win, text="출력",command=final)
btnOUTPUT.pack()
btnreset=tk.Button(win, text="초기화",command=Delete)
btnreset.pack()
win.mainloop()