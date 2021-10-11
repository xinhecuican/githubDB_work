import networkx as nx 
import sympy
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

def sub_hex_ring(coord, n):
    cc = hex2cubic(coord)
    #print(cc)
    nbr = [[coord]]
    for i in range(1, n+1):
        if i == 1:
            start = [cc[0], cc[1]+i, cc[2]-i]
            end = [cc[0], cc[1]+i, cc[2]-i]
            temp = [cubic2hex(start)]
            for j in range(i):
                start[2] += 1
                start[0] -= 1
                #print(start)
                temp.append(cubic2hex(tuple(start)))
            for j in range(i):
                end[1] -= 1
                end[0] += 1
                #print(start)
                temp.append(cubic2hex(tuple(end)))
            nbr.append(temp)
        elif i >= 2:
            start = [cc[0], cc[1]+i, cc[2]-i]
            end = [cc[0], cc[1]+i, cc[2]-i]
            temp = [cubic2hex(start)]
            for j in range(2):
                start[2] += 1
                start[0] -= 1
                #print(start)
                temp.append(cubic2hex(tuple(start)))
            for j in range(2):
                end[1] -= 1
                end[0] += 1
                #print(start)
                temp.append(cubic2hex(tuple(end)))
            nbr.append(temp)
        
    return nbr

def hex_ring(coord, n):
    cc = hex2cubic(coord)
    #print(cc)
    nbr = []
    for i in range(1, n+1):
        start = [cc[0], cc[1]+i, cc[2]-i]
        #print(start)
        temp = [cubic2hex(start)]
        for j in range(i):
            start[2] += 1
            start[0] -= 1
            #print(start)
            temp.append(cubic2hex(tuple(start)))
        for j in range(i):
            start[1] -= 1
            start[2] += 1
            #print(start)
            temp.append(cubic2hex(tuple(start)))
        for j in range(i):
            start[0] += 1
            start[1] -= 1
            #print(start)
            temp.append(cubic2hex(tuple(start)))
        for j in range(i):
            start[2] -= 1
            start[0] += 1
            #print(start)
            temp.append(cubic2hex(tuple(start)))
        for j in range(i):
            start[1] += 1
            start[2] -= 1
            #print(start)
            temp.append(cubic2hex(tuple(start)))
        for j in range(i):
            start[1] += 1
            start[0] -= 1
            #print(start)
            temp.append(cubic2hex(tuple(start)))
        nbr.append(temp[:-1])
        
    return nbr

def hex2cubic(coord):
    return (coord[0], coord[1], -coord[0]-coord[1])

def cubic2hex(coord):
    return (coord[0], coord[1])

def PD(coord):
    nbr = hex_ring(coord, 1)
    root = hex_seq[coord]
    vec = []
    for n in nbr[0]:
        vec.append(abs(hex_seq[n]-root))
    return sum([sympy.isprime(v) for v in vec])

# Trying to HUNT DOWN THE PRIMES!!! 
hex_seq = {(0,0): 1}
H = hex_ring((0,0), 50)
start = hex_seq[(0,0)]
for layer in H:
    for coord in layer:
        hex_seq[coord] = start + 1 
        start += 1

results = []
for k in hex_seq.keys():
    try:
        val = PD(k)
        if val == 3:
            results.append(k)
    except:
        continue

G = nx.Graph(directed=False)
G.add_node((0,0))

vec = G.nodes()
for n in range(50):
    for (q,r) in list(vec): 
        G.add_edge((q,r),(q,r-1))
        G.add_edge((q,r),(q-1,r))
        G.add_edge((q,r),(q-1,r+1))
        G.add_edge((q,r),(q,r+1))
        G.add_edge((q,r),(q+1,r-1))
        G.add_edge((q,r),(q+1,r))

color = []
for v in G.nodes():
    if v in results:
        color.append('blue')
    else:
        color.append('red')

plt.figure(figsize=(20,20))
pos = graphviz_layout(G, prog="neato")
nx.draw(G, pos, alpha=.75, node_color=color, edge_color="black", node_size=200)
ax = plt.gca() # to get the current axis
ax.collections[0].set_edgecolor("black") 
plt.axis('equal')
plt.savefig("hex.pdf", dpi=200)
plt.show()


# The Actual Solution
hex_seq = {(0,0): 1}
H = sub_hex_ring((0,0), 100000)
start = hex_seq[(0,0)]
for i in range(1, len(H)):
    if i == 1:
        hex_seq[H[i][0]] = 2
        for j in range(1, i+1):
            hex_seq[H[i][j]] = hex_seq[H[i][j-1]] + 1

        end = hex_seq[H[i][0]] + 6*i
        for j in range(-i, 0):
            hex_seq[H[i][j]] = end - 1
            end -= 1
    else:
        hex_seq[H[i][0]] = hex_seq[H[i-1][0]] + 6*(i-1)
        for j in range(1, 3):
            hex_seq[H[i][j]] = hex_seq[H[i][j-1]] + 1

        end = hex_seq[H[i][0]] + 6*i
        for j in range(-2, 0):
            hex_seq[H[i][j]] = end - 1
            end -= 1

results = []
for k in hex_seq.keys():
    if k[0] == 0 or k[0] == 1:
        try:
            val = PD(k)
            if val == 3:
                results.append(k)
        except:
            continue

print("Ans: ", hex_seq[results[1998]])