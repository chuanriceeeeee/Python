import turtle
import math

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("两点间距离计算器")

points = []


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def draw_point(x, y, color="black"):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(5)
    t.end_fill()


def draw_line(x1, y1, x2, y2):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.color("blue")
    t.goto(x2, y2)


def show_distance(x1, y1, x2, y2, distance):
    text_x = (x1 + x2) / 2
    text_y = (y1 + y2) / 2 + 10

    t.penup()
    t.goto(text_x, text_y)
    t.pendown()
    t.color("red")
    t.write(f"距离: {distance:.2f}", align="center", font=("Arial", 12, "normal"))


def handle_click(x, y):
    global points

    points.append((x, y))
    draw_point(x, y)

    if len(points) == 2:
        x1, y1 = points[0]
        x2, y2 = points[1]

        draw_line(x1, y1, x2, y2)

        distance = calculate_distance(x1, y1, x2, y2)

        show_distance(x1, y1, x2, y2, distance)

        points = []
        t.color("black")


t.penup()
t.goto(0, 250)
t.pendown()
t.write("请点击画布上的两个点来计算距离", align="center", font=("Arial", 14, "bold"))
t.hideturtle()

screen.onscreenclick(handle_click)

turtle.done()



