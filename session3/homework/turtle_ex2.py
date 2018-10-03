from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
for color in colors:
    pencolor(color)
    fillcolor(color)
    begin_fill()
    forward(50)
    right(90)
    forward(80)
    right(90)
    forward(50)
    right(90)
    forward(80)
    right(90)
    forward(50)
    end_fill()
mainloop()
