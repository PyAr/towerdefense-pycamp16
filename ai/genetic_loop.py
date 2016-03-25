from weighted_random import weighted_random_values
from procrear import procrear
from mute import mutacion
from core import get_available_locations, get_tower_types, start
import random


def genetic_loop(
        initial_games,
        possible_positions=[],
        possible_towers=[],
        mutation_factor=0.1,
        n_games=10,
        cut_value=0,
        max_iterations=10000):

    if n_games % 2 != 0:
        raise Exception("n_games tiene que ser par")

    iterations = 0
    current_games = initial_games
    while True:

        values = []
        for towers in current_games:
            values.append((towers, start(towers)))

        childs = []
        for _ in range(n_games / 2):
            best_games = weighted_random_values(values, 2)
            for child in procrear(best_games):
                childs.append(child)

        current_games = []
        for child in childs:
            if random.random() <= mutation_factor:
                current_games.append(mutacion(child, possible_positions,
                                              possible_towers))
            else:
                current_games.append(child)

        if any([x[1] == cut_value for x in best_games]):
            best_game = [x for x in best_games if x[1] == cut_value][0]
            print("Best game is: %s" % best_game)
            break

        iterations += 1

        if iterations == max_iterations:
            print("Excedido de las iteraciones maximas")
            print("Juegos actuales: %s" % current_games)
            break


if __name__ == '__main__':
    initial_games = []
    genetic_loop(
      initial_games,
      get_available_locations(),
      get_tower_types()
    )
