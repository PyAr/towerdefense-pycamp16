import time

from . import towers, monster
from .field import field

BOARD_LENGTH = 100
TOTAL_REACTOR_LOOPS = 160 * 5   # 5 x path length
TOTAL_MONSTERS = 100

# too many things depends on this invariant
assert TOTAL_MONSTERS < TOTAL_REACTOR_LOOPS


class Drawer:
    """A drawer. Or not."""

    def __init__(self, drawing):
        if drawing:
            from . import painter
            self._painter = painter
        else:
            self._painter = None

    def draw_field(self, *a, **k):
        if self._painter is not None:
            self._painter.draw_field(*a, **k)

    def draw(self, *a, **k):
        if self._painter is not None:
            self._painter.draw(*a, **k)


class VerticalSync:
    """Introduce delays for loop to not be so fast."""

    frame_duration = 100 / 1000  # ms

    def __init__(self, active):
        self._active = active
        self._started = None

    def start(self):
        if not self._active:
            return
        assert self._started is None
        self._started = time.time()

    def stop_and_wait(self):
        if not self._active:
            return
        assert self._started is not None
        used_time = time.time() - self._started
        self._started = None
        to_wait = self.frame_duration - used_time
        if to_wait > 0:
            time.sleep(to_wait)
        else:
            print("WARNING: loop took too much: {:.3f}s".format(used_time))


def go(bootstrap_info, drawing=False):
    """Receive a dict with positions as keys, and tower type as values, return the score."""
    drawer = Drawer(drawing)

    # bootstrap, set up the towers
    game_towers = [towers.get_tower(pos, kind) for pos, kind in bootstrap_info.items()]
    field_board = field.get_board()
    drawer.draw_field(field_board, game_towers)

    score = TOTAL_MONSTERS  # every time a monster finished, -1
    monsters = []
    remaining_monsters = TOTAL_MONSTERS
    initial_monster_position = field.get_monster_entrance()
    vsync = VerticalSync(drawing)

    for step in range(TOTAL_REACTOR_LOOPS):
        vsync.start()

        # update the monsters, remove the dead ones
        for m in monsters:
            m.update()

        # remove the dead monsters
        dead_monsters = []
        for i in range(len(monsters) - 1, -1, -1):
            if monsters[i].life <= 0:
                dead_monsters.append(monsters[i])
                del monsters[i]

        # add one more monster to the board, if any remaining
        if remaining_monsters:
            monsters.append(monster.Monster(initial_monster_position))
            remaining_monsters -= 1

        # if no monsters left, exit
        if not monsters and not remaining_monsters:
            break

        # tell the field to move the monsters
        fallen = field.move(monsters)

        # draw!
        drawer.draw(monsters, dead_monsters, score)

        # remove the fallen monsters (and update the score, they finished!!)
        score -= len(fallen)
        for m in fallen:
            monsters.remove(m)

        # if all finished, exit
        if not monsters and not remaining_monsters:
            break

        # tell the towers to shoot
        for t in [t for t in game_towers if t.pre_shoot()]:
            in_range_monsters = []
            for m in monsters:
                distance = abs(t.position[0] - m.position[0]) + abs(t.position[1] - m.position[1])
                if t.shooting_range >= distance:
                    in_range_monsters.append((m, distance))
            # get monsters for this tower
            t.shoot(in_range_monsters)

        vsync.stop_and_wait()

    drawer.draw(monsters, dead_monsters, score)
    return score
