m = int(input("Enter a month of year: "))

if m == 2:
    print("28 or 29 days")
elif m in [4,6,9,11]:
    print("30 days")
else:
    print("31 days")