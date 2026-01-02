import turtle

t = turtle.Turtle()
t.hideturtle()

name = input("Введіть ім'я та прізвище: ")
color = input("Введіть улюблений колір (англійською): ")

t.color(color)
t.write(name, font=("Arial", 16, "normal"))

turtle.exitonclick()
