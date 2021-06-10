import json
from random import random, choice

import turtle

sqrt2 = 2 ** 0.5

nums = {
    0: 'frrffrrfrrffrr',
    1: 'rrjlllsrrrffrrjrrjjrr',
    2: 'frrfrslllflljjlljllll',
    3: 'frrrslllfrrrsrrrjjrr',
    4: 'rrfllfrrfllllffllji',
    5: 'jifllfllfrrfrrfrrjjrr',
    6: 'jrrrslfllfllfllfrrjrr',
    7: 'frrrslfijjrr',
    8: 'frrfrrfllfllfllflljrrfrr',
    9: 'rrfllfrrrsiulfllfi',
}


def go(x, y, pet=turtle.getturtle()):
    pet.penup()
    pet.goto(x, y)
    pet.pendown()


def ex1(movements=20, dist=50):
    turtle.color('red')
    for i in range(movements):
        turtle.left(360 * random())
        turtle.forward(dist * random())


def ex2(text=141700, x=0, y=0, textsize=50):
    # f вперед на textsize
    # s вперёд на textsize*sqrt2
    # j прыжок вперед на textsize
    # u прыжок вперед на textsize*sqrt2
    # r поворот налево на 45
    # l поворот навправо на 45
    # i поворот на 180

    queue = [int(i) for i in str(text)]

    turtle.goto(x, y)

    for i in queue:

        _map_ = nums[i]

        for i in _map_:
            if i == 'f':
                turtle.forward(textsize)
            elif i == 's':
                turtle.forward(textsize * sqrt2)
            elif i == 'j':
                turtle.penup()
                turtle.forward(textsize)
                turtle.pendown()
            elif i == 'u':
                turtle.penup()
                turtle.forward(textsize * sqrt2)
                turtle.pendown()
            elif i == 'r':
                turtle.right(45)
            elif i == 'l':
                turtle.left(45)
            elif i == 'i':
                turtle.left(180)
        turtle.penup()
        turtle.forward(4 * textsize / 3)
        turtle.pendown()


def ex3():
    with open('font.json', 'w') as f:
        json.dump(nums, f, indent=2)


def ex4(x0=-100, y0=0, vx=10, vy=40, ax=0, ay=-10, t=(0, 1000), dt=0.1, zoom=1):
    moments = int((t[1] - t[0]) / dt)

    go(x0 * zoom, y0 * zoom)

    turtle.forward(500)
    turtle.backward(500)

    x, y = x0, y0

    for i in range(moments):
        # time.sleep(0.02)

        x += vx * dt

        dy = vy * dt + ay * dt * dt / 2
        if y + dy < y0:
            vy *= -0.8
            y += -dy + (y0 - y)
        else:
            y += dy

        vy += ay * dt

        turtle.goto(x * zoom, y * zoom)


def ex5(n=20, size=(500, 500), real=True):
    def draw_box():
        turtle.reset()
        turtle.speed(0)

        go(-size[0] / 2, size[1] / 2)

        for i in range(2):
            turtle.forward(size[0])
            turtle.right(90)
            turtle.forward(size[1])
            turtle.right(90)

        turtle.shape('turtle')

    def create_turtles():
        turtles = []

        # создание черепах
        for i in range(n):
            vx = (random() - 0.5) * v * 2

            vy = (v * v - vx * vx) ** 0.5 * choice([1, -1])

            new_turtle = [
                turtle.Turtle(),
                (random() - 0.5) * size[0],
                (random() - 0.5) * size[1],
                vx,
                vy
            ]

            turtles.append(new_turtle)

        # init
        for tur, x, y, vx, vy in turtles:
            tur.shape('circle')
            tur.speed(0)
            go(x, y, tur)
            tur.penup()

        return turtles

    def calc_distance(t1, t2):
        # ловим переполнение
        try:
            x1, y1 = t1[1], t1[2]
            x2, y2 = t2[1], t2[2]
            r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
            if r < 1000:
                return r
            return False
        except:
            return False
    # константы
    dt = 0.001
    v = 40
    a = 100000

    xmin = -size[0] / 2
    xmax = size[0] / 2
    ymin = -size[1] / 2
    ymax = size[1] / 2

    draw_box()

    turtles = create_turtles()

    turtle.tracer(0, 0)


    # mainloop
    while True:
        for i in range(n):
            tur, x, y, vx, vy = turtles[i]

            # типо реальных газ
            if real:
                for j in range(n):
                    if i != j:
                        tur1, x1, y1, vx1, vy1 = turtles[j]
                        r = calc_distance(turtles[j], turtles[i])
                        if not r:
                            continue
                        F = a / r / r

                        cosa = (x1 - x) / r
                        sina = (y1 - y) / r

                        vx -= F * cosa
                        vy -= F * sina

            dy = vy * dt
            dx = vx * dt

            # коллизия по x
            if y + dy < ymin:
                vy *= -1
                y += -dy + (y - ymin)
            elif y + dy > ymax:
                vy *= -1
                y += dy - (ymax - y)
            else:
                y += dy

            # коллизия по x
            if x + dx < xmin:
                vx *= -1
                x += -dx + (x - ymin)
            elif x + dx > xmax:
                vx *= -1
                x += dx - (xmax - x)
            else:
                x += dx

            turtles[i][1] = x
            turtles[i][2] = y

            turtles[i][3] = vx
            turtles[i][4] = vy

            #go(x, y, tur)  # ультра медленно работает черепаха
            tur.goto(x, y)
            turtle.update()


def main():

    # ex1()
    # ex2()
    # ex3()
    # ex4()
    ex5(20)
    turtle.mainloop()


if __name__ == '__main__':
    main()
