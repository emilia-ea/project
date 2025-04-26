import turtle
import random
import math
import sys
import tkinter.messagebox 

# Constants for the graphic
CIRCLE_RADIUS = 150
CENTER = (0, 0)
total_distance = 0
running = True
colors = ["red", "orange", "yellow", "green", "blue", "purple", "magenta", "cyan"]
color_index = 0
active_entry_index = 0
speed_setting = "medium"

def draw_circle():
    #draw the central reference circle (mostly just for perspective)
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.pensize(2)
    drawer.penup()
    drawer.goto(0, -CIRCLE_RADIUS)
    drawer.pendown()
    drawer.circle(CIRCLE_RADIUS)
    drawer.penup()

def move_turtle():
    #"Move turtle randomly, keep track of the distance
    global total_distance, color_index
    if not running:
        return
    angle = random.randint(0, 360)
    distance = random.randint(20, 40)
    turtle.color(colors[color_index % len(colors)])
    color_index += 1
    turtle.setheading(angle)
    turtle.pendown()
    turtle.forward(distance)
    total_distance += distance
    turtle.ontimer(move_turtle, 200)

def stop():
    #Stop turtle,calculate the scaled number using equation, show it to the user
    global running
    running = False
    
    # why scaling?
    # te turtle's total_distance could be very small (if user stops early)
    # or very large (if user lets it run for a long time)
    # to make sure the number is ALWAYS a valid 3-digit number
    # cap the distance at 8000 pixels (so it doesn't overflow)
    # scale the distance from 0-8000 into 0-899 range
    # add 100 to make sure it's in the 100-999 range
    scaled_number = int(100 + (min(total_distance, 8000) / 8000) * 899)

    # Show result to user before closing turtle window
    tkinter.messagebox.showinfo("Turtle Result", f"You generated the number: {scaled_number}!")

    # Write to file so the gui can retrieve, automatically input it where the user wants it
    with open("turtle_result.txt", "w") as f:
        f.write(f"{active_entry_index}:{scaled_number}")

    turtle.bye()

# read the parameters
if len(sys.argv) >= 3:
    try:
        active_entry_index = int(sys.argv[1])
        speed_setting = sys.argv[2]
    except:
        active_entry_index = 0
        speed_setting = "medium"

screen = turtle.Screen()
screen.title("Turtle Generator")
draw_circle()

turtle.shape("turtle")
turtle.pensize(3)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Adjust turtle speed based on user choice
# the reason for giving the user the option to choose the speed
# is so if they know they want a big number,
# they can choose a faster turle and it wont take that long
if speed_setting == "slow":
    turtle.speed(10)
elif speed_setting == "medium":
    turtle.speed(15)
elif speed_setting == "fast":
    turtle.speed(25)

# read which entry field (first, second, or third number) the user chose to generate this for
if len(sys.argv) > 1:
    try:
        active_entry_index = int(sys.argv[1])
    except:
        active_entry_index = 0

screen.listen()
screen.onkey(stop, "space")
move_turtle()
turtle.mainloop()
