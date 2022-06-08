import os
import time

def mvp_cut():
    file = open('MVP.txt', 'r', encoding='utf-8')
    mvp_text= file.readlines()
    file.close()
    mvp_list=[]
    for i in mvp_text:
        mvp_list.append(i.replace('\n',"").split('\t'))
    mvp_list = mvp_list[1:]
    mvp_list = sorted(mvp_list, key=lambda mvp_list: float(mvp_list[2]),reverse=False)
    return mvp_list


def num_insert(what):
    global mvp_count2
    mvp_list=mvp_cut()
    for i in range(len(mvp_list)):
        what.insert(i,i+1)

def listbox_insert():
    mvp_list=mvp_cut()
    mvp_list=mvp_list[:20]
    return mvp_list
    # for i in range(len(mvp_list)):
    #     what.insert(0, mvp_list[i][num])

def coin_use(user):
    file = open('onedaylife_coin_use.txt', 'r', encoding='utf-8')
    mvp_text = file.readlines()
    file.close()
    use_list = []
    listx=[]
    for i in mvp_text[1:]:
        use_list.append(i.replace('\n','').split('\t'))
    for i in range(len(use_list)):
        if user.id==use_list[i][0] and user.n_name==use_list[i][1]:
            listx.append(use_list[i])
    return listx

def now_fly():
    path="now_fly.txt"
    if os.path.isfile(path):
        pass
    else:
        x="닉네임\t살아남은시간\t코인사용량\n"
        list=open('now_fly.txt','w',encoding='utf-8')
        list.write(x)
        list.close()


def one_day_life_data():
    import os.path

    path = 'onedaylife_coin_use.txt'
    if os.path.isfile(path):
        pass
    else:
        x = '아이디\t닉네임\t코인사용량\t사용시간\n'
        list = open('onedaylife_coin_use.txt', 'w', encoding='UTF-8')
        list.write(x)
        list.close()

def MVP_data():
    import os.path

    path = 'MVP.txt'
    if os.path.isfile(path):
        pass
    else:
        x = '아이디\t닉네임\t살아남은시간\t코인사용량\n'
        list = open('MVP.txt', 'w', encoding='UTF-8')
        list.write(x)
        list.close()

def all_data():
    MVP_data()
    one_day_life_data()
    now_fly()
def coin_count(user):

    file=open('user.txt','r',encoding='utf-8')
    files=file.readlines()
    files2=[]
    for i in files:
        files2.append(i.replace('\n','').split('\t'))
    file.close()
    file=open('user.txt','w',encoding='utf-8')
    for i in range(len(files)):
        if user.id==files2[i][0]:
            user.coin=str(int(user.coin)-1)
            file.write(user.id+'\t'+user.pw+'\t'+user.name+'\t'+user.n_name+'\t'+user.birth+'\t'+user.gen+'\t'+user.email+'\t'+user.coin+'\n')
        else:
            file.write(files[i])
    file.close()

def fly_now(user):
    text=open('now_fly.txt','r',encoding='utf-8')
    texts=text.readlines()
    text.close()
    user_fly=[]
    for i in range(len(texts)):
        texts[i]= texts[i].replace('\n','').split('\t')[i][0]
    my_oneday2.configure(sNumbers)


def check_coin_get():
    import os.path
    path = 'coin_get.txt'
    if os.path.isfile(path):
        pass
    else:
        x = '아이디\t포스팅\t로그인\t인기글\n'
        list = open('coin_get.txt', 'w', encoding='UTF-8')
        list.write(x)
        list.close()


def txt_check():
    text = open('coin_get.txt', 'r', encoding='utf-8')
    texts = text.readlines()
    text.close()
    text2 = []
    for i in texts[1:]:
        text2.append(i.replace('\n', '').split('\t'))
    text2.reverse()
    return text2

def txt_check_user(user):
    text2=txt_check()
    user_get_list=[]
    for i in range(len(text2)):
        if user.id==text2[i][0]:
            user_get_list.append(text2[i])
    return user_get_list

def user_text():
    text=open('user.txt','r',encoding='utf-8')
    texts=text.readlines()
    text.close()
    texts2=[]
    for i in texts:
        texts2.append(i.replace('\n','').split('\t'))
    return texts2

def coin_get_celeb(user):  # 아직 정해지지 않음
    check_coin_get()
    import time
    lista = open('coin_get.txt', 'a', encoding='UTF-8')
    lista.write(user.id + '-' + '-' + str(time.time()) + '\n')
    lista.close()


def coin_get_login(user):  # 코인 5개 지급
    check_coin_get()
    import time
    if user.id == txt_check()[0][0] and float(txt_check()[0][3]) + 43200 <= time.time():
        lista = open('coin_get.txt', 'a', encoding='UTF-8')
        lista.write(user.id + str(time.time()) + '-' + '-' + '\n')
        lista.close()
        user.coin =str(int(user.coin)+5)
        text=user_text()
        listx=open('user.txt','w',encoding='utf-8')
        for i in range(len(text)):
            if user.id==text[i][0]:
                text[i][7]=user.coin
            listx.write(text[i][0]+'\t'+text[i][1]+'\t'+text[i][2]+'\t'+text[i][3]+'\t'+text[i][4]+'\t'+text[i][5]+'\t'+text[i][6]+'\t'+text[i][7]+'\n')
        listx.close()
    else:
        pass


def coin_get_posting(user):  # 코인 3개 지급
    check_coin_get()
    import time
    if user.id == txt_check()[0][0] and float(txt_check()[0][3]) + 43200 <= time.time():
        lista = open('coin_get.txt', 'a', encoding='UTF-8')
        lista.write(user.id + str(time.time()) + '-' + '-' + '\n')
        lista.close()
        user.coin = str(int(user.coin) + 3)
        text = user_text()
        listx = open('user.txt', 'w', encoding='utf-8')
        for i in range(len(text)):
            if user.id == text[i][0]:
                text[i][7] = user.coin
            listx.write(
                text[i][0] + '\t' + text[i][1] + '\t' + text[i][2] + '\t' + text[i][3] + '\t' + text[i][4] + '\t' +
                text[i][5] + '\t' + text[i][6] + '\t' + text[i][7] + '\n')
        listx.close()
    else:
        pass

