#!/usr/bin/env python

import numpy as np

x1 = np.array([1,2,3,4,5,6])
x2 = np.array([1,1.5,2,2.5,3.5,6])
x3 = np.array([6,5,4,3,2,1])
y = np.random.random(6)

nvar = 3
one = np.ones(x1.shape)
A = np.vstack((x1,one,x2,one,x3,one)).T.reshape(nvar,x1.shape[0],2)

for i,Ai in enumerate(A):
    a = np.linalg.lstsq(Ai,y)[0]
    R = np.sqrt( ((y - Ai.dot(a))**2).sum() )
    print (R)