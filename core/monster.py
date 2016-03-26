
class Monster:
    def __init__(self, position, life=2000, defense=20, speed=5, poison_affection=10):
        self.position = position
        self.life = life
        self.defense = defense
        self.speed = speed
        self.step_length = 0
        self.poison_affection = poison_affection

        self._damage = 0
        self._poison = 0
        self._freeze = 0
        self._slowdown = 0
        self._rage = 0
        self.time_counters = (
            self._rage, self._poison, self._freeze, self._slowdown
        )

    def update(self):
        '''
        This function is called by reactor in every tick in order to calculate
        the step_length of the current tick
        '''
        rage = 2 if self._rage > 0 else 1

        if self._damage * rage > self.defense:
            self.life -= self._damage * rage

        if self._poison > 0:
            self.life -= self.poison_affection * rage

        if self._freeze > 0:
            self.step_length = 0
        elif self._slowdown > 0:
            self.step_length = self.speed // 2
        else:
            self.step_length = self.speed

        self.step_length = self.step_length * rage

        self.update_counters()

    def update_counters(self):
        self._damage = 0
        for counter in self.time_counters:
            if counter > 0:
                counter -= 1

    def affect(self, rage=0, damage=0, poison=0, freeze=0, slowdown=0):
        '''
        This method is called by towers during one tick to indicate the
        affections received.
        '''
        self._rage += rage
        self._damage += damage
        self._poison += poison
        self._freeze += freeze
        self._slowdown += slowdown

    def rage(self):
        if self._rage:
            return True
        return False

    def freeze(self):
        if self._freeze:
            return True
        return False

    def poison(self):
        if self._poison:
            return True
        return False
