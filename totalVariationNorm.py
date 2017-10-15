#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

The total variation Norm

"""

def checkVectors(distrib_1,distrib_2):
    import numpy as np
    
    mu = np.asarray(distrib_1)
    nu = np.asarray(distrib_2)
    mu_sum = np.sum(mu)
    nu_sum = np.sum(nu)
    mu_chk = (mu >= 0)
    nu_chk = (nu >= 0)
        
    if mu.size != nu.size:
        print('vectors of diferent length')
        return False
        
    else:
        if (mu_sum != 1) or (nu_sum != 1):
           #print('one of the vectors is not a probability distribution')
            return False
        else:
            if (mu_chk.all() != True) or (nu_chk.all() != True):
                #print('one of the vectors is not a probability distribution')
                return False
            else:
                if mu.shape != nu.shape:
                    return True
                    
        
def totalVariation1(distrib_1,distrib_2):
    import numpy as np
    
    if checkVectors(distrib_1,distrib_2) == False:
        mu = np.asarray(distrib_1)
        nu = np.asarray(distrib_2)
        
        return np.max(np.abs(mu - nu))
        
    else:
        print('Not possible to calculate measure of the vectors')
        
        
def totalVariation2(distrib_1,distrib_2):
    import numpy as np
    
    if checkVectors(distrib_1,distrib_2) == True:
        mu = np.asarray(distrib_1)
        nu = np.asarray(distrib_2)
        temp = []
    
        for x in range(0,nu.size):
            temp.append(np.abs(mu[x] - nu[x]))
        
        temp = np.asarray(temp)
        
        return (0.5)*temp.sum()
        
    else:
        print('Not possible to calculate measure of the vectors')       
    