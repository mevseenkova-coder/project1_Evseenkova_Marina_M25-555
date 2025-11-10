# labyrinth_game/utils.py

from constants import ROOMS  # предполагаем, что ROOMS находится в модуле constants


def describe_current_room(game_state):
    """
    Функция должна принимать один аргумент — словарь game_state.
    Используя game_state['current_room'], получите из константы ROOMS данные 
    о текущей комнате.
    Последовательно выведите на экран:
    Название комнаты в верхнем регистре (например, == ENTRANCE ==).
    Описание комнаты.
    Список видимых предметов. Если они есть, то вывести сообщение "Заметные предметы:"
    с перечисленными предметами
    Доступные выходы("Выходы:").
    Сообщение о наличии загадки, если она есть("Кажется, здесь есть загадка 
    (используйте команду solve).")
    
    Описывает текущую комнату на основе состояния игры.

    Args:
        game_state (dict): Словарь с состоянием игры, 
        должен содержать ключ 'current_room'.
    """
    
    room_name = game_state['current_room']  # название текущей комнаты
    room_data = ROOMS[room_name]  # данные о текущей комнате

    # Название комнаты в верхнем регистре
    print(f"== {room_name.upper()} ==")

    # Описание комнаты
    print(room_data['description'])

    # Список видимых предметов
    if room_data.get('items'):
        print("Заметные предметы:")
        for item in room_data['items']:
            print(f"  -> {item}")

    # Доступные выходы
    exits = room_data.get('exits', [])
    if exits:
        exits_str = ", ".join(exits)
        print(f"Выходы: {exits_str}")

    # Сообщение о загадке
    if room_data.get('puzzle'):
        print("Кажется, здесь есть загадка (используйте команду solve).")