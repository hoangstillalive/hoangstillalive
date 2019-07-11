items=["lol","bts","mtp"]
items.pop(1)
items.remove('mtp')
print(*items)
new_item = input("1 letter: ")
items.append(new_item)
print(items[0].upper())
print(items[2])
print(*items, sep='| ')