import raw_data_to_list as rl

class user_data():
    def __init__(self,id,pw,name,n_name,birth,gen,email,coin):
        self.id=id
        self.pw=pw
        self.name=name
        self.n_name=n_name
        self.birth=birth
        self.gen=gen
        self.email=email
        self.coin = coin

def all_user_data():
    text=rl.userData()
    user_data_list=[]

    for i in range(len(text)):
        globals()['user_data{}'.format(i)]=user_data(text[i][0],text[i][1],text[i][2],text[i][3],text[i][4],text[i][5],text[i][6],text[i][7])
        user_data_list.append(globals()['user_data{}'.format(i)])
    return user_data_list
