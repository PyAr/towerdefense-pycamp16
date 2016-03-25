lista_de_torres=["Comunacha","Indecisa","Bullying","Fresquete","Zika","Patovica","ElNiño","Troll","Camper"]

#diccionario_de_torres={"Comunacha","Indecisa","Bullying","Fresquete","Zika","Patovica","ElNiño","Troll","Camper"}
"""
def get_kinds
    return ListaDeTorres=["Enum"]
"""

def get_tower(position,kind):
    return Tower(position)



#pasar un diccionario con los tipos de torres y los instanciadores de cada tipo
#de torre
class Tower:
    def shoot(self,bichos):
        if len(bichos)==0:
            return
        bichos = sorted(bichos, key = lambda x:x[1])
        bichos[0].affect(damage=self.fuerza)
        self.current_cooldown = self.cooldown

    def can_Shoot(self,cooldown):
        if self.current_cooldown == 0:
            return True
        else:
            self.current_cooldown -=1
            return False

    def __init__(self,posicion,rango=30,fuerza=200,cooldown=4):
        self.shooting_range = rango
        self.fuerza= fuerza
        self.posicion = posicion
        self.cooldown=cooldown
        self.current_cooldown = 0
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
