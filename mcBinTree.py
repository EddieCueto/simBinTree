# -*- coding: utf-8 -*-
"""
Simulation of a random walk on a finite b-ary tree of depth k

"""

import random as rn
import numpy as np
import matplotlib.pyplot as plt
import math as mt

rn.seed(666)

k = 20 # depth of the tree
b = 2 # arity of the tree
T = 100 # number of steps taken by the MC

E = np.zeros(exp)
M = np.zeros(exp)

for b in range(0,exp):
    X = np.zeros(T)
    Y = np.zeros(T)
    Z = np.zeros(T)

    for a in range(0, T):
        Z[a] = T

    X[0] = rn.randint(0,k) # setting the starting level for X
    Y[0] = rn.randint(0,k) # setting the starting level for Y

    for a in range(0, (T - 1)):
        monX = rn.randint(0,1)
        probArisX = rn.randint(0,(b + 1)) 
        monY = rn.randint(0,1)
        probArisY = rn.randint(0,(b + 1)) 
        if X[a] != Y[a]:
            if X[a] > 0 and X[a] < k:
                if monX == 1: 
                    X[a + 1] = X[a]
                if monX == 0: 
                    if probArisX == 0:
                        X[a + 1] = (X[a] - 1)
                    if probArisX != 0:
                        X[a + 1] = (X[a] + 1)
            if X[a] == 0:
                if monX == 1: 
                    X[a + 1] = 0
                if monX == 0:
                    X[a + 1] = 1
            if X[a] == k:
                if monX == 1: 
                    X[a + 1] = k
                if monX == 0:
                    X[a + 1] = (k - 1)
            if Y[a] > 0 and Y[a] < k:
                if monY == 1: 
                    Y[a + 1] = Y[a]
                if monY == 0: 
                    if probArisY == 0:
                        Y[a + 1] = (Y[a] - 1)
                    if probArisY != 0:
                        Y[a + 1] = (Y[a] + 1)
            if Y[a] == 0:
                if monY == 1: 
                    Y[a + 1] = 0
                if monY == 0:
                    Y[a + 1] = 1
            if Y[a] == k:
                if monY == 1: 
                    Y[a + 1] = k
                if monY == 0:
                    Y[a + 1] = (k - 1)
        if X[a] == Y[a]:
            Z[a] = a
            if X[a] > 0 and X[a] < k:
                if monX == 1: 
                    X[a + 1] = X[a]
                    Y[a + 1] = X[a + 1]
                if monX == 0: 
                    if probArisX == 0:
                        X[a + 1] = (X[a] - 1)
                        Y[a + 1] = X[a + 1]
                    if probArisX != 0:
                        X[a + 1] = (X[a] + 1)
                        Y[a + 1] = X[a + 1]
            if X[a] == 0:
                if monX == 1: 
                    X[a + 1] = 0
                    Y[a + 1] = X[a + 1]
                if monX == 0:
                    X[a + 1] = 1
                    Y[a + 1] = X[a + 1]
            if X[a] == k:
                if monX == 1: 
                    X[a + 1] = k
                    Y[a + 1] = X[a + 1]
                if monX == 0:
                    X[a + 1] = (k - 1)
                    Y[a + 1] = X[a + 1]
    E[b] = np.amin(Z)
    
m = np.mean(E)   
for b in range(0,exp):
    M[b] = m
    
n = (mt.pow(b,k + 1) - 1)/(b - 1)
#plt.hist(E,histtype='bar')

plt.plot(E,'bo',ms=0.8)
plt.plot(M, 'r')
plt.show()

#if m <= 4*n:
#    print('Test passed')