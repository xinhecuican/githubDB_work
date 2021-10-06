import sympy
import numpy as np 

# Only finds the next digital root of n E.g. 137 -> returns 11 and not 2 
def digitalroot(n):
    s = str(n)
    if len(s)!=1:
        x = 0
        for i in range(len(s)):
            x+=int(s[i]) 
        s = str(x)
    return int(s)

def max_clock(n):
    s = str(n)
    transitions = np.sum(np.array(num_dict[s]))
    while len(s)>1:
        old_n = n
        n = digitalroot(n)
        s = str(n)

        # Surprisingly, this 2 lines works flawlessly for JJ. :P
        transitions += np.sum((np.array(num_dict[s])<np.array(num_dict[str(old_n)]))) # Number of lights to add to form the next number
        transitions += np.sum((np.array(num_dict[str(old_n)])<np.array(num_dict[s]))) # Number of lights to remove for the next number

    #transitions += np.sum((np.array(num_dict[s])<np.array(num_dict['OFF'])))
    transitions += np.sum((np.array(num_dict['OFF'])<np.array(num_dict[s]))) # Number of lights to OFF lights
    return transitions

def sam_clock(n):
    s = str(n)
    transitions = np.sum(np.array(num_dict[s]))*2 
    while len(s)>1:
        n = digitalroot(n)
        s = str(n)
        transitions += np.sum(np.array(num_dict[s]))*2
    return transitions

clock_dict = {'OFF':[0,0,0,0,0,0,0],'0':[1,1,1,0,1,1,1], '1':[0,0,1,0,0,1,0], '2':[0,1,1,1,1,0,1], '3':[0,1,1,1,0,1,1], '4':[1,0,1,1,0,1,0], '5':[1,1,0,1,0,1,1], '6':[1,1,0,1,1,1,1], '7':[1,1,1,0,0,1,0], '8':[1,1,1,1,1,1,1], '9':[1,1,1,1,0,1,1]}
# clock dictionary -> digits 0 to 9 where each digit -> [0,0,0,0,0,0,0] -> each light location on clock 
# Light Locations in array in this order: Vertical Upp Left, Horizontal Top, Vertical Upp Right, Horizontal Middle, Vertical Lower Left, Vertical Lower Right and Horizontal Bottom

# prepare number dictionary for primes required and the numbers 1 to 1000 
# Note that the largest prime for this qn -> 19999999 -> which digitalroot becomes 64 <<<< 1000
num_dict = dict({'OFF':[clock_dict['OFF'],clock_dict['OFF'],clock_dict['OFF'],clock_dict['OFF'],clock_dict['OFF'],clock_dict['OFF'],clock_dict['OFF'],clock_dict['OFF']]})
primes = list(sympy.sieve.primerange(10**7+1, 2*10**7))

for n in primes:
    s = str(n)
    nvec = []
    if len(s) < 8:
        for i in range(8-len(s)):
            nvec.append(clock_dict['OFF']) # Add off-ed lights for numbers that are less than 8 digits
    for i in range(len(s)):
        nvec.append(clock_dict[s[i]])
    num_dict[s] = nvec

for n in np.arange(1,1000):
    s = str(n)
    nvec = []
    if len(s) < 8:
        for i in range(8-len(s)):
            nvec.append(clock_dict['OFF']) # Add off-ed lights for numbers that are less than 8 digits
    for i in range(len(s)):
        nvec.append(clock_dict[s[i]])
    num_dict[s] = nvec

max_sum = 0
sam_sum = 0
for p in primes:
    s_t = sam_clock(p)
    m_t = max_clock(p)
    max_sum += m_t
    sam_sum += s_t
    print("Prime: ", p, "Max Clock: ", m_t, "Sam Clock: ", s_t)

print("Max's Clock Transitions: ", max_sum)
print("Sam's Clock Transitions: ", sam_sum)
print("Difference in Transitions: ", sam_sum - max_sum)