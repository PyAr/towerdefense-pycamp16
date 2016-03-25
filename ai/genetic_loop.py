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

        current_games = add_game_values(childs)
        iterations += 1

        if iterations == max_iterations:
            return current_games


if __name__ == '__main__':
    initial_games = []
    genetic_loop(
      initial_games,
      get_available_locations(),
      get_tower_types()
    )
