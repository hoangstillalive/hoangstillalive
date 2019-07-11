items=["com","pho","chao","bun","mien","mi tom"]
# l = len(items)
# for i in range(l):
#     print(items[i])

# for item in items:
#     print(item)
a = "o"

for i, item in enumerate(items):
    if a in item:
        print(i+1,"." ,item.upper())