import sys
from math import pi, cos
from random import choice
from time import perf_counter

import numpy as np
import pygame
from pygame.draw import polygon

import src.gameobjects as gameobjects
from Engine.Scene.camera import Camera, Operator, TargetingMethod, MidPoint
from Engine.Scene.gamescene import Level
from Engine.Scene.states import State
from Engine.apps import MicroApp
from Engine.gui.in_game_menu import InGameMenu
from Engine.gui.overlays import FPS, DevMode, HealthBar, WinHandler
from Engine.utils.utils import load_music_from_folder
from settings import SONG_END, game_music_volume, music_volume, global_volume
from settings import game_music_path, SCREEN_WIDTH, SCREEN_HEIGHT, DEVMODE
from .persons import load_characters

gameobjects.register()
load_characters()


def dev_message():
    print('Включение оверлея разработчика F3')
    print('Перезапуск камеры R')


class LoadingScreen(MicroApp):
    """
    Приложение загрузочного экрана
    """

    def __init__(self, screen: pygame.Surface, clock: pygame.time.Clock, lifetime=6):
        super(LoadingScreen, self).__init__(screen, clock)
        self.end_time = perf_counter() + lifetime
        # Фоновый цвет
        self.background_color = (100, 100, 254)
        # Цвета, которыми будут переливаться буквы
        self.colors = [(212, 6, 6), (238, 156, 0), (227, 255, 0), (6, 191, 0), (0, 26, 152)]

        # Музыка на загрузочном экране
        self.bgmusic = pygame.mixer.Sound('Resources/Music/lodingscreen.ogg')

        # Цыганская магия, которая рисует черный прямоугольник с вырезанными прозраычными буквами
        # Точнее создает трафарет
        # Лучше не вникать (реально)
        # Инициализация шрифта
        self.font = pygame.font.SysFont('maturascriptcapitals', SCREEN_HEIGHT // 5)
        # Рисование просто букв цвета temp_color на поверхности
        temp_color = (0, 0, 255)
        self.temp = self.font.render('Need For Otl 10', False, temp_color)
        # Центрирование поверхности на экране
        self.rect = self.temp.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        # Сама поверхность для трафорента текста
        self.text_surface = pygame.Surface(self.rect.size).convert_alpha()
        # Заливаем её цветом, который будем превращать в прозрачный
        self.text_surface.fill((1, 1, 1))
        # Рисуем текст на ней
        self.text_surface.blit(self.temp, (0, 0))
        # Меняем temp_color на прозрачную зону
        self.text_surface.set_colorkey(temp_color)

        # Поверхность на которой будет рисоваться анимированные буквы
        # Потом ее рисуем на экране
        # Нужно, чтобы можно было легко реализовать цыганскую магию
        self.camera_surface = pygame.Surface(self.rect.size).convert_alpha()

        # Технические перемнные
        # Сдвиг переливов (мб при больших значениях упадет точность, но это займет много времени)
        self.position = 0
        # Скорость движения полос
        self.speed = 70
        # Высота полос (она же высота текста)
        self.height_of_strip = self.text_surface.get_height()
        # Кол-во полос на тексте (должно быть кратно кол-ву цветов в self.colors, иначе не будет циклического перехода)
        self.num_strips = 5 * len(self.colors)
        # Длина полос (тоже вычисляется через цыганскую магию)
        # Лучше не трогать
        self.len_of_strip = (self.camera_surface.get_width() + self.height_of_strip * cos(pi / 4)) / (
                self.num_strips - 1)

    def run_once(self):
        self.bgmusic.play()

    def prepare_text(self):
        """
        Рисует буквы с переливающимся цветом
        :return:
        """

        # Рисуем полоски (параллелограммы)
        for strip in range(self.num_strips):
            x_coord = (strip * self.len_of_strip + self.position) % (
                    self.len_of_strip * self.num_strips) - self.len_of_strip
            coords = (
                (x_coord, 0),
                (x_coord - self.height_of_strip * cos(pi / 4), self.height_of_strip),
                (x_coord + self.len_of_strip - self.height_of_strip * cos(pi / 4), self.height_of_strip),
                (x_coord + self.len_of_strip, 0)
            )
            polygon(self.camera_surface, self.colors[strip % len(self.colors)], coords)

        # Вырезаем буквы
        self.camera_surface.blit(self.text_surface, (0, 0))

        # Делаем прозрачным то, что нужно
        # удалив это строчку, можно накинуть 20 фпс
        self.camera_surface.set_colorkey((1, 1, 1))

    def atexit(self):
        """
        Тормозим фоновую музыку
        :return: None
        """
        self.bgmusic.stop()

    def step(self, dt):
        """
        Двигаем полоски
        :param dt: квант времени
        :return:
        """
        self.position += self.speed * dt

    def draw(self):
        """
        Рисуем всё на экране
        :return:
        """
        self.screen.fill(self.background_color)
        self.prepare_text()
        self.screen.blit(self.camera_surface, self.rect.topleft)

        pygame.display.update()


game_songs = load_music_from_folder(game_music_path)
pygame.mixer.music.set_endevent(SONG_END)


def next_song():
    pygame.mixer.music.unload()
    pygame.mixer.music.load(choice(game_songs))
    pygame.mixer.music.play()


class Game(MicroApp):
    def __init__(self, screen, clock, username):
        super(Game, self).__init__(screen, clock, lifetime=float('inf'))
        self.username = username
        self.FPS = 0

        self.scene = Level(Game)
        self.scene.load_level(username)

        self.camera = Camera(self.screen, distance=16)
        self.camera_operator = Operator(camera=self.camera)

        self.overlays = {
            'FPS': FPS(self.screen, self.clock),
            'DevMode': DevMode(self.screen, self),
            'HealthBar_player_1': HealthBar(self.screen, self.clock, self.scene.player, self.camera, left=True),
            'HealthBar_player_2': HealthBar(self.screen, self.clock, self.scene.entities[0] if self.scene.entities \
                else self.scene.player, self.camera, left=False),
            'WinHandler': WinHandler(self.screen, self.scene)
        }

        self.buttons = []
        self.DEVMODE = DEVMODE

        if DEVMODE:
            dev_message()

        pygame.mixer.music.stop()
        pygame.mixer.music.set_volume(game_music_volume * music_volume * global_volume)

    def draw(self):
        self.camera.view(self.scene)
        if self.DEVMODE:
            self.camera.devview(self.scene)

        self.camera.show(self.DEVMODE)

        for overlay in self.overlays.values():
            overlay.draw()

        for button in self.buttons:
            button.draw()

        pygame.display.update()

    def step(self, dt):
        self.scene.step(dt)
        self.camera_operator.step(dt)
        for overlay in self.overlays.values():
            overlay.update(dt)

        if self.scene.player.state == State.DYING:
            self.scene.entities[0].state = State.WIN

        if self.scene.entities[0].state == State.DYING:
            self.scene.player.state = State.WIN

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.atexit()
                pygame.quit()
                sys.exit()

            if event.type == SONG_END:
                next_song()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button.activate(event)

            # Двжение камеры
            if event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed(3)[0]:
                self.camera_operator.aiming = False
                self.camera.position += np.array(event.rel) * [-1, 1] / self.camera.scale_factor

            # Меняем зум камеры (точнее расстояние от камеры до сцены)
            if event.type == pygame.MOUSEWHEEL:
                self.camera.distance -= event.y

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    InGameMenu(self.screen, self.clock).run()

                # Сбрасываем позицию камеры
                if event.key == pygame.K_r:
                    self.camera.position = 0, 0
                    self.camera.distance = 14

                # Переключаем режим разработчика
                if event.key == pygame.K_F3:
                    self.DEVMODE = not self.DEVMODE

                # Возрат камеры в границы уровня
                if event.key == pygame.K_b:
                    self.camera.return_to_borders(self.scene.borders)

                # Возрат камеры в границы уровня
                if event.key == pygame.K_z:
                    for s in self.scene.physical_space.shapes:
                        print(s)

                # Тест фокусировки на игроке
                if event.key == pygame.K_f:
                    if self.camera_operator.target is None:
                        self.camera_operator.target = self.scene.player
                        if len(self.scene.entities) != 0:
                            self.camera_operator.target = MidPoint(self.scene.player, self.scene.entities[0])
                    self.camera_operator.aiming = not self.camera_operator.aiming

                    # Переключение фокусировки фокусировки на игроке
                if event.key == pygame.K_s:
                    if self.camera_operator.targeting_method == TargetingMethod.SMOOTH:
                        self.camera_operator.targeting_method = TargetingMethod.INSTANT
                    else:
                        self.camera_operator.targeting_method = TargetingMethod.SMOOTH

    def run_once(self):
        super(Game, self).run_once()
        # Тикаем часы, чтобы не было рывка физики в начале игры
        # Это нужно сделать дважды
        self.clock.tick()
        self.clock.tick()
        next_song()

    def atexit(self):
        """
        Действия при выходе из приложения
        :return: следущеее приложение, которое запустится сразу или None, если не предусмотрено следущее
        """
        self.scene.save_level(self.username + 'game_exit')
