import logging

from models import *
from input import *
from views import *


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="log_file.log", filemode="a",
                        format="%(asctime)s %(levelname)s %(message)s")
    isExit = 'y'

    while isExit in ('y', 'д'):
        # Заполнение двух фигур.
        first_figure = get_fill_figure(1)
        second_figure = get_fill_figure(2, first_figure)

        print_header('Результаты')
        # Вывод шахматной доски.
        print_chess_board(first_figure, second_figure)
        # Вывод результата сравнения цветов полей.
        print_color_equality(first_figure, second_figure)
        # Вывод угрозы одной фигуры для другой.
        print_danger(first_figure, second_figure)
        # Вывод сруба за два хода.
        print_move_to_kill(first_figure, second_figure)

        # Предложение о повторе.
        print()
        isExit = input_char('Попробовать ещё раз? (Y/N) (Д/Н)', 'y', 'n', 'д', 'н')

    