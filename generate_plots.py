"""

Chad Bloxham. CS 260P Project 1. May 3rd, 2019.

This file takes the data generated in generate_data.py and plots it as well as
the linear regression models of the data.
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_plots(N_file, rand_file, as_file):
    # load data
    N = np.loadtxt(N_file, delimiter=' ')
    rand_times = np.loadtxt(rand_file, delimiter=' ')
    as_times = np.loadtxt(as_file, delimiter=' ')

    # take log base 2 of data
    logN = np.log2(N)
    logRT = np.log2(rand_times)
    logAST = np.log2(as_times)
    # labels and plot colors for each gap sequence
    labels = ['Original', 'A168604', 'Pratt', 'A036562', 'My Seq']
    colors = ['b', 'r', 'y', 'm', 'g']

    # create plot for runtimes on random arrays
    for i in range(len(logRT)):
        plt.plot(logN, logRT[i], '.', color=colors[i])
        # compute linear regression
        rand_fit = np.polyfit(logN, logRT[i], 1)
        slope = ', m = ' + str(rand_fit[0])[0:6]
        rand_fit_fn = np.poly1d(rand_fit)
        # plot linear regression
        plt.plot(logN, rand_fit_fn(logN), '--', color=colors[i], label=labels[i]+slope)
    # format plot
    plt.title('Runtime of Shell Sort on Random Permutations of Length N')
    plt.xlabel('logN (base 2)')
    plt.ylabel('logT (base 2)')
    plt.legend(title='Gap Sequences', loc='upper left')
    plt.show()

    # create plot for runtimes on almost sorted arrays
    for i in range(len(logAST)):
        plt.plot(logN, logAST[i], '.', color=colors[i])
        # compute linear regression
        as_fit = np.polyfit(logN, logAST[i], 1)
        slope = ', m = ' + str(as_fit[0])[0:6]
        as_fit_fn = np.poly1d(as_fit)
        # plot linear regression
        plt.plot(logN, as_fit_fn(logN), '--', color=colors[i], label=labels[i]+slope)
    # format plot
    plt.title('Runtime of Shell Sort on Almost-Sorted Permutations of Length N')
    plt.xlabel('logN (base 2)')
    plt.ylabel('logT (base 2)')
    plt.legend(title='Gap Sequences', loc='upper left')
    plt.show()
