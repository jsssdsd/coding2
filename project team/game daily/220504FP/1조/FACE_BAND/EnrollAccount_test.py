
def check_UserFile():
    import os.path
    path = 'user.txt'
    if os.path.isfile(path):
        pass
    else:
        x = '아이디\t패스워드\t이름\t닉네임\t생년월일\t성별\t이메일\t코인보유량\n'
        list = open('user.txt', 'w', encoding='UTF-8')
        list.write(x)
        list.close()

def check_overlap(what,num):
    check_UserFile()
    f = open('user.txt', 'r', encoding='UTF-8')
    text = f.readlines()
    f.close()
    text_list=[]
    text_lista=[]
    for i in range(len(text)):
        text_list.append(text[i].replace('\n','').split('\t'))
        text_lista.append(text_list[i][num])
    a=what
    while True:
        if a not in text_lista:
            return a
        else:
            return

def check_pw(pw):
    a=pw
    while True:
        count = 0
        # print(a)
        for i in range(len(a)):
            try:
                int(a[i])
            except:
                pass
            else:
                count+=1
        if count>=4:
            return a
        else:
            return

def check_birth(birth):
    if birth.isdigit():
        if len(birth)==6:
            return birth
        else:
            print('6칸이 아닙니다.')
            return
    else:
        print('문자가 입력되었습니다.')
        return

def check_gen(gen):
    if gen == '남' or gen == '여' or gen == '남자' or gen == '여자':
        return gen
    else:
        return

def check_email(email):
    if email.count('@')==1 :
        translation = email.split('@')
        emailaddress =  '.' in translation[1]
        print(emailaddress)
        if emailaddress:
            return email
        else:
            return

def check_alpha(word):
    for i in range(len(word)):
        if not word[i].isdigit():
            if not word[i].encode().isalpha():
                return
    return word

def SaveUser(id,pw, name, nickname, birth, gen ,email):
    if check_overlap(id,0):
        ID=check_overlap(id,0)
    else:
        return 'id'
    if check_alpha(id):
        pass
    else:
        return 'id_alpha'
    if check_pw(pw):
        PW=check_pw(pw)
    else:
        return 'pw'
    Name=name
    if check_overlap(nickname, 3):
        N_name = check_overlap(nickname, 3)
    else:
        return 'nick'
    if check_birth(birth):
        Birth=check_birth(birth)
    else:
        return 'birth'
    if check_gen(gen):
        Gen=gen
    else:
        return 'gen'
    if check_email(email):
        Email = email
    else:
        return 'email'
    Coin = '50'
    newUser = ID + '\t' + PW + '\t' + Name + '\t' + N_name + '\t' + Birth + '\t' + Gen + '\t' + Email + '\t'+Coin+'\n'
    f = open('user.txt', 'a', encoding='UTF-8')
    f.write(newUser)
    f.close()


if __name__ == '__main__':
    print(SaveUser("qweqwe","1234ee","qwe",'tttt',"qweqwe","m","qwewqead"))