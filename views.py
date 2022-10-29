import os
import logging

from models import *
from controllers import *

'''
Выводит заголовок страницы.

Параметры:
text — Текст для заголовка (type str). (Обязательный)
'''
def print_header(text : str):
    os.system('cls')
    print('\033[92m{}\033[0m'.format(text.upper() + '\n'))
    logging.info(text)

'''
Выводит шахматную доску.

Параметры:
figures — Неограниченное количество фигур (type Figure).    (Обязательный)
'''
def print_chess_board(*figures : Figure):
    listFigures = ['P — Пешка (pawn)', 'N — Конь (knight)', 'B — Слон (bishop)', 
                    'R — Ладья (rook)', 'Q — Ферзь (queen)', '', '', '']

    def get_bold_font(text):
        return '\033[1m{}\033[0m'.format(text)
    def get_white_color(text):
        return '\033[37m{}\033[0m'.format(text)
    def get_black_color(text):
        return '\033[30m{}\033[0m'.format(text)

    for i in range(len(figures)):
        print(f'Клетка для фигуры №{i + 1}: ' + __get_coordinates(figures[i]))
    print()
    for i in range(8):
        print(get_bold_font(abs(i - 8)) + '|', end='')
        for j in range(8):
            isFigure = False
            for fig in figures:
                if abs(fig.horizontal - 8) == i and fig.vertical - 1 == j:
                    print(f'[{get_bold_font(listFigures[fig.name.value][0])}]', end='')
                    isFigure = True
            if not isFigure:
                if (i + j) % 2 == 0:
                    print('[' + get_white_color('■') + ']', end='')
                else:
                    print('[' + get_black_color('■') + ']', end='')
        print(f'\t{listFigures[i]}')
    print(end='  ')
    for i in range(len('[ ]') * 8):
        print('—', end='')
    print('\n', end='   ')
    for i in range(8):
        print(get_bold_font(__get_chr_vertical(i)), end='  ')
    print('\n')
    logging.info('Отрисована шахматная доска')

'''
Выводит являются поля фигур полями одного цвета или нет.

Параметры:
figure1 — Первая фигура (type Figure).  (Обязательный)
figure2 — Вторая фигура (type Figure).  (Обязательный)
'''
def print_color_equality(figure1 : Figure, figure2 : Figure):
    is_same = get_color_equality(figure1, figure2)
    word_same = 'одинаковый' if is_same else 'разный' 
    msg = f'а) Поля фигур имеют {word_same} цвет.'
    print(msg)
    logging.info(msg)

'''
Выводит истинность угрозы figure1 для figure2.

Параметры:
figure1 — Первая фигура (type Figure).  (Обязательный)
figure2 — Вторая фигура (type Figure).  (Обязательный)
'''
def print_danger(figure1 : Figure, figure2 : Figure):
    isDanger = get_danger(figure1, figure2)

    word_negation = '' if isDanger else ' не'
    msg = f'б) Фигура на клетке {__get_coordinates(figure1)}{word_negation}' + \
                 f' угрожает фигуре на клетке {__get_coordinates(figure2)}.'
    print(msg)
    logging.info(msg)

'''
Выводит координаты клетки для сруба за два хода, если она существует.

Параметры:
figure1 — Первая фигура (type Figure).  (Обязательный)
figure2 — Вторая фигура (type Figure).  (Обязательный)
'''
def print_move_to_kill(figure1 : Figure, figure2 : Figure):
    if get_danger(figure1, figure2):
        msg = f'в) Фигура на клетке {__get_coordinates(figure1)} может ' + \
              f'срубить фигуру на клетке {__get_coordinates(figure1)} за один ход.'
        print(msg)
        logging.info(msg)
        return

    coordinates = get_move_to_kill(figure1, figure2)

    if coordinates == None:
        msg = f'в) Фигура на клетке {__get_coordinates(figure1)} не может ' + \
              f'срубить фигуру на клетке {__get_coordinates(figure1)} за два хода.'
        print(msg)
        logging.info(msg)
        return

    plural = 'данную клетку' if len(coordinates) == 1 else 'данные клетки'
    msg = f'в) Фигура на клетке {__get_coordinates(figure1)} может ' + \
          f'срубить фигуру на клетке {__get_coordinates(figure1)} за два хода ' + \
          f'через {plural}: '
    coordinates = list(__get_iter_coordinates(coordinates))
    for i in range(len(coordinates)):
        if i == len(coordinates) - 1:
            msg += coordinates[i] + '.'
        else:
            msg += coordinates[i] + ', '
    print(msg)
    logging.info(msg)

'''
Переводит из числа вертикали в символьный формат.

Параметры:
vertical — Номер вертикали (type int).

Возврат:
Символ соответствующий указанной вертикали (type str). 
'''
def __get_chr_vertical(vertical : int):
    return chr(vertical + ord('A')) 

'''
Возвращает координаты клетки фигуры.

Параметры:
figure — Фигура (type Figure).

Возврат:
Координаты клетки фигуры (type str). 
'''
def __get_coordinates(figure: Figure):
    return __get_chr_vertical(figure.vertical - 1) + f'{figure.horizontal}'

'''
Возвращает итератор координат клеток фигур.

Параметры:
coordinates — Список координат (type list).

Возврат:
Итератор координат. 
'''
def __get_iter_coordinates(coordinates : list):
    for c in coordinates:
        yield __get_chr_vertical(c[0] - 1) + str(c[1])