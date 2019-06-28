side = int(input("Enter side of shape you like:"))
angle = 360/side
from turtle import*
shape("turtle")  
for i in range(side):
    forward(100)
    left (angle)
    
mainloop()














