#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from Lib.random import *
import numpy as np
import matplotlib.pyplot as plt
from prepareFiles import *

def DFA():
    # 0
    indexes, array, L = prepareData('nile.txt', None, 2)
    N = len(array)

    # 1 średnia wszystkich danych
    avg = np.average(array)

    # 2 zmiana danych na random walk
    randomWalk = []
    cumulative_sum = 0.0
    for i in range(0, N):
        cumulative_sum += array[i] - avg
        randomWalk.append(cumulative_sum)

    # petla do wybierania długości segmentów
    F_avg = []
    for segment_size in L:
        # print(segment_size)
        # plt.plot(indexes, randomWalk)
        # plt.title('Nile random walk')

        # 3
        temp_array = randomWalk.copy()
        X = indexes.copy()
        i = 0
        k = indexes[0]
        F = []
        while i <= N - segment_size:
            # znalezienie prostej w segmencie: line[0]=a; line[1]=b;
            line = np.polyfit(X[0:segment_size], temp_array[0:segment_size], 1)

            del temp_array[0:segment_size]
            # plt.plot([X[0], X[segment_size-1]],
            #          [line[0] * X[0] + line[1], line[0] * X[segment_size - 1] + line[1]], 'r')
            del X[0:segment_size]

            # 4 wyliczenie F
            F.append(calculateF(line, segment_size, i, k, randomWalk))
            k = k + segment_size
            i = i + segment_size
        # plt.show()

        # 5 obliczenie sredniej fluktuacji dla danej dlugosci segmentu
        F_avg.append(np.average(F))
        print(segment_size, np.average(F))

    # 6 double logaritmic plot
    plt.scatter(np.log(L), np.log(F_avg), s=20)
    plt.title('DFA nile')
    plt.ylabel('log(F(L))')
    plt.xlabel('log(L)')

    result = np.polyfit(np.log(L), np.log(F_avg), 1)
    print('alfa = ', result[0])
    print(result)

    plt.text(5, 7.25, '\u03B1 = {}'.format(round(result[0], 2)))
    x1 = np.log(L[0])
    x2 = np.log(L[-1])
    plt.plot([np.log(L[0]), np.log(L[-1])], [result[0]*x1+result[1], result[0]*x2+result[1]], 'red')
    plt.show()


def calculateF(line, size, i, k, array):
    segment_sum = 0
    for n in range(i, i + size):
        segment_sum += (array[n] - (line[0] * k) - line[1]) * (array[n] - (line[0] * k) - line[1])
        k = k + 1

    F = np.sqrt((1 / size) * segment_sum)
    return F


DFA()
