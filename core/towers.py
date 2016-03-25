#towers_dic={"Comunacha","Indecisa","Bullying","Fresquete","Zika","Patovica","ElNiño","Troll","Camper"}
"""
def get_kinds
    return ListaDeTorres=["Enum"]
"""

def get_tower(position, kind):
    return Tower(position)

class Tower:

    def __init__(self, position, shooting_range=30, strength=200, cooldown=4):
        self.shooting_range = rango
        self.strength= fuerza
        self.position = posicion
        self.cooldown=cooldown
        self.current_cooldown = 0

    def shoot(self, monsters):
        if len(monsters)==0:
            return
        #monsters is a tuple's list (monster, distance)
        monsters = sorted(monsters, key=lambda x: x[1])
        monsters[0].affect(damage=self.strength)
        self.current_cooldown = self.cooldown

    def pre_shoot(self, cooldown):
        if self.current_cooldown == 0:
            return True
        else:
            self.current_cooldown -= 1
            return False

    """

class Comunacha(tower):

class Veneno(tower):
    def __init__(self):
    fuerza = 0
    shooting_range = 0
    cooldown = 0
    def shoot(bichos):
        if self.canShoot():
            #a quien disparo
            #despues aplico hit y affect
        else:
            pass

class Veneno(tower):
    fuerza = 0
    shooting_range = 0
    cooldown = 0
    def shoot(bichos):
        if self.canShoot():
            #a quien disparo
            #despues aplico hit y affect
        else:
            pass

class Veneno(tower):
    fuerza = 0
    shooting_range = 0
    cooldown = 0
    def shoot(bichos):
        if self.canShoot():
            #a quien disparo
            #despues aplico hit y affect
        else:
            pass

class Veneno(tower):
    fuerza = 0
    shooting_range = 0
    cooldown = 0
    def shoot(bichos):
        if self.canShoot():
            #a quien disparo
            #despues aplico hit y affect
        else:
            pass

class Veneno(tower):
    fuerza = 0
    shooting_range = 0
    cooldown = 0
    def shoot(bichos):
        if self.canShoot():
            #a quien disparo
            #despues aplico hit y affect
        else:
            pass

class Veneno(tower):
    fuerza = 0
    shooting_range = 0
    cooldown = 0
    def shoot(bichos):
        if self.canShoot():
            #a quien disparo
            #despues aplico hit y affect
        else:
            pass

class Veneno(tower):
    def __init__(self):
        fuerza = 0
        shooting_range = 0
        cooldown = 0
    def shoot(bichos):
        if self.canShoot():
            #a quien disparo
            #despues aplico hit y affect
        else:
            pass

class Veneno(tower):
    def __init__(self):
        fuerza = 0
        shooting_range = 0
        cooldown = 0
    def shoot(bichos):
        if self.canShoot():
            #a quien disparo
            #despues aplico hit y affect
        else:
            pass

class Veneno(tower):
    def __init__(self):
        fuerza = 0
        shooting_range = 0
        cooldown = 0
    def shoot(bichos):
        if self.canShoot():
            #a quien disparo
            #despues aplico hit y affect
        else:
            pass
"""
