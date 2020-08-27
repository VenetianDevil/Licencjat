#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from Lib.random import *
import numpy as np
import matplotlib.pyplot as plt
from prepareFiles import *


def RS():
    #0
    indexes, X, L = prepareData('nile.txt', 165, 4)         # pobranie danych
    N = len(X)                                              # N = ilo�� badanych danych
    AVG = []                                                # tablica, w kt�rej zbieramy ko�cowe wyniki dla ka�dego n
    for n in L:                                     # (1)
        R_S = []                                    # warto�ci R/S dla n, warto�� R_S[1] odpowiada d�ugo�ci n z L[1]
        Z = []                                      # tablica sum odchyle� dla wszystkich serii o d�ugo�ci n
        total_S = []                                # zbi�r warto�ci S dla przedzia�u o d�ugo�ci n, S[1] -> L[1]
        i = 0
        while i <= N - n:                           # (2)
            segment = X[i:i+n]                      # wybranie kolejnego segmentu o d�ugo�ci n
            m = (np.average(segment))               # wyliczenie �rendniej dla wybranego segmentu o d�ugo�ci n
            Y = []                                  # Seria odchyle� dla danego segmentu
            for s in range(i, i+n):                 # (3)
                Y.append(X[s] - m)

            Z.append(np.sum(Y))                     # zapisanie pe�nego odchylenia �redniej dla przedzia�u

            S = cumulativeSum(n, segment, m)        # (4)
            S = np.sqrt(S/n)                        # Odchylenie standardowe dla wyznaczonego przedzia�u
            total_S.append(S)                       # (5)

            i += n                                  # wybranie pocz�tku nast�pnego przedzia�u o d�ugo�ci n

        R = max(Z) - min(Z)                         # (6) Najwi�ksza r�nica odchyle� dla wszystkich zbadanych podzia��w
        for s in total_S:                           # (7)
            if s != 0:
                R_S.append(R/s)                     # (8) wyznaczenie R/S dla ka�dego przedzia�u o d�ugo�ci n

        AVG.append(np.average(R_S))                 # (9) zapisanie �reniej ze wszystkich zebranych warto�ci R_S[n]

    plt.scatter(np.log(L), np.log(AVG), s=10)
    plt.title('RS Nile')
    plt.ylabel('log((R/S)/n)')
    plt.xlabel('log(n)')
    result = np.polyfit(np.log(L), np.log(AVG), 1)

    plt.text(3.5, -29.7, '\u03B1 = {}'.format(round(result[0], 2)))
    x1 = np.log(L[0])
    x2 = np.log(L[-1])
    plt.plot([np.log(L[0]), np.log(L[-1])], [result[0] * x1 + result[1], result[0] * x2 + result[1]], 'red')
    plt.show()


def cumulativeSum(size, array, m):
    cumulative_sum = 0
    for w in range(0, size):
        cumulative_sum += (array[w] - m) * (array[w] - m)       # (10)
    return cumulative_sum


RS()
