#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from random import *
import numpy as np
import matplotlib.pyplot as plt
from prepareData import *

def DMA():
    # 0
    indexes, X, L = prepareData('files/zurich.txt', 50, 4)
    N = len(X)

    modifiedStandardDeviation = []
    for n in L:
        # 1 srednia ruchoma dla przedziałów dlugosci n
        i = n-1
        movingAverage = X.copy()
        while i < N:
            cumulative_sum = 0.0
            for k in range(0, n):
                cumulative_sum += X[i-k]
            movingAverage[i] = cumulative_sum/n
            i += 1

        #2
        sum = 0.0
        for i in range(n, N):
            sum += (X[i-1] - movingAverage[i-1]) * (X[i-1] - movingAverage[i-1])
        modifiedStandardDeviation.append(np.sqrt(sum / (N - n)))


    # 3 double logaritmic plot
    plt.scatter(np.log(L), np.log(modifiedStandardDeviation), s=20)
    plt.title('DMA zurich')
    plt.ylabel(r'log($\sigma_{DMA}(n)$)')
    plt.xlabel('log(n)')

    result = np.polyfit(np.log(L), np.log(modifiedStandardDeviation), 1)
    print('alfa = ', result[0])
    print(result)

    plt.text(3.3, 3.6, '\u03B1 = {}'.format(round(result[0], 2)))
    x1 = np.log(L[0])
    x2 = np.log(L[-1])
    plt.plot([np.log(L[0]), np.log(L[-1])], [result[0] * x1 + result[1], result[0] * x2 + result[1]], 'red')
    plt.show()


DMA()
