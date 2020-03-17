#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from Lib.random import *
import numpy as np
import matplotlib.pyplot as plt


def prepareData():
    array = []
    with open('nile.txt') as data:
        for line in data:
            i, value = line.split()
            array.append(float(value))
    # array = [1.5, 1, 2, 3.5, 4, 2, 3, 1]

    L = []
    w = len(array)
    while w / 2 > 4:
        if w % 2 == 0:
            L.append(int(w / 2))
            w = w / 2
        else:
            w -= 1

    return array, L


def RS():
    #0
    array, L = prepareData()
    N = len(array)
    AVG = []
    for size in L:
        print('\n\nsize = ', size)
        Total = []
        i = 0
        Z = []
        tot_S = []
        while i <= N - size:
            seg = array[i:i+size]
            # wyliczenie srendniej -> funkcja average chyba tez bd ok
            m = (np.average(seg))
            Y = []
            # Create a series of deviations for each range
            for s in range(i, i+size):
                Y.append(array[s] - m)
            # the running total of the deviations from the mean for each series

            Z.append(np.sum(Y))

            S = cumulativeSum(size, seg, m)  # the standard deviation for each range
            S = np.sqrt(S/size)
            tot_S.append(S)

            i += size

        R = max(Z) - min(Z)  # the widest difference in the series of deviations
        for s in tot_S:
            if s != 0:
                Total.append(R/s)
        # Average the rescaled range values for each region to summarize each range
        AVG.append((np.average(Total)))

    plt.scatter(np.log(L), np.log(AVG), s=10)
    plt.title('RS Nile')
    result = np.polyfit(np.log(L), np.log(AVG), 1)

    plt.text(3.5, -29.7, '\u03B1 = {}'.format(round(result[0], 2)))
    x1 = np.log(L[0])
    x2 = np.log(L[-1])
    plt.plot([np.log(L[0]), np.log(L[-1])], [result[0] * x1 + result[1], result[0] * x2 + result[1]], 'red')
    plt.show()


def cumulativeSum(size, array, m):
    cumulative_sum = 0
    for w in range(0, size):
        cumulative_sum += (array[w] - m) * (array[w] - m)
    return cumulative_sum


RS()
