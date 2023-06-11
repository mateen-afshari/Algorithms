import networkx as nx
from networkx.algorithms import bipartite
class TilingDino:
    def __init__(self):
        return

    def compute(self, lines):
        G = nx.Graph()
        white = []
        black = []
        edges = []
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                if lines[y][x] == "#":
                    if (x + y) % 2 == 0:
                       black.append(str(x) + " " + str(y))
                    else:
                        white.append(str(x) + " " + str(y))
 
        G.add_nodes_from(black, bipartite=0)
        G.add_nodes_from(white, bipartite=1)
        for v in white:
            for w in black:
                x1 = v.split()[0]
                y1 = v.split()[1]
                x2 = w.split()[0]
                y2 = w.split()[1]
                if int(x1) == int(x2) and int(y1) == int(y2) - 1:
                    edges.append((str(v),str(w)))
                if int(x1) == int(x2) and int(y1) == int(y2) + 1:
                    edges.append((str(v),str(w)))
                if int(x1) == int(x2) - 1 and int(y1) == int(y2):
                    edges.append((str(v),str(w)))
                if int(x1) == int(x2) + 1 and int(y1) == int(y2):
                    edges.append((str(v),str(w)))
        G.add_edges_from(edges)

        flow_dict = nx.max_weight_matching(G)
        flow_value = 0.0
        for key in flow_dict:
            flow_value += 1.0
        if flow_value != (len(white) + len(black))/2:
            return ["impossible"]
        dominos = []
        for v in flow_dict:
           dominos.append(v[0] + " " + v[1])




        return dominos
