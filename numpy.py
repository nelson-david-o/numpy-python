# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import time

n = 1000

"lista en python"

l1 = list(range(n))
l2 = list(range(n))

start = time.time()
l3 = []
for x in range(len(l1)):
    l3.append(l1[x]+l2[x])
    end = time.time()
    print("total segundos lista: " , (end - start) * 1000)
    
    n1 = np.arange(n)
    n2 = np.arange(n)
    
start = time.time()
n3 = n1 + n2
end = time.time()

print("Total milSegundos Numpy: ", (end - start) * 1000)

a = [2, 3, 4, 5, 6]
b = [7, 9, 10, 11, 12]

#Convertir el vector en vector numpy

n1 = np.array(a)
n2 = np.array(b)

# operaciones numpy

n3 = n1 + n2
n3 = n1 - n2
n3 = n1 * n2
n3 = n1 / n2



n3.shape


n4 = np.array([[3, 4, 5], [5, 6, 7], [5, 6, 7]])


#Matriz de ceros
n4 = np.ones((4, 4))

# Matriz identidad

n4 = np.eye(5)

n5 = np.random.random((5,5))
print(n5)
identidad = np.eye(5)
print(identidad)
n5 = n5 * identidad
print(n5)

print(n4.max())
print(n4.min())
print(n4.mean())
print(n4.sum())
print(n4.sqrt(n4))
print(n4.sin(n4))
print(n4.cos(n4))
print(n4.log(n4))

f1 = [4, 5, 6, 7, 9]
f2 = [3, 4, 5, 6, 8]
f3 = [1, 5, 6, 9, 10]


matriz = np.array([f1, f2, f3])
trasp = matriz.T



c = [[3, 1, 9], [7, 2, 4], [8, 6, 6]]
d = [[3, 1, 9], [7, 2, 5], [8, 6, 6]]

nc = np.array(c)
nd = np.array(d)


nc == nd

nc * 2

nc ** 2

nc[nc > 5]
nc[nc < 5 and nc %2 == 0]

nc[1, :]

nc[:, 1]

nc[2, 1:2]

nc[2, 1:3]

nc[2, 1:]

























