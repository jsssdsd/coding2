import random
import time
import tkinter as tk
import random as rd
import numpy as np
import onedaylife_data_test as one
import MVP_class as vp

image1=0
image2=0
image3=0

class user_data():
    def __init__(self,id,pw,name,n_name,birth,gen,email,coin):
        self.id=id
        self.pw=pw
        self.name=name
        self.n_name=n_name
        self.birth=birth
        self.gen=gen
        self.email=email
        self.coin=coin
user=user_data("1234","1234","박동진","기린","990325","남자","qwe123@naver.com","999999999")

def game_1():
    global user
    vp.all_data()
    win1 = tk.Tk()
    win1.title("하루살이 Game")
    win1.geometry("800x600")
    win1.resizable(False, False)

    image1 = tk.PhotoImage(file='first.png')
    image2 = tk.PhotoImage(file="second.png")
    image3 = tk.PhotoImage(file="third.png")
    listImage = [image1, image2, image3]

    # 함수 정의 파트
    def ondaylife_death():
        global user
        text=open('onedaylife_coin_use.txt','r',encoding='utf-8')
        texts=text.readlines()
        text.close()
        text2=[]
        death_count=0
        for i in texts:
            text2.append(i.replace('\n','').split('\t'))
        for i in range(len(text2)):
            if text2[i][0] == user.id and text2[i][2]== '죽음':
                death_count+=1
        return str(death_count)

    def cnt_time():
        global user
        file=open('onedaylife_coin_use.txt','r',encoding='UTF-8')
        lines=file.readlines()
        file.close()
        lines=lines[1:]
        temp_1=[]
        for i in range(len(lines)):
            lines[i]=lines[i].strip().split('\t')
        for i in range(len(lines)):
            if lines[i][0] == user.id:
                temp_1.append(lines[i])
        temp_1.reverse()
        temp_2=[]
        for i in range(len(temp_1)):
            temp_2.append(temp_1[i][2])
        temp_3=[]
        if '죽음' in temp_2:
            temp_3=temp_2[:temp_2.index('죽음')]
        a=0
        for i in range(len(temp_3)):
            if temp_3[i] != '죽음':
                a+=float(temp_3[i].split('시간')[0])
        b=len(temp_3)
        return (a,b)

    def num_mvp():
        aa = vp.mvp_cut()[:20]
        temp_str = ''
        for i in range(len(aa)):
            temp_str += ' {}\n'.format(i + 1)
        mvp_count2 = tk.Label(frame_MVP, text=temp_str, anchor='w')
        mvp_count2.place(x=240, y=150, height=315, width=80)

    def live_time():
        aa = vp.mvp_cut()[:20]
        temp_list1 = ''
        for i in range(len(aa)):
            temp_list1 += '  {}\n'.format(vp.listbox_insert()[i][2])
        mvp_listbox2 = tk.Label(frame_MVP, text=temp_list1, anchor='w')
        mvp_listbox2.place(x=320, y=150, height=315, width=90)

    def coin_use():
        aa = vp.mvp_cut()[:20]
        temp_list2 = ''
        for i in range(len(aa)):
            temp_list2 += '  {}\n'.format(vp.listbox_insert()[i][3])
        mvp_listbox4 = tk.Label(frame_MVP, text=temp_list2)
        mvp_listbox4.place(x=410, y=150, height=315, width=100)

    def nick():
        aa = vp.mvp_cut()[:20]
        temp_list3 = ''
        for i in range(len(aa)):
            temp_list3 += '  {}\n'.format(vp.listbox_insert()[i][1])
        mvp_listbox6 = tk.Label(frame_MVP, text=temp_list3)
        mvp_listbox6.place(x=480, y=150, height=315, width=100)

    def mvp_list():
        num_mvp()
        live_time()
        coin_use()
        nick()

    def mylife_new():
        mylife_listbox1 = tk.Listbox(frame_Mylife)
        mylife_listbox1.yview()
        mylife_listbox1.place(x=240, y=190, height=200, width=300)
        user_list = vp.coin_use(user)
        temp_str_space = ' ' * 8
        temp_list4 = ''
        count_num=0
        for i in range(len(user_list)):
            count_num+=1
            time_get = time.localtime(float(user_list[i][3]))
            time_set = time.strftime('%y-%m-%d %H:%M', time_get)
            temp_list4 += '  {}\n'.format(
                time_set + temp_str_space + user_list[i][1] + temp_str_space +str(count_num)+temp_str_space+ user_list[i][2])
            mylife_listbox1.insert(0, temp_list4)
            temp_list4 = ''
            frame_Mylife.tkraise()

        mylife_label2 = tk.Label(frame_Mylife, text=str(len(user_list)))
        mylife_label2.place(x=280, y=140, height=20, width=30)
        mylife_coinuse_label = tk.Label(frame_Mylife, text='코인 사용량')
        mylife_coinuse_label.place(x=260, y=115, height=20, width=80)

        mylife_label3 = tk.Label(frame_Mylife, text=ondaylife_death())
        mylife_label3.place(x=470, y=140, height=20, width=30)
        btn4 = tk.Button(frame_Mylife, text='사\n용\n내\n역', command=user_coin_list)
        btn4.place(x=210, y=190, width=30, height=70)

    def user_coin_list():
        usecoin = tk.Listbox(img_mylife)
        usecoin.yview()
        usecoin.place(x=240, y=190, height=200, width=300)
        user_list = vp.txt_check_user(user)
        temp_str_space = ' ' * 7
        count_all=0
        temp_list4 = ''
        for i in range(len(user_list)): #234 -  -   0
            for j in range(len(user_list[i][1:])):
                if user_list[i][1]!='-':
                    count_all+=5
                    time_get = time.localtime(float(user_list[i][1]))
                    time_set = time.strftime('%y-%m-%d %H:%M', time_get)
                    temp_list4 += '  {}\n'.format(user_list[i][0]+temp_str_space+'포스팅'+temp_str_space+time_set+temp_str_space+str(count_all)+('(+5)'))
                    usecoin.insert(0, temp_list4)
                    temp_list4 = ''
                elif user_list[i][2]!='-':
                    count_all+=3
                    time_get = time.localtime(float(user_list[i][2]))
                    time_set = time.strftime('%y-%m-%d %H:%M', time_get)
                    temp_list4 += '  {}\n'.format(user_list[i][0]+temp_str_space+'로그인'+temp_str_space+time_set+temp_str_space+str(count_all)+('(+3)'))
                    usecoin.insert(0, temp_list4)
                    temp_list4 = ''
                elif user_list[i][3] != '-':
                    count_all+=4
                    time_get = time.localtime(float(user_list[i][3]))
                    time_set = time.strftime('%y-%m-%d %H:%M', time_get)
                    temp_list4 += '  {}\n'.format(user_list[i][0]+temp_str_space+'인기글'+temp_str_space+time_set+temp_str_space+str(count_all)+('(+4)'))
                    usecoin.insert(0, temp_list4)
                    temp_list4 = ''
                btn4 = tk.Button(frame_Mylife, text='획\n득\n내\n역', command=mylife_new)
                btn4.place(x=210, y=190, width=30, height=70)
                frame_Mylife.tkraise()

    def changeIMG():
        # 이미지 전환
        rn = np.random.randint(3)
        label1 = tk.Label(frame_game, image=listImage[rn])
        label1.place(x=250, y=100)
        win1.after(300, changeIMG)
        # elif b!=1:
        #     label1 = tk.Label(frame_game, image=image1)
        #     label1.place(x=250, y=100)
        #     win1.after(300, changeIMG)

    def showMVP():
        mvp_list()
        frame_MVP.tkraise()

        # 내 하루살이 보기

    def showMylife():
        mylife_new()
        frame_Mylife.tkraise()

        # 게임화면 보기

    def showGame():
        frame_game.tkraise()

    def game_random():
        global user
        user_coin = int(user.coin)
        if user_coin >= 1:
            ephemera = ["죽음", "0시간", "0.5시간", "1시간", "1.5시간", "2시간", "2.5시간", "3시간", "4시간", "5시간"]
            sNumbers = np.random.choice(ephemera, 1, p=[0.5, 0.3, 0.1, 0.055, 0.035, 0.002, 0.002, 0.002, 0.002, 0.002])
            sNumbers = str(sNumbers[0])
            if sNumbers == '죽음':
                text = open('MVP.txt', 'a', encoding='utf-8')
                text.write('\n' + user.id + '\t' + user.n_name + '\t' + '{}\t{}'.format(cnt_time()[0], cnt_time()[1]))
            my_oneday3.configure(text=sNumbers)
            file = open('onedaylife_coin_use.txt', 'a', encoding='utf-8')
            file.write('\n' + user.id + '\t' + user.n_name + '\t' + sNumbers + '\t' + str(time.time()))
            file.close()
            vp.coin_count(user)
            my_oneday2_1.configure(text='{}시간 {}코인'.format(cnt_time()[0], cnt_time()[1]))
            return sNumbers
        elif user_coin == 0:
            my_oneday3.configure(text='코인이 없습니다')
            return


    # 마이라이프
    frame_Mylife = tk.Frame(win1, bd=2, bg='yellow')
    frame_Mylife.place(x=0, y=0, width=800, height=600)

    house = tk.PhotoImage(file='imghdd.gif')
    house_image = tk.Label(frame_Mylife, image=house)
    house_image.place(x=0, y=0, width=800, height=600)
    my_oneday1 = tk.Label(frame_Mylife, text='My life')
    my_oneday1.place(x=300, y=40, width=200, height=20)
    my_mvp=tk.Label(frame_Mylife, text='나의 최고 기록')
    my_mvp.place(x=300, y=40, width=200, height=20)

    # -- mylife 버튼
    btn2 = tk.Button(frame_Mylife, text="MVP", command=showMVP)
    btn2.place(x=720, y=15, width=50, height=50)

    btn3 = tk.Button(frame_Mylife, text="Mylife", command=showMylife)
    btn3.place(x=670, y=15, width=50, height=50)

    btn3 = tk.Button(frame_Mylife, text="Game", command=showGame)
    btn3.place(x=620, y=15, width=50, height=50)

    btn4=tk.Button(frame_Mylife, text='획\n득\n내\n역',command=user_coin_list)
    btn4.place(x=210,y=190,width=30, height=70)


    #명예의 전당
    frame_MVP = tk.Frame(win1, bd=2, bg='yellow')
    frame_MVP.place(x=0, y=0,width=800, height=600)

    mvp_count1 = tk.Label(frame_MVP,text='순위')
    mvp_count1.place(x=245, y=110, height=25, width=40)

    mvp_listbox1 = tk.Label(frame_MVP,text='살아남은 시간')
    mvp_listbox1.place(x=300, y=110, height=25, width=80)

    mvp_listbox3 = tk.Label(frame_MVP, text='코인 사용량')
    mvp_listbox3.place(x=410, y=110, height=25, width=80)

    mvp_listbox5 = tk.Label(frame_MVP, text='닉네임')
    mvp_listbox5.place(x=510, y=110, height=25, width=60)

    # -- 명예의 전당 버튼
    MVP = tk.Label(frame_MVP, text='명예의 전당')
    MVP.place(x=300, y=50, width=200, height=20)

    btn2 = tk.Button(frame_MVP, text="MVP", command=showMVP)
    btn2.place(x=720, y=15, width=50, height=50)

    btn3 = tk.Button(frame_MVP, text="Mylife", command=showMylife)
    btn3.place(x=670, y=15, width=50, height=50)

    btn3 = tk.Button(frame_MVP, text="Game", command=showGame)
    btn3.place(x=620, y=15, width=50, height=50)

    # 게임
    frame_game = tk.Frame(win1, bd=2)
    frame_game.place(x=0, y=0,width=800, height=600)

    bg_image = tk.PhotoImage(file='backgound.png')
    background_game=tk.Label(frame_game,image=bg_image)
    background_game.place(x=0,y=0,width=800, height=600)

    back = tk.Label(frame_game)
    back.place(x=1, y=1)
    my_oneday2=tk.Label(frame_game,text='살아남은 시간 →')
    my_oneday2.place(x=250, y=70, width=100, height=20)

    my_oneday2_1 = tk.Label(frame_game, text='{}시간 {}코인'.format(cnt_time()[0],cnt_time()[1]))
    my_oneday2_1.place(x=450, y=70, width=100, height=20)
    my_oneday3 = tk.Label(frame_game, text='코인을 넣어 주세요')
    my_oneday3.place(x=350, y=520, width=120, height=20)

    label1=tk.Label(frame_game, image=changeIMG())
    label1.place(x=250,y=100)
    coin=tk.PhotoImage(file='ccoin.png')
    coin_label=tk.Label(image=coin)
    coin_label1=tk.Button(frame_game,coin_label, command=game_random)
    coin_label1.place(x=470,y=500)

    # -- 게임 버튼
    btn2=tk.Button(frame_game,text="MVP",command=showMVP)
    btn2.place(x=720,y=15,width=50,height=50)

    btn3=tk.Button(frame_game,text="Mylife",width=6,height=3,command=showMylife)
    btn3.place(x=670,y=15,width=50,height=50)

    btn3=tk.Button(frame_game,text="Game",command=showGame)
    btn3.place(x=620,y=15,width=50,height=50)

    win1.mainloop()













