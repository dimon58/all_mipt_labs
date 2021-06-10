from math import sin, cos, radians, sqrt, pi
from random import random

import pygame
from pygame.draw import *
from typing import Tuple, Union

pygame.init()

DEBUG = False

FPS = 30
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

screen.fill((255, 255, 255))


def draw_parallelogram(x: int, y: int, width: int, height: int, angle: int = 90,
                       color: Tuple[int, int, int] = (220, 255, 0), outline: int = 0, outlinecolor=(0, 0, 0)):
    """
    Draws a parallelogram with one vertical side
    If you set negative values for width and height the parallelogram will be drawn in the other direction
    @param x: x coordinate of the upper-left corner of the parallelogram
    @param y: y coordinate of the upper-left corner of the parallelogram
    @param width: length of the not vertical side of the parallelogram
    @param height: length of the vertical side of the parallelogram
    @param angle: angle between sides
    @param color: the fill color of the parallelogram
    @param outline: thickness of the outer line of the parallelogram
    @param outlinecolor: color of the outer line of the parallelogram
    @return: None
    """
    angle = radians(angle)
    vertex = (
        (x, y),
        (x, y + height),
        (int(x + width * sin(angle)), int(y + height + width * cos(angle))),
        (int(x + width * sin(angle)), int(y + width * cos(angle))),
    )
    polygon(screen, color, vertex)
    if outline:
        polygon(screen, outlinecolor, vertex, outline)


def draw_with_outline(func, *args, **kwargs):
    """
    COSTIL'!!!!!!!
    Draws figure with outline using magic
    """
    args = list(args)
    func(*args, **kwargs)
    args[1] = (0, 0, 0)
    func(*args, 1, **kwargs)


def draw_fence(x: int, y: int, width: int, height: int, boards=20):
    """
    Draws a fence
    @param x: x coordinate of upper-left corner of the fence
    @param y: y coordinate of upper-left corner of the fence
    @param width: width of the fence
    @param height: height of the fence
    @param boards: number of boards in the fence
    """

    rect(screen, (255, 255, 0), (x, y, width, height))
    line(screen, (0, 0, 0), (x, y), (width, y))  # top line
    line(screen, (0, 0, 0), (x, y + height), (width, y + height))  # bottom line

    for x_coord in range(x, x + width, width // boards):
        line(screen, (0, 0, 0), (x_coord, y), (x_coord, y + height))


def draw_bg():
    """
    Draws a background
    @return: None
    """
    # sky
    rect(screen, (0, 255, 255), (0, 0, SCREEN_WIDTH, 3 * SCREEN_HEIGHT // 5))

    # grass
    rect(screen, (0, 255, 100), (0, 3 * SCREEN_HEIGHT // 5, SCREEN_WIDTH, 2 * SCREEN_HEIGHT // 5))

    draw_fence(0, SCREEN_HEIGHT // 5, SCREEN_WIDTH, 2 * SCREEN_HEIGHT // 5)


def draw_chain(x: int, y: int, width: int, height: int, links: int):
    """
    Draws a chain
    @param x: x coordinate of upper-left corner of the described rectangle
    @param y: y coordinate of upper-left corner of the described rectangle
    @param width: width of the described rectangle
    @param height: height of  the described rectangle
    @param links: number of links
    @return: None
    """
    # making list of lengths of links
    lengths_of_links = [random() + 0.5 for _ in range(links)]
    sum_of_lengths = sum(lengths_of_links)
    lengths_of_links = [3 * length * width / sum_of_lengths / 2 for length in lengths_of_links]

    # making list of lengths of links
    heights_of_links = [random() + 0.5 for _ in range(links)]
    sum_of_lengths = sum(heights_of_links)
    heights_of_links = [3 * length * height / sum_of_lengths / 2 for length in heights_of_links]

    # TODO: make it better
    for link in range(links):
        ellipse(screen,

                (0, 0, 0),

                (x - int(sum(lengths_of_links[:link]) / 3 * 2) - int(lengths_of_links[link]) * 2,
                 y + int(sum(heights_of_links[:link]) / 3 * 2) - int(heights_of_links[link]) * 2,
                 int(lengths_of_links[link]) * 2,
                 int(heights_of_links[link]) * 2),

                1)


def draw_doghouse(x: int, y: int, length: int, width: int, height: int, roof_height: int):
    """
    Draws a doghouse
    @param x: x coordinate of the lowers point of doghuose
    @param y: y coordinate of the lowers point of doghuose
    @param length: length of the doghouse
    @param width: width of the doghouse
    @param height: height of the doghouse
    @param roof_height: height of the roof of the doghouse
    @return: None
    """

    def poly_with_outline(points, color):
        """
        Draws a polygon with outline
        @param points: points that the polygon passes through
        @param color: the fill color of the polygon
        """
        polygon(screen, color, points)
        polygon(screen, (0, 0, 0), points, 1)

    angle1, angle2 = 60, 110  # some params

    draw_parallelogram(x, y, -width, -height, angle1, outline=1)  # front
    draw_parallelogram(x, y, length, -height, angle2, outline=1)  # right

    # roof
    roof_front = (
        (x,
         y - height),

        (int(x - width * sin(radians(angle1))),
         int(y - width * cos(radians(angle1)) - height)),

        (int(x - width * sin(radians(angle1)) / 2),
         int(y - width * cos(radians(angle1)) // 2 - height - roof_height)),
    )

    roof_right = (
        (x,
         y - height),

        (int(x - width * sin(radians(angle1)) / 2),
         int(y - width * cos(radians(angle1)) / 2 - height - roof_height)),

        (int(x - width * sin(radians(angle1)) / 2 + length * cos(radians(angle2 - 90))),
         int(y - width * cos(radians(angle1)) / 2 - height - roof_height + length * cos(radians(angle2)))),

        (int(x + length * sin(radians(angle2))),
         int(y - height + length * cos(radians(angle2)))),
    )

    poly_with_outline(roof_front, (255, 255, 0))
    poly_with_outline(roof_right, (255, 255, 0))

    # black hole
    radius = int(sqrt(width * width + height * height) * sin(radians(angle1)) / 4)
    circle(screen, (0, 0, 0),
           (int(x - width * sin(radians(angle1)) / 2), int(y - height / 2 - width * cos(radians(angle1)) / 2)), radius)

    # chain
    draw_chain(int(x - width * sin(radians(angle1)) / 2) - radius // 2,
               int(y - height / 2 - width * cos(radians(angle1)) / 2 + radius),
               width,
               height // 2,
               10)


def draw_dog(x, y, width, height, color=(120, 120, 120), mirror=False):
    def convertx(x_: Union[int, float]):
        """
        Magic x coordinate transformation to the coordinate system of a bulldog
        """
        return int(x_ * width / 179)

    def converty(y_: Union[int, float]):
        """
        Magic y coordinate transformation to the coordinate system of a bulldog
        """
        return int(y_ * height / 143)

    def myellipse(x_: Union[int, float], y_: Union[int, float], w: Union[int, float], h: Union[int, float],
                  outline: int = 0, color_: Tuple[int, int, int] = color):
        """
        draws ellipse in bulldog's coordinate system
        @param x_: x coordinate of upper-left corner of the described rectangle of the ellipse
        @param y_: y coordinate of upper-left corner of the described rectangle of the ellipse
        @param w: width of the described rectangle of the ellipse
        @param h: height of the described rectangle of the ellipse
        @param outline: width of the outline of the described rectangle of the ellipse
        @param color_: color of the ellipse
        @return: None
        """
        ellipse(surface, color_,
                (int(width * x_ / 179), int(height * y_ / 143), int(w * width / 179), int(h * height / 143)))
        if outline:
            ellipse(surface, (0, 0, 0),
                    (
                        int(width * x_ / 179), int(height * y_ / 143), int(w * width / 179),
                        int(h * height / 143)),
                    outline)

    def draw_eyes():
        """
        Draws a eyes
        @return: None
        """
        myellipse(28.5, 25, 14.5, 5, color_=(255, 255, 255), outline=1)
        myellipse(55.5, 25, 14.5, 5, color_=(255, 255, 255), outline=1)

        circle(surface, (0, 0, 0), (convertx(35.75), converty(27.5)), min(convertx(2.5), converty(2.5)))
        circle(surface, (0, 0, 0), (convertx(35.75 + 27), converty(27.5)), min(convertx(2.5), converty(2.5)))

    def draw_ears():
        """
        Draws a ears
        @return: None
        """
        myellipse(8, 0, 18, 21, 1)
        myellipse(73, 0, 18, 21, 1)

    def draw_mouth():
        """
        Draws a mouth
        @return: None
        """
        arc(surface, (0, 0, 0), (convertx(29), converty(49), convertx(41), converty(35)), pi / 15, pi - pi / 15)

        left_tooth = (
            (convertx(37.5), converty(52)),
            (convertx(31), converty(59)),
            (convertx(33.5), converty(45)),

        )
        right_tooth = (
            (convertx(61.5), converty(52)),
            (convertx(68), converty(59)),
            (convertx(65.5), converty(45)),

        )

        draw_with_outline(polygon, surface, (255, 255, 255), left_tooth)
        draw_with_outline(polygon, surface, (255, 255, 255), right_tooth)

    def draw_head():
        """
        Draws a head
        @return: None
        """
        # head
        draw_with_outline(rect, surface, color,
                          (int(width * 17 / 179), 0, int(width * 65 / 179), int(height * 72 / 143)))

        # eyes
        draw_eyes()

        # ears
        draw_ears()

        # mouth
        draw_mouth()

    def draw_front_leg(x_, y_):
        """
        Draws a front leg
        @param x_: x coordinate of a certain point of the front leg where drawing starts
        @param y_: y coordinate of a certain point of the front leg where drawing starts
        @return: None
        """
        myellipse(x_, y_, 35, 66)
        myellipse(x_ - 8, y_ + 63, 33, 13)

    def draw_hind_leg(x_, y_):
        """
        Draws a hind leg
        @param x_: x coordinate of a certain point of the hind leg where drawing starts
        @param y_: y coordinate of a certain point of the hind leg where drawing starts
        @return: None
        """
        myellipse(x_, y_, 38, 44)
        myellipse(x_ + 28, y_ + 32, 12, 41)
        myellipse(x_ + 11, y_ + 70, 26, 13)

    def draw_torso(x_, y_):
        """
        Draws a torso
        @param x_: x coordinate of a certain point of the torso where drawing starts
        @param y_: y coordinate of a certain point of the torso where drawing starts
        @return: None
        """
        myellipse(x_, y_, 101, 61)
        myellipse(x_ + 73, y_ - 10, 66, 45)

    def draw_body():
        """
        Draws a body of the bulldog
        @return: None
        """
        # front legs
        draw_front_leg(66, 68)
        draw_front_leg(9, 45)

        # hind legs
        draw_hind_leg(138, 34)
        draw_hind_leg(96, 15)

        # torso
        draw_torso(21, 25)

    surface = pygame.Surface((width, height), pygame.SRCALPHA)

    draw_body()
    draw_head()

    if DEBUG:
        rect(surface, (255, 0, 0), (x, y, width, height), 1)

    screen.blit(pygame.transform.flip(surface, mirror, False), (x, y))


def draw_net(step_x=100, step_y=100):
    """
    Draws a debug grid with the specified step
    @param step_x: grid step by the x-axis
    @param step_y: grid step by the y-axis
    @return: None
    """
    for x_coord in range(0, SCREEN_WIDTH, step_x):
        line(screen, (255, 0, 0), (x_coord, 0), (x_coord, SCREEN_HEIGHT), 1)
    for y_coord in range(0, SCREEN_HEIGHT, step_y):
        line(screen, (255, 0, 0), (0, y_coord), (SCREEN_WIDTH, y_coord), 1)


def draw_picture_v1():
    """
    Draws the first picture
    @return: None
    """
    draw_bg()
    draw_doghouse(650, 700, SCREEN_WIDTH // 6, SCREEN_WIDTH // 7, SCREEN_HEIGHT // 7, SCREEN_HEIGHT // 9)
    draw_dog(100, 500, 179 * 27 // 17, 143 * 27 // 17)

    if DEBUG:
        draw_net()


def draw_picture_v2():
    """
    Draws the second picture
    @return: None
    """
    draw_bg()

    draw_fence(0, 150, 250, 300)

    draw_fence(200, 10, 650, 350)

    draw_dog(600, 400, 179 * 20 // 17, 143 * 20 // 17, mirror=True)

    draw_doghouse(600, 700, SCREEN_WIDTH // 6, SCREEN_WIDTH // 7, SCREEN_HEIGHT // 7, SCREEN_HEIGHT // 9)

    draw_dog(120, 550, 179 * 27 // 17, 143 * 27 // 17, mirror=True)

    draw_dog(70, 335, 179 * 27 // 17, 143 * 27 // 17)

    draw_dog(500, 550, 179 * 27 // 8, 143 * 27 // 8)

    if DEBUG:
        draw_net()


def eventloop():
    """
    Eventloop
    @return: None
    """
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True


clock = pygame.time.Clock()

# draw_picture_v1()

draw_picture_v2()

pygame.display.update()

eventloop()

pygame.quit()
