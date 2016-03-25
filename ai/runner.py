#!/usr/bin/env python
"""Tota game runner.

Usage:
    ./runner.py --help
    ./runner.py [-g GENERATIONS] [-p POPULATION_SIZE] [-m MUTATION_FACTOR] [-f GENERATIONS_FILE]

Options:
    -h --help            Show this help.
    -g GENERATIONS       The number of generations to run.
    -p POPULATION_SIZE   The size of the population of each generation.
    -m MUTATION_FACTOR   The probability (0-1) of a child mutation at birth.
    -f GENERATIONS_FILE  File to save the generations data.
"""
from docopt import docopt

from ai.genetic_loop import Genetic


def run():
    """Run a genetic algorithm of games."""
    arguments = docopt(__doc__)

    pop_size = int(arguments['-p'])
    towers_per_game = 10

    genetic = Genetic()
    last_generation = genetic.loop(
        initial_games=genetic.random_generation(pop_size, towers_per_game),
        mutation_factor=float(arguments['-m']),
        n_games=pop_size,
        max_iterations=int(arguments['-g']),
        save_generations_to=arguments['-f'],
    )
    print(last_generation)


if __name__ == '__main__':
    run()


