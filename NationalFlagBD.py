import turtle

# Setup screen
wn = turtle.Screen()
wn.setup(width=500, height=500)
wn.title("Bangladesh Flag")

t = turtle.Turtle()
t.speed(10)

# Function to draw filled rectangle
def draw_rectangle(x1, y1, x2, y2, color):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(x2 - x1)
        t.right(90)
        t.forward(y1 - y2)
        t.right(90)
    t.end_fill()

# Function to draw filled circle
def draw_circle(center_x, center_y, radius, color):
    t.penup()
    t.goto(center_x, center_y - radius)
    t.setheading(0)
    t.color(color)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw green flag background (rectangle from (50, 50) to (350, 230))
draw_rectangle(50 - 250, 250 - 50, 350 - 250, 250 - 230, "#006A4E")  # shifted to center

# Draw red circle (center at 195,140, radius 60)
draw_circle(195 - 250, 250 - 140, 60, "#F42A41")  # shifted to center

# Draw white pole (rectangle from (40, 40) to (50, 430))
draw_rectangle(40 - 250, 250 - 40, 50 - 250, 250 - 430, "white")

t.hideturtle()
turtle.done()
