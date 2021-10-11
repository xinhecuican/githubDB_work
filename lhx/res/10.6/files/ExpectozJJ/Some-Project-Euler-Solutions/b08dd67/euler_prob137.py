import numpy as np
import sympy as sp
import math
from sympy import symbols

x = symbols("x", positive = True)

# Fibonacci Golden Nuggets -> Indexes A_F(x) whereby A_F(x) = integer and x = p/q rational number.
#
# Mathematical Solution: A_F(x) = Generating Function of Fibonacci polynomials = x / (1-x-x*x) 
# We want A_F(x) = x / (1-x-x*x) = k for some integer k 
# We solve the equation: x = k - k*x - k*x**2 
# Trial Code to solve the equation
cnt = 0
for k in range(1, 10**6):
    solns = sp.solve(k*x**2 + (k+1)*x - k)
    if solns[0].is_rational:
        print(k, solns[0])

# OEIS: A081018 
# 2, 15, 104, 714, 4895, 33552, 229970, 1576239, 10803704, 74049690, 507544127, 3478759200, 23843770274, 
# 163427632719, 1120149658760, 7677619978602, 52623190191455, 360684711361584, 2472169789339634, 16944503814015855, 116139356908771352, 796030994547383610
# Formula to get this sequence: (Lucas Numbers of (4*n+1) - 1)/5 or Fibonacci(2*n)*Fibonacci(2*n+1)
# Solution Code to get the answer
for n in range(1, 20):
    print(n, (sp.lucas(4*n+1)-1)/5)


