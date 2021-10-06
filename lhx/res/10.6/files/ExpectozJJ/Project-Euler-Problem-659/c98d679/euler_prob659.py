import numpy as np 
import sympy as sp 
import time
import multiprocessing as mp
import os 
from collections import OrderedDict

# Test Code to observe pattern 
seq_ = []
for k in range(1,41):
    temp = []
    for n in range(1,10001):
        temp.append(n*n+k*k)
    seq_.append(temp)

ans = []
for i in range(len(seq_)):
    val = 2
    for j in range(len(seq_[i])-1):
        n1 = sp.factorint(seq_[i][j])
        n2 = sp.factorint(seq_[i][j+1])
        
        t = list(set(list(n1.keys())).intersection(set(list(n2.keys()))))
        
        if len(t) > 0:
            val = max(val, max(t))
    ans.append(val)

for n in range(len(ans)):
    print(n+1, ans[n])


# Solution Code
# OEIS A145689 Primitive prime factors of the sequence 4k^2 + 1 in the order that they are found.
# NOT exactly the sequence we want. 
# The sequence for this problem is actually the largest prime factor of the sequence 4k^2 + 1.
# For optimal algorithms, please see http://www.devalco.de/quadr_Sieb_4x%5E2+1.php
# Brute-Force Solution Below.

def func(k, filename):
    val = sp.primefactors(4*k*k+1)[-1]
    fh = open(filename, "a")
    fh.write(str(k)+" "+str(val)+"\n")  
    fh.close()
    print(k, val)

time1 = time.time()
no_threads = mp.cpu_count()
p = mp.Pool(processes = no_threads)
results = p.starmap(func, zip(range(1, 1000001), ["euler_prob659_1.txt"]*1000000))
p.close()
p.join()

p = mp.Pool(processes = no_threads)
results = p.starmap(func, zip(range(1000001, 2000001), ["euler_prob659_2.txt"]*1000000))
p.close()
p.join()

p = mp.Pool(processes = no_threads)
results = p.starmap(func, zip(range(2000001, 3000001), ["euler_prob659_3.txt"]*1000000))
p.close()
p.join()

p = mp.Pool(processes = no_threads)
results = p.starmap(func, zip(range(3000001, 4000001), ["euler_prob659_4.txt"]*1000000))
p.close()
p.join()

p = mp.Pool(processes = no_threads)
results = p.starmap(func, zip(range(4000001, 5000001), ["euler_prob659_5.txt"]*1000000))
p.close()
p.join()

p = mp.Pool(processes = no_threads)
results = p.starmap(func, zip(range(5000001, 6000001), ["euler_prob659_6.txt"]*1000000))
p.close()
p.join()

p = mp.Pool(processes = no_threads)
results = p.starmap(func, zip(range(6000001, 7000001), ["euler_prob659_7.txt"]*1000000))
p.close()
p.join()

p = mp.Pool(processes = no_threads)
results = p.starmap(func, zip(range(7000001, 8000001), ["euler_prob659_8.txt"]*1000000))
p.close()
p.join()

p = mp.Pool(processes = no_threads)
results = p.starmap(func, zip(range(8000001, 9000001), ["euler_prob659_9.txt"]*1000000))
p.close()
p.join()

p = mp.Pool(processes = no_threads)
results = p.starmap(func, zip(range(9000001, 10000001), ["euler_prob659_10.txt"]*1000000))
p.close()
p.join()

vec = dict()
for n in range(1, 11):
    file = open("euler_prob659_"+str(n)+".txt", 'r')
    contents = file.readlines()
    for i in range(len(contents)):
        contents[i] = contents[i].strip("\n").split(" ")
        vec[int(contents[i][0])] = int(contents[i][1])

vec = OrderedDict(sorted(vec.items()))
print(sum(list(vec.values())))
print("Time Taken: ", time.time()-time1)