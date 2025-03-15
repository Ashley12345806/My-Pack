import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create the turtle
forest = turtle.Turtle()
forest.speed(0)  # Set the drawing speed to maximum

def draw_tree(x, y, trunk_color, leaf_color):
    # Move to the starting position
    forest.penup()
    forest.goto(x, y)
    forest.pendown()
    
    # Draw the trunk
    forest.color(trunk_color)
    forest.begin_fill()
    for _ in range(2):
        forest.forward(20)
        forest.left(90)
        forest.forward(40)
        forest.left(90)
    forest.end_fill()
    
    # Draw the leaves
    forest.penup()
    forest.goto(x - 15, y + 40)  # Move to the top of the trunk
    forest.pendown()
    forest.color(leaf_color)
    forest.begin_fill()
    forest.circle(30)
    forest.end_fill()

# Draw multiple trees in random positions
for _ in range(10):
    x = random.randint(-200, 200)
    y = random.randint(-200, 0)
    trunk_color = "brown"
    leaf_color = random.choice(["green", "darkgreen", "forestgreen"])
    draw_tree(x, y, trunk_color, leaf_color)

# Hide the turtle
forest.hideturtle()

# Keep the window open
screen.mainloop()
