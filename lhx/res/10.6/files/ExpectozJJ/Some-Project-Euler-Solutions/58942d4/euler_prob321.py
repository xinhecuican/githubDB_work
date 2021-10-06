from sympy.solvers import solve
from sympy import symbols

# Sequence in Swapping Counters = n*n + 2*n 
# 40 Indices x where Triangular Numbers x*(x+1)/2 = n*n + 2*n: 2, 5, 15,32,90,189,527,1104,3074,6437,17919,37520, 104442,218685,608735,1274592,3547970,
# 7428869,20679087,43298624,120526554,252362877,702480239,1470878640,4094354882,8572908965,23863649055,49966575152,139087539450,291226541949,810661587647,
# 1697392676544,4724881986434,9893129517317,27538630330959,57661384427360,160506899999322,336075177046845,935502769664975,1958789677853712 
# OEIS A006451

def a(n): 
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 5
    elif n == 3:
        return 15
    else:
        return 6*a(n-2) - a(n-4) +2  # Recurrence Relation to generate A006451

vec = []
for n in range(1, 41):
    vec.append(a(n)) 

x = symbols("x", positive=True)
sum = 0
for v in vec:
    temp = v*(v+1)
    solns = solve(2*x*x + 4*x - temp, x) # n*n + 2*n - temp = 0  where temp = v*(v+1)/2 
    # Use sympy to solve for values of n
    sum += solns[0]

print(sum)