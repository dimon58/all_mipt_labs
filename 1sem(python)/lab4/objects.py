from math import pi, sin, cos, tau
from random import uniform, random, choice

import pygame
from pygame import Surface
from pygame.draw import circle, polygon
from pygame.transform import rotate

from settings import *


class Ball:
    """
    Ball object
    """

    def __init__(self, screen, x, y, radius, vx, vy, color=GREEN):
        self.x = x  # x coordinate of the ball
        self.y = y  # y coordinate of the ball
        self.radius = radius  # radius of the ball
        self.vx = vx  # x speed of the ball
        self.vy = vy  # y speed of the ball
        self.color = color  # color of the ball
        self.scores = 1  # scores per click
        self.screen = screen  # screen

        # drawing ball
        self.surface = Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        circle(self.surface, self.color, (self.radius, self.radius), self.radius)
        self.draw()

    def draw(self):
        """
        Draws the ball
        :return: None
        """
        self.screen.blit(self.surface, (self.x - self.radius, self.y - self.radius))

    def move(self, dx, dy):
        """
        Moves the ball
        :param dx: x increment
        :param dy: y increment
        :return: None
        """
        self.x += dx
        self.y += dy

    def step(self, delta_t):
        """
        Moves the ball in the time by delta_t
        :param delta_t: increment of time
        :return: None
        """
        dx = self.vx * delta_t
        dy = self.vy * delta_t
        self.collide_with_display(dx, dy)
        self.draw()

    def check_collision(self, x, y):
        """
        Checks collision with point (x, y)
        :param x:
        :param y:
        :return:
        """
        return (self.x - x) * (self.x - x) + (self.y - y) * (self.y - y) <= self.radius * self.radius

    def check_collision_x(self, x, dx=0):
        """
        Checks collision with line with x coordinate = x
        :param x: const
        :param dx: increment of the x
        :return: None
        """
        return abs(self.x - x - dx) <= self.radius

    def check_collision_y(self, y, dy=0):
        """
        Checks collision with line with y coordinate = y
        :param y: const
        :param dy: increment of the y
        :return: None
        """
        return abs(self.y - y - dy) <= self.radius

    def collide_with_display(self, dx, dy):
        """
        Hadles collision with edges of screen
        :param dx: increment of the x
        :param dy: increment of the y
        :return:
        """
        if self.check_collision_x(0, dx):
            self.move(-dx - self.x + self.radius, 0)
            self.vx *= -1

        elif self.check_collision_x(SCREEN_WIDTH):
            self.move(-dx + SCREEN_WIDTH - self.x - self.radius, 0)
            self.vx *= -1

        elif self.check_collision_y(0, dy):
            self.move(0, -dy - self.y + self.radius)
            self.vy *= -1

        elif self.check_collision_y(SCREEN_HEIGHT):
            self.move(0, -dy + SCREEN_HEIGHT - self.y - self.radius)
            self.vy *= -1

        else:
            self.move(dx, dy)

    def click_handler(self, x, y):
        """
        :param x: x coordinate of clicked point
        :param y: y coordinate of clicked point
        :return: scores, if you clicked on object, else 0
        """
        return self.scores if self.check_collision(x, y) else 0


class Triangle(Ball):
    """
    Triangle object
    """

    def __init__(self, screen, x, y, radius, vx, vy, color=GREEN):
        super().__init__(screen, x, y, radius, 1.5 * vx, 1.5 * vy, color)

        # clear the drawing surface
        self.surface = Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)

        # draw triangle
        polygon(self.surface, self.color,
                [
                    (self.radius, 0),
                    (self.radius * (1 + sin(pi / 3)), self.radius * (1 + cos(pi / 3))),
                    (self.radius * (1 - sin(pi / 3)), self.radius * (1 + cos(pi / 3))),
                ]
                )

        # it helps with rotation
        self.angle = 0
        self.angle_inc_speed = 2000 * (random() + 0.5) * choice([1, -1])

        # scores per click
        self.scores = 3

    def __draw(self, delta_t):
        """
        Draws triangle object
        :param delta_t: it helps with rotation
        :return:
        """

        # rotate angle
        self.angle += self.angle_inc_speed * delta_t % tau

        # drawing
        self.screen.blit(rotate(self.surface, self.angle), (self.x - self.radius, self.y - self.radius))

    def step(self, delta_t):
        """
        Moves the triangle in the time by delta_t
        :param delta_t: increment of time
        :return: None
        """
        dx = self.vx * delta_t
        dy = self.vy * delta_t
        self.collide_with_display(dx, dy)
        self.__draw(delta_t)


def generate_targets(screen, n=10, min_radius=20, max_radius=100, min_speed=500, max_speed=800):
    """
    Makes list of the targets
    :param screen: screen
    :param n: number of the targets
    :param min_radius: minimum radius of the target
    :param max_radius: maximum radius of the target
    :param min_speed: minimum speed of the target
    :param max_speed: minimum speed of the target
    :return: list of the targets
    """
    targets = []
    for n in range(n):
        radius = uniform(min_radius, max_radius)
        speed = uniform(min_speed, max_speed)
        angle = uniform(0, 2 * pi)
        _type = Ball if random() > 0.7 else Triangle
        new_ball = _type(
            screen,
            min_radius + (SCREEN_WIDTH - 2 * radius) * random(),
            min_radius + (SCREEN_HEIGHT - 2 * radius) * random(),
            radius,
            speed * cos(angle),
            speed * sin(angle),
            color=choice(COLORS)
        )

        targets.append(new_ball)
    return targets
