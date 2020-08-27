#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from random import *
import numpy as np
import matplotlib.pyplot as plt
from prepareFiles import *

def prepareData():
    array = []
    indexes = []
    with open('nile.txt') as data:
        for line in data:
            i, value = line.split()
            indexes.append(int(i))
            array.append(float(value))
    # array = [1.5, 1, 2, 3.5, 4, 2, 3, 1, 5.5, 7, 6, 8, 7, 9, 6.5, 5.5]
    # indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    L = []
    w = len(array)
    while w / 2 >= 2:
        if w % 2 == 0:
            L.append(int(w / 2))
            w = w / 2
        else:
            w -= 1

    print(L)
    return indexes, array, L

def DMA():
    # 0
    indexes, array, L = prepareData()
    N = len(array)

    modifiedStandardDeviation = []
    for n in L:
        # 1 srednia ruchoma dla przedziałów dlugosci n
        i = n-1
        # print('n = ', n)
        movingAverage = []
        while i < N:
            cumulative_sum = 0.0
            for k in range(0, n):
                cumulative_sum += array[i-k]
            movingAverage.append(cumulative_sum/n)
            i += 1

        #2
        sum = 0.0
        for i in range(0, len(movingAverage)):
            sum += (array[i+n-1] - movingAverage[i]) * (array[i+n-1] - movingAverage[i])
        modifiedStandardDeviation.append(np.sqrt(sum / (N - n)))


    # 3 double logaritmic plot
    plt.scatter(np.log(L), np.log(modifiedStandardDeviation), s=20)
    plt.title('DMA nile')
    plt.ylabel(r'log($\sigma_{DMA}(n)$)')
    plt.xlabel('log(n)')

    result = np.polyfit(np.log(L), np.log(modifiedStandardDeviation), 1)
    print('alfa = ', result[0])
    print(result)

    plt.text(4, 4.46, '\u03B1 = {}'.format(round(result[0], 2)))
    x1 = np.log(L[0])
    x2 = np.log(L[-1])
    plt.plot([np.log(L[0]), np.log(L[-1])], [result[0] * x1 + result[1], result[0] * x2 + result[1]], 'red')
    plt.show()


DMA()
