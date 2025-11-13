# labyrinth_game/player_actions.py

from constants import ROOMS  # предполагаем, что ROOMS находится в модуле constants
from utils import describe_current_room, random_event


def show_inventory(game_state):
    """
    Функция должна принимать один аргумент — словарь game_state.
    Прочитайте game_state['player_inventory'] и выведите его содержимое 
    или сообщение о том, что инвентарь пуст.
    
    Отображает содержимое инвентаря игрока.

    Args:
        game_state (dict): Словарь с состоянием игры, 
        должен содержать ключ 'player_inventory' (list).
    """
    inventory = game_state['player_inventory']  # Инвентарь игрока

    if inventory:  # если инвентарь не пуст
        print("Инвентарь:")
        for item in inventory:
            print(f"  -> {item}")
    else:  # если инвентарь пуст
        print("Инвентарь пуст.")


def get_input(prompt="> "):
    """
    Запрашивает у пользователя ввод с заданным приглашением (prompt).

    
    Args:
        prompt (str): Текст-приглашение, который выводится перед вводом пользователя.
                      По умолчанию — "> ".
    
    Returns:
        str: "quit" 
    """
    try:
        user_input = input("\n> ").strip().lower()
        return user_input
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit" 

def move_player(game_state, direction):
    """
    Функция должна принимать два аргумента — game_state и направление (строку, 
    например, 'north').
    Проверяет, существует ли выход в этом направлении.
    Если выход есть:
    Обновите текущую комнату.
    Увеличьте шаг на единицу.
    Выведите описание новой комнаты.
    Если выхода нет, выведите на экран сообщение: "Нельзя пойти в этом направлении."
    
    Перемещает игрока в указанном направлении, если выход существует.

    Args:
        game_state (dict): Текущее состояние игры. Должен содержать ключи:
            - 'current_room' (dict): текущая комната,должна содержать ключ 'exits'(dict)
            - 'steps_taken' (int): количество шагов, пройденное в игре
        direction (str): Направление движения (например, 'north').

    Returns:
        bool: True, если перемещение успешно, False — если выхода нет.
    """
    room_name = game_state['current_room']  # название текущей комнаты
    room_data = ROOMS[room_name]  # данные о текущей комнате
    room_exits = room_data.get('exits', [])   # Доступные выходы
   
    # Проверяем, существует ли выход в этом направлении
    if direction in room_exits:
        # Обновляем текущую комнату
        game_state['current_room'] = room_exits[direction]
        
        # Увеличиваем счётчик шагов
        game_state['steps_taken'] += 1

        # Выводим описание новой комнаты
        describe_current_room(game_state)

        # Вызываем случайное событие после перемещения
        random_event(game_state)
        
        return True
    else:
        print("Нельзя пойти в этом направлении.")
        return False

def take_item(game_state, item_name):
    """
    Функция должна принимать два аргумента — game_state и название предмета.
    Проверяет, есть ли предмет в комнате.
    Если предмет есть:
    Добавьте его в инвентарь игрока.
    Удалите его из списка предметов комнаты.
    Напечатайте сообщение о том, что игрок подобрал предмет ("Вы подняли:").
    Если такого предмета в комнате нет, выведите сообщение: "Такого предмета здесь нет."

    Функция для взятия предмета игроком, если такой предмет есть в комнате.
    
    Args:
        game_state (dict): Текущее состояние игры. Должен содержать ключи:
            - 'player_inventory' (list): инвентарь игрока
            - 'current_room' (dict): текущая комната,должна содержать ключ 'items'(list)
        item_name (str): Название предмета, который игрок хочет взять
    """
    current_room = game_state['current_room']  # название текущей комнаты
    room_data = ROOMS[current_room]  # данные о текущей комнате
    player_inventory = game_state['player_inventory']  # инвентарь игрока

    # Проверяем, есть ли предмет в комнате
    if item_name in room_data['items']:
        if item_name == 'treasure_chest':
            print("Вы не можете поднять сундук, он слишком тяжелый.")
        else:
            # Добавляем предмет в инвентарь игрока
            player_inventory.append(item_name)
        
            # Удаляем предмет из списка предметов комнаты
            room_data['items'].remove(item_name)
        
            # Выводим сообщение о том, что игрок подобрал предмет
            print(f"Вы подняли: {item_name}")
    else:
        # Если предмета нет в комнате, выводим сообщение
        print("Такого предмета здесь нет.")

def use_item(game_state, item_name):
    """
    Функция должна проверять, есть ли предмет у игрока, и выполнять уникальное действие 
    для каждого предмета:
    Добавьте проверку на наличие предмета в инвентаре. Если как такого нет, то выведете 
    сообщение (У вас нет такого предмета.)
    torch: выводит сообщение о том, что стало светлее.
    sword: выводит сообщение об уверенности.
    bronze box: выводит сообщение об открытии шкатулки и добавляет 'rusty_key' 
    в инвентарь, если его еще нет в инвентаре, иначе пусто.
    Для остальных предметов выводите сообщение, что игрок не знает, как их использовать.

    Использует предмет из инвентаря игрока.
    
    Args:
        game_state (dict): Текущее состояние игры. Должен содержать 
            ключ 'player_inventory' (list).
        item_name (str): Название предмета, который игрок хочет использовать.
    """
    player_inventory = game_state['player_inventory']
    
    # Проверяем, есть ли предмет в инвентаре
    if item_name not in player_inventory:
        print("У вас нет такого предмета.")
        return
    
    # Обрабатываем использование конкретных предметов
    match item_name:
        case 'torch':
            print("Стало светлее. Вы лучше видите окружающее пространство.")
        
        case 'sword':
            print("Чувствуете уверенность в своих силах. Оружие придаёт вам решимости.")
        
        case 'bronze_box':
            print("Вы открываете бронзовую шкатулку...")
            # Проверяем, есть ли уже ржавый ключ в инвентаре
            if 'rusty_key' not in player_inventory:
                # Добавляем предмет в инвентарь игрока
                player_inventory.append('rusty_key')
                print("Внутри вы нашли ржавый ключ! Он добавлен в инвентарь.")
            else:
                print("Шкатулка пуста — вы уже забирали отсюда ржавый ключ.")
        
        case _:
            print(f"Вы не знаете, как использовать {item_name}.")