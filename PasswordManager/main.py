master_pwd = input("What is the master password ?")
def view():
    with open ('password.txt','r') as f:
       for line in f.readlines():
           print(line.rstrip())
def add():
    name = input("Account name :")
    pwd = input("Password :")
    with open ('password.txt','a') as f:
        f.write(name + "|" + pwd + "\n")
while True:
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
