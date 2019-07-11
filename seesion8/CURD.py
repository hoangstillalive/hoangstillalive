items=["com","pho","chao","bun","mien","mi tom"]
m = input("C or R or U or D")
if m == "C":
    new = input("What food do you want? ")
    items.append(new)
    print(items)
elif m == "R":
    for item in items:
        print(item)
elif m == "U":
    i = int(input("Your number you want to change"))
    items[i-1] = input("What food do you want? ")
    print(items)
elif m == "D":
    i = int(input("What number do you want to remove? "))
    items.pop(i-1)
    print(items)
