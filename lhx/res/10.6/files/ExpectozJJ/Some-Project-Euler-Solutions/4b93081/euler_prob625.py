import math
import sympy
import time
from functools import lru_cache

def F(n):
    return ((n%998244353)*((n%998244353+1)%998244353))//2

@lru_cache(maxsize=None) # Apply Memoization on H(n)
def H(n):
    h1, h2 = 0, 0
    for m in range(2, math.floor(math.sqrt(n))+1):
        h1 += (H(math.floor(n/m)))%998244353
    
    for d in range(1, math.floor(math.sqrt(n))+1):
        if d != math.floor(n/d):
            h2 += ((math.floor(n/d)-math.floor(n/(d+1)))*H(d))%998244353

    return (F(n)-h1-h2)%998244353

def G(N):
    s1, s2 = 0, 0
    for d in range(1, math.floor(math.sqrt(N))+1):
        s1 += (d*H(math.floor(N/d)))%998244353
        #print(d, s1)
    
    print("1st Sum Completed...")
    
    for c in range(1, math.floor(math.sqrt(N))+1):
        s2 += (sympy.totient(c)*F(math.floor(N/c)))%998244353
        #print(c, s2)
        
    print("2nd Sum Completed...")
        
    s3 = (F(math.floor(math.sqrt(N)))*H(math.floor(math.sqrt(N))))%998244353
    return (s1+s2-s3)%998244353

start = time.time()
print("G(10**11): ", G(10**11))
print("Elapsed Time: ", time.time()-start)