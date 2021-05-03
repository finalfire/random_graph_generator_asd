import networkx as nx
import random
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit(1)
    
    n = int(sys.argv[1])
    p = random.randint(15, 95) / 100.0
    g = nx.fast_gnp_random_graph(n, p)
    
    print(n)
    for u,v in g.edges():
        print(u, v)