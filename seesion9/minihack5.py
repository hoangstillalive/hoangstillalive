quan = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
danso = ['150,300', '247,100', '333,300', '266,800', '420,900', '318,000']
n = len(danso)
for m in range(n):
    if danso[m] == max(danso):
        print ("Quan dan so lon nhat", quan[m])
for m in range(n):
    if danso[m] == min(danso):
        print ("Quan dan so nho nhat", quan[m])