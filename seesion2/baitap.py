while True:
    name = input("What's your password ?")
    # print(len(name))
    if((len(name) >= 8) and (name.isalpha() == False) and (name.isdigit() == False)):
        print("invalid")
        break
    else:
        print("illegal")