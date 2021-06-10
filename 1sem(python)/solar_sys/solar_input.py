# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject
import os


def file_name(simulations_path):
    """
    Считывает название файла
    """
    simulation_files = [os.path.join(simulations_path, file) for file in os.listdir(simulations_path)]

    print(f'We have {len(simulation_files)} '
          f'{"file" if len(simulation_files) == 1 else "files"}'
          f' for simulations:')

    for number, file in enumerate(simulation_files):
        print(f'{number}) {file}')

    while True:
        try:
            file_name1 = simulation_files[int(input('Input file number that you like: '))]
        except:
            print('Input correct file number')
        else:
            break
    return file_name1


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.

    Входная строка должна иметь слеюущий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.

    Пример строки:

    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.

    **star** — объект звезды.
    """
    _, radius, color, mass, x, y, Vx, Vy = line.strip().split()

    star.R = float(radius)
    star.color = str(color).lower()
    star.m = float(mass)
    star.x = float(x)
    star.y = float(y)
    star.Vx = float(Vx)
    star.Vy = float(Vy)


def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Входная строка должна иметь слеюущий формат:

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.

    Пример строки:

    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.

    **planet** — объект планеты.
    """
    parse_star_parameters(line, planet)
    """
    На всякий случай оставлю, врдуг будут доп параметры у планет и звезд
    _, radius, color, mass, x, y, Vx, Vy = line.strip().split()

    planet.R = float(radius)
    planet.color = str(color)
    planet.m = float(mass)
    planet.x = float(x)
    planet.y = float(y)
    planet.Vx = float(Vx)
    planet.Vy = float(Vy)
    """


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write('{type_} {radius} {color} {mass} {x} {y} {Vx} '
                           '{Vy}\n'.format(
                type_=obj.type.title(),
                radius=obj.R,
                color=obj.color.lower(),
                mass=obj.m,
                x=obj.x,
                y=obj.y,
                Vx=obj.Vx,
                Vy=obj.Vy
            ))


if __name__ == "__main__":
    print("This module is not for direct call!")
