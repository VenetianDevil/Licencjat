#!/usr/bin/python
# -*- coding: iso-8859-2 -*-


def prepareData(file, start_length, end_length):
    array = []
    indexes = []
    with open(file) as data:
        for line in data:
            i, value = line.split()
            indexes.append(int(i))
            array.append(float(value))

    L = []
    if start_length:
        w = start_length
    else:
        w = len(array)

    # while w / 2 > end_length:
    #     if w % 2 == 0:
    #         L.append(int(w / 2))
    #         w = w / 2
    #     else:
    #         w -= 1

    for i in range(end_length, w):
        L.append(i)

    return indexes, array, L
