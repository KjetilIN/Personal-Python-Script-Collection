import networkx as nx
import matplotlib.pyplot as plt





def plotCompleteGraph(n):
    """ Plots a complete graph of n nodes"""
    G = nx.complete_graph(n)
    nx.draw_spring(G)
    plt.show()



plotCompleteGraph(20)