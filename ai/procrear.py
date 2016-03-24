import random

def procrear(esceA, esceB):
    corte = random.randint(1, len(esceA)-1)
    return  esceA[:corte] + esceB[corte:], esceB[:corte] + esceA[corte:]

