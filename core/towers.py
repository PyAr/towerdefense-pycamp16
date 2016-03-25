import random


def get_kinds():
    return list(towers_dic.keys())


def get_tower(position, kind):
    klass = towers_dic[kind]
    return klass(position)


class Tower:
    """Basic tower."""

    def __init__(self, position, shooting_range=30, strength=200, cooldown=4):
        self.shooting_range = shooting_range
        self.strength = strength
        self.position = position
        self.cooldown = cooldown
        self.current_cooldown = 0

    def shoot(self, monsters):
        if len(monsters)==0:
            return

        targets = self._select_targets(monsters)
        # shoot
        for t in targets:
            self._damage(t)

        self.current_cooldown = self.cooldown

    def pre_shoot(self):
        if self.current_cooldown == 0:
            return True
        else:
            self.current_cooldown -= 1
            return False

    def _select_targets(self, monsters):
        """
        return a list with the nearest target
        """
        # monsters is a tuple's list (monster, distance)
        # select target
        monsters = sorted(monsters, key=lambda x: x[1])
        return [monsters[0][0]]

    def _damage(self, monster):
        monster.affect(damage=self.strength)


class Indecisa(Tower):
    def _select_target(self, monsters):
        """
        return a list of targets by sampling
        """
        targets = [random.choice(monsters)]
        monsters.remove(target1)
        if monsters:
            targets.append(random.choice(monsters))
        return targets


class Bully(Tower):
    def __init__(self, position, shooting_range=20, strength=400, cooldown=2):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)


class Chiflete(Tower):
    def __init__(self, position, shooting_range=30, strength=20, cooldown=4):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)

    def _damage(self, monster):
        monster.affect(damage=self.strength, freeze=5)


class Fresquete(Tower):
    def __init__(self, position, shooting_range=20, strength=400, cooldown=2):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)


class Zika(Tower):
    def __init__(self, position, shooting_range=20, strength=400, cooldown=2):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)


towers_dic = {
    "Comunacha": Tower,
    "Indecisa": Indecisa,
    "Bully": Bully,
    "Chiflete": Chiflete,
    "Fresquete": Fresquete,
    "Zika": Zika
}
