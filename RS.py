#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from Lib.random import *
import numpy as np
import subprocess
import Lib.os
import matplotlib.pyplot as plt


def RS():
    #0
    array = []
    indexes = []
    with open('nile.txt') as data:
        for line in data:
            i, value = line.split()
            indexes.append(int(i))
            array.append(float(value))
    # array = [1.5, 1, 2, 3.5, 4, 2, 3, 1]
    N = len(array)
    # print(array)

    # wybieranie rozmiarów segmentów
    L = []
    w = N
    while w / 2 > 2:
        if w % 2 == 0:
            L.append(int(w / 2))
            w = w / 2
        else:
            w -= 1


    AVG = []
    for size in L:
        print('\n\nsize = ', size)
        Total = []
        i = 0
        Z = []
        tot_S = []
        while i <= N - size:
            seg = array[i:i+size]
            # print(seg)
            # wyliczenie srendniej -> funkcja average chyba tez bd ok
            m = (np.average(seg))
            # print(m)
            Y = []
            # Create a series of deviations for each range
            for s in range(i, i+size):
                # print(s)
                Y.append(array[s] - m)
            # the running total of the deviations from the mean for each series

            Z.append(np.sum(Y))

            S = cumulativeSum(size, seg, m)  # the standard deviation for each range
            S = np.sqrt(S/size)
            # print('\nostateczne S ', S)
            tot_S.append(S)

            i += size
        # print('\nZ = ', Z)
        R = max(Z) - min(Z)  # the widest difference in the series of deviations
        # print('R = ',R)
        # print('S dla n', tot_S)

        for s in tot_S:
            if s != 0:
                Total.append(R/s)
        # R_S = R/S  # rescaled range
        # Total.append(R_S)
        # print(Total)
        # Average the rescaled range values for each region to summarize each range
        AVG.append((np.average(Total)))

    # print(L)
    # print(AVG)
    plt.scatter(np.log(L), np.log(AVG), s=10)
    plt.title('RS Nile')
    result = np.polyfit(np.log(L), np.log(AVG), 1)

    # plt.text(5, 7.25, '\u03B1 = {}'.format(round(result[0], 2)))
    plt.text(4, -29.7, '\u03B1 = {}'.format(round(result[0], 2)))
    x1 = np.log(L[0])
    x2 = np.log(L[-1])
    plt.plot([np.log(L[0]), np.log(L[-1])], [result[0] * x1 + result[1], result[0] * x2 + result[1]], 'red')
    plt.show()


def cumulativeSum(size, array, m):
    cumulative_sum = 0
    for w in range(0, size):
        cumulative_sum += (array[w] - m) * (array[w] - m)
    return cumulative_sum


def mean(i, size, array):
    cumulative_sum = 0
    for w in range(i, i+size):
        print(w)
        cumulative_sum += array[w]
    return cumulative_sum / size


RS()
