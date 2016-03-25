from weighted_random import weighted_random_values
from procrear import procrear
from mute import mutacion
from core import get_available_locations, get_tower_types, start
import random


def add_game_values(games):
    with_values = []
    for game in games:
        with_values.append((game, start(game)))

    return with_values


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
    current_games = add_game_values(initial_games)
    while True:
        childs = []
        for _ in range(n_games / 2):
            chosen_parents = weighted_random_values(current_games, 2)
            for child in procrear(chosen_parents):
                if random.random() <= mutation_factor:
                    child = mutacion(child, possible_positions,
                                     possible_towers)

                childs.append(child)

        childs = add_game_values(childs)

        current_games = childs

        if any([x[1] == cut_value for x in current_games]):
            best_game = [x for x in current_games if x[1] == cut_value][0]
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
