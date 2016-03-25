class Field:

    WIDHT = 100
    HEIGHT = 100
    SECTION  = 20

    MAP_FILENAME = "map.txt"
    BOARD_FILENAME = "board.txt"

    def __init__(self):
        self.map = []
        self.board = []
        self._load_map_from_file()
        self._load_board_from_file()

    def _load_from_file(self, filename):
        file_list = []
        with open(filename, 'r') as f:
            for line in f:
                file_list.append(line)
        matrix = []
        for row in file_list:
            matrix.append(list(row.replace("\n", "")))
        return matrix

    def _load_map_from_file(self):
        self.map = self._load_from_file(self.MAP_FILENAME)

    def _load_board_from_file(self):
        self.board = self._load_from_file(self.BOARD_FILENAME)

    def move(bugs):
        """
        params: bugs must be an iterable
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
            - zero means grass
            - one means land
        """
        return [[]]