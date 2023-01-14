import turtle
import time
import random

hiz = 0.15
pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('pink')
pencere.setup(width=600, height=600)
pencere.tracer(0)

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape('square')
kafa.color('purple')
kafa.penup()
kafa.goto(0, 100)
kafa.direction = 'stop'

yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape('circle')
yemek.color('blue')
yemek.penup()
yemek.goto(0, 0)
yemek.shapesize(0.80, 0.80)

kuyruklar = []
puan = 0

yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("purple")
yaz.penup()
yaz.hideturtle()
yaz.goto(0, 260)
yaz.write("Puan: {}".format(puan), align="center", font=("Courier", 24, "normal"))


def move():
    if kafa.direction == 'up':
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction == 'right':
        x = kafa.xcor()
        kafa.setx(x + 20)
    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x - 20)


def go_up():
    if kafa.direction != 'down':
        kafa.direction = 'up'


def go_down():
    if kafa.direction != 'up':
        kafa.direction = 'down'


def go_right():
    if kafa.direction != 'left':
        kafa.direction = 'right'


def go_left():
    if kafa.direction != 'right':
        kafa.direction = 'left'


pencere.listen()
pencere.onkey(go_up, 'Up')
pencere.onkey(go_down, 'Down')
pencere.onkey(go_right, 'Right')
pencere.onkey(go_left, 'Left')

while True:
    pencere.update()

    if kafa.xcor() > 300 or kafa.xcor() < -300 or kafa.ycor() > 300 or kafa.ycor() < -300:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = 'stop'

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)

        kuyruklar = []
        puan = 0
        yaz.clear()
        yaz.write(f"Puan: {puan}", align="center", font=("Courier", 24, "normal"))

        hiz = 0.15

    if kafa.distance(yemek) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yemek.goto(x, y)

        puan = puan + 10
        yaz.clear()
        yaz.write(f"Puan: {puan}", align="center", font=("Courier", 24, "normal"))

        hiz = hiz - 0.001

        yeni_kuyruk = turtle.Turtle()
        yeni_kuyruk.speed(0)
        yeni_kuyruk.shape('square')
        yeni_kuyruk.color('white')
        yeni_kuyruk.penup()
        kuyruklar.append(yeni_kuyruk)

    for index in range(len(kuyruklar) - 1, 0, -1):
        x = kuyruklar[index - 1].xcor()
        y = kuyruklar[index - 1].ycor()
        kuyruklar[index].goto(x, y)

    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x, y)

    move()
    time.sleep(hiz)
