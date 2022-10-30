# Автор

Бельский Олег ФТ-210007

# Описание

Программа реализует шаблон проектирования MVC. Вся главная логика прописана в файле ФТ-210007Бельский.py.

- models.py — содержит класс figure и enum для названий фигур.
- controllers.py — содержит всю бизнес логику работы с программой.
- views.py — обращается к файлу controllers.py, обрабатывает полученные данные и выводит их пользователю. 
- input.py — берет у пользователя данные из стандартного потока ввода с обработкой ошибок.

Программа выполняет три основные задачи:

- Сравнивает две клетки фигур на одинаковость цветов. 
- Выясняет, может ли одна фигура срубить другую за один ход.
- Если не может, то находит промежуточные клетки для сруба за два хода, если такие имеются.

# Требования к использованию

- **Python v3.10**, т.к. используется оператор match.
- Запуск должен происходить в **терминале** (не в cmd), для корректного отображения Unicode и цветного вывода.

Команда для запуска:

`python ФТ-210007Бельский.py`

# Примеры использования

- Тест 1

![Img alt](https://github.com/retxrika/Chess/blob/master/images/1_1.png)

![Img alt](https://github.com/retxrika/Chess/blob/master/images/1_2.png)

![Img alt](https://github.com/retxrika/Chess/blob/master/images/1_3.png)

- Тест 2

![Img alt](https://github.com/retxrika/Chess/blob/master/images/2_1.png)

![Img alt](https://github.com/retxrika/Chess/blob/master/images/2_2.png)

![Img alt](https://github.com/retxrika/Chess/blob/master/images/2_3.png)

- Тест 3

![Img alt](https://github.com/retxrika/Chess/blob/master/images/3_1.png)

![Img alt](https://github.com/retxrika/Chess/blob/master/images/3_2.png)

![Img alt](https://github.com/retxrika/Chess/blob/master/images/3_3.png)


