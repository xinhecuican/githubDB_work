import numpy as np
import sympy as sp
import math

# Heronian Triangles: Triangles with integer side length and integer area
# Triplets a, b, c can be generated by some pythagorean triplets 
# See Wolfram: http://mathworld.wolfram.com/HeronianTriangle.html
# See Wikipedia: https://en.wikipedia.org/wiki/Integer_triangle#Isosceles_Heronian_triangles

# Trial Code to generate some Isosceles Heronian Triangles (isosceles so that we have 2 equal side lengths)
# BUT still not efficient enough as the problem only wants 3rd length to be within difference of isosceles length at most 1 
triplets = []
sum = 0
for u in range(1, 10001):
    for v in range(1, 10001):
        if sp.igcd(u,v)==1 and u>v and (u+v)%2 != 0:
            if np.sum([2*(u**2-v**2), u**2 + v**2, u**2 +v**2]) <= 10**9 and abs(2*(u**2-v**2)-u**2-v**2) <= 1:
                triplets.append((2*(u**2-v**2), u**2 + v**2, u**2 +v**2))
                sum += np.sum([2*(u**2-v**2), u**2 + v**2, u**2 +v**2])
                print((2*(u**2-v**2), u**2 + v**2, u**2 +v**2))
            if np.sum([4*u*v, u**2 + v**2, u**2 +v**2]) <= 10**9 and abs(4*u*v-u**2-v**2) <= 1:
                triplets.append((4*u*v, u**2 + v**2, u**2 +v**2))
                sum += np.sum([4*u*v, u**2 + v**2, u**2 +v**2])
                print((4*u*v, u**2 + v**2, u**2 +v**2))       

# The Stupid Special Heronian Triangle Triplet Sequences we WANT!!! 💯😜
"""
(6, 5, 5)
(16, 17, 17)
(66, 65, 65)
(240, 241, 241)
(902, 901, 901)
(3360, 3361, 3361)
(12546, 12545, 12545)
(46816, 46817, 46817)
(174726, 174725, 174725)
(652080, 652081, 652081)
(2433602, 2433601, 2433601)
"""

# In order to get these NUMBERS, it is not difficult to see that 😆 those numbers are of OEIS: A120893
# Zat OEIS sequence can be generated using the following recursion 
def a(n):
    if n == 0 or n == 1:
        return sp.N(1)
    elif n == 2:
        return sp.N(5)
    else:
        return sp.N(3*a(n-1) + 3*a(n-2) - a(n-3))

# Next, notice that our numbers starts from sequence a(2) = 5. For a(2), we plus 1 to 3rd length. Then the next set is minus 1. Alternating pattern. 
# In order to avoid precision error in Python, we use sp.N(). TADA!!!
sum = 0
check, check2 = 0, 0
for n in range(2, 101):
    l = sp.N(a(n))
    s = (3*l - 1)/2
    A = sp.N(math.sqrt(s*(s-l)**2*(s-(l-1))))
    if 2*s > 10**9:
        check = 1
    if A == round(A) and check == 0:
        sum += 2*s
        print(l, l-1, "Perimeter: ", 2*s, "Area: ", A)
    
    s = (3*l+1)/2
    A = sp.N(math.sqrt(s*(s-l)**2*(s-(l+1))))
    if 2*s > 10**9:
        check2 = 1
    if A == round(A) and check2 == 0:
        sum += 2*s
        print(l, l+1, "Perimeter: ", 2*s, "Area: ", A)
    
    if check == 1 or check2 == 1:
        break

print("Sum: ", sum)



