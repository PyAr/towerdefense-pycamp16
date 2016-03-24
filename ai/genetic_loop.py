from weighted_random import weighted_random_values
from procrear import procrear
from mute import mutacion
import random

def genetic_loop(
        initial_games,
        possible_positions = [],
        possible_towers = [],
        mutation_factor = 0.1,
        n_games = 10,
        cut_value = 0,
        max_iterations = 10000):

    if n_games % 2 != 0:
        raise Exception("n_games tiene que ser par")

    iterations = 0
    while True:
        childs = []
        for _ in range(n_games / 2):
            best_games = weighted_random_values(initial_games, 2)
            for child in procrear(best_games):
                childs.append(child)

        initial_games = []
        for child in childs:
            if random.random() <= mutation_factor:
                initial_games.append(mutacion(child, possible_positions, possible_towers))
            else:
                initial_games.append(child)

        if any([ x[1] == cut_value for x in best_games ]):
            best_game = [ x for x in best_games if x[1] == cut_value ][0]
            print("Best game is: %s" % best_game)
            break

        iterations += 1

        if iterations == max_iterations:
            print("Excedido de las iteraciones maximas")
            print("Juegos actuales: %s" % initial_games)
            break

