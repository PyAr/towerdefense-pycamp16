#!/usr/bin/env python
"""Genetic history reports.

Usage:
    ./reporting.py --help
    ./reporting.py REPORT_TYPE GENERATIONS_FILE

Options:
    -h --help            Show this help.
    REPORT_TYPE          The report you want to print (possibles: values, ...)
    GENERATIONS_FILE     The file containing the history of generations.
"""
from docopt import docopt
from bokeh.plotting import figure, show, output_file


def read_generations(generations_file):
    with open(generations_file) as generations_data:
        return [eval(line)
                for line in generations_data.readlines()]


def values(generations):
    generation_indexes = range(len(generations))

    fig = figure()

    fig.xaxis.axis_label = 'generation'

    maxes = [max([value for game, value in generation])
             for generation in generations]
    mins = [min([value for game, value in generation])
            for generation in generations]
    averages = [sum([value for game, value in generation]) / len(generation)
                for generation in generations]

    value_groups = (
        ('max value', 'green', maxes),
        ('min value', 'red', mins),
        ('average value', 'blue', averages),
    )

    for name, color, values in value_groups:
        fig.line(generation_indexes, values, color=color, legend=name)

    output_file("values.html")
    show(fig)


def run():
    """Run a genetic algorithm of games."""
    arguments = docopt(__doc__)

    report_type = arguments['REPORT_TYPE']
    generations_file = arguments['GENERATIONS_FILE']

    globals()[report_type](read_generations(generations_file))

if __name__ == '__main__':
    run()


