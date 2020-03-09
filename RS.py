#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from Lib.random import *
import numpy as np
import subprocess
import Lib.os
import matplotlib.pyplot as plt


def RS():
    # 0
    # array = generate_gaussian(N, 0, 1)
    array = []
    indexes = []
    with open('data_to_DFA.txt') as data:
        for line in data:
            i, value = line.split()
            indexes.append(int(i))
            array.append(float(value))
    N = len(array)

    # wybieranie rozmiarów segmentów
    L = []
    for w in range(2, 15):
        L.append(w*int(((N/2)/15)))

    Z = []
    AVG = []
    for size in L:
        Total = []
        for i in range(0, N-size):
            # wyliczenie srendniej -> funkcja average chyba tez bd ok
            m = (mean(i, size, array))
            z_t = 0
            # Create a series of deviations for each range
            for s in range(i, i+size-1):
                # print(s)
                z_t += (array[s] - m)
            # the running total of the deviations from the mean for each series
            Z.append(z_t)
            R = max(Z) - min(Z)  # the widest difference in the series of deviations
            S = np.sqrt((1/size)*cumulativeSum(i, size, array, m))  # the standard deviation for each range
            R_S = R/S  # rescaled range
            Total.append(R_S)
            i += size
        # Average the rescaled range values for each region to summarize each range
        AVG.append((np.average(Total)))

    plt.scatter(np.log(L), np.log(AVG), s=10)
    plt.show()


def cumulativeSum(i, size, array, mean):
    cumulative_sum = 0
    for w in range(i, i+size-1):
        cumulative_sum += (array[w] - mean) * (array[w] - mean)
    return cumulative_sum


def mean(i, size, array):
    cumulative_sum = 0
    for w in range(i, i+size-1):
        # print(w)
        cumulative_sum += array[w]
    return (1/size)*cumulative_sum


RS()
