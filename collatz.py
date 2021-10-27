import turtle
import random
import json
# Iterate through numbers n
# If n is positive, go up
# If n is negative, turn 20* in a random direction, 
Turtle = turtle.Turtle()
Screen = turtle.Screen()

#call if number is odd
def odd(num):
    return (num*3) +1
#call if number is even
def even(num):
    return (num/2)

#Get and Set the values provided by the collatz.json file
with open('collatz.json') as f:
    config = json.load(f)
n = int(config['start_number'])
colours = [config['colour_even'],config['colour_odd']]
Screen.bgcolor(config['bg_colour'])
WIDTH = int(config['window_width'])
HEIGHT = int(config['window_height'])
Screen.screensize(WIDTH, HEIGHT)
angle = int(config['angle'])
distance = int(config['distance'])
fixed = bool(config['fixed_direction'])
Turtle.speed = 10
x = n
Turtle.penup()
Turtle.goto(0, (HEIGHT/2) * -1)
Turtle.pendown()

#mainloop
try:
    while True:
        x = n
        while x != 1:
            if (x % 2 == 0):
                Turtle.setheading(90)
                Turtle.color(colours[0])
                Turtle.forward(distance)
                x = even(x)
            else:
                Turtle.setheading(90)
                if fixed:
                    y = random.randint(0,1)
                    if (y == 1):
                        Turtle.right(angle)
                    else:
                        Turtle.left(angle)
                else:
                    Turtle.right(angle)
                Turtle.color(colours[1])
                Turtle.forward(distance)
                x = odd(x)
                Turtle.setheading(90)

        Turtle.penup()
        Turtle.goto(0, (HEIGHT/2) * -1)
        Turtle.pendown()
        print(n)  
        n += 1
except KeyboardInterrupt:
    pass

Screen.exitonclick()