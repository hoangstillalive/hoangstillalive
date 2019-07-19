    
highscore = [59, 65, 28, 79, 50]
print ("High score:")
for i, score in enumerate(highscore):
    print (i+1, ".", score)
m = input ("New high score:")
highscore.append(m)
for n, p in enumerate(highscore):
    print (n+1, ".", p)