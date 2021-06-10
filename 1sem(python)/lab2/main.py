import turtle
import numpy as np

from numpy import sin, cos, deg2rad


def draw_circle(x=0, y=0, r=100, n=50, right=False, fill=None):
    turtle.penup()
    turtle.goto(r + x, y)
    turtle.pendown()

    if fill is not None:
        turtle.begin_fill()

    angels = np.deg2rad(np.linspace(0, 360, n + 1))

    if right:
        angels *= -1

    for angel in angels:
        turtle.goto(x + r*cos(angel),y + r*sin(angel))

    if fill is not None:
        turtle.color(fill)
        turtle.end_fill()
        turtle.color('black')



def draw_circle_here(r=100, n=50, right=False):
    da = 180 / n
    da_rad = np.deg2rad(da)
    if right:
        da *= -1
    for angel in range(n):
        turtle.forward(2 * r * sin(da_rad))
        turtle.left(2 * da)



def go(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def ex2():
    turtle.shape('turtle')
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)


def ex3(a=100):
    for i in range(4):
        turtle.left(90)
        turtle.forward(a)


def ex4():
    draw_circle()


def ex5(a=50, n=5, step=20):
    for i in range(n):
        go(a/2 + i*step/2, -i*step/2)
        ex3(a + i*step)


def ex6(n=6,r=100):
    da = 360 / n
    turtle.shape('turtle')
    for i in range(n):
        turtle.forward(r)
        turtle.stamp()
        turtle.left(180)
        go(0, 0)
        turtle.left(180 + da)


def ex7(r=3, max_angel=1720, prec=5):
    for angel in np.deg2rad(np.arange(0, max_angel, prec)):
        turtle.goto(r * angel * cos(angel), r * angel * sin(angel))


def ex8(a=10, n=40, step=5):
    for i in range(n):
        turtle.forward(a + i*step)
        turtle.left(90)


def ex9(n=10, r0= 50, step=25):
    for poly in range(n):
        draw_circle(0, 0, r0 + poly*step, poly + 3)


def ex10(n=3):
    dangel = 180 - 360 / n
    for i in range(n):
        draw_circle_here()
        draw_circle_here(right=True)
        turtle.left(dangel)


def ex11(n=4, r0=50, step=10):
    turtle.left(90)
    for i in range(n):
        draw_circle_here(r0 + i*step)
        draw_circle_here(r0 + i*step, right=True)


def ex12(r=50, w=0.4, v=10, t=30, prec=0.1):
    for i in np.arange(0, t, prec):
        turtle.goto(v*i + r*cos(i*w) - r, -r*sin(i*w))


def ex13():
    draw_circle(0, 0, 100, fill='yellow') # ЖЕЛТЫЙ КРУГ

    draw_circle(35, 45, 20, fill='blue') # глаза
    draw_circle(-35, 45, 20, fill='blue') # глаза

    # нос
    go(0, 25)
    turtle.width(10)
    turtle.color('black')
    turtle.goto(0, -30)
    turtle.color('black')

    # улыбка
    r = 50
    turtle.width(10)
    turtle.color('red')

    go(r, -r/3)

    for angel in np.arange(0, np.pi, 0.1):
        turtle.goto(r*cos(angel), -r*sin(angel) - r/3)


def ex14(r=100, n=5):
    angels = np.linspace(0, 2*np.pi, n+1)
    angels += np.pi / 2 / n
    half = (n - 1) // 2
    go(r * cos(angels[0]), r * sin(angels[0]))
    for i in range(n):
        angel = angels[i*half % n]
        turtle.goto(r*cos(angel), r*sin(angel))
    turtle.goto(r * cos(angels[-1]), r * sin(angels[-1]))





def main():
    funcs = [ex2, ex3, ex4, ex5, ex6, ex7, ex8, ex9, ex10, ex11, ex12, ex13, ex14]
    while True:
        for func in funcs:
            func()
            turtle.reset()

    turtle.mainloop()


if __name__ == '__main__':
    main()
