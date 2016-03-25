import random


def get_kinds():
    return list(towers_dic.keys())


def get_tower(position, kind):
    klass = towers_dic[kind]
    return klass(position)


class Tower:
    """Basic tower."""

    def __init__(self, position, shooting_range=35, strength=400, cooldown=4):
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

        #if there is targets to shoot, active cooldown
        if targets:
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
    def _select_targets(self, monsters):
        """
        return a list of targets by sampling
        """
        try:
            return [x[0] for x in random.sample(monsters, 2)]
        except ValueError:
            return [x[0] for x in random.sample(monsters, 1)]


class Bully(Tower):
    def __init__(self, position, shooting_range=25, strength=400, cooldown=2):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)


class Chiflete(Tower):
    def __init__(self, position, shooting_range=35, strength=20, cooldown=4):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)

    def _damage(self, monster):
        monster.affect(damage=self.strength, slowdown=5)


class FresqueteVertical(Chiflete):
    def __init__(self, position, shooting_range=1000, strength=0, cooldown=0):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)

    def _select_targets(self, monsters):
        targets = []
        for (monster, distancia) in monsters:
            if monster.position[0] == self.position[0]:
                targets.append(monster)
        return targets


class FresqueteHorizontal(FresqueteVertical):
    def _select_targets(self, monsters):
        targets = []
        for (monster, distancia) in monsters:
            if monster.position[1] == self.position[1]:
                targets.append(monster)
        return targets


class Zika(Indecisa):
    def __init__(self, position, shooting_range=35, strength=25, cooldown=3):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)

    def _damage(self, monster):
        monster.affect(damage=self.strength, poison=4)


class Camper(Tower):
    def __init__(self, position, shooting_range=85, strength=800, cooldown=15):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)

    def _select_targets(self, monsters):
        monsters = sorted(monsters, key=lambda x: -x[0].position[1])
        return [monsters[0][0]]


class Cagona(Tower):
    def __init__(self, position, shooting_range=85, strength=800, cooldown=7):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)
        self._min_distance = 30

    def _select_targets(self, monsters):
        for m, dist in monsters:
            if dist <= self._min_distance:
                return []
        monsters = sorted(monsters, key=lambda x: -x[0].position[1])
        return [monsters[0][0]]


class CamperDoble(Tower):
    def __init__(self, position, shooting_range=85, strength=400, cooldown=20):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)

    def _select_targets(self, monsters):
        monsters = sorted(monsters, key=lambda x: -x[0].position[1])
        return [x[0] for x in monsters[:2]]


class TormentaFogosa(Tower):
    def __init__(self, position, shooting_range=39, strength=10, cooldown=0):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)

    def _select_targets(self, monsters):
        return [x[0] for x in monsters]

class Troll(Tower):
    def __init__(self, position, shooting_range=35, strength=0, cooldown=2):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)

    def _damage(self, monster):
        monster.affect(damage=self.strength, rage=5)


class MiniGun(Tower):
    def __init__(self, position, shooting_range=35, strength=100, cooldown=7):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)

    def pre_shoot(self):
        if self.current_cooldown == 0:
            return False
        else:
            self.current_cooldown -= 1
            return True


class PechoFrio(CamperDoble):
    def __init__(self, position, shooting_range=1000, strength=30, cooldown=5):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)
    def _damage(self, monster):
        monster.affect(damage=self.strength, freeze=5)


class Patovica(Bully):
    def _damage(self, monster):
        monster.affect(damage=self.strength, freeze=1)


class Comunista(Tower):
    def __init__(self, position, shooting_range=39, strength=1000, cooldown=5):
        super().__init__(position, shooting_range=shooting_range, strength=strength,
                         cooldown=cooldown)
        self._monsters_seen = 0

    def _select_targets(self, monsters):
        self._monsters_seen = 0
        targets = [x[0] for x in monsters]
        self._monsters_seen = len(targets)
        return targets

    def _damage(self, monster):
        damage = self.strength / self._monsters_seen
        monster.affect(damage=damage)


towers_dic = {
    "Comunacha": Tower,
    "Indecisa": Indecisa,
    "Bully": Bully,
    "Chiflete": Chiflete,
    "Fresquete Vertical": FresqueteVertical,
    "Fresquete Horizontal": FresqueteHorizontal,
    "Zika": Zika,
    "Camper": Camper,
    "Cagona": Cagona,
    "Camper Doble": CamperDoble,
    "Tormenta Fogosa": TormentaFogosa,
    "Troll": Troll,
    "MiniGun": MiniGun,
    "Pecho Frio": PechoFrio,
    "Patovica": Patovica,
    "Comunista": Comunista,
}
