from datetime import datetime, timedelta
import datetime as dt
from tkinter import *
import tkinter as tk
import tkinter.ttk


program = tk.Tk()
# program1=tk.Tk()

program.title('oo헬스')
program.geometry('1920x1080+0+0')
program.resizable(True, True)
PN = ''



# 오류메시지 모듈
class notdate(Exception):
    def __str__(self):
        return '일치하는 회원 정보가 없습니다.'


# 신규 회원 창 함수
def new_member_window():
    global name_ent
    global GenderVariety_0
    global birth_ent
    global phone_ent
    new_member_win = tk.Toplevel(program)
    new_member_win.geometry('230x175')
    new_member_win.title('신규 회원 가입')
    label2 = tk.Label(new_member_win, text='신규회원')
    label2.place(x=50, y=0)
    name_label = tk.Label(new_member_win, text='이름')
    name_label.place(x=0, y=25)
    name_ent = tk.Entry(new_member_win)
    name_ent.place(x=50, y=25)
    gen_label = tk.Label(new_member_win, text='성별')
    gen_label.place(x=0, y=50)
    GenderVariety_0 = tk.IntVar()
    gen_ent1 = tk.Radiobutton(new_member_win, text='남', value='1', variable=GenderVariety_0)

    gen_ent2 = tk.Radiobutton(new_member_win, text='여', value='2', variable=GenderVariety_0)
    gen_ent1.place(x=50, y=50)
    gen_ent2.place(x=95, y=50)
    birth_label = tk.Label(new_member_win, text='생년월일')
    birth_label.place(x=0, y=75)
    birth_ent = tk.Entry(new_member_win)
    birth_ent.place(x=50, y=75)
    phone_label = tk.Label(new_member_win, text='전화번호')
    phone_label.place(x=0, y=100)
    phone_ent = tk.Entry(new_member_win)
    phone_ent.place(x=50, y=100)

    # 회원 신규생성 모듈
    def new_member():
        global name_ent
        global GenderVariety_0
        global birth_ent
        global phone_ent
        from datetime import datetime, timedelta
        membergroup = open('member.txt', 'r', encoding='UTF-8')
        member = membergroup.readlines()
        member_list = member[1:]
        membergroup.close()
        confirm = []
        if 1 < len(name_ent.get()) <= 4:  # 이름 2-4자리 입력해달라고
            if len(birth_ent.get()) == 6:
                try:
                    datetime.strptime(birth_ent.get(), '%y%m%d')
                except ValueError:
                    not_date = tk.Toplevel(new_member_win)
                    not_date.geometry('200x100')
                    not_date_label = tk.Label(not_date, text='유효한 날짜를 입력해주세요.')
                    not_date_label.pack()

                    def not_date_withdraw():
                        not_date.withdraw()

                    not_date_withdraw_button = tk.Button(not_date, text='닫기', command=not_date_withdraw)
                    not_date_withdraw_button.pack()
                else:
                    for i in range(len(member_list)):
                        confirm.append(member_list[i][16:24])
                    if GenderVariety_0.get() == 1 or GenderVariety_0.get() == 2:  # 성별 선택 안했으면 하라고
                        if len(phone_ent.get()) == 8:  # 폰번호 8자리 아니면 다시 하라고
                            if phone_ent.get() not in confirm:  # 같은번호 있다고
                                if len(member) == 1:  # 회원번호 생성해주기
                                    add_new_mem = '00001'
                                else:
                                    if int(str(int(member[-1][0:5]) + 1)) < 10:
                                        add_new_mem = '0000'
                                        add_new_mem += str(int(member[-1][0:5]) + 1)
                                    elif int(str(int(member[-1][0:5]) + 1)) < 100:
                                        add_new_mem = '000'
                                        add_new_mem += str(int(member[-1][0:5]) + 1)
                                    elif int(str(int(member[-1][0:5]) + 1)) < 1000:
                                        add_new_mem = '00'
                                        add_new_mem += str(int(member[-1][0:5]) + 1)
                                    elif int(str(int(member[-1][0:5]) + 1)) < 10000:
                                        add_new_mem = '0'
                                        add_new_mem += str(int(member[-1][0:5]) + 1)
                                    elif int(str(int(member[-1][0:5]) + 1)) < 100000:
                                        add_new_mem = ''
                                        add_new_mem += str(int(member[-1][0:5]) + 1)
                                    else:
                                        pass
                                if len(name_ent.get()) == 2:  # 이름 2글자나 3글자인 사람은 앞에 x 붙여주기
                                    add_new_mem += ('xx')
                                    add_new_mem += (name_ent.get())
                                elif len(name_ent.get()) == 3:
                                    add_new_mem += ('x')
                                    add_new_mem += (name_ent.get())
                                elif len(name_ent.get()) == 4:
                                    add_new_mem += (name_ent.get())

                                if GenderVariety_0.get() == 1:  # 성별 고르기
                                    add_new_mem += ('1')
                                elif GenderVariety_0.get() == 2:
                                    add_new_mem += ('2')
                                add_new_mem += (birth_ent.get())
                                add_new_mem += (phone_ent.get())
                                add_new_mem += '000000000000000000000000000000000000000000000000000000000000000000000000000\n'
                                membergroup = open('member.txt', 'a', encoding='UTF-8')
                                print(add_new_mem)
                                membergroup.write(add_new_mem)  # member.txt에 추가해주기
                                membergroup.close()
                                new_member_com = tk.Toplevel(new_member_win)
                                new_member_com.geometry('200x100')
                                congratulation = tk.Label(new_member_com, text='환영합니다.')
                                congratulation.pack()

                                def withdraw_1():
                                    new_member_win.withdraw()
                                    new_member_com.withdraw()

                                new_mem_win_withdraw = tk.Button(new_member_com, text='닫기', command=withdraw_1)
                                new_mem_win_withdraw.pack()
                            else:
                                same_phone = tk.Toplevel(new_member_win)
                                same_phone.geometry('285x50')
                                same_phone_label = tk.Label(same_phone, text='동일한 전화번호의 회원이 이미 등록되어있습니다.')
                                same_phone_label.pack()

                                def same_phone_withdraw():
                                    same_phone.withdraw()

                                same_phone_withdraw_button = tk.Button(same_phone, text='닫기',
                                                                       command=same_phone_withdraw)
                                same_phone_withdraw_button.pack()
                        else:
                            phone_len_win = tk.Toplevel(new_member_win)
                            phone_len_win.geometry('200x100')
                            phone_len_label = tk.Label(phone_len_win, text="'010'과 '-'을 제외한 8자리의 번호를 입력해주세요.")
                            phone_len_label.pack()

                            def phone_withdraw():
                                phone_len_win.withdraw()

                            phone_withdraw_button = tk.Button(phone_len_win, text='닫기', command=phone_withdraw)
                            phone_withdraw_button.pack()
                    else:
                        gender_plz = tk.Toplevel(new_member_win)
                        gender_plz.geometry('200x100')
                        gender_plz_label = tk.Label(gender_plz, text='성별을 선택해주세요.')
                        gender_plz_label.pack()

                        def gender_plz_withdraw():
                            gender_plz.withdraw()

                        gender_plz_withdraw_button = tk.Button(gender_plz, text='닫기', command=gender_plz_withdraw)
                        gender_plz_withdraw_button.pack()
            else:
                birth_index_win = tk.Toplevel(new_member_win)
                birth_index_win.geometry('200x100')
                birth_index_label = tk.Label(birth_index_win, text='6자리의 생년월일을 입력해주세요.')
                birth_index_label.pack()

                def birth_index_withdraw():
                    birth_index_win.withdraw()

                birth_index_withdraw_button = tk.Button(birth_index_win, text='닫기', command=birth_index_withdraw)
                birth_index_withdraw_button.pack()
        else:
            name_index_win = tk.Toplevel(new_member_win)
            name_index_win.geometry('200x100')
            name_index_label = tk.Label(name_index_win, text='2-4자리의 이름을 입력해주세요.')
            name_index_label.pack()

            def name_index_withdraw():
                name_index_win.withdraw()

            name_index_withdraw_button = tk.Button(name_index_win, text='닫기', command=name_index_withdraw)
            name_index_withdraw_button.pack()

    make_new = tk.Button(new_member_win, text='생성', command=new_member)
    make_new.place(x=80, y=125)


# 기존회원 로그인


def loginID():
    global PN
    membergroup = open('member.txt', 'r', encoding='UTF-8')
    member = membergroup.readlines()
    membergroup.close()
    member_list = member[1:]
    a = member_list
    for i in range(len(a)):
        if num_ent.get() == a[i][16:24]:
            name = member_list[i][5:9]
            name = name.replace('x', '')
            PN_Label.configure(text='%s 님 반갑습니다.' % name)
            PN = num_ent.get()
            break
        else:
            PN_Label.configure(text='회원정보가 존재하지 않습니다.')


def logoutID():
    global PN
    PN = ''
    PN_Label.configure(text='로그아웃 되었습니다.')
    num_ent.delete(0,8)

your_locker = 0

label1 = tk.Label(program, text='헬스클럽')
label1.place(x=950, y=0)
button1 = tk.Button(program, text='신규회원가입', command=new_member_window)
button1.place(x=50, y=25)

client_label = tk.Label(program, text='기존회원')
client_label.place(x=200, y=51)
input_num = tk.Label(program, text='전화번호')
input_num.place(x=200, y=75)
num_ent = tk.Entry(program)
num_ent.place(x=250, y=75)
login_button = tk.Button(program, text='Login', command=loginID)
login_button.place(x=400, y=75)
logout_button = tk.Button(program, text='Logout', command=logoutID)
logout_button.place(x=460, y=75)
PN_Label = tk.Label(program, text='')
PN_Label.place(x=450, y=100)

f2 = tk.Frame(program, width=900, height=3, bd=2, bg='black')
f2.place(x=0, y=150)
f2.propagate(0)

f3 = tk.Frame(program, width=3, height=1080, bd=2, bg='black')
f3.place(x=900, y=0)
f3.propagate(0)
#######################################################################################
client_label2 = tk.Label(program, text='이용권 결제')
client_label2.place(x=200, y=175)
sell_code_file = open('상품코드.txt', 'r', encoding='UTF-8')
sell_code_list = sell_code_file.readlines()
for i in range(len(sell_code_list)):
    sell_code_list[i] = sell_code_list[i].replace('\n', '')
code_name = sell_code_list[0]
code_name = code_name.replace('\n', '')
code_name = code_name.split('\t')
sell_code_list = sell_code_list[1:]


def creat_Label():
    global code_name
    global sell_code_list
    a = []
    b = 0
    for i in range(len(sell_code_list)):
        if sell_code_list[i][0] in a:
            pass
        else:
            a.append(sell_code_list[i][0])
            globals()['Label_{}'.format(i)] = tk.Label(program, text=(str(code_name[int(sell_code_list[i][0])])))
            globals()['Label_{}'.format(i)].place(x=0 + (200 * b), y=225)

            b += 1


def creat_RadioB():
    global sell_code_list
    global today
    from datetime import datetime, timedelta
    today = datetime.now()
    today = today.strftime('%y%m%d')

    a = []
    b = 1
    c = -1
    for i in range(len(sell_code_list)):
        if sell_code_list[i][0] in a:
            b += 1
        else:
            a.append(sell_code_list[i][0])
            b = 1
            c += 1
        if sell_code_list[i][1:3] == 'dd':
            long = '일일권:'
        elif 0 < int(sell_code_list[i][1:3]) < 12:
            long = str(int(sell_code_list[i][1:3])) + '개월:'
        elif int(sell_code_list[i][1:3]) == 12:
            long = '1년:'
        else:
            long = str(int(sell_code_list[i][1:3])) + '개월:'
        pay = str(format((int(sell_code_list[i][3:8]) * 1000), ',')) + '원'
        Text = long + pay
        globals()['RadioVariety_{}'.format(i)] = tk.IntVar()
        globals()['Radio_{}_{}'.format(c, i)] = tk.Radiobutton(program, text=Text, value=b, variable=globals()['RadioVariety_{}'.format(c)])  # 라디오버튼 비활성화 생성
        globals()['Radio_{}_{}'.format(c, i)].place(x=55 + (200 * c), y=225 + (25 * b))
    for i in range(len(a)):  # 선택안함 버튼
        globals()['cancle_R_{}'.format(i)] = tk.Label(program, text='선택취소')
        globals()['cancle_R_{}'.format(i)].place(x=0 + (200 * (i)), y=250)

        globals()['NONE_{}'.format(i)] = tk.Radiobutton(value=0, variable=globals()['RadioVariety_{}'.format(i)])
        globals()['NONE_{}'.format(i)].place(x=0 + (200 * (i)), y=275)

    for i in range(len(a)):  # 운동시작날짜적어달라는 라벨&앤트리
        globals()['Label_{}'.format(i)] = tk.Label(program, text='운동시작날짜YYMMDD')
        globals()['Label_{}'.format(i)].place(x=55 + (200 * i), y=200)
        globals()['Entry_{}'.format(i)] = tk.Entry(program)
        globals()['Entry_{}'.format(i)].place(x=55 + (200 * i), y=225)
        globals()['Entry_{}'.format(i)].insert(0, today)

###########################################################################
creat_Label()
creat_RadioB()

locker_label = tk.Label(program, text='사물함 선택')
locker_label.place(x=50, y=400)
locker_list_box = tk.Listbox(program, selectmode='single', width=50)
locker_file = open('locker.txt', 'r', encoding='UTF-8')
locker_list = locker_file.readlines()
locker_list = locker_list[1:]
your_locker_label = tk.Label(program, text='')
your_locker_label.place(x=170, y=400)

# 코드를 사람이 읽는 언어로 변환해서 locker list box에 하나씩 더해줘서 출력              라커리스트 출력
for i in range(len(locker_list)):
    insert_locker = ''
    insert_locker += locker_list[i][0:3]
    if locker_list[i][3] == '1':
        insert_locker += '사용가능'
    elif locker_list[i][3] == '2':
        insert_locker += '사용불가 ' + locker_list[i][4:9] + '번 회원님이 사용중 ' + locker_list[i][15:17] + '년' + locker_list[i][17:19] + '월' + locker_list[i][19:21] + '일' + '만료예정'
    elif locker_list[i][3] == '3':
        insert_locker += '사용불가'
    locker_list_box.insert(i, insert_locker)
locker_list_box.place(x=0, y=425)
f1 = tk.Frame(program, relief='solid')
f1.configure(width=15, height=165)
f1.place(x=354, y=425)
f1.pack_propagate(0)
scrollbar = tk.Scrollbar(f1)
scrollbar.pack(fill="both", expand=True)
scrollbar["command"] = locker_list_box.yview
locker_S_label = tk.Label(program, text='사용시작날짜YYMMDD')
locker_S_label.place(x=400, y=500)
locker_S_entry = tk.Entry(program)
locker_S_entry.insert(0, today)
locker_S_entry.place(x=400, y=525)

locker_E_label = tk.Label(program, text='사용종료날짜YYMMDD')
locker_E_label.place(x=400, y=550)
locker_E_entry = tk.Entry(program)
locker_E_entry.insert(0, today)
locker_E_entry.place(x=400, y=575)
your_locker_price = 0


def empty_locker():
    global locker_list_box
    locker_file = open('locker.txt', 'r', encoding='UTF-8')
    locker_list = locker_file.readlines()
    locker_list = locker_list[1:]
    del_index = []
    for i in range(len(locker_list)):
        if locker_list[i][3] == '2':
            del_index.append(i)
        elif locker_list[i][3] == '3':
            del_index.append(i)
    del_index.reverse()
    for i in range(len(del_index)):
        locker_list_box.delete(del_index[i])
    every_button.configure(state='normal')
    empty_button.configure(state='disabled')


def every_locker():
    global locker_list_box
    locker_file = open('locker.txt', 'r', encoding='UTF-8')
    locker_list = locker_file.readlines()
    locker_list = locker_list[1:]
    add_index = []
    for i in range(len(locker_list)):
        if locker_list[i][3] == '2':
            add_index.append(i)
        elif locker_list[i][3] == '3':
            add_index.append(i)
    for i in range(len(add_index)):
        insert_locker = ''
        insert_locker += locker_list[add_index[i]][0:3]
        if locker_list[add_index[i]][3] == '1':
            insert_locker += '사용가능'
        elif locker_list[add_index[i]][3] == '2':
            insert_locker += '사용불가 ' + locker_list[add_index[i]][4:9] + '번 회원님이 사용중 ' + locker_list[add_index[i]][
                                                                                        15:17] + '년' + locker_list[
                                                                                                           add_index[
                                                                                                               i]][
                                                                                                       17:19] + '월' + \
                             locker_list[add_index[i]][19:21] + '일' + '만료예정'
        elif locker_list[add_index[i]][3] == '3':
            insert_locker += '사용불가'
        locker_list_box.insert(add_index[i], insert_locker)
    every_button.configure(state='disabled')
    empty_button.configure(state='normal')


empty_button = tk.Button(program, text='사용 가능 사물함만 보기', command=empty_locker)
empty_button.place(x=400, y=425)
every_button = tk.Button(program, text='모든 사물함 보기', command=every_locker, state='disabled')
every_button.place(x=400, y=450)

empty_locker()
every_locker()


def locker_choise():
    global locker_list_box
    global your_locker
    global print_your_locker
    global your_locker_price
    global locker_list
    global PN

    if PN == '':
        login_plz = tk.Toplevel(program)
        login_plz.geometry('200x100+60+600')
        login_plz_label = tk.Label(login_plz, text='로그인후 이용할 수 있습니다.')
        login_plz_label.pack()

        def login_plz_withdraw_button():
            login_plz.withdraw()

        login_plz_withdraw = tk.Button(login_plz, text='닫기', command=login_plz_withdraw_button)
        login_plz_withdraw.pack()
    else:
        if locker_list_box.curselection() == None:
            pass
        else:
            your_locker = int(
                locker_list_box.get(locker_list_box.curselection()[0])[0:3])  # 선택한 라카의 라카번호 / 문제 생기면 int 빼주기
            print(your_locker)
            membertxt = open('member.txt', 'r', encoding='UTF-8')
            have_locker = membertxt.readlines()
            for i in range(len(have_locker)):
                if PN == have_locker[i][16:24]:
                    your_locker_num = have_locker[i][84:87]
                    break
            if your_locker_num != '000':
                your_locker_label.configure(text='이미 사물함을 이용중입니다.')
                your_locker = 0
                your_locker_price = 0
            else:
                if locker_list[int(locker_list_box.get(locker_list_box.curselection()[0])[0:3]) - 1][3] == '1':
                    print_your_locker = '%d 번 사물함을 선택하셨습니다.' % your_locker
                    your_locker_label.configure(text=print_your_locker)
                    your_locker_price = 5000
                else:
                    your_locker_label.configure(text='사용 불가능한 사물합입니다.')
                    your_locker = 0
                    your_locker_price = 0
def locker_cancle():
    global your_locker
    global print_your_locker
    global locker_list_box
    global your_locker_price
    your_locker = 0
    your_locker_price = 0
    your_locker_label.configure(text='')  # your_locker 가 내가 선택한 사물함 번호가 저장 됨


locker_cho = tk.Button(program, text='선택', command=locker_choise)
locker_cho.place(x=200, y=600)
locker_can = tk.Button(program, text='취소', command=locker_cancle)
locker_can.place(x=100, y=600)


# import datetime
# from datetime import timedelta  # 양윤성


def payment():  # 결제 창 띄우는 함수 programTk에서 결제 누르면 함수호출 / 하고
    global PN
    global locker_S_entry
    global locker_E_entry
    from datetime import datetime, timedelta

    if PN == '':
        login_plz = tk.Toplevel(program)
        login_plz.geometry('200x100+60+600')
        login_plz_label = tk.Label(login_plz, text='로그인후 이용할 수 있습니다.')
        login_plz_label.pack()

        def login_plz_withdraw_button():
            login_plz.withdraw()

        login_plz_withdraw = tk.Button(login_plz, text='닫기', command=login_plz_withdraw_button)
        login_plz_withdraw.pack()

    else:

        if len(locker_S_entry.get()) != 6:
            six_plz = tk.Toplevel(program)
            six_plz.geometry('200x100+60+600')
            six_plz_label = tk.Label(six_plz, text='날짜정보를 바르게 입력해주세요.')
            six_plz_label.pack()

            def six_plz_withdraw_button():
                six_plz.withdraw()

            six_plz_withdraw = tk.Button(six_plz, text='닫기', command=six_plz_withdraw_button)
            six_plz_withdraw.pack()
        elif len(locker_S_entry.get()) == 6:
            try:
                datetime.strptime(locker_S_entry.get(), '%y%m%d')
            except ValueError:
                not_date = tk.Toplevel(program)
                not_date.geometry('200x100+60+600')
                not_date_label = tk.Label(not_date, text='유효한 날짜를 입력해주세요.')
                not_date_label.pack()

                def not_date_withdraw_button():
                    not_date.withdraw()

                not_date_withdraw = tk.Button(not_date, text='닫기', command=not_date_withdraw_button)
                not_date_withdraw.pack()
            else:
                # https://jkim83.tistory.com/170
                pay_win = tk.Toplevel(program)
                pay_win.geometry("500x500+820+100")
                global pay_list
                pay_list = []
                global your_locker
                global locker_code
                global locker_day
                global your_locker_price
                global a
                a = []
                b = [0]
                c = -1
                d = 0
                for i in range(len(sell_code_list)):
                    if sell_code_list[i][0] in a: #a에 새로운 종목을 넣어주는 즉, 각기 다른 종목이 0,1,2,3으로 들어있겠다.
                        b[c + 1] += 1
                        pass
                    else:
                        a.append(sell_code_list[i][0])
                        b.append(1) #각 종목의 항목 갯수(개월수가 몇갠지 관한 내용)
                        c += 1
                for i in range(len(a)):
                    if globals()['RadioVariety_{}'.format(i)].get() == 0:
                        pay_list.append('00000000')
                        d += b[i]
                    else:
                        d += b[i]
                        pay_list.append(sell_code_list[d + globals()['RadioVariety_{}'.format(i)].get() - 1])
                print(pay_list)

                price = []
                for i in range(len(pay_list)):
                    price.append(int(pay_list[i][3:8]) * 1000)
                price.append(your_locker_price)
                total = sum(price)
                price_label = tk.Label(pay_win, text='총결제 금액은 %s원 입니다.' % (format(total, ',')))
                price_label.pack()

                def pay_complete():  # 결제 버튼 누르면 실행
                    global PN
                    global your_locker
                    global locker_day
                    global locker_list_box
                    global empty_button
                    global a
                    from datetime import datetime, timedelta
                    pay1_label = tk.Label(pay_win, text='결제 완료')
                    pay_button1.configure(state='disabled')
                    pay1_label.pack()
                    startday_list = []  # 운동 시작 날짜가 순서대로 들어가져 있음
                    endday_list = []  # 운동 끝 날짜가 순서대로 들어가져 있음
                    # pay_list 는 결제한 상품코드가 들어있음
                    for i in range(len(a)):
                        if len(globals()['Entry_{}'.format(i)].get()) != 6:  # 나중엔 이게 날짜가 아니면 또는 선택을 안했을 때 라고 바꿔줘야 할 듯
                            startday_list.append('000000')
                            print('여길로 들어갔는지 확인을 해보자')
                        else:
                            startday_list.append(globals()['Entry_{}'.format(i)].get())
                        print(globals()['Entry_{}'.format(i)].get())
                        print(startday_list)
                    startday_D = datetime.strptime(startday_list[i], "%y%m%d")  # 선택 문자날짜를 날짜형태로 변환
                    for i in range(len(a)):
                        if pay_list[i][1:3].isdigit():
                            endday_D = startday_D + timedelta(days=30 * int(pay_list[i][1:3]))  # startday_D 는 날짜형으로 바꾼것
                            endday_str = str(endday_D.date()).replace('-', '')
                            endday_list.append(endday_str[2:])
                        else:
                            endday_D = startday_D + timedelta(days=1)
                            endday_str = str(endday_D.date()).replace('-', '')
                            endday_list.append(endday_str[2:])

                    if your_locker < 10:
                        your_locker = '00' + str(your_locker)
                    elif your_locker < 100:
                        your_locker = '0' + str(your_locker)
                    elif your_locker < 1000:
                        your_locker = str(your_locker)
                    # 결제정보 회원에 업데이트(양윤성)

                    # locker_day[0] 사물함 시작 YYMMDD
                    # locker_day[1] 사물함 끝 YYMMDD
                    locker_day = []
                    if locker_S_entry.get() == '':
                        locker_day.append('000000')
                    else:
                        locker_day.append(locker_S_entry.get())
                    if locker_E_entry.get() == '':
                        locker_day.append('000000')
                    else:
                        locker_day.append(locker_E_entry.get())

                    # 이제 사람들 정보에 접근해서 수정해주면 끝!

                    old = open('member.txt', 'r', encoding='UTF-8')
                    old_list = old.readlines()
                    for i in range(len(old_list)):
                        old_list[i] = old_list[i].replace('\n', '')
                    for i in range(len(old_list)):
                        if PN == old_list[i][16:24]:
                            member_index = i
                            member_no = old_list[i][0:5]
                    first_line = old_list[0:member_index]
                    second_line = old_list[member_index]+'\n'
                    third_line = old_list[member_index + 1:]
                    add_info = ''
                    print('스타트데이 리스트', startday_list)
                    print('엔드데이 리스트', endday_list)
                    if your_locker=='000':
                        locker_day[0]='000000'
                        locker_day[1]='000000'
                    for o in range(len(pay_list)):
                        add_info += pay_list[o][0:3] + startday_list[o] + endday_list[o]
                    add_info += your_locker + locker_day[0] + locker_day[1]
                    second_line=second_line[0:24]+add_info+'\n'
                    # for i in range(len(pay_list)):
                    #     pay_list[i] == '0000000000'
                    #     startday_list[i] = '000000'
                    #     endday_list[i] = '000000'
                    # for i in range(len(real_line)):
                    #     if PN == real_line[i][16:24]:
                    #         member_no = real_line[i][0:5]
                    #     for o in range(len(pay_list)):
                    #         add_info += pay_list[o][0:3] + startday_list[o] + endday_list[o]
                    #     add_info += your_locker + locker_day[0] + locker_day[1]
                    #     real_line[i] = real_line[i][:24] + add_info
                    # old.close()
                    new = open('member.txt', 'w', encoding='UTF-8')
                    for i in range(len(first_line)):
                        new.write(first_line[i]+'\n')
                    new.write(second_line)
                    for i in range(len(third_line)):
                        new.write(third_line[i]+'\n')


                    # for i in range(len(real_line)):
                    #     new.write(real_line[i])
                    #     new.write('\n')
                    new.close()
                    # memeber.txt업데이트 완료

                    # locker.txt 에 업데이트 해야 함
                    locker_file = open('locker.txt', 'r', encoding='UTF=8')
                    locker_list = locker_file.readlines()
                    locker_file.close()
                    for i in range(len(locker_list)):
                        locker_list[i] = locker_list[i].replace('\n', '')
                    new_locker_txt = locker_list[0]
                    locker_list = locker_list[1:]
                    for i in range(len(locker_list)):
                        if your_locker == locker_list[i][0:3]:
                            locker_list[i] = your_locker + '2' + member_no + locker_day[0] + locker_day[1]  # 변경된 사물함 내역
                            # locker_file.close()
                    locker_file = open("locker.txt", 'w', encoding='UTF-8')
                    locker_file.write(new_locker_txt)
                    locker_file.write('\n')
                    for i in range(len(locker_list)):
                        locker_file.write(locker_list[i])
                        locker_file.write('\n')
                    locker_file.close()

                    # locker.txt 업데이트 완료 후

                    # locker_list_box업데이트 해야 함
                    try:
                        curselected = locker_list_box.curselection()[0]
                        locker_list_box.delete(curselected)
                        locker_file = open('locker.txt', 'r', encoding='UTF=8')
                        locker_list = locker_file.readlines()
                        locker_file.close()
                        locker_list = locker_list[1:]
                        insert_locker = ''
                        insert_locker += locker_list[int(your_locker) - 1][0:3]
                        if locker_list[int(your_locker) - 1][3] == '1':
                            insert_locker += '사용가능'
                        elif locker_list[int(your_locker) - 1][3] == '2':
                            insert_locker += '사용불가 ' + locker_list[int(your_locker) - 1][4:9] + '번 회원님이 사용중 ' + \
                                             locker_list[int(your_locker) - 1][15:17] + '년' + \
                                             locker_list[int(your_locker) - 1][17:19] + '월' + locker_list[
                                                                                                  int(your_locker) - 1][
                                                                                              19:21] + '일' + '만료예정'
                        elif locker_list[int(your_locker) - 1][3] == '3':
                            insert_locker += '사용불가'
                        if empty_button['state'] == tk.NORMAL:
                            locker_list_box.insert(curselected, insert_locker)
                    except:
                        pass

                    ##################################### #여기부터 결제정보에 추가

                    for i in range(len(old_list)):
                        if PN == old_list[i][16:24]:
                            mem_info = old_list[i]

                    from datetime import datetime, timedelta
                    today = datetime.now()
                    today_6digits = today.strftime('%y%m%d')

                    total_pay_list0 = []  # 헬스
                    total_pay_list1 = []  # 필라테스
                    total_pay_list2 = []  # 요가
                    total_pay_list3 = []  # 스ㅠㅣ
                    total_pay_list_box = []  # 사물

                    total_pay_list0.append(mem_info[0:5])
                    total_pay_list1.append(mem_info[0:5])
                    total_pay_list2.append(mem_info[0:5])
                    total_pay_list3.append(mem_info[0:5])
                    total_pay_list_box.append(mem_info[0:5])

                    total_pay_list0.append(mem_info[5:9])
                    total_pay_list1.append(mem_info[5:9])
                    total_pay_list2.append(mem_info[5:9])
                    total_pay_list3.append(mem_info[5:9])
                    total_pay_list_box.append(mem_info[5:9])

                    total_pay_list0.append('0')
                    total_pay_list1.append('1')
                    total_pay_list2.append('2')
                    total_pay_list3.append('3')
                    total_pay_list_box.append('-')

                    if your_locker == '':
                        total_pay_list0.append('x')
                        total_pay_list1.append('x')
                        total_pay_list2.append('x')
                        total_pay_list3.append('x')
                        total_pay_list_box.append('x')
                    else:
                        total_pay_list0.append('o')
                        total_pay_list1.append('o')
                        total_pay_list2.append('o')
                        total_pay_list3.append('o')
                        total_pay_list_box.append('o')

                    total_pay_list0.append(today_6digits)
                    total_pay_list1.append(today_6digits)
                    total_pay_list2.append(today_6digits)
                    total_pay_list3.append(today_6digits)
                    total_pay_list_box.append(today_6digits)

                    total_pay_list0.append(str(int(pay_list[0][3:8])))
                    total_pay_list1.append(str(int(pay_list[1][3:8])))
                    total_pay_list2.append(str(int(pay_list[2][3:8])))
                    total_pay_list3.append(str(int(pay_list[3][3:8])))
                    total_pay_list_box.append('5')

                    total_pay_list0.append(PayVariety.get())
                    total_pay_list1.append(PayVariety.get())
                    total_pay_list2.append(PayVariety.get())
                    total_pay_list3.append(PayVariety.get())
                    total_pay_list_box.append(PayVariety.get())

                    files = open('결제정보.txt', 'r', encoding='UTF=8')
                    files.close()
                    # 결제정보 리스트 문자열로 변환
                    a0 = ''.join(map(str, total_pay_list0))
                    a1 = ''.join(map(str, total_pay_list1))
                    a2 = ''.join(map(str, total_pay_list2))
                    a3 = ''.join(map(str, total_pay_list3))
                    abox = ''.join(map(str, total_pay_list_box))
                    mem_info_list = ''.join(map(str, mem_info))  # 회원정보를 하나의 문자열로 합침
                    if pay_list[0] == '00000000':
                        pass
                    else:
                        if total_pay_list0[2] == '0':  # 헬스
                            if len(a0[17:]) == 3:  # 만원대->00
                                # 회원정보+변경된 이용권 내역 ->로그인한 회원 정보(회원번호+이름) + 결제정보(운동1~4/일자/금액/현금,카드)
                                b0 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a0[9] + '\t' + a0[
                                    10] + '\t' + a0[11:17] + '\t' + '000' + a0[17:19] + '\t' + a0[19]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(b0)
                                    f.write('\n')
                                files.close()
                            elif len(a0[17:]) == 4:  # 십만원대->000
                                c0 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a0[9] + '\t' + a0[
                                    10] + '\t' + a0[11:17] + '\t' + '00' + a0[17:20] + '\t' + a0[20]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(c0)
                                    f.write('\n')
                                files.close()
                            elif len(a0[17:]) == 5:  # 백만원대->0000
                                d0 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a0[9] + '\t' + a0[
                                    10] + '\t' + a0[11:17] + '\t' + '0' + a0[17:21] + '\t' + a0[21]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(d0)
                                    f.write('\n')
                                files.close()
                            elif len(a0[17:]) == 6:  # 천만원대->00000
                                e0 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a0[9] + '\t' + a0[
                                    10] + '\t' + a0[11:17] + '\t' + a0[17:22] + '\t' + a0[22]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(e0)
                                    f.write('\n')
                                files.close()
                    if pay_list[1] == '00000000':
                        pass
                    else:
                        if total_pay_list1[2] == '1':

                            if len(a1[17:]) == 3:  # 만원대->00
                                # 회원정보+변경된 이용권 내역 ->로그인한 회원 정보(회원번호+이름) + 결제정보(운동1~4/일자/금액/현금,카드)
                                b1 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a1[9] + '\t' + a1[
                                    10] + '\t' + a1[11:17] + '\t' + '000' + a1[17:19] + '\t' + a1[19]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(b1)
                                    f.write('\n')
                                files.close()
                            elif len(a1[17:]) == 4:  # 십만원대->000
                                c1 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a1[9] + '\t' + a1[
                                    10] + '\t' + a1[11:17] + '\t' + '00' + a1[17:20] + '\t' + a1[20]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(c1)
                                    f.write('\n')
                                files.close()
                            elif len(a1[17:]) == 5:  # 백만원대->0000
                                d1 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a1[9] + '\t' + a1[
                                    10] + '\t' + a1[11:17] + '\t' + '0' + a1[17:21] + '\t' + a1[21]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(d1)
                                    f.write('\n')
                                files.close()
                            elif len(a1[17:]) == 6:  # 천만원대->00000
                                e1 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a1[9] + '\t' + a1[
                                    10] + '\t' + a1[11:17] + '\t' + i[17:22] + '\t' + a1[22]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(e1)
                                    f.write('\n')
                                files.close()
                    if pay_list[2] == '00000000':
                        pass
                    else:
                        if total_pay_list2[2] == '2':
                            if len(a2[17:]) == 3:  # 만원대->00
                                # 회원정보+변경된 이용권 내역 ->로그인한 회원 정보(회원번호+이름) + 결제정보(운동1~4/일자/금액/현금,카드)
                                b2 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a2[9] + '\t' + a2[
                                    10] + '\t' + a2[11:17] + '\t' + '000' + a2[17:19] + '\t' + a2[19]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(b2)
                                    f.write('\n')
                                files.close()
                            elif len(a2[17:]) == 4:  # 십만원대->000
                                c2 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a2[9] + '\t' + a2[
                                    10] + '\t' + a2[11:17] + '\t' + '00' + a2[17:20] + '\t' + a2[20]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(c2)
                                    f.write('\n')
                                files.close()
                            elif len(a2[17:]) == 5:  # 백만원대->0000
                                d2 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a2[9] + '\t' + a2[
                                    10] + '\t' + a2[11:17] + '\t' + '0' + a2[17:21] + '\t' + a2[21]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(d2)
                                    f.write('\n')
                                files.close()
                            elif len(a2[17:]) == 6:  # 천만원대->00000
                                e2 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a2[9] + '\t' + a2[
                                    10] + '\t' + a2[11:17] + '\t' + a2[17:22] + '\t' + a2[22]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(e2)
                                    f.write('\n')
                                files.close()
                    if pay_list[3] == '00000000':
                        pass
                    else:
                        if total_pay_list3[2] == '3':
                            if len(a3[17:]) == 3:  # 만원대->00
                                # 회원정보+변경된 이용권 내역 ->로그인한 회원 정보(회원번호+이름) + 결제정보(운동1~4/일자/금액/현금,카드)
                                b3 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a3[9] + '\t' + a3[
                                    10] + '\t' + a3[11:17] + '\t' + '000' + a3[17:19] + '\t' + a3[19]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(b3)
                                    f.write('\n')
                                files.close()
                            elif len(a3[17:]) == 4:  # 십만원대->000
                                c3 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a3[9] + '\t' + a3[
                                    10] + '\t' + a3[11:17] + '\t' + '00' + a3[17:20] + '\t' + a3[20]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(c3)
                                    f.write('\n')
                                files.close()
                            elif len(a3[17:]) == 5:  # 백만원대->0000
                                d3 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a3[9] + '\t' + a3[
                                    10] + '\t' + a3[11:17] + '\t' + '0' + a3[17:21] + '\t' + a3[21]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(d3)
                                    f.write('\n')
                                files.close()
                            elif len(a3[17:]) == 6:  # 천만원대->00000
                                e3 = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + a3[9] + '\t' + a3[
                                    10] + '\t' + a3[11:17] + '\t' + a3[17:22] + '\t' + a3[22]
                                with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                    f.write(e3)
                                    f.write('\n')
                                files.close()
                    if your_locker == 0:
                        pass
                    else:
                        if total_pay_list_box[1] == 'o':
                            abox_list = mem_info_list[:5] + '\t' + mem_info_list[5:9] + '\t' + abox[9] + '\t' + abox[
                                10] + '\t' + abox[11:17] + '\t' + '00005' + '\t' + abox[18]
                            with open('결제정보.txt', 'a', encoding='UTF=8') as f:
                                f.write(abox_list)
                                f.write('\n')
                            files.close()

                    # 여기까지 결제정보 추가

                PayVariety = tk.IntVar()
                PayVariety.set('2')
                pay_how1 = tk.Radiobutton(pay_win, text='현금', value='1', variable=PayVariety)
                pay_how2 = tk.Radiobutton(pay_win, text='카드', value='2', variable=PayVariety)
                pay_how1.pack()
                pay_how2.pack()
                pay_button1 = tk.Button(pay_win, text='결제', command=pay_complete)
                pay_button1.pack()

                def pay_win_withdraw():
                    pay_win.withdraw()

                pay_button2 = tk.Button(pay_win, text='닫기', command=pay_win_withdraw)
                pay_button2.pack()


paynow = tk.Button(program, text='결제', command=payment)
paynow.place(x=150, y=625)

manager_no = 'ironman'
manager_Label = tk.Label(program, text='패스워드를 입력하세요.')
manager_Label.place(x=960, y=50)
manager_Entry = tk.Entry(program)
manager_Entry.place(x=960, y=75)


def manager_login():
    global manager_no
    global manager_Entry
    if manager_Entry.get() == manager_no:
        manager_win = tk.Toplevel(program)
        manager_win.title('oo헬스 관리자')
        manager_win.geometry('1920x1080+0+0')
        member_label = tk.Label(manager_win, text='회원관리')
        member_label.place(x=0, y=150)
        member_list_label = tk.Label(manager_win, text='NO    이름  성별  생년월일     전화번호')
        member_list_label.place(x=0, y=175)
        member_list_box = tk.Listbox(manager_win, selectmode='single', width=50)
        membergroup = open('member.txt', 'r', encoding='UTF-8')
        member = membergroup.readlines()
        member_list = member[1:]
        membergroup.close()
        for i in range(len(member_list)):
            insert_member = ''
            insert_member += member_list[i][0:5] + ' '
            insert_member += member_list[i][5:9].replace('x', '   ')
            if member_list[i][9:10] == '1':
                insert_member += ' 남'
            elif member_list[i][9:10] == '2':
                insert_member += ' 여'
            insert_member += '  ' + member_list[i][10:16]
            insert_member += '      010-' + member_list[i][16:20] + '-' + member_list[i][20:24]
            member_list_box.insert(i, insert_member)
            member_list_box.place(x=0, y=200)

        def who_member():
            member_info_win = tk.Toplevel(manager_win)
            member_info_win.title('회원정보')
            member_info_win.geometry('500x300+0+400')
            index_member = int(member_list_box.get(member_list_box.curselection()[0])[0:5]) - 1  # 고른사람 인덱스번호 가져오기
            choose_member_info = member_list[index_member]  # 고른 사람의 정보만 빼온 리스트의 한 인덱스
            num1_label = tk.Label(member_info_win, text=choose_member_info[0:5])
            num1_label.place(x=25, y=0)

            name1_label = tk.Label(member_info_win, text='이름')
            name1_label.place(x=25, y=25)
            name1_ent = tk.Entry(member_info_win)
            name1_ent.place(x=100, y=25)
            name1_ent.insert(0, choose_member_info[5:9].replace('x', ''))

            gender1_label = tk.Label(member_info_win, text='성별')
            gender1_label.place(x=25, y=50)
            gender1_entry = tk.Entry(member_info_win)
            gender1_entry.place(x=100, y=50)
            gender1_entry.insert(0, choose_member_info[9:10])

            birth1_label = tk.Label(member_info_win, text='생년월일')
            birth1_label.place(x=25, y=75)
            birth1_ent = tk.Entry(member_info_win)
            birth1_ent.place(x=100, y=75)
            birth1_ent.insert(0, choose_member_info[10:16])

            phone1_label = tk.Label(member_info_win, text='전화번호')
            phone1_label.place(x=25, y=100)
            phone1_ent = tk.Entry(member_info_win)
            phone1_ent.place(x=100, y=100)
            phone1_ent.insert(0, choose_member_info[16:24])

            my_program_label = tk.Label(member_info_win, text='내 회원권 목록')
            my_program_label.place(x=25, y=125)
            my_program_list_label = tk.Label(member_info_win, text='이용권     시작날짜 종료날짜')
            my_program_list_label.place(x=25, y=150)
            my_program_list = tk.Listbox(member_info_win, selectmode='single')
            my_program_list.place(x=25, y=175, height=100, width=250)
            print(code_name)
            for i in range(4):
                insert_program = ''
                insert_program += code_name[int(choose_member_info[24 + (i * 15):25 + (i * 15)])]
                if choose_member_info[25 + (i * 15):27 + (i * 15)].isdigit():
                    insert_program += choose_member_info[25 + (i * 15):27 + (i * 15)] + '개월'
                else:
                    insert_program += '일일권'
                insert_program += ' ' + choose_member_info[27 + (i * 15):33 + (i * 15)]
                insert_program += ' ' + choose_member_info[33 + (i * 15):39 + (i * 15)]
                my_program_list.insert(i, insert_program)

        who_member_button = tk.Button(manager_win, text='선택', command=who_member)
        who_member_button.place(x=318, y=375)

        trainer_label = tk.Label(manager_win, text='강사관리')
        trainer_label.place(x=480, y=150)
        trainer_list_label = tk.Label(manager_win, text='NO   이름  성별  생년월일     전화번호             담당분야')
        trainer_list_label.place(x=480, y=175)
        trainer_list_box = tk.Listbox(manager_win, selectmode='single', width=50)
        trainergroup = open('trainer.txt', 'r', encoding='UTF-8')
        trainer = trainergroup.readlines()
        trainer_list = trainer[1:]
        trainergroup.close()
        for i in range(len(trainer_list)):
            insert_trainer = ''
            insert_trainer += trainer_list[i][0:3] + ' '
            insert_trainer += trainer_list[i][3:7].replace('x', '   ')
            if trainer_list[i][7:8] == '1':
                insert_trainer += ' 남'
            elif trainer_list[i][7:8] == '2':
                insert_trainer += ' 여'
            insert_trainer += '  ' + trainer_list[i][8:14]
            insert_trainer += '      010-' + trainer_list[i][14:18] + '-' + trainer_list[i][18:22]
            if trainer_list[i][23:24] == '0':
                insert_trainer += '  기타'
            elif trainer_list[i][22:23] == '1':
                insert_trainer += '  필라테스'
            elif trainer_list[i][22:23] == '2':
                insert_trainer += '  요가'
            elif trainer_list[i][22:23] == '3':
                insert_trainer += '  스피닝'
            elif trainer_list[i][22:23] == '4':
                insert_trainer += '  PT'

            trainer_list_box.insert(i, insert_trainer)
            trainer_list_box.place(x=480, y=200)

            def who_trainer():
                global sell_code_list
                global choose_trainer_info
                global name2_ent
                global GenderVariety_1
                #################
                trainer_info_win = tk.Toplevel(manager_win)
                trainer_info_win.title('강사정보')
                trainer_info_win.geometry('500x300+0+400')
                index_trainer = int(trainer_list_box.get(trainer_list_box.curselection()[0])[0:3]) - 1  # 고른사람 인덱스번호 가져오기
                choose_trainer_info = trainer_list[index_trainer]  # 고른 사람의 정보만 빼온 리스트의 한 인덱스

                num2_label = tk.Label(trainer_info_win, text=choose_trainer_info[0:3])
                num2_label.place(x=25, y=0)

                name2_label = tk.Label(trainer_info_win, text='이름')
                name2_label.place(x=25, y=25)
                name2_ent = tk.Entry(trainer_info_win)
                name2_ent.place(x=100, y=25)
                name2_ent.insert(0, choose_trainer_info[3:7].replace('x', ''))

                gender2_label = tk.Label(trainer_info_win, text='성별')
                gender2_label.place(x=25, y=50)
                GenderVariety_1 = tk.IntVar()
                gender3_Radiobutton = tk.Radiobutton(trainer_info_win, text='남', value='1', variable=GenderVariety_1)
                gender4_Radiobutton = tk.Radiobutton(trainer_info_win, text='여', value='2', variable=GenderVariety_1)
                gender3_Radiobutton.place(x=100, y=50)
                gender4_Radiobutton.place(x=150, y=50)

                birth2_label = tk.Label(trainer_info_win, text='생년월일')
                birth2_label.place(x=25, y=75)
                birth2_ent = tk.Entry(trainer_info_win)
                birth2_ent.place(x=100, y=75)
                birth2_ent.insert(0, choose_trainer_info[8:14])

                phone2_label = tk.Label(trainer_info_win, text='전화번호')
                phone2_label.place(x=25, y=100)
                phone2_ent = tk.Entry(trainer_info_win)
                phone2_ent.place(x=100, y=100)
                phone2_ent.insert(0, choose_trainer_info[14:22])

                my_program1_label = tk.Label(trainer_info_win, text='담당분야')
                my_program1_label.place(x=25, y=125)
                myProVariety=tk.IntVar()
                for i in range(len(code_name)):
                    globals()['my_program_{}'.format(i)] = tk.Radiobutton(trainer_info_win, value=i,variable=myProVariety)
                    globals()['my_program_{}'.format(i)].place(x=25+(i*100), y=200)
                    globals()['my_pro_label_{}'.format(i)]=tk.Label(trainer_info_win,text=code_name[i])
                    globals()['my_pro_label_{}'.format(i)].place(x=25+(i*100),y=175)
                myProVariety.set(choose_trainer_info[22:23])

                if choose_trainer_info[22:23] == '0':
                    myPro = '헬스'
                elif choose_trainer_info[22:23] == '1':
                    myPro = '필라테스'
                elif choose_trainer_info[22:23] == '2':
                    myPro = '요가'
                elif choose_trainer_info[22:23] == '3':
                    myPro = '스피닝'
                elif choose_trainer_info[22:23] == '4':
                    myPro='PT'
                else:
                    myPro = '기타'
                my_program_ent=tk.Label(trainer_info_win,text=myPro)
                my_program_ent.place(x=25,y=150)
                def trainer_info_withdraw():
                    trainer_info_win.withdraw()
                trainer_info_withdraw_button=tk.Button(trainer_info_win,text='닫기',command=trainer_info_withdraw)
                trainer_info_withdraw_button.place(x=25,y=225)

                #################################################수정 하는 중####################

                def trainer_info_save():
                    global name2_ent
                    global GenderVariety_1

                    file_read = open('trainer.txt', 'r', encoding='UTF-8')
                    a = file_read.readlines()
                    print('a',a)
                    print('chosse_tra..',choose_trainer_info)


                    file_read.close()
##################### choose_trainer_info[0:3]#############################################
                    cristal=''
                    cristal+=choose_trainer_info[0:3]
                    choice_index=int(choose_trainer_info[0:3])
                    first_a=a[0:choice_index]
                    second_a=a[choice_index+1:]
                    sc_list=[]
                    only_num = []
                    only_gender = []
                    only_birth = []
                    only_phonenum = []
                    only_work = []
                    for i in a[1:]:
                        num = i[0:3]
                        only_num.append(num)
                    for i in a[1:]:
                        gender = i[7:8]
                        only_gender.append(gender)
                    for i in a[1:]:
                        birth = i[8:14]
                        only_birth.append(birth)
                    for i in a[1:]:
                        pn = i[14:22]
                        only_phonenum.append(pn)
                    for i in a[1:]:
                        work = i[22]
                        only_work.append(work)

                    # print(only_num) #선생 고유번호
                    # print(only_gender) #선생 성별
                    # print(only_birth) #선생 생년월일
                    # print(only_phonenum) #선생 휴대폰번호
                    # print(only_work) #선생 업무

                    except_x = []  # 선생 이름
                    teacher_names_list = []
                    temp_list = []
                    se_na_loca = []






                    for m in range(len(a)):
                        x = a[m].split('\t')
                        for i in range(len(x)):
                            if x[i] and x[i] != '\n':
                                sc_list.append(x[i])
                        for i in range(len(sc_list)):
                            if '\n' in sc_list[i]:
                                sc_list[i] = sc_list[i].replace('\n', '')
                                if '-' in sc_list[i]:
                                    sc_list[i] = sc_list[i].replace('-', '0')

                    for i in a[1:]:  # 선생들 이름만 추출하는 for문
                        teacher_names = i[3:7]
                        teacher_names_list.append(teacher_names)
                    for i in teacher_names_list:
                        aa = i.replace('x', '')
                        except_x.append(aa)

                    if len(name2_ent.get())==4:
                        search_name = name2_ent.get()
                    elif len(name2_ent.get())==3:
                        search_name = 'x'+name2_ent.get()
                    elif len(name2_ent.get())==2:
                        search_name = 'xx'+name2_ent.get()
                    else:
                        search_name = '0000'
                    cristal+=search_name
                    ####################################################################
                    cristal+=str(GenderVariety_1.get())
                    cristal+=birth2_ent.get()
                    x = []
                    temp_list = []
                    if len(search_name) == 4:  # 강사이름이 4글자 일때
                        if search_name in teacher_names_list:
                            search_name_location = teacher_names_list.index(search_name)
                            for i in range(len(except_x)):
                                if search_name in except_x[i]:
                                    temp_list.append(search_name)
                            # print(temp_list) #동명이인 몇 명있는지 리스트 출력
                            count_sameman = int(len(temp_list))  # (int)동명이인수
                            for i in range(len(except_x)):
                                if search_name == except_x[i]:
                                    x.append(a[i + 1].replace('\n', ''))
###############################################################################들여쓰기
                    str_pn = phone2_ent.get().replace('\n','')
                    cristal+=str_pn
                    print('폰넘버추가 후',cristal)
####################################################들여쓰기 맞춰주기
                    str_wo = myProVariety.get()
                    cristal+=str(str_wo)
                    cristal+='\n'
                    print('특기추가 후', cristal)

                    text = open('trainer.txt', 'w', encoding='utf-8')
                    print('firsta',first_a)
                    print('cristal',cristal)
                    print('secon_a',second_a)
                    for i in range(len(first_a)):
                        text.write(first_a[i])
                    text.write(cristal)
                    for i in range(len(second_a)):
                        text.write(second_a[i])
                    text.close()
                    who_del = myProVariety.get()
                    x=code_name
                    a=sell_code_list
                    for i in range(len(teacher_names_list)):
                        if x[0] in a[0]:
                            only_phonenum[i] = str_pn
                            only_work[i] = str_wo
                    for x in range(len(teacher_names_list)):
                        edit_teacher_info='aa'
                        pass
                    if edit_teacher_info == 2:
                        who_del = name2_ent
                        text = open('강사정보.txt', 'w', encoding='utf-8')
                        for i in a:
                            if x[who_del - 1] in i:
                                del i
                                continue
                        text.close()

                    else:
                        print('검색한 강사가 존재하지 않습니다.')

                    if len(search_name) == 3:  # 강사이름이 3글자 일때
                        search_name = 'x' + search_name
                        if search_name in teacher_names_list:
                            search_name_location = teacher_names_list.index(search_name)
                            for i in range(len(except_x)):
                                if search_name.replace('x', '') in except_x[i]:
                                    temp_list.append(search_name)
                            count_sameman = int(len(temp_list))  # (int)동명이인수
                            for i in range(len(except_x)):
                                if search_name.replace('x', '') == except_x[i]:
                                    x.append(a[i + 1].replace('\n', ''))
                            for i in range(len(x)):
                                print('%s.' % (i + 1) + x[i])

                                if edit_teacher_info == 1:
                                    text = open('강사정보.txt', 'r', encoding='utf-8')
                                    for i in range(len(teacher_names_list)):
                                        if x[who_del - 1] in a[i + 1]:
                                            only_phonenum[i] = str_pn
                                            only_work[i] = str_wo
                                    for x in range(len(teacher_names_list)):
                                        text.write(
                                            only_num[x] + teacher_names_list[x] + only_gender[x] + only_birth[x] +
                                            only_phonenum[x] +
                                            only_work[x] + '\n')
                                    text.close()

                                elif int(edit_teacher_info) == 2:
                                    text = open('강사정보.txt', 'r', encoding='utf-8')
                                    for i in a:
                                        if x[who_del - 1] in i:
                                            del i
                                            continue
                                    text.close()
                    elif len(search_name) == 2:  # 강사이름이 2글자 일때
                        search_name = 'xx' + search_name
                        if search_name in teacher_names_list:
                            search_name_location = teacher_names_list.index(search_name)
                            for i in range(len(except_x)):
                                if search_name.replace('xx', '') in except_x[i]:
                                    temp_list.append(search_name)
                            count_sameman = int(len(temp_list))
                            for i in range(len(except_x)):
                                if search_name.replace('x', '') == except_x[i]:
                                    x.append(a[i + 1].replace('\n', ''))
                            for i in range(len(x)):
                                print('%s.' % (i + 1) + x[i])
                            text = open('강사정보.txt', 'r', encoding='utf-8')
                            for i in range(len(teacher_names_list)):
                                if x[who_del - 1] in a[i + 1]:
                                    only_phonenum[i] = str_pn
                                    only_work[i] = str_wo
                            for x in range(len(teacher_names_list)):
                                pass
                            text.close()

                        elif edit_teacher_info == 2:
                            text = open('강사정보.txt', 'r', encoding='utf-8')
                            for i in a:
                                if x[who_del - 1] in i:
                                    del i
                                    continue
                            text.close()



                    #############################################################################################################################################
###############################여기까지






                trainer_info_save_button=tk.Button(trainer_info_win,text='저장',command=trainer_info_save)
                trainer_info_save_button.place(x=100,y=225)

########################################################myPro에 대해서 자세학 ㅔ알아보자
            def add_trainer():
                global name2_ent
                global GenderVariety_1
                global birth2_ent
                global phone2_ent
                global myProVariety
                add_trainer_info_win = tk.Toplevel(manager_win)
                add_trainer_info_win.title('신입강사')
                add_trainer_info_win.geometry('500x300+480+400')
                num2_label = tk.Label(add_trainer_info_win, text='추가되는 회원번호 적어줘야 할 듯')
                num2_label.place(x=25, y=0)

                name2_label = tk.Label(add_trainer_info_win, text='이름')
                name2_label.place(x=25, y=25)
                name2_ent = tk.Entry(add_trainer_info_win)
                name2_ent.place(x=100, y=25)


                gender2_label = tk.Label(add_trainer_info_win, text='성별')
                gender2_label.place(x=25, y=50)
                GenderVariety_1 = tk.IntVar()
                gender3_Radiobutton = tk.Radiobutton(add_trainer_info_win, text='남', value='1', variable=GenderVariety_1)
                gender4_Radiobutton = tk.Radiobutton(add_trainer_info_win, text='여', value='2', variable=GenderVariety_1)
                gender3_Radiobutton.place(x=100, y=50)
                gender4_Radiobutton.place(x=150, y=50)

                birth2_label = tk.Label(add_trainer_info_win, text='생년월일')
                birth2_label.place(x=25, y=75)
                birth2_ent = tk.Entry(add_trainer_info_win)
                birth2_ent.place(x=100, y=75)


                phone2_label = tk.Label(add_trainer_info_win, text='전화번호')
                phone2_label.place(x=25, y=100)
                phone2_ent = tk.Entry(add_trainer_info_win)
                phone2_ent.place(x=100, y=100)

                ###
                my_program1_label = tk.Label(add_trainer_info_win, text='담당분야')
                my_program1_label.place(x=25, y=125)
                myProVariety = tk.IntVar()
                for i in range(len(code_name)):
                    globals()['my_program_{}'.format(i)] = tk.Radiobutton(add_trainer_info_win, value=i,variable=myProVariety)
                    globals()['my_program_{}'.format(i)].place(x=25 + (i * 100), y=200)
                    globals()['my_pro_label_{}'.format(i)] = tk.Label(add_trainer_info_win, text=code_name[i])
                    globals()['my_pro_label_{}'.format(i)].place(x=25 + (i * 100), y=175)

                def add_cancle():
                    add_trainer_info_win.withdraw()
                def add_complete():
                    global name2_ent
                    global GenderVariety_1
                    global birth2_ent
                    global phone2_ent
                    global myProVariety

                    add_trainer_text=''
                    #강사번호 추가 먼저
                    file_read = open('trainer.txt', 'r', encoding='UTF-8')
                    trainer_list= file_read.readlines()
                    file_read.close()
                    add_trainer_num=int(trainer_list[-1][0:3])+1
                    if int(add_trainer_num)<10:
                        trainercode='00'+str(add_trainer_num)
                    elif int(add_trainer_num)<100:
                        trainercode='0'+str(add_trainer_num)
                    elif int(add_trainer_num)<1000:
                        trainercode=str(add_trainer_num)
                    else:
                        trainercode='000'
                    add_trainer_text+=trainercode

                    if len(name2_ent.get()) == 4:  # 이름 자리 수에 따른 상황별 입력 4자리면 pass, 3자리면 N신태용, 2자리면 NN태용
                        teacher_name=name2_ent.get()

                    elif len(name2_ent.get()) == 3:  # 이름이 3자리일 경우
                        teacher_name = 'x'+name2_ent.get()  # 이름이 3자리 일때 한 자리 추가

                    elif len(name2_ent.get()) == 2:  # 이름이 2자리일 경우
                        teacher_name = 'xx'+name2_ent.get()
                    else:
                        teacher_name='아무거나'

                    add_trainer_text+=teacher_name  #이름 더하기
                    add_trainer_text+=str(GenderVariety_1.get())  #성별 더하기
                    add_trainer_text+=birth2_ent.get() #생년월일 더하기
                    add_trainer_text+=phone2_ent.get() #전화번호 더하기
                    add_trainer_text+=str(myProVariety.get())
                    add_trainer_text+='\n'
                    file_add = open('trainer.txt', 'a', encoding='UTF-8')
                    file_add.write(add_trainer_text)
                    file_add.close()
                    add_trainer_complete=tk.Toplevel(add_trainer_info_win)
                    add_trainer_complete_label=tk.Label(add_trainer_complete,text='저장이 완료 되었습니다.')
                    add_trainer_complete_label.pack()
                    def add_trainer_complete_OK():
                        add_trainer_complete.withdraw()
                        add_trainer_info_win.withdraw()
                        global trainer_list_box

                        insert_trainer = ''
                        insert_trainer += add_trainer_text[0:3] + ' '
                        insert_trainer += add_trainer_text[3:7].replace('x', '   ')
                        if trainer_list[i][7:8] == '1':
                            insert_trainer += ' 남'
                        elif trainer_list[i][7:8] == '2':
                            insert_trainer += ' 여'
                        insert_trainer += '  ' + add_trainer_text[8:14]
                        insert_trainer += '      010-' + add_trainer_text[14:18] + '-' + add_trainer_text[18:22]
                        if add_trainer_text[23:24] == '0':
                            insert_trainer += '  기타'
                        elif add_trainer_text[22:23] == '1':
                            insert_trainer += '  필라테스'
                        elif add_trainer_text[22:23] == '2':
                            insert_trainer += '  요가'
                        elif add_trainer_text[22:23] == '3':
                            insert_trainer += '  스피닝'
                        elif add_trainer_text[22:23] == '4':
                            insert_trainer += '  PT'



                    addtrainer_complete_button=tk.Button(add_trainer_complete,text='확인',command=add_trainer_complete_OK)
                    addtrainer_complete_button.pack()
                add_complete_button=tk.Button(add_trainer_info_win,text='저장',command=add_complete)
                add_complete_button.place(x=125,y=250)
                add_cancle_button=tk.Button(add_trainer_info_win,text='닫기',command=add_cancle)
                add_cancle_button.place(x=25,y=250)


            add_trainer_button = tk.Button(manager_win, text='추가', command=add_trainer)
            add_trainer_button.place(x=700, y=375)
            who_trainer_button = tk.Button(manager_win, text='선택', command=who_trainer)
            who_trainer_button.place(x=800, y=375)

        sales = open('결제정보.txt', 'r', encoding='UTF-8')
        sale = sales.readlines()
        sales.close()
        sales_label=tk.Label(manager_win,text='매출관리')
        sales_label.place(x=960,y=150)
        sales_list_box=tk.Listbox(manager_win,selectmode='single', width=50)
        sale=sale[1:-1]
        print('sale',sale)
        for i in range(len(sale)):
            sale[i]=sale[i].replace('\n','')
            sale[i]=sale[i].split('\t')
        for i in range(len(sale)):
            add_sales=''
            add_sales+=sale[i][0]
            add_sales+=sale[i][1].replace('x',' ')
            if sale[i][2]=='0':
                add_sales+='   헬스        '
            elif sale[i][2]=='1':
                add_sales+='   필라테스  '
            elif sale[i][2]=='2':
                add_sales+='   요가        '
            elif sale[i][2]=='3':
                add_sales+='   스피닝     '
            elif sale[i][2]=='-':
                add_sales+='   사물함     '
            add_sales+=sale[i][3]
            add_sales+='   '+sale[i][4]
            add_sales+='   '+str(format((int(sale[i][5])*1000),','))+'원'
            if sale[i][6]=='1':
                add_sales+='(현금)'
            elif sale[i][6]=='2':
                add_sales+='(카드)'
            elif sale[i][6]=='3':
                add_sales+='(환불)'
            elif sale[i][6]=='4':
                add_sales+='(양도)'
                #사물함 여부랑, 결제 날짜,결제금액, 결제종류(카드,현금,환불)
            sales_list_box.insert(i,add_sales)
            print('addsales는',add_sales)
        sales_list_box.place(x=960,y=200)

        def search():
            try:
                datetime.strptime(start_entry.get(), '%y%m%d')
                datetime.strptime(end_entry.get(), '%y%m%d')
            except ValueError:
                not_date1 = tk.Toplevel(manager_win)
                not_date1.geometry('200x100')
                not_date1_label = tk.Label(not_date1, text='유효한 날짜를 입력해주세요.')
                not_date1_label.pack()
                def not_date1_withdraw():
                    not_date1.withdraw()
                not_date1_withdraw_button = tk.Button(not_date1, text='닫기', command=not_date1_withdraw)
                not_date1_withdraw_button.pack()
            else:
                sales_list_box.delete(0, END)
                for i in range(len(sale)):
                    print(start_entry.get())
                    # search_start_day = datetime.strptime(start_entry.get())
                    # search_day=datetime.strptime(sale[i][4])
                    # search_end_day = datetime.strptime(end_entry.get())
                    if start_entry.get()<=sale[i][4]<=end_entry.get():
                        add_sales = ''
                        add_sales += sale[i][0]
                        add_sales += sale[i][1].replace('x', ' ')
                        if sale[i][2] == '0':
                            add_sales += '   헬스        '
                        elif sale[i][2] == '1':
                            add_sales += '   필라테스  '
                        elif sale[i][2] == '2':
                            add_sales += '   요가        '
                        elif sale[i][2] == '3':
                            add_sales += '   스피닝     '
                        elif sale[i][2] == '-':
                            add_sales += '   사물함     '
                        add_sales += sale[i][3]
                        add_sales += '   ' + sale[i][4]
                        add_sales += '   ' + str(format((int(sale[i][5]) * 1000), ',')) + '원'
                        if sale[i][6] == '1':
                            add_sales += '(현금)'
                        elif sale[i][6] == '2':
                            add_sales += '(카드)'
                        elif sale[i][6] == '3':
                            add_sales += '(환불)'
                        elif sale[i][6] == '4':
                            add_sales += '(양도)'
                            # 사물함 여부랑, 결제 날짜,결제금액, 결제종류(카드,현금,환불)
                        sales_list_box.insert(i, add_sales)




        start_label=tk.Label(manager_win,text='시작 날짜')
        start_label.place(x=960,y=375)
        end_label=tk.Label(manager_win,text='끝 날짜')
        end_label.place(x=1050,y=375)
        start_entry=tk.Entry(manager_win,width=10)
        start_entry.place(x=960,y=400)
        end_entry=tk.Entry(manager_win,width=10)
        end_entry.place(x=1050,y=400)

        search_button=tk.Button(manager_win,text='검색',command=search)
        search_button.place(x=1150,y=400)




        locker_file = open('locker.txt', 'r', encoding='UTF-8')
        locker_list = locker_file.readlines()
        locker_list = locker_list[1:]
        locker_list_label = tk.Label(manager_win, text='사물함 관리')
        locker_list_label.place(x=1440, y=175)

        locker_list_box = tk.Listbox(manager_win, selectmode='single', width=50)
        for i in range(len(locker_list)):
            insert_locker = ''
            insert_locker += locker_list[i][0:3]
            if locker_list[i][3] == '1':
                insert_locker += '사용가능'
            elif locker_list[i][3] == '2':
                insert_locker += '사용불가 ' + locker_list[i][4:9] + '번 회원님이 사용중 ' + locker_list[i][15:17] + '년' + \
                                 locker_list[i][17:19] + '월' + locker_list[i][19:21] + '일' + '만료예정'
            elif locker_list[i][3] == '3':
                insert_locker += '사용불가'
            locker_list_box.insert(i, insert_locker)
        locker_list_box.place(x=1440, y=200)
        which_locker_button = tk.Button(manager_win, text='선택')
        which_locker_button.place(x=1770, y=375)



    else:
        manager_login_error = tk.Toplevel(program)
        manager_login_error.geometry('200x100+1075+50')
        login_fail_label = tk.Label(manager_login_error, text='패스워드가 일치하지 않습니다.')
        login_fail_label.pack()

        def with1():
            manager_login_error.withdraw()

        manager_login_error_withdraw = tk.Button(manager_login_error, text='닫기', command=with1, width=10)
        manager_login_error_withdraw.pack()


manager_button = tk.Button(program, text='관리자 로그인', command=manager_login)
manager_button.place(x=1125, y=75)

program.mainloop()
# program1.mainloop()