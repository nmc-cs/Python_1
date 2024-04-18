import turtle

def draw_square(size):
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def draw_fractal(x, y, size, level):
    if level == 0:
        return
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    draw_square(size)
    new_size = size * 0.8
    new_level = level - 1
    draw_fractal(x - new_size / 2, y + new_size / 2, new_size, new_level)
    draw_fractal(x + new_size / 2, y + new_size / 2, new_size, new_level)
    draw_fractal(x - new_size / 2, y - new_size / 2, new_size, new_level)
    draw_fractal(x + new_size / 2, y - new_size / 2, new_size, new_level)

def main():
    turtle.speed('fastest')
    screen = turtle.Screen()
    screen.setworldcoordinates(-200, -200, 200, 200)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.left(45)
    draw_fractal(0, 0, 100, 4)
    screen.exitonclick()

if __name__ == "__main__":
    main()
