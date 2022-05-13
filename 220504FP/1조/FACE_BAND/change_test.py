import EnrollAccount_test as Et
import id_pw as ip
import login
import raw_data_to_list as rl



def check_pw(pw):
    global user
    if pw==user.pw:
        return 'yes'
    elif pw!=user.pw:
        return 'pw'

# def change_pw(a):
#     global user
#     if Et.check_pw(a):
#        return a
#     else:
#        return "pw"

# def change_nick(b):
#     global user
#     if Et.check_overlap(b,3):
#         return b
#     else:
#         return "nick"
#
# def change_email(c):
#     global user
#     return c

def change_pw(user,a):
    b=rl.userData()
    text=open("user.txt",'w',encoding='UTF-8')
    x = '아이디\t패스워드\t이름\t닉네임\t생년월일\t성별\t이메일\t코인보유량\n'
    text.write(x)
    for i in range(len(b)):
        if user.id==b[i][0]:
            # print('yes')
            b[i][1]=a
        text.write(b[i][0]+'\t'+b[i][1]+'\t'+b[i][2]+'\t'+b[i][3]+'\t'+b[i][4]+'\t'+b[i][5]+'\t'+b[i][6]+'\t'+b[i][7]+'\n')
    user.pw = a
    text.close()
    return user

def change_nick(user,a):
    b=rl.userData()
    text=open("user.txt",'w',encoding='UTF-8')
    x = '아이디\t패스워드\t이름\t닉네임\t생년월일\t성별\t이메일\t코인보유량\n'
    text.write(x)
    for i in range(len(b)):
        if user.id==b[i][0]:
            # print('yes')
            b[i][3]=a
        text.write(b[i][0]+'\t'+b[i][1]+'\t'+b[i][2]+'\t'+b[i][3]+'\t'+b[i][4]+'\t'+b[i][5]+'\t'+b[i][6]+'\t'+b[i][7]+'\n')
    text.close()

    b=rl.postData()
    text=open("post.txt",'w',encoding='UTF-8')
    x = 'post_num\tID\t제목\t시간\t비밀글여부\t닉네임\n'
    text.write(x)
    for i in range(len(b)):
        if user.id==b[i][1]:
            # print('yes')
            b[i][5]=a
        text.write(b[i][0]+'\t'+b[i][1]+'\t'+b[i][2]+'\t'+b[i][3]+'\t'+b[i][4]+'\t'+b[i][5]+'\n')
    text.close()

    b=rl.commentData()
    text=open("comment.txt",'w',encoding='UTF-8')
    x = 'post_num\tcomment_num\t아이디\t닉네임\t시간\t내용\n'
    text.write(x)
    for i in range(len(b)):
        if user.id==b[i][2]:
            b[i][3]=a
        text.write(b[i][0]+'\t'+b[i][1]+'\t'+b[i][2]+'\t'+b[i][3]+'\t'+b[i][4]+'\t'+b[i][5]+'\n')
    text.close()

    b=rl.likeData()
    text=open("like.txt",'w',encoding='UTF-8')
    x = 'post_num\t아이디\t닉네임\n'
    text.write(x)
    for i in range(len(b)):
        if user.id==b[i][1]:
            b[i][2]=a
        text.write(b[i][0]+'\t'+b[i][1]+'\t'+b[i][2]+'\n')
    text.close()

    user.n_name = a
    return user

def change_email(user,a):
    b=rl.userData()
    text=open("user.txt",'w',encoding='UTF-8')
    x = '아이디\t패스워드\t이름\t닉네임\t생년월일\t성별\t이메일\t코인보유량\n'
    text.write(x)
    for i in range(len(b)):
        if user.id==b[i][0]:
            # print('yes')
            b[i][6]=a
        text.write(b[i][0]+'\t'+b[i][1]+'\t'+b[i][2]+'\t'+b[i][3]+'\t'+b[i][4]+'\t'+b[i][5]+'\t'+b[i][6]+'\t'+b[i][7]+'\n')
    user.email = a
    text.close()
    return user


if __name__=="__main__":
    user=rl.userData()[1]
    print(user)
    change_pw('1111111')





