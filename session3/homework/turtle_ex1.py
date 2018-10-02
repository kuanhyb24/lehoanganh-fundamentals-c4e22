from turtle import *
    colors = ['red', 'blue', 'brown', 'yellow', 'grey']
while True:
        for a in range(5):
            if a%2==1:
                #color("red")
                for i in range(7-a):
                    forward(100) 
                    left(360/(7-a))     
            else:
                #color("grey")       
                for i in range(7-a):
                    forward(100) 
                    left(360/(7-a))
                    break     
    mainloop() 