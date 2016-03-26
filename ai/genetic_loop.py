from weighted_random import weighted_random_values
from core import get_available_locations, get_tower_types, start
import random
import sys
from multiprocessing import Pool, cpu_count



def play(game):
    return game, start(game)

def add_game_values(games):
    pool = Pool(cpu_count())

    return pool.map(play, games)


class Genetic:
    def __init__(self):
        self.available_locations = get_available_locations()
        self.tower_types = get_tower_types()

    def mutate(self, game):
        coord_used = game.keys()
        coord_free = self.free_coord(coord_used)
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

    def free_coord(self, coord_used):
        coord_free = []
        for i in self.available_locations:
            if i not in coord_used:
                coord_free.append(i)
        return coord_free

    def change_coord(self, coord, list_coord_used):
        x1, y1 = coord
        def distance(other_coord):
            x2, y2 = other_coord
            return abs(x1 - x2) + abs(y1 - y2)

        list_coord_used.append(coord)
        coord_free = self.free_coord(list_coord_used)
        close_coords = list(sorted(coord_free, key=distance))[:3]
        coord = random.choice(close_coords)
        return coord

    def build_valid_child(self, towers):
        child = {}
        for position, tower_type in towers:
            if position in child:
                position = self.change_coord(position, list(child.keys()))
            child[position] = tower_type

        assert len(child) == len(towers)

        return child

    def crossover(self, game1, game2):
        child1 = {}
        child2 = {}

        towers = []
        towers.extend(game1.items())
        towers.extend(game2.items())

        random.shuffle(towers)
        half = int(len(towers) / 2)

        child1 = self.build_valid_child(towers[:half])
        child2 = self.build_valid_child(towers[half:])

        return child1, child2

    def random_game(self, towers_size):
        available = list(self.available_locations[:])
        random.shuffle(available)
        positions = [available.pop()
                     for _ in range(towers_size)]
        return {position: random.choice(self.tower_types)
                for position in positions}

    def random_generation(self, population_size, towers_size):
        return [self.random_game(towers_size)
                for _ in range(population_size)]

    def loop(self, initial_games, mutation_factor, n_games, max_iterations,
             save_generations_to=None, elite_games_count=None):

        if save_generations_to:
            self.prepare_generations_file(save_generations_to)

        if n_games % 2 != 0:
            raise Exception("n_games tiene que ser par")

        iterations = 0
        current_games = add_game_values(initial_games)
        elite_games = []
        while True:
            print('.', end='')
            sys.stdout.flush()
            if save_generations_to:
                self.save_generation(current_games)

            if iterations == max_iterations:
                return current_games

            childs = []
            for _ in range(int(n_games / 2)):
                chosen_parents = weighted_random_values(current_games + elite_games, 2)
                for child in self.crossover(*chosen_parents):
                    if random.random() <= mutation_factor:
                        child = self.mutate(child)

                    childs.append(child)

            childs = add_game_values(childs)

            best_of_all_games = sorted(current_games + childs + elite_games,
                                       key=lambda t: t[1])
            if elite_games_count:
                elite_games = list(best_of_all_games)[-elite_games_count:]

            current_games = childs
            iterations += 1

    def prepare_generations_file(self, generations_file_name):
        self.generations_file = open(generations_file_name, 'w')

    def save_generation(self, games):
        line = repr(games)
        self.generations_file.write(line + '\n')
        self.generations_file.flush()
