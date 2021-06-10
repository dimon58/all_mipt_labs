from time import time

import pygame
import os
from objects import generate_targets
from settings import *

pygame.init()

FPS = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.font.init()

if not os.path.exists(SCORE_FILE):
    file = open(SCORE_FILE, 'w')
    file.close()

class ScoreBoard:
    def __init__(self, x, y, fontsize=50, font='Comic Sans MS'):
        """

        :param x: x coordinate of left corner of the scoreboard
        :param y: y coordinate of left corner of the scoreboard
        :param fontsize: size of the font
        :param font: font
        """
        self.x = x
        self.y = y
        self.scores = 0
        self.font = pygame.font.SysFont(font, fontsize)
        self.textsurface = self.font.render(f'{self.scores} Очков', False, (255, 0, 0))
        self.draw()

    def increment_scores(self, delta):
        """
        Update scoreboard with delta
        :param delta: increment of the scores
        :return: None
        """
        self.scores += delta
        self.textsurface = self.font.render(f'{self.scores} Очков', False, (255, 0, 0))

    def draw(self):
        """
        Draws scoreboard
        :return:
        """
        screen.blit(self.textsurface, (100, 100))


class EventLoop:
    def __init__(self, score_board, targets):
        """
        :param score_board: scoreboard object
        :param targets: list of the targets
        """
        self.Name = 'LOL'
        self.Name = input('Введите имя: ')
        self.targets = targets
        pygame.display.update()
        self.clock = pygame.time.Clock()
        self.finished = False
        self.start_time = self.end_time = time()
        self.score_board = score_board

    def mouse_handler(self, event):
        """
        Handle mouseclick
        :param event: click event
        :return: None
        """
        for number, ball in enumerate(self.targets):
            # removes target is clicked
            if inc := ball.click_handler(*event.pos):
                self.targets.pop(number)
                self.score_board.increment_scores(inc)

    def win(self):
        """
        Draws pretty win screen
        :return: None
        """
        self.end_time = time()
        self.finished = True

        screen.fill(BG_COLOR)

        # draws congratulation
        myfont = pygame.font.SysFont('Comic Sans MS', 100)
        textsurface = myfont.render(f'Победа за {round(self.end_time - self.start_time, 1)} сек', False, (255, 0, 0))
        screen.blit(textsurface, (SCREEN_WIDTH // 2 - 450, SCREEN_HEIGHT // 2 - 50))

        # draws scoreboard
        self.score_board.draw()

        pygame.display.update()
        pygame.time.delay(2000)

        # write scores in scores.txt
        # format: player_name number_of_targets time
        with open(SCORE_FILE, 'a') as file:
            file.write(f'{self.Name} {self.score_board.scores} {round(self.end_time - self.start_time, 1)}\n')

    def run(self):
        """
        run eventloop until not self.finished
        :return:
        """
        while not self.finished:
            # clear the screen
            screen.fill(BG_COLOR)
            # iter in events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_handler(event)

            # moves all targets and check win
            if self.targets:
                for target in self.targets:
                    target.step(self.clock.get_time() / 1000)
            else:
                self.win()

            pygame.display.set_caption(str(self.clock.get_fps()))
            self.score_board.draw()

            pygame.display.update()
            self.clock.tick(FPS)


def main():
    score_board = ScoreBoard(0, 0)
    loop = EventLoop(score_board, generate_targets(screen, 15))
    loop.run()
    pygame.quit()


if __name__ == '__main__':
    main()
