# labyrinth_game/constants.py

ROOMS = {
    'entrance': {
        'description': 'Вы в темном входе лабиринта. Стены покрыты мхом. На полу лежит старый факел.',  # noqa: E501
        'exits': {'north': 'hall', 'east': 'trap_room'},
        'items': ['torch'],
        'puzzle': None
    },
    'hall': {
        'description': 'Большой зал с эхом. По центру стоит пьедестал с запечатанным сундуком.',  # noqa: E501
        'exits': {'south': 'entrance', 'west': 'library', 'north': 'treasure_room', 'east': 'garden'},  # noqa: E501
        'items': [],
        'puzzle': ('На пьедестале надпись: "Назовите число, которое идет после девяти". Введите ответ цифрой или словом.', '10')  # noqa: E501
    },
    'trap_room': {
          'description': 'Комната с хитрой плиточной поломкой. На стене видна надпись: "Осторожно — ловушка".',  # noqa: E501
          'exits': {'west': 'entrance', 'north': 'garden'},
          'items': ['rusty_key'],
          'puzzle': ('Система плит активна. Чтобы пройти, назовите слово "шаг" три раза подряд (введите "шаг шаг шаг")', 'шаг шаг шаг')  # noqa: E501
    },
    'library': {
          'description': 'Пыльная библиотека. На полках старые свитки. Где-то здесь может быть ключ от сокровищницы.',  # noqa: E501
          'exits': {'east': 'hall', 'north': 'armory'},
          'items': ['ancient_book'],
          'puzzle': ('В одном свитке загадка: "Что растет, когда его съедают?" (ответ одно слово)', 'резонанс')  # noqa: E501
    },
        'armory': {
          'description': 'Старая оружейная комната. На стене висит меч, рядом — небольшая бронзовая шкатулка.',  # noqa: E501
          'exits': {'south': 'library'},
          'items': ['sword', 'bronze_box'],
          'puzzle': None
    },
    'treasure_room': {
          'description': 'Комната, на столе большой сундук. Дверь заперта — нужен особый ключ.',  # noqa: E501
          'exits': {'south': 'hall', 'east': 'cave'},
          'items': ['treasure_chest'],
          'puzzle': ('Дверь защищена кодом. Введите код (подсказка: это число пятикратного шага, 2*5= ? )', '10')  # noqa: E501
    },
    'garden': {
          'description': 'Старый заброшенный сад. Впереди должно быть что-то интересное.',  # noqa: E501
          'exits': {'west': 'hall', 'south': 'trap_room', 'north': 'cave'},
          'items': ['dwarf'],
          'puzzle': None
    },
    'cave': {
          'description': 'Темная пещера. Вход завален камнями — нужно как-то расчистить проход.',  # noqa: E501
          'exits': {'south': 'garden', 'west': 'treasure_room'},
          'items': [],
          'puzzle': ('Скажи волшебное слово, чтобы привлечь гнома.', 'золото')
    }
}