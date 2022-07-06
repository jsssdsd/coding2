import os
import time
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

def MVP():
    MVP_data()
    lista=open("MVP.txt",'r',encoding='utf-8')
    MVP_list=lista.readlines()
    del MVP_list[0]
    lista.close()
    list_mvp=[]
    for i in MVP_list:
        list_mvp.append(i.replace('\n','').split('\t'))
    print(list_mvp)
    x=0
    time_list=[]
    coin_list=[]

    for i in range(len(list_mvp)):
        list_mvp[i][2]=int(list_mvp[i][2])
        time_list.append(list_mvp[i][2])
        list_mvp[i][3]=int(list_mvp[i][3])
        coin_list.append(int(list_mvp[i][3]))
        list_mvp[i][2]=int(list_mvp[i][2])
    list_mvp=sorted(list_mvp, key=lambda list_mvp: list_mvp[3])
    list_mvp=sorted(list_mvp, key=lambda list_mvp: list_mvp[2],reverse=True)
    print(list_mvp)
    listx=open("MVP.txt",'w',encoding='utf-8')
    x = '아이디\t닉네임\t살아남은시간\t코인사용량\n'
    lisx.write(x)
    for i in range(len(list_mvp)):
        listx.write(list_mvp[i][0]+'\t'+list_mvp[i][1]+'\t'+str(list_mvp[i][2])+'\t'+str(list_mvp[i][3])+'\n')
    listx.close()

def pay():
    user=login.all_user_data()[1]
    if int(user.coin)<=0:
        pass
    else:
        user.coin=str(int(user.coin)-1)
        file=open('onedaylife_coin_use.txt','a',encoding='utf-8')
        file.write(user.id+'\t'+user.n_name+'\t'+'1'+'\t'+str(time.time())+'\n')
        file.close()
def coin():
    global user
    return user.coin




if __name__=="__main__":
    MVP()

























