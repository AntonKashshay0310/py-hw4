import turtle

t = turtle.Turtle()
t.hideturtle()

name = input("Введіть ім'я та прізвище: ")

t.write(name, font=("Arial", 16, "normal"))

turtle.exitonclick()
