from turtle import *

shape("turtle")
speed(-1)
color("red")

left(30)
forward(100)
right(60)
forward(100)
right(120)
forward(100)
right(60)
forward(100)

for i in range(3):
    right(30)
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)

mainloop()
