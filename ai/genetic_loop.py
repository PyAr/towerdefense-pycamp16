from weighted_random import weighted_random_values
from core import get_available_locations, get_tower_types, start
import random


def add_game_values(games):
    with_values = []
    for game in games:
        with_values.append((game, start(game)))

    return with_values


class Genetic:
    def __init__(self):
        self.available_locations = get_available_locations(),
        self.tower_types = get_tower_types()

    def mutate(self, game):
        return game

    def crossover(self, game1, game2):
        child1 = {}
        child2 = {}

        towers = []
        towers.extend(game1.items())
        towers.extend(game2.items())

        random.shuffle(towers)
        half = len(towers) / 2

        child1 = dict(towers[:half])
        child2 = dict(towers[half:])

        return child1, child2

    def loop(self, initial_games, mutation_factor=0.1, n_games=10, cut_value=0,
             max_iterations=10000):

        if n_games % 2 != 0:
            raise Exception("n_games tiene que ser par")

        iterations = 0
        current_games = add_game_values(initial_games)
        while True:
            childs = []
            for _ in range(n_games / 2):
                chosen_parents = weighted_random_values(current_games, 2)
                for child in self.crossover(*chosen_parents):
                    if random.random() <= mutation_factor:
                        child = self.mutate(child)

                    childs.append(child)

            current_games = add_game_values(childs)
            iterations += 1

            if iterations == max_iterations:
                return current_games


if __name__ == '__main__':
    genetic = Genetic()
    genetic.loop([])
