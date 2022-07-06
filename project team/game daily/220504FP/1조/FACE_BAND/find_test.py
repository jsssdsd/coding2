# 아이디 비밀번호 찾기 시스템

import login
log_user_data=login.all_user_data()
# print(log_user_data)

def user_find_id(name,birth,gen,email):
    for i in range(len(log_user_data)):
        if name == log_user_data[i].name and birth == log_user_data[i].birth and gen == log_user_data[i].gen and email == log_user_data[i].email:
            return (log_user_data[i].id,log_user_data[i].pw)

if __name__=="__main__":
    user_find_id('김준철','950814','남자','ri@naver.com')
    # user_find_pw('q','asd','asd','q','asd')
