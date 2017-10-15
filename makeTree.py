#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:14:29 2017
This function creates a Tree given a depth and an optional arity.
The output can be the set of vertex and edges, or the adjacency 
matrix of the tree.
@author: eddie
"""

try:
    def tree(depth,n_arity=2,matrix=False,self_loop = False):
        import numpy as np
        import math as mt
        
        if (n_arity >= 2) and (depth > 1):  # this checks the depth and arity of the tree
            E = []
            i = 0
            n = int((mt.pow(n_arity,depth) - 1)/(n_arity - 1))  # number of vertex in the tree
            for r in range(0,n_arity,n_arity):  # this for builds the edges of the tree 
                i=0
                for j in range(1,n):
                    E.append((i,j))
                    if (np.mod(j,n_arity)) == 0:
                        i+=1
                                
            if (matrix == False) and (self_loop == True):
                for r in range(0,n):
                    E.append((r,r))
                    
                G = []
                V = []
                
                for v in range(n):
                    V.append(v)
                        
                G = [V, sorted(E)]
                return G
        
            if (matrix == True) and (self_loop == True):
                G = []
                for v in E:
                    G.append(tuple(sorted(v,reverse=True)))
                
                E = E + G
                for r in range(0,n):
                    E.append((r,r))
                
                R = np.zeros((n,n))
                for v in E:
                    R[v] = 1

                return R
        
            if (matrix == False) and (self_loop == False):
                G = []
                V = []
                for v in range(n):
                    V.append(v)
                    
                G = [V, E]
                return G
            else:
                G = []
                for v in E:
                    G.append(tuple(sorted(v,reverse=True)))

                E = E + G
                R = np.zeros((n,n))
                
                for v in E:
                    R[v] = 1

                return R
        if depth == 1:
            V = [0]
            E = []
            
            if (matrix == True) and (self_loop == False):
                print('This option is not available whith depth 1 and no loop')
                
            if (matrix == True) and (self_loop == True):
                R = np.zeros((1,1))
                R[0,0] = 1
                return R
            
            if (matrix == False) and (self_loop == True):
                E = [(0,0)]
                G = [V,E]
                
                return G
            
            G = [V,E]
            return G
        
        if n_arity == 1 and depth > 1:
            E = []
            n = depth
            for i in range(0,n-1):
                E.append((i,i+1))
            
            if (matrix == False) and (self_loop == True):
                for r in range(0,n):
                    E.append((r,r))
                    
                G = []
                V = []
                
                for v in range(n):
                    V.append(v)
                    
                G = [V, sorted(E)]
                return G
        
            if (matrix == True) and (self_loop == True):
                G = []
                for v in E:
                    G.append(tuple(sorted(v,reverse=True)))
                
                E = E + G
                
                for r in range(0,n):
                    E.append((r,r))
                
                R = np.zeros((n,n))
                
                for v in E:
                    R[v] = 1

                return R
        
            if (matrix == False) and (self_loop == False):
                G = []
                V = []
                
                for v in range(n):
                    V.append(v)
                    
                G = [V, E]
                return G
            else:
                G = []
                
                for v in E:
                    G.append(tuple(sorted(v,reverse=True)))

                E = E + G
                R = np.zeros((n,n))
                
                for v in E:
                    R[v] = 1

                return R
            
        if (n_arity < 1) or (depth < 1):
            print('There is no tree with this properties!!!')
        
except IndexError:
    print('error!')

T = tree(3,2,False, True)


        