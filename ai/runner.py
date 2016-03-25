#!/usr/bin/env python
"""Genetic experiment runner.

Usage:
    ./runner.py --help
    ./runner.py [-p POPULATION_SIZE] [-g GENERATIONS] [-m MUTATION_FACTOR] [-f GENERATIONS_FILE] [-t TOWERS_PER_GAME] [-e ELITE_GAMES]

Options:
    -h --help            Show this help.
    -g GENERATIONS       The number of generations to run.
    -p POPULATION_SIZE   The size of the population of each generation.
    -m MUTATION_FACTOR   The probability (0-1) of a child mutation at birth.
    -f GENERATIONS_FILE  File to save the generations data.
    -t TOWERS_PER_GAME   The number of towers to place in each game.
    -e ELITE_GAMES       The number of elite games that survive generations.
"""
from docopt import docopt

from ai.genetic_loop import Genetic


def run():
    """Run a genetic algorithm of games."""
    arguments = docopt(__doc__)

    pop_size = int(arguments['-p'] or 100)
    towers_per_game = int(arguments['-t'] or 10)
    mutation_factor = float(arguments['-m'] or 0.1)
    generations = int(arguments['-g'] or 100)
    elite_count = arguments['-e']
    if elite_count:
        elite_count = int(elite_count)

    genetic = Genetic()
    last_generation = genetic.loop(
        initial_games=genetic.random_generation(pop_size, towers_per_game),
        mutation_factor=mutation_factor,
        n_games=pop_size,
        max_iterations=generations,
        save_generations_to=arguments['-f'],
        elite_games_count=elite_count,
    )
    print(last_generation)


if __name__ == '__main__':
    run()


