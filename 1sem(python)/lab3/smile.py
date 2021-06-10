import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))

screen.fill((255, 255, 255))

# body
circle(screen, (255, 255, 0), (400, 400), 250)

# eyes
circle(screen, (255, 0, 0), (300, 300), 50)
circle(screen, (0, 0, 0), (300, 300), 20)
circle(screen, (255, 0, 0), (500, 300), 35)
circle(screen, (0, 0, 0), (500, 300), 20)

line(screen, (0, 0, 0), (450, 300), (600, 150), 20)
line(screen, (0, 0, 0), (350, 275), (200, 150), 30)

# mouth
rect(screen, (0, 0, 0), (250, 500, 300, 50))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
