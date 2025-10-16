class JARVIS:
    def __init__(self):
        self.set_user = 'loki'
        self.set_password = '127'
        self.enter_your_user_name = str(input('enter your user name--->'))

        if self.enter_your_user_name == self.set_user:
            self.enter_your_password = str(input("enter your password-.-.->"))
            if self.enter_your_password == self.set_password:
                print("welcome you sir")
            else:
                if self.enter_your_password != self.set_password:
                    print("your password is in mis match")
                    check = JARVIS()
        else:
            if self.enter_your_user_name != self.set_user:
                print("your user name incorrect")
                check = JARVIS()
    def user_welcome(self,user_welcome_in):
        self.u ={
            'happy':'😎',
            'sad':'😭',
            'normal':'😔'
        }
        self.user_wel=''
        m=''
        for self.us in user_welcome_in:
            m+=self.us
        print(m)
        self.user_wel +=self.u.get(m,"me to")
        return (self.user_wel)

ass = JARVIS()
user_welcome_in=input("enter your status: ").lower()
print(ass.user_welcome(user_welcome_in))


#ass.user_welcome()
