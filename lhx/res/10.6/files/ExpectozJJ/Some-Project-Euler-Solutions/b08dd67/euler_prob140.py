import numpy as np
import sympy as sp
import math
from sympy import symbols

x = symbols("x", positive = True)

# Following Problem 137, we should be able to get the following equation to get some patterns 
# Trial Code
cnt = 0
for k in range(1, 1000):
    solns = sp.solve(k*x**2 + (k-2)*x + 3 - k) # OEIS A104449
    if len(solns) > 0:
        if solns[0].is_rational:
            print(k-3, solns[0])

# For a detailed mathematical explanation of this solution, please see the supplementary pdf document. 
# Note that one can solve PE137 by simply checking OEIS but this is not the case for PE140.
# The objective of PE140 is to let solver understand how to fully derive any formula to get any sequence of any FIBONACCI GOLDEN NUGGETS you DESIRE!!!
# SOLUTION: 😁
def a(n):
    return (sp.fibonacci(n+1)+sp.lucas(n))/(sp.fibonacci(n+2)+sp.lucas(n+1))

cnt = 0
sum = 0
n = 1
while cnt < 30:
    cnt += 1
    print(cnt, (3-2*a(2*n-1))/(1-a(2*n-1)-(a(2*n-1)*a(2*n-1)))-3)
    cnt += 1
    print(cnt, 3*sp.fibonacci(2*n+1)**2-2*sp.fibonacci(2*n)*sp.fibonacci(2*n+1)-3)
    sum += (3-2*a(2*n-1))/(1-a(2*n-1)-(a(2*n-1)*a(2*n-1)))-3 + 3*sp.fibonacci(2*n+1)**2-2*sp.fibonacci(2*n)*sp.fibonacci(2*n+1)-3
    n += 1

print("Ans: ", sum)

"""
1 2
2 5
3 21
4 42
5 152
6 296
7 1050
8 2037
9 7205
10 13970
11 49392
12 95760
13 338546
14 656357
15 2320437
16 4498746
17 15904520
18 30834872
19 109011210
20 211345365
21 747173957
22 1448582690
23 5121206496
24 9928733472
25 35101271522
26 68052551621
27 240587694165
28 466439127882
29 1649012587640
30 3197021343560
"""