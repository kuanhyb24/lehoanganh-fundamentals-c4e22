from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
colormode()
for a in range(5):
    for color in colors:
        pencolor(color)
        fillcolor(color)
        begin_fill()
    if a%2==1:
        for i in range(7-a):
            forward(100) 
            left(360/(7-a))    
    else:     
        for i in range(7-a):
            forward(100) 
            left(360/(7-a)) 
            end_fill()                  
mainloop() 