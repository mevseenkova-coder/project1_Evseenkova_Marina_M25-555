#!/usr/bin/env python3

from constants import COMMANDS
from player_actions import get_input, move_player, show_inventory, take_item, use_item
from utils import attempt_open_treasure, describe_current_room, show_help, solve_puzzle


def process_command(game_state, command):
    """
    Функция process_command должна принимать game_state и введенную пользователем строку
    Внутри нее разделите строку на части, чтобы отделить команду от аргумента 
    (например, 'go north' -> 'go', 'north').
    Используя match / case, определите, какую команду ввел пользователь (look, use, go, 
    take, inventory, quit).
    Вызовите соответствующую функцию (describe_current_room, move_player, take_item 
    и т.д.) в рамках условия, передав ей нужный аргумент.
    В цикле while в функции main() вызывайте process_command для каждой введенной 
    пользователем строки. Убедитесь, что команда quit или exit завершает игру.

    Реализуйте возможность движения по односложным командам (north, south и т.д.) 
    без слова go.
    Если игрок находится в treasure_room и вводит команду solve, вместо solve_puzzle() 
    должна вызываться attempt_open_treasure().
    
    Обрабатывает введенную пользователем команду.
    
    Args:
        game_state (dict): Текущее состояние игры
        command (str): Введенная пользователем команда
    """
    # Разделяем команду на части (команда + аргумент)
    parts = command.strip().lower().split()
    if not parts:
        return  # Пустая команда — ничего не делаем
    
    action = parts[0]  # команда
    argument = parts[1] if len(parts) > 1 else None  # аргумент
    
    # Обрабатываем команды через match/case
    match action:
        case 'help':
            show_help(COMMANDS)

        case 'look':
            describe_current_room(game_state)

        case 'use':
            if argument:
                use_item(game_state, argument)
            else:
                print("Укажите, какой предмет хотите использовать.")
       
        case 'go':
            if argument:
                move_player(game_state, argument)
            else:
                print("Укажите направление движения (north, south, east, west).")

        case 'north' | 'south' | 'east' | 'west':
            move_player(game_state, action)
        
        case 'take':
            if argument:
                take_item(game_state, argument)
            else:
                print("Укажите, какой предмет хотите взять.")
                
        case 'inventory' | 'inv':
            show_inventory(game_state)

        case 'solve':
            if game_state['current_room'] == 'treasure_room':
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)
        
        case 'quit' | 'exit':
            print("Игра завершена. До свидания!")
            game_state['game_over'] = True
            return 'quit'  # Специальный сигнал для выхода
        
        case _:
            print(f"Неизвестная команда: '{action}'. Попробуйте: look, use, go, take, inventory, quit.")  # noqa: E501
    
    return None  # Нормальное продолжение игры

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
        process_command(game_state, command)
        
if __name__ == "__main__":
    main()