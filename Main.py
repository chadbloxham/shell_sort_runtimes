"""

Chad Bloxham. CS 260P Project 1. May 3rd, 2019.

Main file for a set of programs which performs shell-sorting on integer arrays of
varying size (random as well as almost sorted). Compares the performance of five
different gap sequences (the separation of the indices compared in the shell-sort
process). See generate_gap_seq for a description of each gap sequence used.
"""

from generate_data import *
from generate_plots import *
import os


def main():
    if not (os.path.exists('as_times.txt') and os.path.exists('rand_times.txt') and os.path.exists('N.txt')):
        generate_data()
    generate_plots('N.txt', 'rand_times.txt', 'as_times.txt')


if __name__ == '__main__':
    main()
