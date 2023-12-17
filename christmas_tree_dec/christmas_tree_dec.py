
import turtle
import random

def draw_ball(turtle, x, y, size):
    """Draws a red ball at the specified position."""
    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow", "cyan", "magenta"]
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    random_color = random.choice(colors)
    turtle.color(random_color)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()

def draw_tree(turtle, branch_length, shorten_by, angle):
    """Draws a Christmas tree with multiple branches."""
    if branch_length > 10:
        turtle.forward(branch_length)
        turtle.left(angle)
        draw_tree(turtle, branch_length - shorten_by, shorten_by, angle)
        draw_ball(turtle, turtle.xcor(), turtle.ycor(), 5)  # Draw ball at the branch's end
        turtle.right(angle * 2)
        draw_tree(turtle, branch_length - shorten_by, shorten_by, angle)
        draw_ball(turtle, turtle.xcor(), turtle.ycor(), 5)  # Draw ball at the branch's end
        turtle.left(angle)
        turtle.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("forest green")
    t.speed("fastest")

    draw_tree(t, 100, 10, 30)

    # Draw the trunk
    t.color("saddle brown")
    t.up()
    t.goto(0, -100)
    t.down()
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()

    t.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    main()




