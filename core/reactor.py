
from . import tower, field, monster, painter

BOARD_LENGTH = 100
TOTAL_REACTOR_LOOPS = 160 * 5   # 5 x path length
TOTAL_MONSTERS = 100


def go(bootstrap_info, drawing):
    """Receive a dict with positions as keys, and tower type as values, return the score."""
    # bootstrap, set up the towers
    towers = [tower.get_tower(pos, kind) for pos, kind in bootstrap_info.items()]
    field_board = field.get_board()
    painter.draw_field(field_board, towers)

    score = 0  # negative, every time a monster finished, +1
    monsters = []
    remaining_monsters = TOTAL_MONSTERS
    initial_monster_position = field.get_monster_entrance()

    for step in range(TOTAL_REACTOR_LOOPS):
        # update the monsters, remove the dead ones
        for m in monsters:
            m.update()

        # remove the dead monsters
        for i in range(len(monsters) - 1, -1, -1):
            if monsters[i].life <= 0:
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
        painter.draw(monsters, score)

        # remove the fallen monsters (and update the score, they finished!!)
        score += len(fallen)
        for m in fallen:
            monsters.remove(m)

        # if all finished, exit
        if not monsters and not remaining_monsters:
            break

        # tell the towers to shoot
        for t in [t for t in towers if t.pre_shoot()]:
            in_range_monsters = []
            for m in monsters:
                distance = abs(t.position[0] - m.position[0]) + abs(t.position[1] - m.position[1])
                if t.shooting_range >= distance:
                    in_range_monsters.append((m, distance))
            # get monsters for this tower
            t.shoot(in_range_monsters)

    painter.draw(monsters, score)
    return score
