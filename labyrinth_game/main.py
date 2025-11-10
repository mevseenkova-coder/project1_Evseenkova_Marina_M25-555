#!/usr/bin/env python3

# from constants import ROOMS
from player_actions import get_input, show_inventory
from utils import describe_current_room


def main():
    """
    Создайте словарь game_state, как было описано выше.
    Внутри main() сперва выведите приветственное сообщение
    ("Добро пожаловать в Лабиринт сокровищ!").
    Затем вызовите функцию, описывающую стартовую комнату.
    Создайте цикл while, который будет работать, пока игра не окончена.
    Внутри цикла считывайте команду от пользователя.
    Не забудьте добавить стандартную конструкцию в конце файла для запуска 
    функции main(), так как main.py является исполняемым файлом.
    """

    # Инициализация состояния игры
    game_state = {
    'player_inventory': [], # Инвентарь игрока
    'current_room': 'entrance', # Текущая комната
    'game_over': False, # Значения окончания игры
    'steps_taken': 0 # Количество шагов
    }

    # Приветственное сообщение
    print("Добро пожаловать в Лабиринт сокровищ!")  # noqa: E501

    # Описание стартовой комнаты
    describe_current_room(game_state)

    # Игровой цикл
    while not game_state['game_over']:
        command = get_input(prompt="> ")
        if command == "осмотреть":
            describe_current_room(game_state)
        elif command == "инвентарь":
            show_inventory(game_state)
    # ... другие команды
        game_state['game_over'] = not game_state['game_over']


if __name__ == "__main__":
    main()