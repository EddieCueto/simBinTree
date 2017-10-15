#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 16:02:18 2017

@author: eddie
"""

from mcMatrix import markovTreeMatrix as mc
from totalVariationNorm import totalVariation1 as TV
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

np.random.seed(666)

arity = 2  # arity of tree
depth = 3  # depth of tree

P = mc(depth,arity)  # mc(depth of tree, arity of tree 2 by default)

pi = np.random.randn(len(P))  # the initial randomly generated vector, to show
                              # that in fact pi will converge to stationary.

stat = []
for x in range(0,len(P)):  # uniform distribution of the tree
    stat.append(1/arity)



near = []

for x in range(100):
    pi = P.dot(pi)
    near.append(TV(pi,stat))
    
    
red_patch = mpatches.Patch(color='red', label='TV convergence to stationary dist')
plt.legend(handles=[red_patch])    
plt.plot(near,'ro', ms='0.8')
plt.show()