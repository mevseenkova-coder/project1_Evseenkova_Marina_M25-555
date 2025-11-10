# labyrinth_game/player_actions.py

def show_inventory(game_state):
    """
    Функция должна принимать один аргумент — словарь game_state.
    Прочитайте game_state['player_inventory'] и выведите его содержимое 
    или сообщение о том, что инвентарь пуст.
    
    Отображает содержимое инвентаря игрока.

    Args:
        game_state (dict): Словарь с состоянием игры, 
        должен содержать ключ 'player_inventory'.
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
