
items = input("A list of number, separated by',':").split(",")
print(items)
for a in items:
    if int(a) %2 == 0:
        print(a)