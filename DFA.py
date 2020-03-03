#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
from random import *
import numpy as np
import subprocess
import os

def generate_gaussian(N, mu, sigma):
    array = [None] * N
    for i in range(0, N):
        array[i] = gauss(mu, sigma)
    return array

def DFA():
    L = 200
    X = []
    # 0
    # array = generate_gaussian(N, 0, 1)
    array = []
    with open('data_to_DFA.txt') as data:
        for line in data:
            i, value = line.split()
            array.append(float(value))
    # N = len(array)

    plik = open('data.dat', 'w')
   
    # 1
    avg = np.average(array)

    # 2
    randomWalk = []
    for j in range (0, len(array)):
        cumul_sum = 0.0
        for i in range (0, j):
            cumul_sum += array[i] - avg
        randomWalk.append(cumul_sum)
    write_to_file(plik, randomWalk)

    # 3
    linear_plik = open('linear.dat', 'w')
    temp_array = randomWalk.copy()
    for i in range(0,L):
        X.append(i)
    i=0
    F = []
    while i <= len(randomWalk)-L:
        line = np.polyfit(X, temp_array[0:L], 1)
        del temp_array[0:L]
        write_line_file (linear_plik, line, i, i+L-1, L)
        
        # 4
        F.append(calculate_F(line, L, i, randomWalk))
        i=i+L

    # 5
    F_avg = np.average(F)
    
    plik.close()
    linear_plik.close()
    os.system("gnuplot create.gnu")
    
    return cumul_sum

def calculate_F(line, L, i, array):
    segment_sum = 0
    for n in range(i, i+L-1):
        segment_sum += (array[n] - line[0]*n - line[1])* (array[n] - line[0]*n - line[1])

    F = np.sqrt((1/L)*segment_sum)
    return F

def write_to_file(plik, L):
    for i in range(0, len(L)):
        plik.write(str(i) + "\t" + str(L[i]) + "\n")

def write_line_file(plik, line, one, two, L):
    plik.write('\n')
    plik.write(str(one) + "\t" + str(line[0]*0 + line[1]) + "\n")
    plik.write(str(two) + "\t" + str(line[0]*L + line[1]) + "\n")
    plik.write('\n')

print (DFA())