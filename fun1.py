from turtle import *
import colorsys

def draw_stem():
    """Draws the flower stem."""
    color("white")
    fillcolor("green")
    begin_fill()
    forward(300)
    left(90)
    forward(10)
    left(90)
    forward(300)
    left(90)
    forward(10)
    end_fill()

def draw_leaf():
    """Draws a single leaf."""
    color("white")
    fillcolor("green")
    begin_fill()
    circle(100, 90)
    left(90)
    circle(100, 90)
    end_fill()

def draw_petals():
    """Draws multiple gradient-colored petals."""
    h = 0  # Start hue for colors
    for i in range(150):
        c = colorsys.hsv_to_rgb(h, 1, 1)  # Generate RGB color
        h += 0.005  # Smooth gradient change
        fillcolor(c)
        pencolor(c)
        begin_fill()
        circle(150 - i, 90)  # Draw a petal shape
        left(90)
        circle(150 - i, 90)
        left(18)  # Slight turn for petal spacing
        end_fill()

def main():
    """Main function to draw the entire flower."""
    speed(0)
    bgcolor("black")
    tracer(0, 0) 

    # Draw petals
    penup()
    goto(0, 100)
    pendown()
    draw_petals()

    update()  # Refresh screen to display drawing
    done()  # Keeps window open

if __name__ == "__main__":
    main()



       




    




