BOARD = """\
GLGGG
GLLLG
GGGLG
GGLLG
GGLGG
"""
MAP = """\
TETTT
T...T
TTT.T
TT..T
TTOTT
"""


class Field:

    WIDHT = 100
    HEIGHT = 100
    SECTION  = 20

    def __init__(self):
        self.map = self._load_map(MAP)
        self.board = self._load_map(BOARD)

    def _load_map(self, map_string):
        matrix = []
        list_of_lines = map_string.split("\n")
        for line in list_of_lines:
            matrix.append(list(line))
        return matrix

    def move(self, monsters):
        """
        params: monsters must be an iterable
        return: an iterable of monster outside of map
        """
        return ()

    def get_tower_locations(self):
        """
        returns an iterable of tower locations as tuble (x, y)
        """
        return ()

    def get_monster_entrance(self):
        """
        returns a monster entrance as a tuble (x, y)
        """
        return ()

    def get_board(self):
        """
        returns a matrix:
            - G means grass
            - L means land
        """
        return self.board
