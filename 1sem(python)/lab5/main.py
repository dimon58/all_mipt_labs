from random import random

import pygame

from objects import Ball, Cannon, generate_targets
from settings import *


def start_message():
    print('Управление основной(зеленой) пушкой AD')
    print('Управление вспомогательной(красной) пушкой LEFT RIGHT')
    print('Переключение между режимами стрельбы F5')
    print('Вторая пушка - компаньон')
    print('Вдвое медленее перезаряжается и передвигается')
    print('И её нельзя переключить во второй режим стрельбы')


start_message()


class EventLoop:
    def __init__(self):
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.finished = False
        self.target_balls: list[Ball] = generate_targets(self.screen)
        self.bullets: list[Ball] = []
        self.bombs = []
        self.cannon = Cannon(self.screen, 100, SCREEN_HEIGHT - 58)
        self.comrad = Cannon(self.screen, 300, SCREEN_HEIGHT - 58, speed=200, color=(128, 0, 0))
        self.clicked = False
        self.reloading = False
        self.shots = 0  # number of shoots

    def restart(self):
        """
        Restarts the game, its wrapped __init__()
        :return: None
        """
        self.__init__()

    def win(self):
        """
        Execute this scrips if all targets destroyed
        :return: None
        """
        # draws congratulation
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', 45)
        textsurface = font.render(f'Победа за {self.shots} выстрелов', False, (255, 0, 0))
        self.screen.blit(textsurface, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 - 50))
        pygame.display.update()
        pygame.time.delay(2000)

    def run(self):
        while not self.finished:
            # get delta time after last iteration
            delta_t = self.clock.get_time() / 1000
            # clear the screen
            self.screen.fill(BG_COLOR)
            # iter in events
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.finished = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    # handle click
                    self.clicked = True
                    self.reloading = True
                    self.cannon.aiming(*event.pos)
                    self.comrad.aiming(*event.pos)

                if event.type == pygame.MOUSEMOTION:
                    # aiming cannon to cursor
                    if self.clicked:
                        self.cannon.aiming(*event.pos)
                        self.comrad.aiming(*event.pos)

                if event.type == pygame.MOUSEBUTTONUP:
                    # shooting
                    self.clicked = False
                    self.reloading = False
                    self.shots += 1
                    self.cannon.aiming(*event.pos)
                    self.comrad.aiming(*event.pos)
                    self.bullets.append(self.cannon.shot())
                    self.bullets.append(self.comrad.shot())
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F5:
                        self.cannon.change_bullettype()
            # moving cannon
            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[pygame.K_a]:
                self.cannon.move_right(-self.clock.get_time() / 1000)
            if pressed_keys[pygame.K_d]:
                self.cannon.move_right(self.clock.get_time() / 1000)

            if pressed_keys[pygame.K_LEFT]:
                self.comrad.move_right(-self.clock.get_time() / 1000)
            if pressed_keys[pygame.K_RIGHT]:
                self.comrad.move_right(self.clock.get_time() / 1000)

            for bullet_number, bullet in enumerate(self.bullets):

                # checking lifetime
                if bullet.step(delta_t):
                    self.bullets.pop(bullet_number)
                    continue

                # checking collision with targets
                for target_number, target in enumerate(self.target_balls):
                    if bullet.check_collision_with_ball(target):
                        self.bullets.pop(bullet_number)
                        self.target_balls.pop(target_number)
                        break

                # drawing bullets if it alive
                bullet.draw()

            # check win
            if not self.target_balls:
                self.win()
                self.restart()

            # move targets
            for ball in self.target_balls:
                ball.step(delta_t)
                if random() > 0.99988:
                    self.bombs.append(ball.spawn_bomb())
                ball.draw()

            # move bombs
            for num, bomb in enumerate(self.bombs):
                if not bomb.step(delta_t):
                    self.bombs.pop(num)
                bomb.draw()

            # increment powwer of the cannon
            if self.reloading:
                self.cannon.reloading(delta_t)
                self.comrad.reloading(delta_t / 2)

            # drawing
            self.cannon.draw()
            self.comrad.draw()
            pygame.display.set_caption(str(self.clock.get_fps()))
            pygame.display.update()
            self.clock.tick(FPS)


def main():
    loop = EventLoop()
    loop.run()


if __name__ == '__main__':
    main()
