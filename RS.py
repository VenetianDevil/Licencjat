#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from Lib.random import *
import numpy as np
import matplotlib.pyplot as plt
from prepareData import *

def RS():
    #0
    indexes, X, L = prepareData('files/zurich.txt', None, 2)   # pobranie danych
    N = len(X)                                               # N = ilość badanych danych
    AVG = []                                                 # tablica, w której zbieramy końcowe wyniki dla każdego n
    for n in L:                                              # (1)
        R_S = []                                             # wartości R/S dla serii o długości n
        R = []                                               # zbiór największych różnic odchyleń w przedziałach długości n
        S = []                                               # zbiór wartości odchyleń standardowych dla przedziałów o długości n
        i = 0
        while i <= N - n:                                    # (2)
            segment = X[i:i+n]                               # wybranie kolejnego segmentu o długości n
            m = np.average(segment)                        	 # wyliczenie średniej dla wybranego segmentu o długości n
            Y = []                                           # Seria odchyleń dla danego segmentu
            Z = []                                           # tablica sum odchyleń dla wszystkich serii o długości n
            for s in range(i, i+n):                          # (3)
                Y.append(X[s] - m)
                Z.append(np.sum(Y))                          # zapisanie pełnego odchylenia średniej dla przedziału
            
            R.append(max(Z) - min(Z))                        # (6) Największa rónica odchyleń dla zbadanego podziału
            S.append(satndardDeviation(n, Y))                # (4) Odchylenie standardowe dla wyznaczonego przedziału
                                                             # (5)
            i += n                                           # wybranie początku następnego przedziału o długości n

        for r, s in zip(R, S):                               # (7)
            if s != 0:
                R_S.append(r/s)                              # (8) wyznaczenie R/S dla każdego przedziału o długości n
        
        AVG.append(np.average(R_S))                          # (9) zapisanie średniej ze wszystkich zebranych wartości R_S[n]

    plt.scatter(np.log(L), np.log(AVG), s=10)
    plt.title('RS zurich')
    plt.ylabel('log((R/S)/n)')
    plt.xlabel('log(n)')
    result = np.polyfit(np.log(L), np.log(AVG), 1)
    print('alfa = ', result[0])

    plt.text(4, 2.75, '\u03B1 = {}'.format(round(result[0], 2)))
    x1 = np.log(L[0])
    x2 = np.log(L[-1])
    plt.plot([np.log(L[0]), np.log(L[-1])], [result[0] * x1 + result[1], result[0] * x2 + result[1]], 'red')
    plt.show()


def satndardDeviation(n, Y):
    cumulative_sum = 0
    for i in range(0, n):
        cumulative_sum += Y[i] * Y[i]                 # (10)
    return np.sqrt(cumulative_sum / n)


RS()
