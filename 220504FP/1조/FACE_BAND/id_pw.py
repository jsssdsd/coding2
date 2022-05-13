

def check_id_pw(id,pw):
    global log_user_data
    import login
    log_user_data = login.all_user_data()
    for i in range(len(log_user_data)):
        if id == log_user_data[i].id and pw == log_user_data[i].pw:
            return log_user_data[i]


if __name__=="__main__":
    print(check_id_pw('회ㄴㅁㅇ원1','123'))
