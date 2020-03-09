#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from Lib.random import *
import numpy as np
import subprocess
import Lib.os
import matplotlib.pyplot as plt


# def generate_gaussian(N, mu, sigma):
#     array = [None] * N
#     for i in range(0, N):
#         array[i] = gauss(mu, sigma)
#     return array


def DFA():
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

    # ??????????????????????????????????? jak dobrać te dlugosci??
    L = []
    for w in range(1, 15):
        L.append(w*int(((N/2)/15)))
    # L = [5, 11, 33, 66, 120, 165, 331]

    # 1 OK
    avg = np.average(array)

    # 2 OK
    randomWalk = []
    for j in range(0, N):
        cumulative_sum = 0.0
        for i in range(0, j):
            cumulative_sum += array[i] - avg
        randomWalk.append(cumulative_sum)

    # petla do wybierania długości segmentów
    F_avg = []
    for segment_size in L:
        # plt.plot(indexes, randomWalk)
        # 3
        temp_array = randomWalk.copy()
        X = []
        for i in range(0, segment_size):
            X.append(i)

        i = 0
        k = indexes[0]
        F = []
        while i <= N - segment_size:
            # znalezienie prostej w segmencie: line[0]=a; line[1]=b;
            line = np.polyfit(X, temp_array[0:segment_size], 1)
            del temp_array[0:segment_size]
            # plt.plot([i+indexes[0], i+segment_size-1+indexes[0]],
            #          [line[0] * 0 + line[1], line[0] * segment_size + line[1]], 'r')

            # 4 wyliczenie F
            F.append(calculateF(line, segment_size, i, k, randomWalk))
            k = k + segment_size
            i = i + segment_size
        # plt.show()

        print(F)
        # 5 obliczenie sredniej fluktuacji dla danej dlugosci segmentu
        F_avg.append(np.average(F))
        print(segment_size, np.average(F))

    print('lista sredniach F', F_avg)

    #6 double logaritmic plot
    plt.scatter(np.log(L), np.log(F_avg), s=10)
    plt.show()

    result = np.polyfit(np.log(L), np.log(F_avg), 1)
    print('alfa = ', result[0])


def calculateF(line, size, i, k, array):
    segment_sum = 0
    for n in range(i, i + size):
        segment_sum += (array[n] - (line[0] * k) - line[1]) * (array[n] - (line[0] * k) - line[1])
        k = k + 1

    F = np.sqrt((1 / size) * segment_sum)
    return F


DFA()
