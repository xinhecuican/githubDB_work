import sympy
import numpy as np
import math

def SmoothTotients(num, index, sum_):
    
    # Finds the sum of all the numbers <= 10**12 where totients are 5-smooth

    for a in range(exps[index]):
        if num > 10**12:
            return sum_%(2**32)
        else:
            if index == len(primes)-1:
                if num*primes[index] <= 10**12:
                    sum_ += (num*primes[index])%(2**32)
                    return sum_
            else:
                if num*primes[index] <= 10**12 and a+1 < exps[index]:
                    sum_ += (num*primes[index])%(2**32)
                    
                sum_ = SmoothTotients(num, index+1 , sum_)
                num *= primes[index]

    print(num, index, sum_)
    return sum_%(2**32)

# Generate all the 5-smooth numbers <= 10**12
vec = []
for a in range(math.ceil(math.log10(10**12)/math.log10(2))):
    for b in range(math.ceil(math.log10(10**12)/math.log10(3))):
        for c in range(math.ceil(math.log10(10**12)/math.log10(5))):
            n = 2**a * 3**b * 5**c
            vec.append(n)

primes = []
for v in vec:
    if sympy.isprime(v+1): # p-1=v is 5- smooth so v+1 are all the primes   
        primes.append(v+1)

primes = list(np.sort(primes))
primes = list(np.array(primes)[np.array(primes)<10**12]) # List of 5-smooth prime numbers :P

exps = []
for p in primes:
    if p == 2 or p == 3 or p == 5:
        exps.append(math.ceil(math.log10(10**12)/math.log10(p)))
    else:
        exps.append(2) # Every 5-smooth prime number >= 7 has at most multiplicity 1 

print(SmoothTotients(1,0,0))

