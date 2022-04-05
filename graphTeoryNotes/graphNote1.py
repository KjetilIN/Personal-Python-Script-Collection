import networkx as nx
import matplotlib.pyplot as plt





def plotCompleteGraph(n):
    """ Plots a complete graph of n nodes"""
    G = nx.complete_graph(n)
    nx.draw_spring(G)
    plt.show()


def drawRandom():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=4)
    G.add_edge('B', 'D', weight=2)
    G.add_edge('A', 'C', weight=3)
    G.add_edge('C', 'D', weight=4)

    nx.draw_networkx(G)
    print(nx.shortest_path(G, 'A', 'D', weight='weight'))
    plt.show()


drawRandom()