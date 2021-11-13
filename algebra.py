#!/usr/bin/env python
# coding: utf-8

# In[ ]:



import numpy as numpy
import matplotlib.pyplot as plt
from numpy.linalg import inv

A= numpy.array([[2, -1], [-1, 2]])
print("A = ")
print (A)
print("")
B = numpy.array([0, 3])

print("B = ")
print(B)
print("")
k= numpy.linalg.solve(A,B)
print( "using .linalg.solve() X = ")
print(k)
 
    
print("")
inv =numpy.linalg.inv(A).dot(B)    
print("using .linalg.inv() inverse =")
print(inv)


V1 = numpy.array([2,-1])
V2 = numpy.array([-1,2])

Ve1= inv[0]*V1 # scaling V1 by x equals 1
Ve2 = inv[1]*V2 # scaling V2 by y equals 2

sum = Ve1 + Ve2

plt.ylabel('X')
plt.xlabel('Y')

plt.plot([0,B[0]], [0,B[1]], label = ' linear comb')
plt.plot([0,Ve1[0]], [0,Ve1[1]], label = ' scaling V1 by inv[0]')
plt.plot([0,V1[0]], [0,V1[1]], label = ' 1st col of vec A')
plt.plot([0,V2[0]], [0,V2[1]], label = ' 2nd col of vec A')
plt.plot([2,sum[0]], [-1,sum[1]], label = ' scaling A by inv[1]')

plt.legend()
plt.grid(True)

print("")
print("")
print("                Plotting the vectors")
plt.show()

