import turtle

t = turtle.Turtle()
t.hideturtle()

t.color("red")
t.write("Hello, World!", font=("Arial", 20, "normal"))

t.penup()
t.goto(0, -40)
t.pendown()

t.color("blue")
t.write("Hello, World!", font=("Times New Roman", 22, "bold"))

t.penup()
t.goto(0, -80)
t.pendown()

t.color("green")
t.write("Hello, World!", font=("Courier", 18, "italic"))

turtle.exitonclick()
