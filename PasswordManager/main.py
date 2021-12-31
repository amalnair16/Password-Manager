master_pwd = input("What is the master password ?")
def view():
    pass
def add():
    name = input("Account name :")
    pwd = input("Password :")
    with open ('password.txt','a') as f:
while true:
    mode = input("Add new password or view existing password? please enter add or view , press q to quit " .lower())
    if mode=="q":
        break
    if mode == "view":
       view()
    elif mode=="add":
       add()
    else:
       print("Invalid mode")
       continue
