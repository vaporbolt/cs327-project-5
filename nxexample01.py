#!/usr/bin/python
import networkx as nx
import pygeoip

#
# The following lines must appear at the beginning for graph drawing to work
# Do not touch them
import matplotlib
matplotlib.use('Agg')

# The following line imports Matplotlib so that you can draw a graph
import pylab as plt

# The following is needed to take arguments from command line
import sys

def getDegree(node, graph1):
    return graph1.degree(node)


def lookUpCountrtryOne (inIP):
    GEOIP = pygeoip.GeoIP("GeoIP.dat", pygeoip.MEMORY_CACHE)
    country = GEOIP.country_name_by_addr(inIP)
    return country

def load_and_display_file():
    # graph1 = nx.read_graphml('127.0.1.1_l14340.cs.jmu.edu_2018-03-18-06-45-12-700579-bitcoingraph-cleaned.graphml')
    graph1 = nx.read_graphml('small-bitcoingraph.graphml')
    all_nodes = graph1.nodes()
    #print ('Nodes: ', all_nodes)
    print ('# of nodes: ', len(all_nodes))

    all_edges = graph1.edges()
    #print ('Edges: ', all_edges)
    print ('# of edges: ', len(all_edges))

    
    # min = None
    # max = None
    max_set = []
    min_set = []
    first = True

   

    sorted_dict = sorted(graph1.keys(), key = getDegree, reverse = True)

    for x in sorted_dict:
        print(x)


    # for node in all_nodes: 
    #     if first:
    #         min = graph1.degree(node)
    #         max = graph1.degree(node)
    #         first = False
        

    #     if graph1.degree(node) > max:
    #         max = graph1.degree(node)
    #         max_set.clear()

    #     if graph1.degree(node) == max:
    #         max_set.append(node)

    #     if graph1.degree(node) < min:
    #         max = graph1.degree(node)
    #         max_set.clear()

    #     if graph1.degree(node) == min:
    #         min_set.append(node)

    #     print ("Node PRINTER: " + node + ": degree = ",  + graph1.degree(node))


    # print("Min degree is : \n", min)
    # # printing the list using loop
    # print("Nodes with this degree include :\n")
    # for x in range(len(min_set)):
    #     print (min_set[x] + " : " + lookUpCountrtryOne(min_set[x]))
    # print("Max degree is : \n", max)
    # print("Nodes with this degree include :\n")
    # for x in range(len(max_set)):
    #     print (max_set[x])
    




        

# def create_new_graph ():
#     g2 = nx.Graph()

#     # The following line adds a node a to the graph
#     g2.add_node ('a')

#     # This will add an edge (a, b) with weight 0.1
#     # It automatically adds node b too
#     g2.add_edge('a', 'b', weight=0.1)

#     # This will add an edge (b, c) with weight 1.5
#     g2.add_edge('b', 'c', weight=1.5)

#     # This will add an edge (a, c) with weight 1.0
#     g2.add_edge('a', 'c', weight=1.0)

#     # This will add an edge (c, d) with weight 2.2
#     g2.add_edge('c', 'd', weight=2.2)

#     # This will add an edge (e, f) with weight 10
#     # It automatically adds nodes e & f too
#     g2.add_edge('e', 'f', weight=10)

#     # The following line prints all existing nodes in graph g2
#     print ("List of nodes: " + str(g2.nodes()))
#     # The following line prints all edges nodes in graph g2
#     print ("List of edges: " + str(g2.edges()))
#     # The following line prints every node and its degree
#     for node in g2.nodes(): 
#         print ("Node " + node + ": degree = " + str(g2.degree(node)))

#     return g2

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

    #g2 = create_new_graph ()
    # draw_graph (g2, 'cs327-graph.png')
    # save_graph_to_file(g2, 'cs327-created-graph.graphml')

if __name__ == "__main__":
    main()
