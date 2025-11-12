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


def solve_puzzle(game_state):
    """
    Сначала проверьте, есть ли загадка в текущей комнате. 
    Если нет, выведите сообщение "Загадок здесь нет." и завершите выполнение функции.
    Если загадка есть, выведите на экран вопрос.
    Получите ответ от пользователя("Ваш ответ: ").
    Сравните ответ пользователя с правильным ответом.
    Если ответ верный:
    Сообщите игроку об успехе.
    Уберите загадку из комнаты, чтобы ее нельзя было решить дважды.
    Добавьте игроку награду.
    Если ответ неверный, сообщите об этом игроку("Неверно. Попробуйте снова.").

    Позволяет игроку решить загадку в текущей комнате.
    
    Args:
        game_state (dict): Текущее состояние игры. Должен содержать ключи:
            - 'current_room' (dict): текущая комната с ключом 'puzzle' (опционально)
            - 'player_inventory' (list): инвентарь игрока
    """
    current_room = game_state['current_room']  # название текущей комнаты
    room_data = ROOMS[current_room]  # данные о текущей комнате
    puzzle = room_data.get('puzzle', [])  # загадка в текущей комнате
    
    # Проверяем, есть ли загадка в текущей комнате
    if not puzzle:
        print("Загадок здесь нет.")
        return

    question = puzzle[0]  # вопрос загадки
    answer = puzzle[1] if len(puzzle) > 1 else None  # правильный ответ
    reward = puzzle[2] if len(puzzle) > 2 else None  # награда за отгаданную загадку

    # Выводим вопрос загадки
    print(question)
    
    # Получаем ответ от пользователя
    user_answer = input("Ваш ответ: ").strip().lower()
    
    # Сравниваем ответ с правильным (без учёта регистра)
    if user_answer == answer.lower():
        print("Правильно! Вы успешно разгадали загадку.")
        
        # Убираем загадку из комнаты
        del room_data['puzzle']

        # Добавляем награду в инвентарь игрока        
        if reward:
            game_state['player_inventory'].append(reward)
            print(f"Вы получили награду: {reward}")
    else:
        print("Неверно. Попробуйте снова.")


def attempt_open_treasure(game_state):
    """
    Попытка открыть сундук с сокровищами.
    
    Args:
        game_state (dict): Текущее состояние игры. Должен содержать ключи:
            - 'current_room' (dict): текущая комната с ключом 'puzzle' (опционально)
            - 'player_inventory' (list): инвентарь игрока
    """
    current_room = game_state['current_room']  # название текущей комнаты
    room_data = ROOMS[current_room]  # данные о текущей комнате
    player_inventory = game_state['player_inventory']  # инвентарь игрока
    
    # Проверяем, есть ли сундук в комнате
    if 'treasure_chest' not in room_data.get('items', []):
        print("Здесь нет сундука с сокровищами.")
        return
    
    # Проверяем наличия ключа
    if 'treasure_key' in player_inventory:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        
        # Удаляем сундук из комнаты
        room_data['items'].remove('treasure_chest')
        
        print("В сундуке сокровище! Вы победили!")
        game_state['game_over'] = True
        return 'quit'  # Специальный сигнал для выхода
    
    # Если ключа нет — предлагаем ввести код
    choice = input("Сундук заперт. ... Ввести код? (да/нет) ").strip().lower()
        
    if choice in ('да', 'yes', 'y'):
        # Проверяем наличие загадки для сундука
        if 'puzzle' not in room_data:
            print("Не удаётся найти подсказку для ввода кода.")
            return
             
        puzzle = room_data.get('puzzle', [])  # загадка в текущей комнате
    
        question = puzzle[0]  # вопрос загадки
        answer = puzzle[1] if len(puzzle) > 1 else None  # правильный ответ
        # reward=puzzle[2] if len(puzzle) > 2 else None  # награда за отгаданную загадку
        
        print(question)
        user_code = input("Ваш код: ").strip().lower()
        
        if user_code == answer.lower():
            print("Код принят! Замок щёлкает, и сундук открывается.")
            room_data['items'].remove('treasure_chest')
            print("В сундуке сокровище! Вы победили!")
            game_state['game_over'] = True
        else:
            print("Неверный код. Замок не поддаётся.")
    elif choice in ('нет', 'no', 'n'):
        print("Вы отступаете от сундука.")
    else:
        print("Ваш ответ не понятен. Действие отменено.")