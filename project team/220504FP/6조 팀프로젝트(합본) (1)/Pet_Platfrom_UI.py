
import tkinter as tk
import petSitter as pS
import seleniummodul as gk
import os
from tkinter import messagebox
import tkinter.font as tkf
from pathlib import Path
PPpath = os.getcwd()

#로그인
loglist = []

pS.filecheck("구인게시글목록") 
pS.filecheck("구직게시글목록")
def login():
    if not os.path.isfile("회원정보.txt") == True:
        gk.signin()
    ID = entryID.get()
    PW = entryPW.get()
    ULIST = open('회원정보.txt', 'r', encoding="utf-8")
    ULIST = ULIST.readlines()
    del ULIST[0]
    for i in range(len(ULIST)):
        ULIST[i] = ULIST[i].replace('\n', '')
        ULIST[i] = ULIST[i].split('\t')
    logdic = {}
    for i in range(len(ULIST)):
        IDkey = ULIST[i][0]
        PWvalue = ULIST[i][1]
        NNvalue = ULIST[i][4]
        trustValue = ULIST[i][5]
        logdic[IDkey] = [PWvalue, NNvalue, trustValue]
    IDlist = []
    for i in range(len(ULIST)):
        IDlist.append(ULIST[i][0])
    if ID == '':
        messagebox.showinfo('로그인 실패', '아이디를 입력해주세요.')
    elif ID not in IDlist:
        messagebox.showinfo('로그인 실패', '존재하지 않는 아이디입니다.')
    elif PW == '':
        messagebox.showinfo('로그인 실패', '비밀번호를 입력해주세요.')
    elif logdic.get(ID)[0] != PW:
        messagebox.showinfo('로그인 실패', '비밀번호를 잘못 입력하였습니다.')
    elif logdic.get(ID)[0] == PW:
        global loglist
        loglist.append(logdic.get(ID)[1])
        loglist.append(logdic.get(ID)[2])
        loglist.append(ID)
        loglist.append(PW)
        messagebox.showinfo('로그인 성공', '로그인 성공!')
        mainPop()
        return loglist


def signup():
    def destroy():
        signupPop.destroy()

    signupPop = tk.Toplevel(log)
    signupPop.geometry("300x220")
    signupPop.resizable(False, False)

    gk.signin()

    ID = tk.Label(signupPop, text="ID:")
    PW = tk.Label(signupPop, text="비밀번호:")
    name = tk.Label(signupPop, text="이름:")
    sex = tk.Label(signupPop, text="성별:")
    nickname = tk.Label(signupPop, text="닉네임:")
    ID.place(x=50, y=20)
    PW.place(x=50, y=50)
    name.place(x=50, y=80)
    sex.place(x=50, y=110)
    nickname.place(x=50, y=140)

    makeID = tk.Entry(signupPop)
    makePW = tk.Entry(signupPop)
    inputname = tk.Entry(signupPop)
    chsex = tk.Entry(signupPop)
    makenn = tk.Entry(signupPop)
    makeID.place(x=110, y=20)
    makePW.place(x=110, y=50)
    inputname.place(x=110, y=80)
    chsex.place(x=110, y=110)
    makenn.place(x=110, y=140)



    def signupcom():
        getID = makeID.get()
        getPW = makePW.get()
        getname = inputname.get()
        getsex = chsex.get()
        getNname = makenn.get()
        if getID == '':
            messagebox.showinfo('가입 실패', '아이디를 입력해주세요.')
        elif getPW == '':
            messagebox.showinfo('가입 실패', '비밀번호를 입력해주세요.')
        elif getname == '':
            messagebox.showinfo('가입 실패', '이름을 입력해주세요.')
        elif getsex == '':
            messagebox.showinfo('가입 실패', '성별을 입력해주세요.')
        elif getNname == '':
            messagebox.showinfo('가입 실패', '닉네임을 입력해주세요.')
        else:
            gk.signinSuc(getID, getPW, getname, getsex, getNname)
            signupPop.destroy()


    combtn = tk.Button(signupPop, text="완료", command=signupcom, bg='gainsboro')
    combtn.place(x=120, y=170)
    cancelbtn = tk.Button(signupPop, text="취소", command=destroy, bg='gainsboro')
    cancelbtn.place(x=170, y=170)

def mainPop():
    log.withdraw()
    print(loglist)

    mainScr = tk.Toplevel(log, bg='lemonchiffon')
    mainScr.title("메인 화면")
    mainScr.geometry("510x850")
    mainScr.resizable(False, False)

    logFrame = tk.Frame(mainScr, bg='white', bd=5)
    logFrame.place(width=200, height=150, x=0, y=30)
    NNText = tk.Label(logFrame, bg='white', text="%s 님" % loglist[0], font=tkf.Font(family="Arial", size=16, weight='bold'))
    NNText.place(x=60, y=20)
    auth = tk.Label(logFrame, bg='white', text="신뢰도: %s" % loglist[1], font=tkf.Font(family="Arial", size=16))
    auth.place(x=45, y=55)

    btnfont = tkf.Font(family="modern", size=18, weight="bold")

    logoimage = tk.PhotoImage(file="%s/puppy_paw.png" % PPpath)
    logo = tk.Label(mainScr, bg='lemonchiffon', image=logoimage)
    logo.image = logoimage
    logo.place(x=320, y=10)

    titlelabel = tk.Label(mainScr, text="애완견 플랫폼", font=tkf.Font(size=20, family='맑은 고딕'), bg='lemonchiffon')
    titlelabel.place(x=310, y=160)

    # 로그아웃
    def logout():
        global loglist
        loglist = []
        pS.l_e = []
        log.deiconify()
        mainScr.destroy()
    logoutbtn = tk.Button(logFrame, text="로그아웃", command=logout, bg='gainsboro')
    logoutbtn.place(x=105, y=100)

    # 회원정보
    def accinfo():
        def delacc():  # 회원탈퇴
            warning = tk.Toplevel(infoWin, bg='lemonchiffon')
            warning.geometry('300x150')
            warning.resizable(False, False)
            def finalC():
                gk.Udel(loglist[2], loglist[0])
                warning.destroy()
                logout()
            ctimage = tk.PhotoImage(file="%s/caution.png" % PPpath)
            Caution = tk.Label(warning, image=ctimage,
                                font=tkf.Font(weight='bold', size=10), bg='lemonchiffon')
            Caution.image = ctimage
            Caution.place(x=120, y=0)
            warningT = tk.Label(warning, text='정말로 회원 탈퇴를 하겠습니까?',
                                font=tkf.Font(size=12, weight='bold'), bg='lemonchiffon')
            warningT.place(x=30, y=70)
            yesbtn = tk.Button(warning, text='진행', command=finalC)
            yesbtn.place(x=110, y=110)
            nobtn = tk.Button(warning, text='취소', command=warning.destroy)
            nobtn.place(x=160, y=110)


        infofont = tkf.Font(size=12, weight='bold')
        infoWin = tk.Toplevel(mainScr, bg='lemonchiffon')
        infoWin.title("회원 정보")
        infoWin.geometry("350x300")
        infoWin.resizable(False, False)
        label = tk.Label(infoWin, text="ID:\n\nPW:\n\n이름:\n\n성별:\n\n닉네임:\n\n신뢰도:",
                         font=infofont, bg='lemonchiffon')
        label.place(x=80, y=20)

        pS.viewinfo(loglist[2])
        infolabel = tk.Label(infoWin, text="%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s" %
                                           (pS.acc_info[0], pS.acc_info[1], pS.acc_info[2],
                                            pS.acc_info[3], pS.acc_info[4], pS.acc_info[5]), bg='lemonchiffon',
                             font=infofont)
        infolabel.place(x=160, y=20)


        def editinfo():
            infofont = tkf.Font(size=12, weight='bold')
            editWin = tk.Toplevel(infoWin, bg='lemonchiffon')
            editWin.title("정보 수정")
            editWin.geometry("350x200")
            editWin.resizable(False, False)

            label = tk.Label(editWin, text="PW:\n\n닉네임:", font=infofont, bg='lemonchiffon')
            label.place(x=70, y=50)
            pS.viewinfo(loglist[2])
            changePW = tk.Entry(editWin, bg='white')
            changePW.insert(0, pS.acc_info[1])
            changePW.place(x=140, y=50)
            changeNN = tk.Entry(editWin, bg='white')
            changeNN.insert(0, pS.acc_info[4])
            changeNN.place(x=140, y=90)


            def editNNPW():
                nPW = changePW.get()
                nNN = changeNN.get()

                Ulist = open("회원정보.txt", 'r', encoding='utf-8')
                Ulist = Ulist.readlines()
                del Ulist[0]
                for i in range(len(Ulist)):
                    Ulist[i] = Ulist[i].replace("\n", "")
                    Ulist[i] = Ulist[i].split("\t")
                secPW = []
                thrnick = []
                for i in range(len(Ulist)):
                    sec = Ulist[i][1]
                    thr = Ulist[i][4]
                    thrnick.append(thr)
                    secPW.append(sec)
                def chNN():
                    if nNN == loglist[0]:
                        gk.changeNN(loglist[0], nNN)
                        pS.changeallNN(loglist[0], nNN)
                        loglist[0] = nNN
                        NNText.config(text="%s 님" % loglist[0])
                        infoWin.destroy()
                    elif nNN not in thrnick:
                        gk.changeNN(pS.acc_info[0], nNN)
                        pS.changeallNN(loglist[0], nNN)
                        loglist[0] = nNN
                        NNText.config(text="%s 님" % loglist[0])
                        infoWin.destroy()
                    else:
                        messagebox.showinfo('중복 오류', '이미 존재하는 닉네임입니다.')
                if nPW == loglist[3]:
                    gk.changeinfoPW(loglist[2], nPW)
                    chNN()
                elif nPW not in secPW:
                    gk.changeinfoPW(loglist[2], nPW)
                    chNN()
                else:
                    messagebox.showinfo("중복 오류", '이미 존재하는 비밀번호입니다.')

                pS.acc_info = []

            combtn = tk.Button(editWin, text='완료', command=editNNPW, bg='gainsboro')
            combtn.place(x=120, y=150)
            closebtn = tk.Button(editWin, text="닫기", command=editWin.destroy, bg='gainsboro')
            closebtn.place(x=200, y=150)


        def closeWin():
            pS.acc_info = []
            infoWin.destroy()


        editbtn = tk.Button(infoWin, text="정보 수정", command=editinfo, bg='gainsboro')
        editbtn.place(x=60, y=250)
        signout = tk.Button(infoWin, text="회원탈퇴", command=delacc, bg='gainsboro')
        signout.place(x=150, y=250)
        closebtn = tk.Button(infoWin, text="닫기", command=closeWin, bg='gainsboro')
        closebtn.place(x=240, y=250)

    editinfo = tk.Button(logFrame, text="회원 정보", command=accinfo, bg='gainsboro')
    editinfo.place(x=25, y=100)


    # 종료
    def quit():
        global loglist
        loglist = []
        mainScr.destroy()
        log.destroy()
    quitbtn = tk.Button(mainScr, text="종료", command=quit, bg='gainsboro')
    quitbtn.place(x=230, y=810)



    def trade():
        tradeScr = tk.Toplevel(mainScr, bg='lemonchiffon')
        tradeScr.title('용품 거래')
        tradeScr.geometry('680x400')
        tradeScr.resizable(False, False)

        def sell_post_page():
            nickname = loglist[0]

            sell_post_page = tk.Toplevel(tradeScr, bg='lemonchiffon')
            sell_post_page.geometry('800x400')
            sell_post_page.resizable(True, True)

            # 제목
            title = tk.Label(sell_post_page, text='제목:', bg='lemonchiffon')
            title.place(x=130, y=50)
            title_write = tk.Entry(sell_post_page)
            title_write.place(x=200, y=50, width=380)

            # 용품
            product = tk.Label(sell_post_page, text='용품', bg='lemonchiffon')
            product.place(x=130, y=80)
            product_write = tk.Entry(sell_post_page)
            product_write.place(x=200, y=80, width=380)

            # 종류
            type = tk.Label(sell_post_page, text='종류', bg='lemonchiffon')
            type.place(x=130, y=110)
            type_write = tk.Entry(sell_post_page)
            type_write.place(x=200, y=110, width=380)

            # 가격
            price = tk.Label(sell_post_page, text='가격', bg='lemonchiffon')
            price.place(x=130, y=140)
            price_write = tk.Entry(sell_post_page)
            price_write.place(x=200, y=140, width=380)

            # 게시글
            post = tk.Label(sell_post_page, text='게시글:', bg='lemonchiffon')
            post.place(x=130, y=170)
            post_write = tk.Text(sell_post_page)
            post_write.place(x=200, y=170, width=380, height=100)

            def sell_post():
                if not os.path.isfile('sell_post_database.txt') == True:
                    file = open('sell_post_database.txt', 'w', encoding='utf-8')
                    file.close()

                # 판매글 작성
                title = title_write.get()
                product = product_write.get()
                type = type_write.get()
                price = price_write.get()
                post = post_write.get('1.0', 'end')
                if title == '':
                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                    return
                elif product == '':
                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                    return
                elif type == '':
                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                    return
                elif price == '':
                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                    return
                elif post == '':
                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                    return
                else:

                    # 게시글 데이터베이스 업로드
                    with open('sell_post_database.txt', 'a', encoding='utf-8') as file:
                        file.write(nickname + '\t' + title + '\t' + product + '\t' + type + '\t' + price + '\t' + post)
                        file.write('')
                        sell_post_page.destroy()

                        # 판매글 제목 출력
                    with open('sell_post_database.txt', 'r', encoding='utf-8') as file:
                        sell_posts = file.readlines()
                        sell_posts = ''.join(sell_posts).strip()
                        sell_posts = sell_posts.split('\n')

                        titles = []
                        for sell_post in sell_posts:
                            sell_post = sell_post.split('\t')
                            title = sell_post[1]
                            titles.append(title)

                    sell_post_list.delete(0, 'end')
                    count = 0
                    for title in titles:
                        sell_post_list.insert(count, title)
                        count += 1

            button_write = tk.Button(sell_post_page, text='작성', command=sell_post, bg='gainsboro')
            button_write.place(x=320, y=330)
            button_close = tk.Button(sell_post_page, text='취소', command=sell_post_page.destroy, bg='gainsboro')
            button_close.place(x=400, y=330)

        def purchase_post_page():
            nickname = loglist[0]

            purchase_post_page = tk.Toplevel(tradeScr, bg='lemonchiffon')
            purchase_post_page.geometry('800x400')
            purchase_post_page.resizable(True, True)

            # 제목
            title = tk.Label(purchase_post_page, text='제목:', bg='lemonchiffon')
            title.place(x=130, y=50)
            title_write = tk.Entry(purchase_post_page)
            title_write.place(x=200, y=50, width=380)

            # 용품
            product = tk.Label(purchase_post_page, text='용품', bg='lemonchiffon')
            product.place(x=130, y=80)
            product_write = tk.Entry(purchase_post_page)
            product_write.place(x=200, y=80, width=380)

            # 종류
            type = tk.Label(purchase_post_page, text='종류', bg='lemonchiffon')
            type.place(x=130, y=110)
            type_write = tk.Entry(purchase_post_page)
            type_write.place(x=200, y=110, width=380)

            # 가격
            price = tk.Label(purchase_post_page, text='가격', bg='lemonchiffon')
            price.place(x=130, y=140)
            price_write = tk.Entry(purchase_post_page)
            price_write.place(x=200, y=140, width=380)

            # 게시글
            post = tk.Label(purchase_post_page, text='게시글:', bg='lemonchiffon')
            post.place(x=130, y=170)
            post_write = tk.Text(purchase_post_page)
            post_write.place(x=200, y=170, width=380, height=100)

            def purchase_post():
                if not os.path.isfile('purchase_post_database.txt') == True:
                    file = open('purchase_post_database.txt', 'w', encoding='utf-8')
                    file.close()

                # 구매글 작성
                title = title_write.get()
                product = product_write.get()
                type = type_write.get()
                price = price_write.get()
                post = post_write.get('1.0', 'end')
                if title == '':
                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                    return
                if product == '':
                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                    return
                if type == '':
                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                    return
                if price == '':
                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                    return
                if post == '':
                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                    return
                else:

                    with open('purchase_post_database.txt', 'a', encoding='utf-8') as file:
                        file.write(nickname + '\t' + title + '\t' + product + '\t' + type + '\t' + price + '\t' + post)
                        file.write('')
                        purchase_post_page.destroy()

                    # 구매글 제목 출력
                    with open('purchase_post_database.txt', 'r', encoding='utf-8') as file:
                        purchase_posts = file.readlines()
                        purchase_posts = ''.join(purchase_posts).strip()
                        purchase_posts = purchase_posts.split('\n')

                    titles = []
                    for purchase_post in purchase_posts:
                        purchase_post = purchase_post.split('\t')
                        title = purchase_post[1]
                        titles.append(title)

                    purchase_post_list.delete(0, 'end')
                    count = 0
                    for title in titles:
                        purchase_post_list.insert(count, title)
                        count += 1
                    return

            btn_write = tk.Button(purchase_post_page, text='완료', command=purchase_post, bg='gainsboro')
            btn_write.place(x=320, y=330)
            button_close = tk.Button(purchase_post_page, text='취소', command=purchase_post_page.destroy, bg='gainsboro')
            button_close.place(x=400, y=330)

        labelBuy = tk.LabelFrame(tradeScr, text="구매", font=tkf.Font(size=14, weight='bold'))
        labelBuy.place(width=400, height=320, x=0, y=20)
        purchase_post_list = tk.Listbox(labelBuy, width=70, height=15)
        purchase_post_list.config(font=tkf.Font(size=14, weight='bold'))
        purchase_post_list.pack()

        def purchase_list():
            with open('purchase_post_database.txt', 'r', encoding='utf-8') as file:
                purchase_posts = file.readlines()
                purchase_posts = ''.join(purchase_posts).strip()
                purchase_posts = purchase_posts.split('\n')


            if purchase_posts == ['']:
                return

            titles = []
            for purchase_post in purchase_posts:
                purchase_post = purchase_post.split('\t')
                title = purchase_post[1]
                titles.append(title)

            count = 0
            for title in titles:
                purchase_post_list.insert(count, title)
                count += 1

        if os.path.isfile('purchase_post_database.txt') == True:
            purchase_list()

        def p_list_select():
            if purchase_post_list.curselection():
                value = str((purchase_post_list.get(purchase_post_list.curselection())))
                if value:
                    with open('purchase_post_database.txt', 'r', encoding='utf-8') as file:
                        purchase_posts = file.readlines()
                        purchase_posts = ''.join(purchase_posts).strip()
                        purchase_posts = purchase_posts.split('\n')

                    titles = []
                    for purchase_post in purchase_posts:
                        purchase_post = purchase_post.split('\t')
                        title = purchase_post[1]
                        titles.append(title)

                    index = titles.index(value)
                    post = purchase_posts[index].split('\t')
                    nickname = post[0]
                    title = post[1]
                    product = post[2]
                    type = post[3]
                    price = post[4]
                    post_content = '\t'.join(post[5:])

                    select_page = tk.Toplevel(tradeScr, bg='lemonchiffon')
                    select_page.title("%s" % title)
                    select_page.geometry('500x450')
                    select_page.resizable(False, False)

                    label_title = tk.Label(select_page, text=f'닉네임: {nickname}', wraplength=200, bg='lemonchiffon', font=tkf.Font(size=12))
                    label_title.place(x=0, y=25)
                    label_title = tk.Label(select_page, text=f'제목: {title}', wraplength=200, bg='lemonchiffon', font=tkf.Font(size=12))
                    label_title.place(x=0, y=0)
                    label_title = tk.Label(select_page, text=f'용품: {product}', wraplength=200, bg='lemonchiffon', font=tkf.Font(size=12))
                    label_title.place(x=0, y=50)
                    label_title = tk.Label(select_page, text=f'종류: {type}', wraplength=200, bg='lemonchiffon', font=tkf.Font(size=12))
                    label_title.place(x=0, y=75)
                    label_title = tk.Label(select_page, text=f'가격: {price}', wraplength=200, bg='lemonchiffon', font=tkf.Font(size=12))
                    label_title.place(x=0, y=100)
                    label_title = tk.Label(select_page, text=f'게시글: {post_content}', wraplength=200, bg='lemonchiffon', font=tkf.Font(size=12))
                    label_title.place(x=0, y=125)

                    def p_post_del():
                        del purchase_posts[index]

                        file = open('purchase_post_database.txt', 'w', encoding='utf-8')
                        file.close()

                        titles = []
                        for purchase_post in purchase_posts:
                            post = purchase_post.split('\t')
                            nickname = post[0]
                            title = post[1]
                            product = post[2]
                            type = post[3]
                            price = post[4]
                            post_content = post[5]
                            titles.append(title)

                            with open('purchase_post_database.txt', 'a', encoding='utf-8') as file:
                                file.write(
                                    nickname + '\t' + title + '\t' + product + '\t' + type + '\t' + price + '\t' + post_content)
                                file.write('\n')

                        purchase_post_list.delete(0, 'end')
                        purchase_list()
                        select_page.destroy()

                def p_post_edit():
                    del purchase_posts[index]

                    file = open('purchase_post_database.txt', 'w', encoding='utf-8')
                    file.close()

                    titles = []
                    for purchase_post in purchase_posts:
                        post = purchase_post.split('\t')
                        nickname = post[0]
                        title = post[1]
                        product = post[2]
                        type = post[3]
                        price = post[4]
                        post_content = post[5]
                        titles.append(title)

                        with open('purchase_post_database.txt', 'a', encoding='utf-8') as file:
                            file.write(
                                nickname + '\t' + title + '\t' + product + '\t' + type + '\t' + price + '\t' + post_content)
                            file.write('\n')

                    purchase_post_page()
                    select_page.destroy()

                def p_post_comment():

                    commentPop = tk.Toplevel(select_page, bg='lemonchiffon')
                    commentPop.title('댓글 작성')
                    commentPop.geometry('300x160')
                    commentPop.resizable(False, False)

                    comment_section = tk.Text(commentPop, bg='white', width=25, height=5)
                    comment_section.place(x=90, y=20)

                    def completeCMT():
                        comment = comment_section.get(1.0, 'end')
                        if comment == '':
                            messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                        else:
                            comment_list_p.insert(0, comment)
                            commentPop.destroy()
                            with open(f'comment_list_p_{title}_{product}.txt', 'a', encoding='utf-8') as file:
                                file.write(comment)

                    label = tk.Label(commentPop, text='작성:', bg='lemonchiffon')
                    label.place(x=30, y=20)
                    finBtn = tk.Button(commentPop, text='완료', bg='gainsboro', command=completeCMT)
                    finBtn.place(x=100, y=100)
                    closeBtn = tk.Button(commentPop, text='닫기', bg='gainsboro', command=commentPop.destroy)
                    closeBtn.place(x=180, y=100)



                def p_post_comment_del():
                    if comment_list_p.curselection():
                        comment_del = str((comment_list_p.get(comment_list_p.curselection())))

                        with open(f'comment_list_p_{title}_{product}.txt', 'r', encoding='utf-8') as file:
                            comments = file.readlines()

                            del_index = comments.index(comment_del)
                            comment_list_p.delete(0, 'end')
                            del comments[del_index]

                        file = open(f'comment_list_p_{title}_{product}.txt', 'w', encoding='utf-8')
                        file.close()

                        with open(f'comment_list_p_{title}_{product}.txt', 'a', encoding='utf-8') as file:
                            for comment in comments:
                                file.write(comment)
                                comment_list_p.insert(0, comment)
                    else:
                        messagebox.showinfo('선택 오류', '글을 선택해주세요.')

                edit_btn = tk.Button(select_page, text='게시글 편집', command=p_post_edit, bg='gainsboro')
                edit_btn.place(x=10, y=180)
                del_btn = tk.Button(select_page, text='게시글 삭제', command=p_post_del, bg='gainsboro')
                del_btn.place(x=100, y=180)
                comment_btn = tk.Button(select_page, text='댓글 작성', command=p_post_comment, bg='gainsboro')
                comment_btn.place(x=160, y=400)
                del_comment_btn = tk.Button(select_page, text='댓글 삭제', command=p_post_comment_del, bg='gainsboro')
                del_comment_btn.place(x=260, y=400)
                close_btn = tk.Button(select_page, text='닫기', command=select_page.destroy, bg='gainsboro')
                close_btn.place(x=430, y=400)
                title = str((purchase_post_list.get(purchase_post_list.curselection())))
                comment_list_p = tk.Listbox(select_page, width=75)
                comment_list_p.place(x=0, y=220)

                if os.path.isfile(f'comment_list_p_{title}_{product}.txt') == True:
                    with open(f'comment_list_p_{title}_{product}.txt', 'r', encoding='utf-8') as file:
                        comments = file.readlines()
                        for comment in comments:
                            comment_list_p.insert(0, comment)

            else:
                messagebox.showinfo('선택 오류', '글을 선택해주세요.')

        p_list_select = tk.Button(labelBuy, text='선택', command=p_list_select, bg='gainsboro')
        p_list_select.place(x=100, y=250)
        postBuy = tk.Button(labelBuy, text="작성", command=purchase_post_page, bg='gainsboro')
        postBuy.place(x=200, y=250)
        labelSell = tk.LabelFrame(tradeScr, text="판매", font=tkf.Font(size=14, weight='bold'))
        labelSell.place(width=400, height=320, x=340, y=20)
        sell_post_list = tk.Listbox(labelSell, width=70, height=15)
        sell_post_list.config(font=tkf.Font(size=14, weight='bold'))
        sell_post_list.pack()

        def sell_list():
            with open('sell_post_database.txt', 'r', encoding='utf-8') as file:
                sell_posts = file.readlines()
                sell_posts = ''.join(sell_posts).strip()
                sell_posts = sell_posts.split('\n')
                if sell_posts == ['']:
                    return

                titles = []
                for sell_post in sell_posts:
                    sell_post = sell_post.split('\t')
                    title = sell_post[1]
                    titles.append(title)

                sell_post_list.delete(0, 'end')
                count = 0
                for title in titles:
                    sell_post_list.insert(count, title)

        if os.path.isfile('sell_post_database.txt') == True:
            sell_list()

        def s_list_select():
            if sell_post_list.curselection():
                value = str((sell_post_list.get(sell_post_list.curselection())))
                if value:
                    with open('sell_post_database.txt', 'r', encoding='utf-8') as file:
                        sell_posts = file.readlines()
                        sell_posts = ''.join(sell_posts).strip()
                        sell_posts = sell_posts.split('\n')

                        titles = []
                        for sell_post in sell_posts:
                            sell_post = sell_post.split('\t')
                            title = sell_post[1]
                            titles.append(title)

                        index = titles.index(value)
                        post = sell_posts[index].split('\t')
                        nickname = post[0]
                        title = post[1]
                        product = post[2]
                        type = post[3]
                        price = post[4]
                        post_content = '\t'.join(post[5:])

                        select_page = tk.Toplevel(tradeScr, bg='lemonchiffon')
                        select_page.geometry('500x450')

                        label_title = tk.Label(select_page, text=f'닉네임: {nickname}', wraplength=200, bg='lemonchiffon',
                                               font=tkf.Font(size=12))
                        label_title.place(x=0, y=25)
                        label_title = tk.Label(select_page, text=f'제목: {title}', wraplength=200, bg='lemonchiffon',
                                               font=tkf.Font(size=12))
                        label_title.place(x=0, y=0)
                        label_title = tk.Label(select_page, text=f'용품: {product}', wraplength=200, bg='lemonchiffon',
                                               font=tkf.Font(size=12))
                        label_title.place(x=0, y=50)
                        label_title = tk.Label(select_page, text=f'종류: {type}', wraplength=200, bg='lemonchiffon',
                                               font=tkf.Font(size=12))
                        label_title.place(x=0, y=75)
                        label_title = tk.Label(select_page, text=f'가격: {price}', wraplength=200, bg='lemonchiffon',
                                               font=tkf.Font(size=12))
                        label_title.place(x=0, y=100)
                        label_title = tk.Label(select_page, text=f'게시글: {post_content}', wraplength=200,
                                               bg='lemonchiffon', font=tkf.Font(size=12))
                        label_title.place(x=0, y=125)

                        def s_post_del():
                            del sell_posts[index]

                            file = open('sell_post_database.txt', 'w', encoding='utf-8')
                            file.close()

                            titles = []
                            for sell_post in sell_posts:
                                post = sell_post.split('\t')
                                nickname = post[0]
                                title = post[1]
                                product = post[2]
                                type = post[3]
                                price = post[4]
                                post_content = post[5]
                                titles.append(title)

                                with open('sell_post_database.txt', 'a', encoding='utf-8') as file:
                                    file.write(
                                        nickname + '\t' + title + '\t' + product + '\t' + type + '\t' + price + '\t' + post_content)
                                    file.write('\n')
                            sell_post_list.delete(0, 'end')
                            sell_list()
                            select_page.destroy()

                        def s_post_edit():
                            del sell_posts[index]

                            file = open('sell_post_database.txt', 'w', encoding='utf-8')
                            file.close()

                            titles = []
                            for sell_post in sell_posts:
                                post = sell_post.split('\t')
                                nickname = post[0]
                                title = post[1]
                                product = post[2]
                                type = post[3]
                                price = post[4]
                                post_content = post[5]
                                titles.append(title)

                                with open('sell_post_database.txt', 'a', encoding='utf-8') as file:
                                    file.write(
                                        nickname + '\t' + title + '\t' + product + '\t' + type + '\t' + price + '\t' + post_content)
                                    file.write('\n')

                            sell_post_page()
                            select_page.destroy()

                        def s_post_comment():

                            commentPop = tk.Toplevel(select_page, bg='lemonchiffon')
                            commentPop.title('댓글 작성')
                            commentPop.geometry('300x160')
                            commentPop.resizable(False, False)

                            comment_section = tk.Text(commentPop, bg='white', width=25, height=5)
                            comment_section.place(x=90, y=20)

                            def completeCMT():
                                comment = comment_section.get(1.0, 'end')
                                if comment == '':
                                    messagebox.showinfo('빈칸을 입력하거라~', '빈칸을 입력하거라~')
                                else:
                                    comment_list_s.insert(0, comment)
                                    commentPop.destroy()
                                    with open(f'comment_list_s_{title}_{product}.txt', 'a', encoding='utf-8') as file:
                                        file.write(comment)


                            label = tk.Label(commentPop, text='작성:', bg='lemonchiffon')
                            label.place(x=30, y=20)
                            finBtn = tk.Button(commentPop, text='완료', bg='gainsboro', command=completeCMT)
                            finBtn.place(x=100, y=100)
                            closeBtn = tk.Button(commentPop, text='닫기', bg='gainsboro', command=commentPop.destroy)
                            closeBtn.place(x=180, y=100)

                        def s_post_comment_del():
                            if comment_list_s.curselection():
                                comment_del = str((comment_list_s.get(comment_list_s.curselection())))

                                with open(f'comment_list_s_{title}_{product}.txt', 'r', encoding='utf-8') as file:
                                    comments = file.readlines()

                                    del_index = comments.index(comment_del)
                                    comment_list_s.delete(0, 'end')
                                    del comments[del_index]

                                file = open(f'comment_list_s_{title}_{product}.txt', 'w', encoding='utf-8')
                                file.close()

                                with open(f'comment_list_s_{title}_{product}.txt', 'a', encoding='utf-8') as file:
                                    for comment in comments:
                                        file.write(comment)
                                        comment_list_s.insert(0, comment)
                            else:
                                messagebox.showinfo('선택 오류', '글을 선택해주세요.')

                        edit_btn = tk.Button(select_page, text='게시글 편집', command=s_post_edit, bg='gainsboro')
                        edit_btn.place(x=10, y=180)
                        del_btn = tk.Button(select_page, text='게시글 삭제', command=s_post_del, bg='gainsboro')
                        del_btn.place(x=100, y=180)
                        comment_btn = tk.Button(select_page, text='댓글 작성', command=s_post_comment, bg='gainsboro')
                        comment_btn.place(x=160, y=400)
                        del_comment_btn = tk.Button(select_page, text='댓글 삭제', command=s_post_comment_del,
                                                    bg='gainsboro')
                        del_comment_btn.place(x=260, y=400)
                        close_btn = tk.Button(select_page, text='닫기', command=select_page.destroy, bg='gainsboro')
                        close_btn.place(x=430, y=400)
                        title = str((sell_post_list.get(sell_post_list.curselection())))
                        comment_list_s = tk.Listbox(select_page, width=75)
                        comment_list_s.place(x=0, y=220)

                        if os.path.isfile(f'comment_list_s_{title}_{product}.txt') == True:
                            with open(f'comment_list_s_{title}_{product}.txt', 'r', encoding='utf-8') as file:
                                comments = file.readlines()
                                for comment in comments:
                                    comment_list_s.insert(0, comment)
            else:
                messagebox.showinfo('선택 오류', '글을 선택해주세요.')


        s_list_select = tk.Button(labelSell, text='선택', command=s_list_select, bg='gainsboro')
        s_list_select.place(x=100, y=250)
        postSell = tk.Button(labelSell, text="작성", command=sell_post_page, bg='gainsboro')
        postSell.place(x=200, y=250)
        closebtn = tk.Button(tradeScr, text='닫기', command=tradeScr.destroy, bg='gainsboro')
        closebtn.place(x=320, y=350)

    tradeimg = tk.PhotoImage(
            file="%s/puppy_commodities1.png" % PPpath)
    tradebtn = tk.Button(mainScr, text='용품 거래', font=btnfont, image=tradeimg, compound='bottom', command=trade)
    tradebtn.image = tradeimg
    tradebtn.place(x=0, y=220)



    def Hospital():

        Hscr = tk.Toplevel(mainScr, bg='lemonchiffon')
        Hscr.title("병원 찾기")
        Hscr.geometry("500x450")
        Hscr.resizable(False, False)

        # frame_hospital = tk.LabelFrame(Hscr, bd=2, text="병원 찾기")
        # frame_hospital.pack(side="left", expand=True)

        # 병원 검색 버튼
        def searchH():
            gk.Hsearch()

            count = 1
            for info in gk.listH:
                infolistbox.insert(count, info)
                count += 1
            gk.listH = []

        searchicn = tk.PhotoImage(file="%s/search.png" % PPpath)
        searchbtn = tk.Button(Hscr, text="주변 병원 찾기", font=tkf.Font(size=10, weight='bold'), command=searchH, image=searchicn,  compound='bottom')
        searchbtn.image = searchicn
        searchbtn.place(x=210, y=20)

        # 병원 정보
        label_info = tk.LabelFrame(Hscr, width=90, height=30, bd=2, text="병원 목록", font=tkf.Font(size=14, weight='bold'))
        label_info.place(x=0, y=120)

        def locH():
            if infolistbox.curselection():
                selH = infolistbox.get(infolistbox.curselection())
                gk.hh(selH)
            else:
                messagebox.showinfo('선택 오류', '병원을 선택해주세요.')

        infolistbox = tk.Listbox(label_info, width=90, height=15)
        infolistbox.pack()

        closebtn = tk.Button(Hscr, text='닫기', command=Hscr.destroy, bg='gainsboro')
        closebtn.place(x=400, y=400)
        infoH = tk.Button(Hscr, text='상세 위치', command=locH, bg='gainsboro')
        infoH.place(x=220, y=400)

    vetimg = tk.PhotoImage(file="%s/vet4.png" % PPpath)
    vetbtn = tk.Button(mainScr, text='병원 찾기', font=btnfont,image=vetimg, compound='bottom', command=Hospital)
    vetbtn.image = vetimg
    vetbtn.place(x=0, y=450)

    def employ():
        employWin = tk.Toplevel(mainScr, bg='lemonchiffon')
        employWin.title("구인구직")
        employWin.geometry("680x400")
        employWin.resizable(False, False)

        # 구인 글 작성
        def employerPost():
            def destroy():
                write_erPost.destroy()

            write_erPost = tk.Toplevel(mainScr, bg='lemonchiffon')
            write_erPost.geometry("800x500")
            write_erPost.resizable(True, True)

            title = tk.Label(write_erPost, text="제목:", bg='lemonchiffon')
            writer = tk.Label(write_erPost, text="글쓴이:", bg='lemonchiffon')
            writernn = tk.Label(write_erPost, text="%s" % loglist[0], bg='lemonchiffon')
            task = tk.Label(write_erPost, text="해야할 일:", bg='lemonchiffon')
            caution = tk.Label(write_erPost, text="주의 사항:", bg='lemonchiffon')
            price = tk.Label(write_erPost, text="가격:", bg='lemonchiffon')
            place = tk.Label(write_erPost, text="인수 장소:", bg='lemonchiffon')
            phonenum = tk.Label(write_erPost, text="연락처:", bg='lemonchiffon')
            etc = tk.Label(write_erPost, text="그 외 사항:", bg='lemonchiffon')

            title.place(x=130, y=50)
            writer.place(x=130, y=80)
            writernn.place(x=200, y=80)
            task.place(x=130, y=130)
            caution.place(x=130, y=160)
            price.place(x=130, y=190)
            place.place(x=130, y=220)
            phonenum.place(x=130, y=250)
            etc.place(x=130, y=280)

            entryTitle = tk.Entry(write_erPost)
            entryTask = tk.Entry(write_erPost)
            entryCaution = tk.Entry(write_erPost)
            entryPrice = tk.Entry(write_erPost)
            entryPlace = tk.Entry(write_erPost)
            entryPhone = tk.Entry(write_erPost)
            entryETC = tk.Entry(write_erPost)

            entryTitle.place(x=200, y=50, width=380)
            entryTask.place(x=200, y=130, width=380)
            entryCaution.place(x=200, y=160, width=380)
            entryPrice.place(x=200, y=190, width=380)
            entryPlace.place(x=200, y=220, width=380)
            entryPhone.place(x=200, y=250, width=380)
            entryETC.place(x=200, y=280, width=380, height=100)

            def employer():
                def destroy():
                    write_erPost.destroy()
                eTt = entryTitle.get()
                eTk = entryTask.get()
                eCt = entryCaution.get()
                ePr = entryPrice.get()
                ePl = entryPlace.get()
                ePn = entryPhone.get()
                eEtc = entryETC.get()
                if eTt == "":
                    messagebox.showinfo('작성 실패', '제목을 입력해주세요.')
                elif eTk == "":
                    messagebox.showinfo('작성 실패', '해야할 일을 입력해주세요.')
                elif eCt == "":
                    messagebox.showinfo('작성 실패', '주의 사항을 입력해주세요.')
                elif ePr == "":
                    messagebox.showinfo('작성 실패', '가격을 입력해주세요.')
                elif ePl == "":
                    messagebox.showinfo('작성 실패', '인수 장소를 입력해주세요.')
                elif ePn == "":
                    messagebox.showinfo('작성 실패', '연락처를 입력해주세요.')
                else:
                    pS.employer(eTt, loglist[0], eTk, eCt, ePr, ePl, ePn, eEtc)
                    er_insertlist()
                    destroy()

            combtn = tk.Button(write_erPost, text="완료", command=employer, bg='gainsboro')
            combtn.place(x=320, y=400)
            cancelbtn = tk.Button(write_erPost, text="취소", command=destroy, bg='gainsboro')
            cancelbtn.place(x=400, y=400)
        # 구직 글 작성
        def employeePost():
            def destroy():
                write_eePost.destroy()

            write_eePost = tk.Toplevel(employWin, bg='lemonchiffon')
            write_eePost.geometry("800x500")
            write_eePost.resizable(True, True)

            title = tk.Label(write_eePost, text="제목:", bg='lemonchiffon')
            writer = tk.Label(write_eePost, text="글쓴이:", bg='lemonchiffon')
            writernn = tk.Label(write_eePost, text="%s" % loglist[0], bg='lemonchiffon')
            time = tk.Label(write_eePost, text="가능한 날짜 및 시간:", bg='lemonchiffon')
            preferTask = tk.Label(write_eePost, text="선호하는 일:", bg='lemonchiffon')
            preferSize = tk.Label(write_eePost, text="선호하는 견종 사이즈:", bg='lemonchiffon')
            #priceRange = tk.Label(write_eePost, text="찾는 가격:", bg='lemonchiffon')
            area = tk.Label(write_eePost, text="가능한 지역:", bg='lemonchiffon')
            phonenum = tk.Label(write_eePost, text="연락처:", bg='lemonchiffon')
            etc = tk.Label(write_eePost, text="그 외 사항:", bg='lemonchiffon')

            title.place(x=70, y=50)
            writer.place(x=70, y=80)
            writernn.place(x=200, y=80)
            time.place(x=70, y=130)
            preferTask.place(x=70, y=160)
            preferSize.place(x=70, y=190)
            # priceRange.place(x=70, y=220)
            area.place(x=70, y=220)
            phonenum.place(x=70, y=250)
            etc.place(x=70, y=280)

            entryTitle = tk.Entry(write_eePost)
            entryTime = tk.Entry(write_eePost)
            entrypT = tk.Entry(write_eePost)
            entrypS = tk.Entry(write_eePost)
            # entrypR = tk.Entry(write_eePost)
            entryA = tk.Entry(write_eePost)
            entryPn = tk.Entry(write_eePost)
            entryETC = tk.Entry(write_eePost)

            entryTitle.place(x=200, y=50, width=380)
            entryTime.place(x=200, y=130, width=380)
            entrypT.place(x=200, y=160, width=380)
            entrypS.place(x=200, y=190, width=380)
            # entrypR.place(x=200, y=220, width=380)
            entryA.place(x=200, y=220, width=380)
            entryPn.place(x=200, y=250, width=380)
            entryETC.place(x=200, y=280, width=380, height=100)

            def employee():
                def destroy():
                    write_eePost.destroy()
                eTt = entryTitle.get()
                eTm = entryTime.get()
                epT = entrypT.get()
                epS = entrypS.get()
                # epR = entrypR.get()
                eA = entryA.get()
                ePn = entryPn.get()
                if eTt == "":
                    messagebox.showinfo('작성 실패', '제목을 입력해주세요.')
                elif eTm == "":
                    messagebox.showinfo('작성 실패', '날짜 및 시간을 입력해주세요.')
                elif epT == "":
                    messagebox.showinfo('작성 실패', '선호하는 일을 입력해주세요.')
                elif epS == "":
                    messagebox.showinfo('작성 실패', '선호하는 견종 크기를 입력해주세요.')
                # elif epR == "":
                #     messagebox.showinfo('작성 실패', '찾는 가격을 입력해주세요.')
                elif eA == "":
                    messagebox.showinfo('작성 실패', '지역을 입력해주세요.')
                elif ePn == "":
                    messagebox.showinfo('작성 실패', '연락처를 입력해주세요.')
                else:
                    pS.employee(eTt, loglist[0], eTm, epT, epS, eA, ePn)
                    pS.list("구직게시글목록")
                    ee_insertlist()
                    destroy()

            combtn = tk.Button(write_eePost, text="완료", command=employee, bg='gainsboro')
            combtn.place(x=320, y=430)
            cancelbtn = tk.Button(write_eePost, text="취소", command=destroy, bg='gainsboro')
            cancelbtn.place(x=400, y=430)
        def showlist(listbox):  #리스트박스의 요소 출력
            count = 1
            for post in pS.l_e:
                listbox.insert(count, post)
                count += 1
            listbox.config(font=tkf.Font(size=14, weight='bold'))
        def editPost(listname, listbox):  # 글 수정
            index = listbox.curselection()
            if index:
                selec = listbox.get(index)
                if listname == "구인게시글목록":
                    employerPost()
                    pS.deletepost(selec, "구인게시글목록")
                elif listname == "구직게시글목록":
                    employeePost()
                    pS.deletepost(selec, "구직게시글목록")
        def selecPost(listbox, label):  #리스트박스에서 글 선택
            if label == labelEmployer:
                def delPost():
                    pS.deletepost(selec, "구인게시글목록")
                    listbox.delete(index)
                    postPop.destroy()
                def edPost():
                    editPost("구인게시글목록", er_listbox)
            elif label == labelEmployee:
                def delPost():
                    pS.deletepost(selec, "구직게시글목록")
                    listbox.delete(index)
                    postPop.destroy()
                def edPost():
                    editPost("구직게시글목록", ee_listbox)

            index = listbox.curselection()
            if index:
                selec = listbox.get(index)
                postPop = tk.Toplevel(label, bg='lemonchiffon')
                postPop.geometry("500x400")
                postPop.resizable(False, False)
                pS.click(selec)
                commentF = tk.Frame(postPop, bg='lemonchiffon')
                commentF.place(x=140, y=0)
                for i in pS.post_l:
                    content = tk.Label(commentF, text="%s" % i, bg='lemonchiffon')
                    content.pack()
                if "글쓴이:%s" % loglist[0] in pS.post_l:
                    def choose():   # 신청자 댓글 선택 및 나머지 삭제
                        comtindex = commentList.curselection()
                        if comtindex:
                            warning = tk.Toplevel(postPop, bg='lemonchiffon')
                            warning.geometry('300x150')
                            warning.resizable(False, False)
                            def finalchoice():
                                selecCm = commentList.get(comtindex)
                                pS.chEmployee(selec, selecCm)
                                warning.destroy()

                            ctimage = tk.PhotoImage(file="%s/caution.png" % PPpath)
                            Caution = tk.Label(warning, image=ctimage,
                                               text='경고!', font=tkf.Font(weight='bold', size=10), bg='lemonchiffon')
                            Caution.image = ctimage
                            Caution.place(x=120, y=0)
                            warningT = tk.Label(warning, text='해당 댓글 선택시 나머지 댓글이 삭제됩니다.\n정말로 진행하시겠습니까?',
                                                font=tkf.Font(size=10), bg='lemonchiffon')
                            warningT.place(x=20, y=60)
                            yesbtn = tk.Button(warning, text='진행', command=finalchoice)
                            yesbtn.place(x=110, y=110)
                            nobtn = tk.Button(warning, text='취소', command=warning.destroy)
                            nobtn.place(x=160, y=110)
                        else:
                            messagebox.showinfo('선택 오류', '댓글을 선택해주세요.')
                    def rateEE():   # 업무 후 구직자 평가
                        comtindex = commentList.curselection()
                        if comtindex:
                            ratePop = tk.Toplevel(postPop, bg='lemonchiffon')
                            ratePop.geometry("180x150")
                            ratePop.resizable(False, False)
                            spin = tk.Spinbox(ratePop, from_=0, to=10, width=10)
                            spin.place(relx=0.5, rely=0.5, anchor='center')
                            def rate():
                                score = spin.get()
                                pS.rateEE(selec, score)
                                messagebox.showinfo('평가 완료', '게시글이 삭제됩니다.')
                                pS.deletepost(selec,'구인게시글목록')
                                postPop.destroy()
                            ratebtn = tk.Button(ratePop, text="평가 완료", command=rate, bg='gainsboro')
                            ratebtn.place(relx=0.5, anchor='s')
                        else:
                            messagebox.showinfo('선택 오류', '댓글을 선택 후 평가해주세요.')
                    deletebtn = tk.Button(postPop, text="삭제", command=delPost, bg='gainsboro')
                    deletebtn.place(x=190, y=170)
                    edtbtn = tk.Button(postPop, text="수정", command=edPost, bg='gainsboro')
                    edtbtn.place(x=260, y=170)
                    selec_btn = tk.Button(postPop, text="선택", command=choose, bg='gainsboro')
                    selec_btn.place(x=300, y=370)
                    if label == labelEmployer:
                        comTask = tk.Button(postPop, text="평가", command=rateEE, bg='gainsboro')
                        comTask.place(x=230, y=370)
                    compTask = tk.Button(postPop, text="닫기", command=postPop.destroy, bg='gainsboro')
                    compTask.place(x=160, y=370)
                elif "글쓴이:%s" % loglist[0] not in pS.post_l:
                    def applyComment():
                        commentPop = tk.Toplevel(postPop, bg='lemonchiffon')
                        commentPop.geometry("500x260")
                        commentPop.resizable(False, False)
                        if label == labelEmployer:
                            applicantNum = tk.Label(commentPop, text="신청자 연락처:", bg='lemonchiffon')
                            applicantNum.place(x=90, y=60)
                            entryNum = tk.Entry(commentPop)
                            entryNum.place(x= 180, y=60)
                            comment = tk.Label(commentPop, text="댓글:", bg='lemonchiffon')
                            comment.place(x=90, y=90)
                            writecomment = tk.Entry(commentPop)
                            writecomment.place(x=180, y=90, width=200, height=100)
                        elif label == labelEmployee:
                            applicantNum = tk.Label(commentPop, text="신청자 연락처:", bg='lemonchiffon')
                            applicantNum.place(x=90, y=30)
                            entryNum = tk.Entry(commentPop)
                            entryNum.place(x=180, y=30)
                            offerPrice = tk.Label(commentPop, text="제시 가격:", bg='lemonchiffon')
                            offerPrice.place(x=90, y=60)
                            entry_oP = tk.Entry(commentPop)
                            entry_oP.place(x=180, y=60)
                            comment = tk.Label(commentPop, text="댓글:", bg='lemonchiffon')
                            comment.place(x=90, y=90)
                            writecomment = tk.Entry(commentPop)
                            writecomment.place(x=180, y=90, width=200, height=100)
                        def commentCom():
                            import os.path
                            write = writecomment.get()
                            oP = entry_oP.get()
                            num = entryNum.get()
                            path = "%s 댓글 목록.txt" % selec
                            if label == labelEmployer:
                                com = ("닉네임: %s /" % loglist[0] + "\t" + "신뢰도: %s /" % loglist[1]
                                       + '\t' + "연락처: %s /" % num + '\t' + "댓글: %s" % write + "\n")
                                if os.path.isfile(path):
                                    list = open("%s 댓글 목록.txt" % selec, 'a', encoding='utf-8')
                                    list.write(com)
                                    list.close()
                                else:
                                    list = open("%s 댓글 목록.txt" % selec, 'w', encoding='utf-8')
                                    list.write(com)
                                    list.close()
                                commentList.insert(tk.END, com)
                                commentPop.destroy()
                            elif label == labelEmployee:
                                com = ("닉네임: %s /" % loglist[0] + "\t" + "제시 가격: %s /" % oP + '\t'
                                       + "연락처: %s /" % num + '\t' + "댓글: %s" % write + "\n")
                                if os.path.isfile(path):
                                    list = open("%s 댓글 목록.txt" % selec, 'a', encoding='utf-8')
                                    list.write(com)
                                    list.close()
                                else:
                                    list = open("%s 댓글 목록.txt" % selec, 'w', encoding='utf-8')
                                    list.write(com)
                                    list.close()
                                commentList.insert(tk.END, com)
                                commentPop.destroy()
                        combtn = tk.Button(commentPop, text="완료", command=commentCom, bg='gainsboro')
                        combtn.place(x=160, y=200)
                        close = tk.Button(commentPop, text="닫기", command=commentPop.destroy, bg='gainsboro')
                        close.place(x=230, y=200)

                    def deletecomment():
                        list = []
                        if commentList.curselection():
                            sel = commentList.get(commentList.curselection())
                            list.append(sel)
                            list[0] = list[0].strip('닉네임: ')
                            list[0] = list[0].split(' /')
                            if loglist[0] == list[0][0]:
                                pS.delcomt(selec, sel)
                                commentList.delete(commentList.curselection())
                            else:
                                messagebox.showinfo('잘못된 글쓴이', '삭제는 해당 댓글의 글쓴이만 가능합니다.')
                        else:
                            messagebox.showinfo('선택 오류', '댓글 선택 후 이용해주세요.')

                    def rateEE():   # 업무 후 구직자 평가
                        comtindex = commentList.curselection()
                        if comtindex:
                            ratePop = tk.Toplevel(postPop, bg='lemonchiffon')
                            ratePop.geometry("180x150")
                            ratePop.resizable(False, False)
                            spin = tk.Spinbox(ratePop, from_=0, to=10, width=10)
                            spin.place(relx=0.5, rely=0.5, anchor='center')
                            def rate():
                                score = spin.get()
                                pS.rateEE(selec, score)
                                messagebox.showinfo('평가 완료', '게시글이 삭제됩니다.')
                                pS.deletepost(selec, '구직게시글목록')
                                postPop.destroy()
                            ratebtn = tk.Button(ratePop, text="평가 완료", command=rate, bg='gainsboro')
                            ratebtn.place(relx=0.5, anchor='n')
                        else:
                            messagebox.showinfo('선택 오류', '댓글을 선택 후 평가해주세요.')

                    comment = tk.Button(postPop, text="댓글 달기", command=applyComment, bg='gainsboro')
                    comment.place(x=110, y=170)
                    delbtn = tk.Button(postPop, text='댓글 삭제', command=deletecomment, bg='gainsboro')
                    delbtn.place(x=310, y=170)
                    compTask = tk.Button(postPop, text="닫기", command=postPop.destroy, bg='gainsboro')
                    compTask.place(x=180, y=370)
                    comTask = tk.Button(postPop, text="평가", command=rateEE, bg='gainsboro')
                    comTask.place(x=280, y=370)
                def insertcomList():
                    if  os.path.isfile("%s 댓글 목록.txt" % selec) == True:
                        clist = open("%s 댓글 목록.txt" % selec, 'r', encoding='utf-8')
                        ctlist = clist.readlines()
                        clist.close()
                        for i in range(len(ctlist)):
                            ctlist[i] = ctlist[i].replace("\n", '')
                            ctlist[i] = ctlist[i].strip("\t")
                        if "글쓴이:%s" % loglist[0] in pS.post_l:
                            count = 1
                            for post in ctlist:
                                commentList.insert(count, post)
                                count += 1
                        elif "글쓴이:%s" % loglist[0] not in pS.post_l:
                            for i in range(len(ctlist)):
                                ctlist[i] = ctlist[i].split(' /\t제시')
                            count = 1
                            for post in ctlist:
                                commentList.insert(count, post[0])
                                count += 1
                    else:
                        pass
                commentList = tk.Listbox(postPop, width=70)
                commentList.place(x=0, y=200)
                insertcomList()
                pS.post_l = []
            else:
                messagebox.showinfo('선택 오류', '글을 선택해주세요.')

        #구인
        labelEmployer = tk.LabelFrame(employWin, text="구인",
                                      font=tkf.Font(size=14, weight='bold'))
        labelEmployer.place(width=400, height=320, x=0, y=20)
        #구인 리스트박스
        er_listbox = tk.Listbox(labelEmployer, width=30, height=10)
        er_listbox.place(x=0, y=5)
        pS.list("구인게시글목록")
        def er_insertlist():
            pS.list("구인게시글목록")
            er_listbox.insert(tk.END, pS.l_e[-1])
        showlist(er_listbox)
        pS.l_e = []
        def er_selecPost():
            selecPost(er_listbox, labelEmployer)

        selecbtn = tk.Button(labelEmployer, text="선택", command=er_selecPost, bg='gainsboro')
        selecbtn.place(x=100, y=250)
        postEmployer = tk.Button(labelEmployer, text="작성", command=employerPost, bg='gainsboro')
        postEmployer.place(x=200, y=250)

        #구직
        labelEmployee = tk.LabelFrame(employWin, text="구직",
                                      font=tkf.Font(size=14, weight='bold'))
        labelEmployee.place(width=400, height=320, x=340, y=20)

        #구직 리스트박스
        ee_listbox = tk.Listbox(labelEmployee, width=30, height=10)
        ee_listbox.place(x=0, y=5)
        pS.list("구직게시글목록")
        def ee_insertlist():
            pS.list("구직게시글목록")
            ee_listbox.insert(tk.END, pS.l_e[-1])
        showlist(ee_listbox)
        pS.l_e = []
        def ee_selecPost():
            selecPost(ee_listbox, labelEmployee)

        selecbtn = tk.Button(labelEmployee, text="선택", command=ee_selecPost, bg='gainsboro')
        selecbtn.place(x=100, y=250)
        postEmployee = tk.Button(labelEmployee, text="작성", command=employeePost, bg='gainsboro')
        postEmployee.place(x=200, y=250)
        closebtn = tk.Button(employWin, text='닫기', command=employWin.destroy, bg='gainsboro')
        closebtn.place(x=320, y=350)

    employimg = tk.PhotoImage(
        file="%s/walking_dog1.png" % PPpath)
    employbtn = tk.Button(mainScr, text='구인구직', font=btnfont, image=employimg, compound='bottom', command=employ)
    employbtn.image = employimg
    employbtn.place(x=300, y=220)



log  = tk.Tk()  #창 객체 생성 및 객체명 지정
log.title("애완견 플랫폼")  #창의 타이틀멸
log.geometry("400x200")  #창의 사이즈
log.resizable(False, False)

labelID = tk.Label(log, text="ID:")
labelPW = tk.Label(log, text="PW:")
labelID.place(x= 100, y=50)
labelPW.place(x= 100, y=70)



entryID = tk.Entry(log)
entryID.place(x=130, y=50)
entryPW = tk.Entry(log)
entryPW.place(x=130, y=70)
loginbtn = tk.Button(log,text="로그인", command=login, bg='gainsboro')
loginbtn.place(x=140, y=100)
signupbtn = tk.Button(log, text="회원가입",command=signup, bg='gainsboro')
signupbtn.place(x=205, y=100)





log.mainloop()