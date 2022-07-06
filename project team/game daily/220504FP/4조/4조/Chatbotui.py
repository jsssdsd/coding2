import os
import tkinter.scrolledtext
from tkinter import *
import tkinter.font
import module as m
import requests
from tkinter import messagebox
import tkinter.ttk
import time
import bs4
import random
import module as m

def chatbot():
    root = Tk()
    root.title("BIGF CHATBOT")
    root.geometry("400x700")
    root.resizable(False,False)

    #폰트 설정
    font1=tkinter.font.Font(family="배달의민족 도현",size=13)
    font2=tkinter.font.Font(family="맑은 고딕",size=8)
    font3=tkinter.font.Font(family="맑은 고딕",size=10)
    font4=tkinter.font.Font(family="맑은 고딕",size=2)

    #메뉴설정
    menu = Menu(root)
    menu.add_cascade(label="설정")

    def close():
        root.quit()
        root.destroy()
    def Men1():

        root1 = Tk()
        root1.title("말투 설정")
        root1.geometry("150x150")
        root1.resizable(False, False)

        labelframe = LabelFrame(root1, text="말투 선택")
        labelframe.pack(fill='both',padx=10,pady=10,expand=True)

        menu_1=IntVar()

        menu1 = Radiobutton(labelframe, text="말투 1", value=1,variable=menu_1)
        menu1.pack(expand=True)
        #menu1 = Radiobutton(labelframe, text="말투 2", value=2,variable=menu_1)
        menu1.pack(expand=True)
    def Men2():
        root2 = Tk()
        root2.title("테마설정")
        root2.geometry("150x150")
        root2.resizable(False, False)

        labelframe = LabelFrame(root2, text="테마 선택")
        labelframe.pack(fill='both',padx=10,pady=10,expand=True)

        menu_2=IntVar()

        menu2 = Radiobutton(labelframe, text="테마 1", value=1,variable=menu_2)
        menu2.pack(expand=True)
        menu2 = Radiobutton(labelframe, text="테마 2", value=2,variable=menu_2 )
        #menu2.pack(expand=True)


    color1='dimgray'
    color2='darkgrey'
    color3='gainsboro'

    color4='seashall2'
    color5='seashall3'
    def theme():
        pass



    def ID_1():

        root3 = Tk()
        root3.title("계정 생성")
        root3.geometry("400x300")
        root3.resizable(True, True)

        idframe = LabelFrame(root3, text="계정 목록", width=50)
        idframe.pack(fill='y', padx=5, pady=5)

        idlist = Listbox(idframe, width=30, height=10)
        idlist.pack(side='top', fill='x', padx=3, pady=3)

        idframe2 = LabelFrame(root3, text=" 이름 / 전화번호 ")
        idframe2.pack(fill='y', padx=10, pady=5)

        def id_ent():
            x = entry_id.get()
            idlist.insert(END, x)
            entry_id.delete(0, "end")
            user = open('./userlist/' + x + '.txt', 'a', encoding='UTF-8')
            user.close()
            return x


        def id_ent2(event):
            x = entry_id.get()
            idlist.insert(END, x)
            entry_id.delete(0, "end")
            user = open('./userlist/' + x + '.txt', 'a', encoding='UTF-8')
            user.close()

        entry_id = Entry(idframe2)
        entry_id.pack(side='left')
        id_enter = Button(idframe2, text="등록", command=id_ent)
        id_enter.pack(fill='y')
        entry_id.bind('<Return>', id_ent2)

        root3.mainloop()



        def delit():
            import os
            idlist.delete(ANCHOR)
            open('./userlist/' + "cxv" + '.txt', 'a', encoding='UTF-8')
            os.remove('./userlist/' + "cxv" + '.txt')

        def delete_user():
            open('./userlist/' + "cxv" + '.txt', 'a', encoding='UTF-8')
            os.remove('./userlist/' + "cxv" + '.txt')



    def attendance():
        root4 = Tk()
        root4.title("출석 관리")
        root4.geometry("200x150")
        root4.resizable(True, True)

        notebook = tkinter.ttk.Notebook(root4, width=300, height=300)
        notebook.pack(expand=True, fill=BOTH)
        framei = Frame(root4)
        framei.pack(fill=BOTH, expand=True)
        framei2 = Frame(root4)
        framei2.pack(fill=BOTH, expand=True)
        notebook.add(framei, text="입/퇴실 체크")
        notebook.add(framei2,text='출석률 비교')

        btn_at=Button(framei2,command=m.compare_Adays,text='그래프 보기')
        btn_at.pack(fill=BOTH,expand=True)

        label_framei2 = Frame(framei)
        label_framei2.pack(side=TOP)
        labeli2 = Label(label_framei2)
        labeli2.pack(side=BOTTOM, expand=True)
        labeli = Label(label_framei2)
        labeli.pack(side=BOTTOM, expand=True)

        import datetime as dt

        today = dt.datetime.today().strftime("%Y-%m-%d")
        present = dt.datetime.today().strftime("%H:%M")
        weekdays = ['(일)', '(월)', '(화)', '(수)', '(목)', '(금)', '(토)']
        result = dt.datetime.today().strftime("%Y-%m-%d") + weekdays[int(dt.datetime.today().strftime("%w"))]
        dd = result[2:]

        def i():
            with open('./userlist/' + '최수정7652' + '.txt', 'r', encoding='UTF-8') as user:
                line = user.readlines()
                if dd not in line[-1]:
                    checkin = open('./userlist/' + '최수정7652' + '.txt', 'a', encoding='UTF-8')
                    checkin.writelines(dd + '\t' + present)
                    checkin.close()
                    labeli.configure(text='입실 시간 : ' + str(present))
                else:
                    messagebox.showwarning('경고', '오늘 입실 이력이 있습니다.')

        def o():
            with open('./userlist/' + '최수정7652' + '.txt', 'r', encoding='UTF-8') as user:
                line = user.readlines()
                if dd in line[-1]:
                    checkout = open('./userlist/' + '최수정7652' + '.txt', 'a', encoding='UTF-8')
                    checkout.writelines('-' + present + '\n')
                    checkout.close()
                    labeli2.configure(text='퇴실 시간 : ' + str(present))
                if '-' in line[-1]:
                    messagebox.showwarning('경고', '퇴실 처리 되었습니다.')

        label_framei = LabelFrame(framei)
        label_framei.pack()
        btn_i = Button(label_framei, text='입실', relief='flat', command=i)
        btn_i.pack(side='left', fill='both', padx=5, pady=1)
        btn_o = Button(label_framei, text='퇴실', relief='flat', command=o)
        btn_o.pack(side='left', fill='both', padx=5, pady=1)

        root4.mainloop()


        label_framei=LabelFrame(framei)
        label_framei.pack()
        btn_i=Button(label_framei,text='입실',relief='flat',command=i)
        btn_i.pack(side='left',fill='both',padx=5,pady=1)
        btn_o = Button(label_framei, text='퇴실',relief='flat',command=o)
        btn_o.pack(side='left', fill='both', padx=5, pady=1)

        label_framei2 = LabelFrame(framei)
        label_framei2.pack()
        labeli=Frame(label_framei2)
        labeli.pack(side=TOP,expand=True)


    path = './userlist'
    userlist = os.listdir(path)
    namelist = []
    for u in userlist:
        if u[2].isdigit():
            namelist.append(u[:2])
        else:
            namelist.append(u[:3])
    a = namelist[1]


    menu=Menu(root)

    menu1=Menu(menu,tearoff=0)
    m1=menu1.add_command(label='말투 설정',command=Men1)
    m2=menu1.add_command(label='테마 설정',command=Men2)
    m4=menu1.add_command(label='출석 관리',command=attendance)

    menu1.add_separator()
    menu1.add_command(label='나가기',command=close)
    menu.add_cascade(label='설정',menu=menu1)

    root.config(menu=menu)




    label1=Label(root,text="BIGF",fg='black', bg='seashell3',height=2,width=45,font=font1,anchor='w')
    label1.pack(fill="x", padx=1, pady=0)

    label2=Message(root,fg='black',bg='seashell2',relief='flat',font=font2,anchor='e')
    label2.pack(fill="both", padx=1, pady=0)



    # 채팅방 배경

    label_frame2 = Frame(root,bg='white',relief='flat',height=20)
    label_frame2.pack(fill='both',expand=True, padx=5, pady=5)
    scrollbar=Scrollbar(label_frame2)
    scrollbar.pack(side=RIGHT,fill=Y,expand=True)


    BIGF=Text(label_frame2,relief='flat',height=20,font=font3,yscrollcommand=scrollbar.set)
    BIGF.pack(side='left',fill='both')
    BIGF.see(END)
    scrollbar.config(command=BIGF.yview)


    label_frame3 = LabelFrame(root,bg='seashell2',relief='flat')
    label_frame3.pack(side='bottom',fill='both',expand=True, padx=3, pady=3)


    # 메세지 입력 창
    path_frame = LabelFrame(label_frame3,bg='seashell2',relief='flat')
    path_frame.pack(side='bottom',fill="x", padx=2, pady=3,expand=True)


    def M_Enter(event):
        x=entry1.get("1.0",END)
        print(x)
    #rjust 오른쪽정렬
        a="나 : "
        b= x.replace("\n","")
        BIGF.insert(END,a.rjust(50)+b)
        BIGF.insert(END, '\n')
        BIGF.see(END)
        entry1.delete("1.0", END)

        for word in x.split():
            if word in start_i:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(start_r))
                BIGF.insert(END,'\n')
                BIGF.see(END)

        for word in x.split():
            if word in start_iw:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(start_rw))
                BIGF.insert(END,'\n')
                btn_W()
                BIGF.see(END)

        for word in x.split():
            if word in start_it:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(start_rt))
                BIGF.insert(END,'\n')
                btn_T()
                BIGF.see(END)

        for word in x.split():
            if word in start_il:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(start_rl))
                lunch()

            for word in x.split():
                if word in local1:
                    BIGF.insert(END, '\n')
                    BIGF.insert(END, "BIGF : " + random.choice(local1_1)+'\n')
                    Dunsan()
                for word in x.split():
                    if word in local2:
                        BIGF.insert(END, '\n')
                        BIGF.insert(END, "BIGF : " + random.choice(local1_2))
                        BIGF.insert(END, '\n')
                        Tanb()
                for word in x.split():
                    if word in local3:
                        BIGF.insert(END, '\n')
                        BIGF.insert(END, "BIGF : " + random.choice(local1_3))
                        BIGF.insert(END, '\n')
                        Galma()

        for word in x.split():
            if word in start_1:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(start_2))
                BIGF.insert(END,'\n')
                BIGF.see(END)

        for word in x.split():
            if word in thx:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(thx_1))
                BIGF.insert(END,'\n')
                BIGF.see(END)

        for word in x.split():
            if word in start_im:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(start_rm))
                BIGF.insert(END,'\n')
                BIGF.see(END)
                memo()

        for word in x.split():
            if word in simsim:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(simsim1))
                BIGF.insert(END,'\n')
                BIGF.see(END)

        for word in x.split():
            if word in schedu:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(schedu1))
                BIGF.insert(END,'\n')
                BIGF.see(END)
                M_timet()

        for word in x.split():
            if word in goog:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(goog1))
                BIGF.insert(END,'\n')
                BIGF.see(END)
                chrome_B()

        for word in x.split():
            if word in atte:
                BIGF.insert(END, '\n')
                BIGF.insert(END,"BIGF : "+random.choice(atte1))
                BIGF.insert(END,'\n')
                BIGF.see(END)
                attendance()



    def M_Enter2():
        x = entry1.get("1.0", END)
        print(x)
        # rjust 오른쪽정렬
        a = "나 : "
        b = x.replace("\n", "")
        BIGF.insert(END, a.rjust(50) + b)
        BIGF.insert(END, '\n')
        BIGF.see(END)
        entry1.delete("1.0", END)

        for word in x.split():
            if word in start_i:
                BIGF.insert(END, '\n')
                BIGF.insert(END, "BIGF : " + random.choice(start_r))
                BIGF.insert(END, '\n')
                BIGF.see(END)

        for word in x.split():
            if word in start_iw:
                BIGF.insert(END, '\n')
                BIGF.insert(END, "BIGF : " + random.choice(start_rw))
                BIGF.insert(END, '\n')
                btn_W()
                BIGF.see(END)

        for word in x.split():
            if word in start_it:
                BIGF.insert(END, '\n')
                BIGF.insert(END, "BIGF : " + random.choice(start_rt))
                BIGF.insert(END, '\n')
                btn_T()
                BIGF.see(END)

        for word in x.split():
            if word in start_il:
                BIGF.insert(END, '\n')
                BIGF.insert(END, "BIGF : " + random.choice(start_rl))
                lunch()

            for word in x.split():
                if word in local1:
                    BIGF.insert(END, '\n')
                    BIGF.insert(END, "BIGF : " + random.choice(local1_1) + '\n')
                    Dunsan()
                for word in x.split():
                    if word in local2:
                        BIGF.insert(END, '\n')
                        BIGF.insert(END, "BIGF : " + random.choice(local1_2))
                        BIGF.insert(END, '\n')
                        Tanb()
                for word in x.split():
                    if word in local3:
                        BIGF.insert(END, '\n')
                        BIGF.insert(END, "BIGF : " + random.choice(local1_3))
                        BIGF.insert(END, '\n')
                        Galma()

        for word in x.split():
            if word in start_1:
                BIGF.insert(END, '\n')
                BIGF.insert(END, "BIGF : " + random.choice(start_2))
                BIGF.insert(END, '\n')
                BIGF.see(END)

        for word in x.split():
            if word in thx:
                BIGF.insert(END, '\n')
                BIGF.insert(END, "BIGF : " + random.choice(thx_1))
                BIGF.insert(END, '\n')
                BIGF.see(END)

        for word in x.split():
            if word in start_im:
                BIGF.insert(END, '\n')
                BIGF.insert(END, "BIGF : " + random.choice(start_rm))
                BIGF.insert(END, '\n')
                BIGF.see(END)
                memo()

        for word in x.split():
            if word in simsim:
                BIGF.insert(END, '\n')
                BIGF.insert(END, "BIGF : " + random.choice(simsim1))
                BIGF.insert(END, '\n')
                BIGF.see(END)

        for word in x.split():
            if word in schedu:
                BIGF.insert(END, '\n')
                BIGF.insert(END, "BIGF : " + random.choice(schedu1))
                BIGF.insert(END, '\n')
                BIGF.see(END)
                M_timet()

        for word in x.split():
            if word in goog:
                BIGF.insert(END, '\n')
                BIGF.insert(END, "BIGF : " + random.choice(goog1))
                BIGF.insert(END, '\n')
                BIGF.see(END)
                chrome_B()

        entry1.delete("1.0", END)

    image7=PhotoImage(file='enter.png',master=root)
    btn_enter = Button(path_frame, image=image7, bg='seashell2',command=M_Enter2,width=100,relief='flat')
    btn_enter.pack(side="right", padx=2,pady=2,fill='both')
    entry1=Text(path_frame,bg='seashell2',relief='flat',height=10)
    entry1.bind('<Return>',M_Enter)
    entry1.pack(side='left',padx=3,pady=0,fill='both',expand=True)


    thx=('고마워','고마워..','감사','알겠어','ㅇㅋ','응','웅','오키','그래','그냥','미안','미안해')
    thx_1=('네','별 말씀을요','알겠습니다')

    local1=('둔산동','둔산','둔동')
    local1_1=('둔산동 식당을 보여드릴게요','둔산동 식당 5개를 추천합니다.','추천 리스트에요.')

    local2=('탄방동','탄방')
    local1_2=('탄방동 식당을 보여드릴게요','탄방동 식당 5개를 추천합니다.','추천 리스트에요.')

    local3=('갈마동','갈마')
    local1_3=('갈마동 식당을 보여드릴게요','갈마동 식당 5개를 추천합니다.','추천 리스트에요.')

    start_i=('안녕','저기','하이','야','.','뭐해','빅프야','뭐하니','반가워','뭐하냐고','안녕이라고','ㅎㅇ')
    start_r=('안녕하세요', '부르셨나요?', '왜 그러시나요?','저 여기 있어요.','네?','그냥 가만히 있어요')
    start_R=('네?','뭐요?','뭐라고요','다시 입력해 주세요','다시 말해봐')

    start_iw=('날씨','밖에',"온도","비",'몇도','날씨나','추워?','더워?','날씨는?','날씨는' )
    start_rw=('날씨가 어떤가 하면','날씨를 알려드릴게요.')

    start_it=('시간','몇시','시각','타임','몇시야','시간은','시간은?','몇시?','몇시야?','몇시지','시간알려줘')
    start_rt=('시간이 궁금하시군요','시간을 알려드릴게요.')

    start_im=('메모장','메모','투두','투두리스트','메모장켜줘','투두켜줘','메모장열어줘','투두열어줘','메모할','적어야겠다','적을까?','적을까')
    start_rm=('메모장을 열어드리겠습니다.','메모장을 실행합니다.')

    start_il=('밥','점심','저녁','카페','뭐먹','뭐먹지','점메추','배고프다','뭐먹을까','뭐먹을까?','배고파','배고픈걸')
    start_rl=('어디에서 드실 건가요?','식당을 추천해 드릴게요.','밥 먹을 시간이죠.')

    start_1=('바보','멍청이','개새끼','좆같네','ㅈㄹ','지랄','좆같은','죽어','죽인다','죽일거야','죽고싶다','좆같다','새끼','시발','죽일거다',)
    start_2=('나쁜 말은 쓰지 마세요','그런 말은 하지 마세요','예쁜말을 쓰는 건 어떨까요?','무슨 일 있으신가요?')

    simsim=('심심해','심심하다','놀아줘','뭐하지','뭐할까','재밌는','얘기','야아')
    simsim1=('할 짓이 없으신가요?','넷플릭스를 보는 건 어떨까요','저는 바빠요','왜 이러세요?','시리한테 물어보는 게 어떨까요?')

    schedu=('시간표','쉬는날','스케줄','스케쥴','시간표보여줘')
    schedu1=('시간표를 보여드릴게요','시간표가 궁금하신가봐요')

    goog=('구글','인터넷','검색창','구글열어줘','인터넷켜줘','구글켜줘','인터넷열어줘','검색창켜줘','검색')
    goog1=('인터넷 창을 열게요','구글을 실행합니다.','인터넷을 열고있어요.')

    atte=('출석','입실','퇴실','출첵','입실체크','퇴실체크','입실시간','퇴실시간')
    atte1=('입퇴실 체크 화면을 열어드리겠습니다.','입실 퇴실은 항상 잊지 마세요','출석체크 하셨나요?')

    def weather():

        from urllib.request import urlopen
        import bs4

        w_url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'
        html=urlopen(w_url).read()

        soup= bs4.BeautifulSoup(html, 'html.parser')

        temparature=soup.find(class_='temperature_text')
        w_condition=soup.find(class_='before_slash')
        before_y=soup.find(class_="temperature")

        return (temparature.text+w_condition.text,"어제보다 "+before_y.text)

    def t_weather():
        from urllib.request import urlopen
        import bs4

        w_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'
        html = urlopen(w_url).read()

        soup = bs4.BeautifulSoup(html, 'html.parser')

        t_ltemp=soup.find(class_="lowest")
        t_htemp=soup.find(class_="highest")
        return (t_ltemp.text,t_htemp.text)

    def btn_W():

        a=str(weather())

        w=a.replace('{',"")
        w1=w.replace('}',"")
        w2=w1.replace("(","")
        w3=w2.replace(")","")
        w4= w3.replace("'", "")

        BIGF.insert(END, "BIGF :"+w4+'.')

        b=str(t_weather())
        w=b.replace('{',"")
        t1=w.replace('}',"")
        t2=t1.replace("(","")
        t3=t2.replace(")","")
        t4= t3.replace("'", "")
        BIGF.insert(END, "\n")
        a="내일은 "
        BIGF.insert(END, a +t4+" 입니다.")
        BIGF.insert(END, "\n")
        BIGF.see(END)

    from datetime import datetime
    def currentTime():
        dt = datetime.now()
        return "현재 시간은  %s시 %s분" %(dt.hour,dt.minute),"입니다."

    def btn_T():
        t = str(currentTime())
        a=t.replace(",","")
        a1=a.replace("'","")
        a2=a1.replace("(","")
        a3=a2.replace(")","")

        BIGF.insert(END,"BIGF : "+a3)
        BIGF.insert(END,'\n')
        BIGF.see(END)
    def btn_B():
        greet = ('안녕하세요', '안녕','하이','대화를 시작할까요?', '부르셨나요?', '왜 그러시나요?','저 여기 있어요.')
        h=random.choice(greet)

        BIGF.insert(END, "BIGF : "+h)
        BIGF.insert(END,'\n')
        BIGF.see(END)
    def chrome_B():
        BIGF.insert(END,"BIGF : 구글 실행 중")
        BIGF.insert(END, '\n')
        BIGF.see(END)

        import webbrowser
        url_c="http://google.com"
        webbrowser.open(url_c)


    def lunch():
        BIGF.insert(END, '\n')
        BIGF.insert(END, "BIGF : 둔산동 탄방동 갈마동 중 하나를 입력해 주세요.")
        BIGF.insert(END, '\n')
        BIGF.see(END)



    def Dunsan():
        BIGF.insert(END, '\n')
        keyword='둔산동'
        url = f'https://www.mangoplate.com/search/{keyword}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)

        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        data = soup.select('li.server_render_search_result_item > div.list-restaurant-item')

        for item in data[:5]:
            title = item.select_one('h2.title').text.replace('\n', '')
            category = item.select_one('p.etc').text
            rating = item.select_one('strong.search_point').text

            BIGF.insert(END,"카테고리 : "+ category+'\n')
            BIGF.insert(END,"이름 : "+title.replace("(본점)", "")+title.replace("(둔산점)","")+'\n')
            BIGF.insert(END,"평점 : "+rating+'\n')
            BIGF.insert(END,'\n')
            BIGF.see(END)
    def Tanb():
        keyword = '탄방동'
        url = f'https://www.mangoplate.com/search/{keyword}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)

        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        data = soup.select('li.server_render_search_result_item > div.list-restaurant-item')

        for item in data[:5]:
            title = item.select_one('h2.title').text.replace('\n', '')
            category = item.select_one('p.etc').text
            rating = item.select_one('strong.search_point').text

            BIGF.insert(END, "카테고리 : " + category + '\n')
            BIGF.insert(END, "이름 : " + title.replace("(본점)", "") + '\n')
            BIGF.insert(END, "평점 : " + rating + '\n')
            BIGF.insert(END, '\n')
            BIGF.see(END)
    def Galma():
        keyword = '갈마동'
        url = f'https://www.mangoplate.com/search/{keyword}'
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)

        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        data = soup.select('li.server_render_search_result_item > div.list-restaurant-item')

        for item in data[:5]:
            title = item.select_one('h2.title').text.replace('\n', '')
            category = item.select_one('p.etc').text
            rating = item.select_one('strong.search_point').text

            BIGF.insert(END, "카테고리 : " + category + '\n')
            BIGF.insert(END, "이름 : " + title.replace("(본점)", "") + '\n')
            BIGF.insert(END, "평점 : " + rating + '\n')
            BIGF.insert(END, '\n')
            BIGF.see(END)


    def M_timet():
        BIGF.insert(END, "BIGF : 스케줄 보기")
        BIGF.insert(END, '\n')
        BIGF.see(END)

        import module as m

        window = Tk()
        window.geometry("400x300+50+50")
        window.title("Schedule")

        notebook = tkinter.ttk.Notebook(window, width=300, height=300)
        notebook.pack(expand=True, fill=BOTH)

        frame1 = Frame(window)
        frame1.pack(fill=BOTH, expand=True)
        notebook.add(frame1, text="전체")

        label1 = Label(frame1)
        frame = Frame(window)
        frame.pack()

        T_schedule = tkinter.ttk.Treeview(frame1, columns=(1, 2), height=5, show="headings")
        T_schedule.pack(side=LEFT, fill=BOTH, expand=True)

        T_schedule.heading(1, text="날짜")
        T_schedule.heading(2, text="시간")

        T_schedule.column(1, width=100)
        T_schedule.column(2, width=100)

        data = m.result

        for val in data:
            T_schedule.insert('', 'end', values=(val[0], val[1]))

        scroll = Scrollbar(frame1, orient=VERTICAL, command=T_schedule.yview)
        scroll.pack(side=RIGHT, fill=Y)
        T_schedule.configure(yscrollcommand=scroll.set)

        frame2 = Frame(window)
        frame2.pack(fill=BOTH, expand=True)
        notebook.add(frame2, text="월별")

        label2 = Label(frame2)
        label2.pack(fill=BOTH)

        M_schedule = tkinter.ttk.Treeview(frame2, columns=(1, 2), height=5, show="headings")
        M_schedule.pack(side=LEFT, fill=BOTH, expand=False)

        M_schedule.heading(1, text="날짜")
        M_schedule.heading(2, text="시간")

        M_schedule.column(1, width=100)
        M_schedule.column(2, width=100)

        scroll.pack(side=RIGHT, fill=Y)
        M_schedule.configure(yscrollcommand=scroll.set)

        holiday = Label(frame2)
        holiday.pack(side=TOP)

        def delButton():
            x = M_schedule.get_children()
            for item in x:
                M_schedule.delete(item)

        def March():
            March = m.monthly_timetable('03')
            delButton()
            for val in March:
                M_schedule.insert('', 'end', values=(val[0], val[1]))
            holiday["text"] = '쉬는 날' + '\n' + '25(금)' + '\n'

        def April():
            April = m.monthly_timetable('04')
            delButton()
            for val in April:
                M_schedule.insert('', 'end', values=(val[0], val[1]))
            holiday["text"] = '쉬는 날' + '\n' + '1일(금),8일(금),15일(금)' + '\n'

        def May():
            May = m.monthly_timetable('05')
            delButton()
            for val in May:
                M_schedule.insert('', 'end', values=(val[0], val[1]))
            holiday["text"] = '쉬는 날' + '\n' + '5일(목)' + '\n'

        def June():
            June = m.monthly_timetable('06')
            delButton()
            for val in June:
                M_schedule.insert('', 'end', values=(val[0], val[1]))
            holiday["text"] = '쉬는 날' + '\n' + '1일(수),6일(월)' + '\n'

        def July():
            July = m.monthly_timetable('07')
            delButton()
            for val in July:
                M_schedule.insert('', 'end', values=(val[0], val[1]))
            holiday["text"] = '쉬는 날 없음' + '\n'

        def August():
            August = m.monthly_timetable('08')
            delButton()
            for val in August:
                M_schedule.insert('', 'end', values=(val[0], val[1]))
            holiday["text"] = '쉬는 날 없음' + '\n'

        scroll2 = Scrollbar(frame2, orient=VERTICAL, command=M_schedule.yview)
        scroll2.pack(side=LEFT, fill=Y)
        M_schedule.configure(yscrollcommand=scroll2.set)

        btn = Button(frame2, text='3월', command=(March))
        btn.pack(side=TOP)
        btn = Button(frame2, text='4월', command=(April))
        btn.pack(side=TOP)
        btn = Button(frame2, text='5월', command=(May))
        btn.pack(side=TOP)
        btn = Button(frame2, text='6월', command=(June))
        btn.pack(side=TOP)
        btn = Button(frame2, text='7월', command=(July))
        btn.pack(side=TOP)
        btn = Button(frame2, text='8월', command=(August))
        btn.pack(side=TOP)

        window.mainloop()

    def memo():
        BIGF.insert(END, "BIGF : 메모장 여는 중")
        BIGF.insert(END, '\n')
        BIGF.see(END)

        window = tkinter.Tk()
        window.title("MEMO")
        window.geometry("300x450+500+100")
        window.resizable(True, True)

        notebook = tkinter.ttk.Notebook(window, width=300, height=300)
        notebook.pack(expand=True, fill=BOTH)

        # memo
        frame1 = tkinter.Frame(window)
        frame1.pack(fill=BOTH, expand=True)
        notebook.add(frame1, text="메모장")

        label1 = tkinter.Label(frame1)

        scrollbar = tkinter.Scrollbar(label1)
        scrollbar.pack(side="right", fill="y")
        txt = tkinter.Text(label1, yscrollcommand=scrollbar.set, font=('맑은 고딕', 12))

        def m_save():
            note = open('./notetodo/새로운 메모.txt', 'w', encoding='UTF-8')
            ts = str(txt.get(0, END))
            note.writelines(ts)
            note.close()

        btm=Button(label1,text='저장',command=m_save)
        btm.pack()



        txt.pack(side="left", fill="both", expand=True)

        label1.pack()


        # todo
        frame2 = tkinter.Frame(window)
        frame2.pack(fill=BOTH, expand=True)
        notebook.add(frame2, text="TODO LIST")

        label2 = tkinter.Label(frame2)
        label2.pack(fill=BOTH)

        listframe = LabelFrame(label2, text='TODO LIST', width=10, height=10)
        listframe.pack(side='top', fill='both', expand=True, pady=3, padx=5)

        lb = Listbox(listframe, font=('맑은 고딕', 13), width=20, bd=0, activestyle="none")
        lb.pack(fill=BOTH, expand=True, padx=5, pady=5)

        addframe = LabelFrame(listframe, text="추가 / 삭제")
        addframe.pack(side=BOTTOM, fill='both', expand=True, padx=5, pady=5)
        my_entry = Entry(addframe, font=('맑은 고딕', 10))
        my_entry.pack(fill='both', pady=5, expand=True)

        def newTask():
            import tkinter.messagebox

            task = my_entry.get()
            if task != "":
                lb.insert(END, task)
                my_entry.delete(0, "end")
            else:
                tkinter.messagebox.showwarning("TODO", "추가할 내용을 입력해 주세요.")

        def newTask2(event):
            task = my_entry.get()
            if task != "":
                lb.insert(END, task)
                my_entry.delete(0, "end")
            else:
                messagebox.showwarning("TODO", "추가할 내용을 입력해 주세요.")

        def deleteTask():
            lb.delete(ANCHOR)

        button_frame = addframe
        button_frame.pack(pady=20)

        imageI = PhotoImage(file='add.png',master=window)
        addTask_btn = Button(button_frame, image=imageI,padx=5, pady=5, command=newTask, relief=FLAT)
        addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)
        my_entry.bind('<Return>', newTask2)

        imageII = PhotoImage(file='del.png',master=window)
        delTask_btn = Button(button_frame,image=imageII, padx=5, pady=5, command=deleteTask, relief=FLAT)
        delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

        window.mainloop()
    def user():
        BIGF.insert(END,"BIGF : 사용자 정보 보기")
        BIGF.insert(END, '\n')
        BIGF.see(END)

    def calculat():
        BIGF.insert(END, "BIGF : 훈련수당 계산하기")
        BIGF.insert(END, '\n')
        BIGF.see(END)





    #이미지 버튼

    image1=PhotoImage(file='raccoon.png',master=root)
    btn0=Button(label_frame3,command=btn_B,image=image1,compound='top',relief='flat',bg='seashell2')
    btn0.pack(side='left',fill='both',padx=5,pady=1)

    image2=PhotoImage(file='clock.png',master=root)
    btn1=Button(label_frame3,command=btn_T,image=image2,compound='top',relief='flat',bg='seashell2')
    btn1.pack(side='left',fill='both',padx=5,pady=1)

    image5=PhotoImage(file='sun.png',master=root)
    btn4=Button(label_frame3,image=image5,compound='top',command=btn_W,relief='flat',bg='seashell2')
    btn4.pack(side='left',fill='both',padx=5,pady=1)

    image13=PhotoImage(file='schedule.png',master=root)
    btn13=Button(label_frame3,image=image13,command=M_timet,compound='top',relief='flat',bg='seashell2')
    btn13.pack(side='left',fill='both',padx=5,pady=1)


    image9=PhotoImage(file='memo.png',master=root)
    btn9=Button(label_frame3,image=image9,compound='top',command=memo,relief='flat',bg='seashell2')
    btn9.pack(side='left',fill='both',padx=5,pady=1)


    image3=PhotoImage(file='dinner.png',master=root)
    btn2=Button(label_frame3,height=3,relief='flat',image=image3,command=lunch,compound='top',bg='seashell2')
    btn2.pack(side='left',fill='both',padx=5,pady=1)

    image4=PhotoImage(file='game.png',master=root)
    btn3=Button(label_frame3,image=image4,compound='top',relief='flat',bg='seashell2')



    image8=PhotoImage(file='chromeicon.png',master=root)
    btn8=Button(label_frame3,image=image8,compound='top',command=chrome_B,relief='flat',bg='seashell2')
    btn8.pack(side='left',fill='both',padx=5,pady=1)


    image_i=PhotoImage(file='add.png',master=root)
    image12 = PhotoImage(file='del.png',master=root)

    image_i2=PhotoImage(file='user.png',master=root)

    btn14=Button(label_frame3,compound='top',image=image_i2,relief='flat',bg='seashell2')
    #btn14.pack(side='right',fill='both',padx=5,pady=1)

    image_i4=PhotoImage(file='won.png',master=root)
    btn15=Button(label_frame3,image=image_i4,compound='top',command=calculat,relief='flat',bg='seashell2')


    root.mainloop()


window = Tk()
window.title('LOGIN')
window.geometry('300x150+200+200')
window.resizable(False, False)


iframe2 = LabelFrame(window, text=" 이름 / 전화번호(뒤 4자리) ")
iframe2.pack(fill='y', padx=10, pady=5)

def id_ent():
    x = entry_i.get()
    entry_i.delete(0, "end")
    if x != "":
        user = open('./userlist/' + x + '.txt', 'a', encoding='UTF-8')
        user.close()
        messagebox.showwarning("경고", "계정 생성 완료.")


        window.quit()
        window.destroy()
        chatbot()

    else:
        messagebox.showwarning("경고", "이름과 전화번호를 확인해 주세요.")

def id_ent2(event):
    x = entry_i.get()
    entry_i.delete(0, "end")
    if x != "":

        window.quit()
        window.destroy()
        chatbot()
    elif x + '.txt' not in os.listdir('userlist'):
        messagebox.showwarning("경고", "존재하지 않는 계정입니다." + '\n' + "계정 생성을 눌러주십시오.")
    else:
        messagebox.showwarning("경고", "이름과 전화번호를 입력해 주세요.")

def id_ent3():
    x = entry_i.get()
    entry_i.delete(0, "end")
    if x != "":
        window.quit()
        window.destroy()
        chatbot()

    elif x + '.txt' not in os.listdir('userlist'):
        messagebox.showwarning("경고", "존재하지 않는 계정입니다." + '\n' + "계정 생성을 눌러주십시오.")
    else:
        messagebox.showwarning("경고", "이름과 전화번호를 확인해 주세요.")


entry_i = Entry(iframe2)
entry_i.pack(side='left',padx=3)
id_enter = Button(iframe2, text="계정 생성", command=id_ent)
id_enter.pack(fill='y',padx=5)
id_enter2 = Button(iframe2, text="로그인", command=id_ent3)
id_enter2.pack(fill='both',padx=5,pady=5)
entry_i.bind('<Return>', id_ent2)


window.mainloop()

