from controllers import *
from views import print_header


'''
Запрашивает у пользователя ввод одного из доступных символов.

Параметры:
msg         — Информационное сообщение пользователю о вводе (type str).     (Обязательный)
chars       — Доступные для ввода символы (type int).                       (Опциональный)

Ошибки:
Value must be one of the options   — Значение не является одним из доступных символов.

Возврат:
Корректно введенный символ пользователем (type str).
'''
def input_char(msg : str, *chars : str):
    while True:
        text = input('\033[34m{}\033[0m'.format(msg + '\n— ')).lower()

        if len(chars) > 0:
            if text not in chars:
                print(__get_error(f'Value must be one of the options: {chars}'))   
                continue

        return text

'''
Выводит интерфейс для заполнения фигуры пользователем.

Параметры:
number_figure   — Номер заполняемой фигуры (type int). (Обязательный)
previousFigures — Предыдущие фигуры (type Figure).     (Опциональный)

Ошибки:
Figures have the same coordinates — Фигуры имеют одинаковые координаты.

Возврат:
Заполненная фигура (type Figure).
'''
def get_fill_figure(number_figure : int, *previousFigures : Figure):
    print_header('Заполнение ' + str(number_figure) + '-ой фигуры')
    
    if len(previousFigures) == 0:
        name = __input_figure_name()
    else:
        name = NamesFigures.pawn

    vertical = __input_int('Введите номер вертикали: ', 1, 8)

    while True:
        horizontal = __input_int('Введите номер горизонтали: ', 1, 8)
        
        if len(previousFigures) == 0:
            break

        isSame = False
        for fig in previousFigures:
            if fig.vertical == vertical and fig.horizontal == horizontal:
                isSame = True
                break
        
        if isSame:
            print(__get_error('Figures have the same coordinates'))
            continue
        
        break

    return Figure(name, vertical, horizontal)

'''
Возвращает текст ошибки в нужном формате.

Параметры:
text — Текст ошибки (type str).

Возврат:
Сообщение ошибки в нужном формате (type str). 
'''
def __get_error(text : str):
    return '\033[31m{}\033[0m'.format('ERROR: ' + text + '! Try again...')

'''
Запрашивает у пользователя ввод числа.

Параметры:
msg         — Информационное сообщение пользователю о вводе (type str).     (Обязательный)
min_lim     — Минимальное доступное значение в диапазоне (type int).        (Опциональный)
max_lim     — Максимально доступное значение в диапазоне (type int).        (Опциональный)

Ошибки:
Value is not a number   — Неверно введено число.
Value is not in range   — Число вне диапазона.

Возврат:
Корректно введенное число пользователем в заданном диапазоне (type int).
'''
def __input_int(msg : str, min_lim : int = None, max_lim : int = None):
    invalid_input = 'Value is not a number' 
    out_of_range = f'Value is not in range [{min_lim}, {max_lim}]'

    while True:
        try:
            num = int(input(msg))
        except:
            print(__get_error(invalid_input))
            continue
        
        if min_lim != None and max_lim != None:
            if num < min_lim or num > max_lim:
                print(__get_error(out_of_range))
                continue
        return num
    
'''
Запрашивает у пользователя ввод требуемой фигуры.

Ошибки:
Value is not a number   — Неверно введено число.
Value is not in range   — Число вне диапазона.

Возврат:
Название фигуры (type NamesFigures).
'''
def __input_figure_name():
    print('1 — Конь\n' +
          '2 — Слон\n' +
          '3 — Ладья\n' +
          '4 — Ферзь\n')
    figure_number = __input_int('Выберите фигуру из доступных: ', 1, 4)
    for name in NamesFigures:
        if name.value == figure_number:
            return name