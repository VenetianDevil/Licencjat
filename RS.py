#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from Lib.random import *
import numpy as np
import matplotlib.pyplot as plt
from prepareFiles import *


def RS():
    #0
    indexes, X, L = prepareData('nile.txt', 165, 4)         # pobranie danych
    N = len(X)                                              # N = ilość badanych danych
    AVG = []                                                # tablica, w której zbieramy końcowe wyniki dla każdego n
    for n in L:                                     # (1)
        R_S = []                                    # wartości R/S dla n, wartość R_S[1] odpowiada długości n z L[1]
        Z = []                                      # tablica sum odchyleń dla wszystkich serii o długości n
        total_S = []                                # zbiór wartości S dla przedziału o długości n, S[1] -> L[1]
        i = 0
        while i <= N - n:                           # (2)
            segment = X[i:i+n]                      # wybranie kolejnego segmentu o długości n
            m = (np.average(segment))               # wyliczenie śrendniej dla wybranego segmentu o długości n
            Y = []                                  # Seria odchyleń dla danego segmentu
            for s in range(i, i+n):                 # (3)
                Y.append(X[s] - m)

            Z.append(np.sum(Y))                     # zapisanie pełnego odchylenia średniej dla przedziału

            S = cumulativeSum(n, segment, m)        # (4)
            S = np.sqrt(S/n)                        # Odchylenie standardowe dla wyznaczonego przedziału
            total_S.append(S)                       # (5)

            i += n                                  # wybranie początku następnego przedziału o długości n

        R = max(Z) - min(Z)                         # (6) Największa różnica odchyleń dla wszystkich zbadanych podziałów
        for s in total_S:                           # (7)
            if s != 0:
                R_S.append(R/s)                     # (8) wyznaczenie R/S dla każdego przedziału o długości n

        AVG.append(np.average(R_S))                 # (9) zapisanie śreniej ze wszystkich zebranych wartości R_S[n]

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
