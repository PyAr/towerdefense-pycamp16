import random


def procrear(escenario_a, escenario_b):
    corte = random.randint(1, len(escenario_a)-1)
    return (escenario_a[:corte] + escenario_b[corte:],
            escenario_b[:corte] + escenario_a[corte:])
