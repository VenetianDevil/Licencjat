#!/usr/bin/python
# -*- coding: iso-8859-2 -*-


def prepareData(file, max_n, min_n):
    X = []
    indexes = []
    with open(file) as data:
        for line in data:
            i, value = line.split()
            indexes.append(int(i))
            X.append(float(value))

    L = []
    if max_n:
        w = max_n
    else:
        w = len(X)

    # while w / 2 > min_n:
    #     if w % 2 == 0:
    #         L.append(int(w / 2))
    #         w = w / 2
    #     else:
    #         w -= 1
    
    while w > min_n:
        L.append(int(w))
        w = w-1

    return indexes, X, L



