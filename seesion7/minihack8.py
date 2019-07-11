from random import*
count = 0
while True:
    number1 = randint(1,100)
    number2 = randint(1,100)
    
    operation = ["+" ,"-"]
    randomOper = choice(operation)

    step = randint(-1,1)

    if randomOper == "+":
        result = number1 + number2 + step
        print(number1, randomOper, number2, "=", result)
        user = input("True or False: ")
        if step == 0:
            if user == "t":
                print("Correct")
                count = count + 1
                print(count)
            else:
                print("You lose")
                print(count)
                break
        else:
            if user == "f":
                print("Correct")
                count = count + 1
                print(count)
            else:
                print("You lose")
                print(count)
                break
    else:
        result = number1 - number2 + step
        print(number1, randomOper, number2, "=", result)
        user = input("True or False: ")
        if step == 0:
            if user == "t":
                print("Correct")
                count = count + 1
                print(count)
            else:
                print("You lose")
                print(count)
                break
        else:
            if user == "f":
                print("Correct")
                count = count + 1
                print(count)
            else:
                print("You lose")
                print(count)
                break



