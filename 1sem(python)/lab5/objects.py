from math import cos, sin, asin, sqrt, pi
from random import choice, uniform, random
from time import perf_counter
from typing import Union

import pygame
from pygame import Rect, Surface
from pygame.draw import circle, line, polygon, rect

from settings import *


class Ball:
    """
    Ball object
    """

    def __init__(self, screen, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2,
                 radius: Union[float, int] = 50, vx: Union[float, int] = 0, vy: Union[float, int] = 0,
                 fixed=False, color=Colors.GREEN, lifetime=float('inf'),
                 decay=0.9):
        self.x = x  # x coordinate of the ball
        self.y = y  # y coordinate of the ball
        self.radius = radius  # radius of the ball
        self.vx = vx  # x speed of the ball
        self.vy = vy  # y speed of the ball
        self.decay = decay
        self.color = color  # color of the ball
        self.fixed = fixed
        self.scores = 1  # scores per click
        self.screen = screen  # screen
        self.lifetime = lifetime
        self.createtime = perf_counter()
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
        :return: True if it must die else False
        """
        dx = self.vx * delta_t
        dy = self.vy * delta_t + GRAVITY * delta_t * delta_t / 2
        self.vy += GRAVITY * delta_t
        self.collide_with_display(dx, dy)
        self.draw()
        if perf_counter() - self.createtime >= self.lifetime:
            return True
        return False

    def spawn_bomb(self):
        return Bomb(self.screen, self.x, self.y)

    def check_collision(self, x, y):
        """
        Checks collision with point (x, y)
        :param x:
        :param y:
        :return:
        """
        return (self.x - x) * (self.x - x) + (self.y - y) * (self.y - y) <= self.radius * self.radius

    def check_collision_with_ball(self, ball):
        return (self.x - ball.x) * (self.x - ball.x) + (self.y - ball.y) * (self.y - ball.y) <= \
               (self.radius + ball.radius) * (self.radius + ball.radius)

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
        Handles collision with edges of screen
        :param dx: increment of the x
        :param dy: increment of the y
        :return:
        """
        if self.check_collision_x(0, dx):
            self.move(-dx - self.x + self.radius, 0)
            self.vx *= -self.decay

        elif self.check_collision_x(SCREEN_WIDTH):
            self.move(-dx + SCREEN_WIDTH - self.x - self.radius, 0)
            self.vx *= -self.decay

        elif self.check_collision_y(0, dy):
            self.move(0, -dy - self.y + self.radius)
            self.vy *= -self.decay

        elif self.check_collision_y(SCREEN_HEIGHT):
            self.move(0, -dy + SCREEN_HEIGHT - self.y - self.radius)
            self.vy *= -self.decay
        else:
            self.move(dx, dy)
        if abs(self.vy) <= CRITICAL_SPEED and self.y >= SCREEN_HEIGHT - self.radius - CRITICAL_DISTANCE:
            self.vy = 0
            self.y = SCREEN_HEIGHT - self.radius


class Square:
    def __init__(self, screen, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2,
                 radius: Union[float, int] = 50, vx: Union[float, int] = 0, vy: Union[float, int] = 0,
                 fixed=False, color=Colors.GREEN, lifetime=float('inf'),
                 decay=0.9):
        self.x = x  # x coordinate of the ball
        self.y = y  # y coordinate of the ball
        self.radius = radius  # radius of the ball
        self.vx = vx  # x speed of the ball
        self.vy = vy  # y speed of the ball
        self.decay = decay
        self.color = color  # color of the ball
        self.fixed = fixed
        self.scores = 1  # scores per click
        self.screen = screen  # screen
        self.lifetime = lifetime
        self.createtime = perf_counter()
        # drawing ball
        self.surface = Surface((2 * self.radius, 2 * self.radius), pygame.SRCALPHA)
        circle(self.surface, self.color, (self.radius, self.radius), self.radius)
        self.draw()
        self.spawntime = None

    def draw(self):
        rect(self.screen, self.color, Rect(self.x, self.y, self.radius, self.radius))

    def spawn_bomb(self):
        return Bomb(self.screen, self.x + self.radius / 2, self.y + self.radius / 2)

    def step(self, dt):
        if self.spawntime is None:
            self.spawntime = perf_counter()
        if perf_counter() >= self.spawntime + 1:
            self.spawntime = None
            self.x = uniform(0, SCREEN_WIDTH - self.radius)
            self.y = uniform(0, SCREEN_HEIGHT - self.radius)


class Bomb:
    def __init__(self, screen, x, y, radius=30):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = 50
        self.radius = 10

    def step(self, dt):
        self.y += dt * self.speed
        rect = Rect(self.x, self.y, self.radius, self.radius)
        if not rect.colliderect(self.screen.get_rect()):
            return False
        return True

    def draw(self):
        circle(self.screen, choice(all_colors), (self.x, self.y), self.radius)


class Laser_quant():
    def __init__(self, screen, x=SCREEN_WIDTH // 2, y=SCREEN_HEIGHT // 2,
                 length: Union[float, int] = 50, vx: Union[float, int] = 0, vy: Union[float, int] = 0,
                 color=Colors.GREEN, lifetime=float('inf')):
        self.x = x  # x coordinate of the ball
        self.y = y  # y coordinate of the ball
        self.length = length  # radius of the ball
        self.vx = vx * 3  # x speed of the ball
        self.vy = vy * 3  # y speed of the ball
        self.v = sqrt(self.vx ** 2 + self.vy ** 2)
        self.color = color  # color of the ball
        self.screen = screen  # screen
        self.lifetime = lifetime
        self.createtime = perf_counter()
        # drawing ball
        self.surface = Surface((2 * self.length, 2 * self.length), pygame.SRCALPHA)
        circle(self.surface, self.color, (self.length, self.length), self.length)
        self.draw()

    def draw(self):
        """
        Draws the ball
        :return: None
        """
        line(self.screen,
             self.color,
             (self.x, self.y),
             (self.x + self.length * self.vx / self.v, self.y + self.length * self.vy / self.v),
             5
             )

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
        :return: True if it must die else False
        """
        dx = self.vx * delta_t
        dy = self.vy * delta_t
        self.move(dx, dy)
        self.draw()
        if perf_counter() - self.createtime >= self.lifetime:
            return True
        return False

    def check_collision_with_ball(self, ball):
        return (self.x - ball.x) * (self.x - ball.x) + (self.y - ball.y) * (self.y - ball.y) <= \
               ball.radius * ball.radius

    def collide_with_display(self, dx, dy):
        """
        Handles collision with edges of screen
        :param dx: increment of the x
        :param dy: increment of the y
        :return:
        """
        pass


class Cannon:
    def __init__(self, screen, x, y, speed=400, color=(0, 128, 0)):
        self.screen = screen  # screen
        self.x = x  # x coordinate of the cannon
        self.y = y  # x coordinate of the cannon
        self.speed = speed
        self.color = color
        self.angle = 0  # angle over horizon clockwise
        self.startlen = 50  # initial length of the cannon
        self.endlen = 200  # max length of the cannon
        self.power = 0  # current loading percent
        self.reloading_speed = 35
        self.max_bullet_speed = 2000
        self.bullet_size = 20

        self.bullettypes = [Ball, Laser_quant]
        self.bullettype = 0

    def change_bullettype(self):
        self.bullettype += 1
        self.bullettype %= len(self.bullettypes)

    def draw(self):
        """
        Draws a cannon
        :return: None
        """
        color = (255 * self.power // 100, 0, 0)  # чем заряженнее, тем краснее
        # gun
        line(self.screen,
             color,
             (self.x, self.y),
             (self.x + (self.startlen + (self.endlen - self.startlen) * self.power / 100) * cos(self.angle),
              self.y + (self.startlen + (self.endlen - self.startlen) * self.power / 100) * sin(self.angle)),
             5
             )

        # tower
        polygon(self.screen, self.color,
                ((self.x, self.y),
                 (self.x - 20, self.y + 30),
                 (self.x + 20, self.y + 30)
                 )
                )

        # body
        polygon(self.screen, self.color, (
            (self.x - 50, self.y + 30),
            (self.x - 35, self.y + 50),
            (self.x + 35, self.y + 50),
            (self.x + 50, self.y + 30),
        ))

        # wheels
        circle(self.screen, (105, 105, 105), (self.x - 35, self.y + 47), 11)
        circle(self.screen, (105, 105, 105), (self.x - 12, self.y + 47), 11)
        circle(self.screen, (105, 105, 105), (self.x + 12, self.y + 47), 11)
        circle(self.screen, (105, 105, 105), (self.x + 35, self.y + 47), 11)

    def aiming(self, x, y):
        """
        Changes aiming angle of the cannon
        :param x: x coordinate of the mouse cursor
        :param y: y coordinate of the mouse cursor
        :return: None
        """
        r = sqrt((self.x - x) * (self.x - x) + (self.y - y) * (self.y - y))
        self.angle = asin((y - self.y) / r)
        if (self.x - x) > 0:
            self.angle = pi - self.angle

    def reloading(self, delta_t):
        """
        Increment self.power by self.speed*delta_t
        :param delta_t: increment of the time
        :return: None
        """
        if self.power < 100:
            self.power = min(self.power + self.reloading_speed * delta_t, 100)

    def shot(self):
        """
        Shoots a ball
        :return: Ball object of launched ball
        """
        ball = self.bullettypes[self.bullettype](
            self.screen,
            self.x + (self.startlen + (self.endlen - self.startlen) * self.power / 100) * cos(self.angle),
            self.y + (self.startlen + (self.endlen - self.startlen) * self.power / 100) * sin(self.angle),
            self.bullet_size,
            self.max_bullet_speed * self.power / 100 * cos(self.angle),
            self.max_bullet_speed * self.power / 100 * sin(self.angle),
            color=choice(all_colors),
            lifetime=2
        )
        self.power = 0  # setting power to zero
        return ball

    def move_right(self, dt):
        self.x += self.speed * dt


def generate_targets(screen, n=10, min_radius=15, max_radius=40, min_speed=500, max_speed=800):
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
        _type = Ball if random() > 0.3 else Square
        new_ball = _type(
            screen,
            min_radius + (SCREEN_WIDTH - 2 * radius) * random(),
            min_radius + (SCREEN_HEIGHT - 2 * radius) * random(),
            radius,
            speed * cos(angle),
            speed * sin(angle),
            color=choice(all_colors),
        )

        targets.append(new_ball)
    return targets
