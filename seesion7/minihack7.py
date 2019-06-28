    
while True:
    m = input("Your account: ")
    name = input("What's your password ?")
    v = input("Your email: ")
    b = input("Enter again your password: ")
    a = "@gmail.com"
    # print(len(name))
    if((len(name) >= 8) and (name == b)):
        if a in v:
            print("accept")
            break
        else:
            print("email wrong")
    elif name != b:
        print("Your password is wrong, please do it again:")
    
   