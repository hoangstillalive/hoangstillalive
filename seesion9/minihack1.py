items = ["red","blue","orange"]
print("Our color list: ")
for n, item in enumerate(items):
    print(n+1,".",item)


# a = input("Enter a new color: ")
# items.append(a)
# print("Our new color list: ")
# print(*items, sep=(", "))
# i = int(input("Enter position: "))-1
# print("Color at position",i+1,":",items[i])


m = input("Item to delete: ")

if m.isdigit() == True :        
    if int(m) <= len(items):
        items.pop(int(m)-1)
    else:
        print("Not found")
    
elif m.isalpha() == True:
    if m in items:
        items.remove(m)
    else:
        print("Not found")

    
print(items)