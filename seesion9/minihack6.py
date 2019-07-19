quan = ['ST', 'BD', 'BTL', 'CG', 'DD', 'HBT']
danso = [150300, 247100, 333300, 266800, 420900, 318000]
km2 = [117.43, 9.224, 433.5, 12.04, 9.96, 10.09]
mdds = []
for i, p in zip(danso, km2):
    m = i/p
    mdds.append(m)
    count = 0
for m in mdds:
    count = count + m
sq = len(quan)
mddctb = count / sq
print (round(mddctb, 2))