import turtle
import math
import time

def draw_koch_curve(pen, start, end, depth):
    if depth == 0:
        pen.penup()
        pen.goto(start)
        pen.pendown()
        pen.goto(end)
        return

    dx, dy = (end[0]-start[0])/3, (end[1]-start[1])/3
    p1 = (start[0]+dx, start[1]+dy)
    p3 = (start[0]+2*dx, start[1]+2*dy)
    px = p1[0] + (p3[0]-p1[0])/2 + math.sqrt(3)*(p3[1]-p1[1])/2
    py = p1[1] + (p3[1]-p1[1])/2 - math.sqrt(3)*(p3[0]-p1[0])/2
    p2 = (px, py)

    draw_koch_curve(pen, start, p1, depth-1)
    draw_koch_curve(pen, p1, p2, depth-1)
    draw_koch_curve(pen, p2, p3, depth-1)
    draw_koch_curve(pen, p3, end, depth-1)

def draw_snowflake(pen, vertices, depth, color):
    pen.pencolor(color)
    pen.pensize(2)
    for i in range(3):
        draw_koch_curve(pen, vertices[i], vertices[(i+1)%3], depth)

# Setup screen and turtle
screen = turtle.Screen()
screen.setup(900,700)
screen.bgcolor("white")
screen.title("Koch Snowflake Transformation")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

triangle = [(0,150), (-130,-75), (130,-75)]
colors = ["black","red","blue","green","purple"]

for i in range(5):  # iterations 0-4
    pen.clear()
    pen.penup()
    pen.goto(-350,280)
    pen.pencolor("black")
    pen.write(f"Koch Snowflake - Iteration {i}", font=("Arial",18,"bold"))
    pen.goto(-350,250)
    pen.write("Starting triangle" if i==0 else f"Depth {i}", font=("Arial",12,"normal"))
    draw_snowflake(pen, triangle, i, colors[i%len(colors)])
    screen.update()
    time.sleep(2 if i>0 else 3)
 
screen.exitonclick()
