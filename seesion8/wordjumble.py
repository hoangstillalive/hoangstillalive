from random import*

items = ["guitar","mountain","friend","garden"]
randumItems = choice(items)

item=list(randumItems)
shuffle(item)

for i in item :
    print(i)

a = input("The correct word? ")
if a == randumItems :
    print("Corret")
else:
    print("Wrong")