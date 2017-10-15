#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:20:10 2017
A matrix of a Markov Chain is creatated
@author: eddie
"""

def markovTreeMatrix(depth, arity=2, lazy=False):
    from makeTree import tree
    import numpy as np
    import math as mt
    
    if lazy == True:
        T = tree(depth, arity)
        G = []
        for v in T[1]:
            G.append(tuple(sorted(v,reverse=True)))
        #for v in T[0]:
        #    G.append((v,v))
            
        G = T[1] + G
        G = sorted(G)
        
        nodes = mt.pow(arity,depth - 1) - 1  # this is the first leaf
        
        n = len(T[0])
        
        R = np.zeros((n,n))  # we define a zeros matrix
        
        for x in G:
            if x[0] == 0:
                R[x] = (1/arity)  # the probability of moving from the root
                
            if x[0] > 0 and x[1] >= nodes:
                R[x] = (1/(arity + 1))  # the probability of moving from middle nodes
            
            if x[0] >= nodes:
                R[x] = 1  # the probability of moving from a leaf
                
        for y in G:
            if R[y] == 0:
                R[y] = (1/(arity + 1))
                
        E = []

        for m in range(0,len(R)):
            E.append((m,m))
    
        for z in E:
            R[z] = (1/2)
            
        #R = (1/2)*R  # this is lazy because we have 0.5 probability of not moving from our node
                        
        return R
    
    else:
        T = tree(depth, arity)
        G = []
        for v in T[1]:
            G.append(tuple(sorted(v,reverse=True)))
            
        G = T[1] + G
        
        nodes = mt.pow(arity,depth - 1) - 1
        
        n = len(T[0])
        
        R = np.zeros((n,n))
        
        for x in G:
            if x[0] == 0:
                R[x] = (1/arity)
                
            if x[0] > 0 and x[1] >= nodes:
                R[x] = (1/(arity + 1))
            
            if x[0] >= nodes:
                R[x] = 1
                
        for y in G:
            if R[y] == 0:
                R[y] = (1/(arity + 1))
            
        return R
        
T = markovTreeMatrix(5,2,False)