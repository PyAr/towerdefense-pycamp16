#!/usr/bin/env python
"""Genetic history reports.

Usage:
    ./reporting.py --help
    ./reporting.py REPORT_TYPE GENERATIONS_FILE [-t TOWER_TYPE]

Options:
    -h --help            Show this help.
    REPORT_TYPE          The report you want to print (alternatives: values,
                         heatmap, ...)
    GENERATIONS_FILE     The file containing the history of generations.
    -t TOWER_TYPE        Filter data for the specified tower type.
"""
from docopt import docopt
import numpy as np
from bokeh.plotting import figure, show, output_file


def read_generations(generations_file):
    with open(generations_file) as generations_data:
        return [eval(line)
                for line in generations_data.readlines()]


class Report():
    def __init__(self, generations, tower_type=None):
        self.generations = generations
        self.tower_type = tower_type

    def values(self):
        generation_indexes = range(len(self.generations))

        fig = figure(title='Game values over generations')

        fig.xaxis.axis_label = 'generation'

        maxes = [max([value for game, value in generation])
                 for generation in self.generations]
        mins = [min([value for game, value in generation])
                for generation in self.generations]
        averages = [sum([value for game, value in generation]) / len(generation)
                    for generation in self.generations]

        value_groups = (
            ('max value', 'green', maxes),
            ('min value', 'red', mins),
            ('average value', 'blue', averages),
        )

        for name, color, values in value_groups:
            fig.line(generation_indexes, values, color=color, legend=name)

        output_file("values.html")
        show(fig)

    def heatmap(self):
        img = np.zeros((5, 5), dtype=np.uint32)
        view = img.view(dtype=np.uint8).reshape((5, 5, 4))

        positions_sum = {}
        positions_count = {}
        positions_max = {}
        positions_min = {}
        for generation in self.generations:
            for game, value in generation:
                for position, tower_type in game.items():
                    if self.tower_type is not None and \
                       self.tower_type != tower_type:
                        continue

                    if position not in positions_sum:
                        positions_sum[position] = 0
                    positions_sum[position] += value
                    if position not in positions_count:
                        positions_count[position] = 0
                    positions_count[position] += 1
                    if position not in positions_max:
                        positions_max[position] = 0
                    positions_max[position] = max(positions_max[position],
                                                  value)
                    if position not in positions_min:
                        positions_min[position] = 0
                    positions_min[position] = min(positions_min[position],
                                                  value)

                    x, y = position
                    x = (x + 10) / 20 - 1
                    y = 4 - ((y + 10) / 20 - 1)
                    view[y, x, 0] = 0
                    view[y, x, 1] = 0
                    view[y, x, 2] = 0
                    view[y, x, 3] = (positions_sum[position] /
                                     positions_count[position]) * 2.5

        fig = figure(title='Game value over locations',
                     x_range=(0, 5), y_range=(0, 5))

        # must give a vector of images
        fig.image_rgba(image=[img], x=0, y=0, dw=5, dh=5)

        output_file("heatmap.html")

        show(fig)


def run():
    """Run a genetic algorithm of games."""
    arguments = docopt(__doc__)

    report_type = arguments['REPORT_TYPE']
    generations_file = arguments['GENERATIONS_FILE']
    tower_type = arguments['-t']

    report = Report(
        generations=read_generations(generations_file),
        tower_type=tower_type,
    )
    getattr(report, report_type)()

if __name__ == '__main__':
    run()


