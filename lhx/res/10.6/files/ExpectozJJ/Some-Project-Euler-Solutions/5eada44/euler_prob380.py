import numpy as np 
import sympy as sp 

prod = sp.N(1)
m, n = 100, 500
for k in range(1, m):
    sub_prod = sp.N(1)
    for h in range(1, n):
        sub_prod *= 4*(math.sin((k*math.pi)/(2*m))**2) +  4*(math.sin((h*math.pi)/(2*n))**2)
    prod *= sub_prod

print(prod)