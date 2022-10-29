from models import *


'''
Возвращает истинность соответствия цветов двух координат.

Параметры:
figure1 — Первая фигура (type Figure).  (Обязательный)
figure2 — Вторая фигура (type Figure).  (Обязательный)

Возврат:
Истинность соответствия цветов двух координат
'''
def get_color_equality(figure1 : Figure, figure2 : Figure):
    return (figure1.vertical + figure1.horizontal) % 2 == \
                (figure2.vertical + figure2.horizontal) % 2

'''
Возвращает истинность угрозы figure1 для figure2.

Параметры:
figure1 — Первая фигура (type Figure).  (Обязательный)
figure2 — Вторая фигура (type Figure).  (Обязательный)

Возврат:
True — figure1 может за один ход срубить figure2.
False — figure1 не может срубить за один ход figure2.
'''
def get_danger(figure1 : Figure, figure2 : Figure):
    isDanger = False

    ver1 = figure1.vertical
    hor1 = figure1.horizontal
    ver2 = figure2.vertical
    hor2 = figure2.horizontal

    # Проверка угроз для разных типов фигур.
    match figure1.name:
        # Слон.
        case NamesFigures.bishop:
            isDanger = abs(ver1 - ver2) == abs(hor1 - hor2)
        # Конь.
        case NamesFigures.knight:
            isDanger = abs(ver1 - ver2) == 1 and abs(hor1 - hor2) == 2 or \
                        abs(ver1 - ver2) == 2 and abs(hor1 - hor2) == 1
        # Ладья.
        case NamesFigures.rook:
            isDanger = ver1 == ver2 or hor1 == hor2
        # Ферзь.
        case NamesFigures.queen:
            isDanger = ver1 == ver2 or hor1 == hor2 or abs(ver1 - ver2) == abs(hor1 - hor2)
    
    return isDanger

'''
Возвращает список координат клеток для сруба за два хода.

Параметры:
figure1 — Первая фигура (type Figure).  (Обязательный)
figure2 — Вторая фигура (type Figure).  (Обязательный)

Возврат:
Список кортежей, где первый элемент номер вертикали, второй 
номер горизонтали. Если координаты не найдены, то None.
'''
def get_move_to_kill(figure1: Figure, figure2: Figure):
    match figure1.name:
        # Слон.
        case NamesFigures.bishop:
           coordinates = __get_coordinates_bishop(figure1, figure2) 
        # Конь.
        case NamesFigures.knight:
            coordinates = __get_coordinates_knight(figure1, figure2)
        # Ладья.
        case NamesFigures.rook:
            coordinates = __get_coordinates_rook(figure1, figure2)
        # Ферзь.
        case NamesFigures.queen:
            coordinates = __get_coordinates_bishop(figure1, figure2) + \
                            __get_coordinates_rook(figure1, figure2)
    
    if len(coordinates) == 0:
        return None

    return coordinates

'''
Параметры:
figure1 — Первая фигура (type Figure).  (Обязательный)
figure2 — Вторая фигура (type Figure).  (Обязательный)

Возврат:
Координаты клеток слона для дальнейшего сруба,
если такие имеются, иначе None.
'''
def __get_coordinates_bishop(figure1 : Figure, figure2 : Figure):
    ver1 = buffer_ver1 = figure1.vertical
    hor1 = buffer_hor1 = figure1.horizontal
    ver2 = figure2.vertical
    hor2 = figure2.horizontal
    coordinates = list()
    
    if not get_color_equality(figure1, figure2):
        return coordinates
    
    while ver1 < 8 and hor1 < 8:
        ver1 += 1
        hor1 += 1
        if get_danger(Figure(NamesFigures.bishop, ver1, hor1),
                      Figure(NamesFigures.bishop, ver2, hor2)):
            coordinates.append((ver1, hor1))

    ver1 = buffer_ver1
    hor1 = buffer_hor1
    while ver1 < 8 and hor1 > 1:
        ver1 += 1
        hor1 -= 1
        if get_danger(Figure(NamesFigures.bishop, ver1, hor1),
                      Figure(NamesFigures.bishop, ver2, hor2)):
            coordinates.append((ver1, hor1))

    ver1 = buffer_ver1
    hor1 = buffer_hor1
    while ver1 > 1 and hor1 < 8:
        ver1 -= 1
        hor1 += 1
        if get_danger(Figure(NamesFigures.bishop, ver1, hor1),
                      Figure(NamesFigures.bishop, ver2, hor2)):
            coordinates.append((ver1, hor1))

    ver1 = buffer_ver1
    hor1 = buffer_hor1
    while ver1 > 1 and hor1 > 1:
        ver1 -= 1
        hor1 -= 1
        if get_danger(Figure(NamesFigures.bishop, ver1, hor1),
                      Figure(NamesFigures.bishop, ver2, hor2)):
            coordinates.append((ver1, hor1))
    
    return coordinates

'''
Параметры:
figure1 — Первая фигура (type Figure).  (Обязательный)
figure2 — Вторая фигура (type Figure).  (Обязательный)

Возврат:
Координаты клеток коня для дальнейшего сруба, если такие имеются.
'''
def __get_coordinates_knight(figure1 : Figure, figure2 : Figure):
    ver1 = buffer_ver1 = figure1.vertical
    hor1 = buffer_hor1 = figure1.horizontal
    ver2 = figure2.vertical
    hor2 = figure2.horizontal
    coordinates = list()
    moves = [(1, 2), (2, 1), (-1, 2), (2, -1), 
            (1, -2), (-2, 1), (-1, -2), (-2, -1)]

    for move in moves:
        ver1 += move[0]
        hor1 += move[1]

        if ver1 >= 1 and ver1 <= 8 and hor1 >= 1 and hor1 <= 8:
            if get_danger(Figure(NamesFigures.knight, ver1, hor1),
                      Figure(NamesFigures.knight, ver2, hor2)):
                coordinates.append((ver1, hor1))

        ver1 = buffer_ver1
        hor1 = buffer_hor1

    return coordinates

'''
Параметры:
figure1 — Первая фигура (type Figure).  (Обязательный)
figure2 — Вторая фигура (type Figure).  (Обязательный)

Возврат:
Координаты клеток ладьи для дальнейшего сруба.
'''
def __get_coordinates_rook(figure1 : Figure, figure2 : Figure):
    ver1 = figure1.vertical
    hor1 = figure1.horizontal
    ver2 = figure2.vertical
    hor2 = figure2.horizontal

    return[(ver1, hor2), (ver2, hor1)]
