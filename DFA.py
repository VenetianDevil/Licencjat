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
    array = []
    indexes = []
    with open('nile.txt') as data:
        for line in data:
            i, value = line.split()
            indexes.append(int(i))
            array.append(float(value))
    # array = [1.5, 1, 2, 3.5, 4, 2, 3, 1]
    # indexes = [1, 2, 3, 4, 5, 6, 7, 8]
    N = len(array)

    L = []
    w = N
    while w / 2 > 4:
        if w % 2 == 0:
            L.append(int(w / 2))
            w = w / 2
        else:
            w -= 1
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
        X = indexes.copy()
        # for i in range(0, segment_size):
        #     X.append(i)

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

    #6 double logaritmic plot
    plt.scatter(np.log(L), np.log(F_avg), s=20)
    # plt.title('DFA Nile')
    plt.title('DFA assigment 2')
    plt.ylabel('log(F(L))')
    plt.xlabel('log(L)')

    result = np.polyfit(np.log(L), np.log(F_avg), 1)
    print('alfa = ', result[0])
    print(result)

    # plt.text(5, 7.25, '\u03B1 = {}'.format(round(result[0], 2)))
    plt.text(6, 3.5, '\u03B1 = {}'.format(round(result[0], 2)))
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
