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

        coord_used = game.keys()
        coord_free = free_coord(coord_used)
        mutation_num = random.randint(0, len(game))
        for i in range(mutation_num):
            if (i % 2) == 0:
                # cambiar posiciones de torres
                old_pos, new_pos = random.choice(list(zip(game, coord_free)))
                game[new_pos] = game[old_pos]
                del game[old_pos]
                coord_free.append(old_pos)
                coord_free.remove(new_pos)
            else:
                # cambiar torres
                coord_tower, new_tower = random.choice(list(zip(game, self.tower_types)))
                game[coord_tower] = new_tower
        return game

    def free_coord(coord_used):
        coord_free = []
        for i in self.available_locations:
            if i not in coord_used:
                coord_free.append(i)
        return coord_free

    def change_coord(coord, list_coord_used):
        list_coord_used.append(coord)
        coord_free = free_coord(list_coord_used)
        coord = random.choice(coord_free)
        return coord

    def build_valid_child(self, towers):
        # TODO fix repeated towers
        return dict(towers)

    def crossover(self, game1, game2):
        child1 = {}
        child2 = {}

        towers = []
        towers.extend(game1.items())
        towers.extend(game2.items())

        random.shuffle(towers)
        half = len(towers) / 2

        child1 = self.build_valid_child(towers[:half])
        child2 = self.build_valid_child(towers[half:])

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
