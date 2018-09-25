from turtle import *
speed(50)
for a in range(4):
    if a%2==1:
        color("blue")
        for i in range(6-a):
            forward(100) 
            left(360/(6-a))     
    else:
        color("red")       
        for i in range(6-a):
            forward(100) 
            left(360/(6-a))       
mainloop() 