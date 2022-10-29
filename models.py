import enum

class NamesFigures(enum.Enum):
    pawn = 0
    knight = 1
    bishop = 2
    rook = 3
    queen = 4

class Figure:
    def __init__(self, name : NamesFigures, vertical : int, horizontal : int):
        self.name = name
        self.vertical = vertical
        self.horizontal = horizontal

