#!/usr/bin/python
import networkx as nx

#
# The following lines must appear at the beginning for graph drawing to work
# Do not touch them
import matplotlib
matplotlib.use('Agg')

# The following line imports Matplotlib so that you can draw a graph
import pylab as plt

# The following is needed to take arguments from command line
import sys

def load_and_display_file():
    graph1 = nx.read_graphml('small-bitcoingraph.graphml')

    all_nodes = graph1.nodes()
    print ('Nodes: ', all_nodes)
    print ('# of nodes: ', len(all_nodes))

    all_edges = graph1.edges()
    print ('Edges: ', all_edges)
    print ('# of edges: ', len(all_edges))

    for node in all_nodes: 
        print ("Node " + node + ": degree = ",  + graph1.degree(node))

def create_new_graph ():
    g2 = nx.Graph()

    # The following line adds a node a to the graph
    g2.add_node ('a')

    # This will add an edge (a, b) with weight 0.1
    # It automatically adds node b too
    g2.add_edge('a', 'b', weight=0.1)

    # This will add an edge (b, c) with weight 1.5
    g2.add_edge('b', 'c', weight=1.5)

    # This will add an edge (a, c) with weight 1.0
    g2.add_edge('a', 'c', weight=1.0)

    # This will add an edge (c, d) with weight 2.2
    g2.add_edge('c', 'd', weight=2.2)

    # This will add an edge (e, f) with weight 10
    # It automatically adds nodes e & f too
    g2.add_edge('e', 'f', weight=10)

    # The following line prints all existing nodes in graph g2
    print ("List of nodes: " + str(g2.nodes()))
    # The following line prints all edges nodes in graph g2
    print ("List of edges: " + str(g2.edges()))
    # The following line prints every node and its degree
    for node in g2.nodes(): 
        print ("Node " + node + ": degree = " + str(g2.degree(node)))

    return g2

def draw_graph (inGraph, inPngFilename):
    # The following line draws graph inGraph
    nx.draw_networkx(inGraph)
    plt.show()

    # The following line saves graph as picture to inPngFilename1
    plt.savefig (inPngFilename)

    # The following line clears the old graph
    plt.clf()

def save_graph_to_file(inGraph, inFilename):
    nx.write_graphml(inGraph, inFilename)    

def main():
    load_and_display_file()

    g2 = create_new_graph ()
    draw_graph (g2, 'cs327-graph.png')
    save_graph_to_file(g2, 'cs327-created-graph.graphml')

if __name__ == "__main__":
    main()
