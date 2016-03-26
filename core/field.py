"""
# Board
G: grass
L: Land
"""
BOARD = """\
GLGGG
GLLLG
GGGLG
GGLLG
GGLGG
"""

VERTICES = [
    (30, 0),
    (30, 30),
    (70, 30),
    (70, 70),
    (50, 70),
    (50, 100),
]


class _Field:

    WIDHT = 100
    HEIGHT = 100
    SECTION = 20

    def __init__(self):
        self.board = self._load_map(BOARD)
        self.path = self._generate_path_list(VERTICES)

    def _load_map(self, map_string):
        matrix = []
        list_of_lines = map_string.split("\n")
        for line in list_of_lines:
            matrix.append(list(line))
        return matrix

    def _generate_path_list(self, vertices):
        path = []
        for start, stop in zip(vertices, vertices[1:]):
            path.extend(self._generate_segment_list(start, stop))
        return path

    def _generate_segment_list(self, start, stop):
        result = []
        if start[0] == stop[0]:
            if start[1] < stop[1]:
                step = 1
            else:
                step = -1
            for i in range(start[1], stop[1], step):
                result.append((start[0], i))
        else:
            if start[0] < stop[0]:
                step = 1
            else:
                step = -1
            for i in range(start[0], stop[0], step):
                result.append((i, start[1]))
        return result

    def move(self, monsters):
        """
        params: monsters must be an iterable
        return: an iterable of monster outside of map
        """
        monsters_outside = []
        for monster in monsters:
            current_position = monster.position
            current_index = self.path.index(current_position)
            next_index = current_index + monster.step_length
            try:
                next_position = self.path[next_index]
                monster.position = next_position
            except IndexError:
                monster.position = VERTICES[-1]  # go outside
                monsters_outside.append(monster)
        return monsters_outside

    def get_tower_locations(self):
        """Return an iterable of tower locations as tuple (x, y)."""
        positions = []
        for lineno, line in enumerate(self.board):
            for itemno, item in enumerate(line):
                if item == 'G':
                    positions.append((itemno * self.SECTION + self.SECTION // 2,
                                      lineno * self.SECTION + self.SECTION // 2))
        return positions

    def get_monster_entrance(self):
        """Return a monster entrance as a tuble (x, y)."""
        return self.path[0]

    def get_board(self):
        """Return a matrix, with G meaning grass and L land."""
        return self.board


field = _Field()
