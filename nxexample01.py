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


def lookUpCountrtryOne (inIP):
    GEOIP = pygeoip.GeoIP("GeoIP.dat", pygeoip.MEMORY_CACHE)
    country = GEOIP.country_name_by_addr(inIP)
    return country

def load_and_display_file():
    graph1 = nx.read_graphml('127.0.1.1_l14340.cs.jmu.edu_2018-03-18-06-45-12-700579-bitcoingraph-cleaned.graphml')
    #graph1 = nx.read_graphml('small-bitcoingraph.graphml')
    draw_graph (graph1, 'cs327-graph.png')
    save_graph_to_file(graph1, 'cs327-created-graph.graphml')


    print("1. How many Bitcoin nodes does the Bitcoin network in the data file have?")
    all_nodes = graph1.nodes() #Question 1
    print ('    # of nodes: ', len(all_nodes))
    print("\n")

    print("2. How many edges does the Bitcoin network in the data file have?")
    all_edges = graph1.edges() #Question 2
    print ('    # of edges: ', len(all_edges))
    print("\n")

    max_set = []
    min_set = []
    first = True

    top10 = []
    countries = {}
    count = 0
    for node in all_nodes:

        if first:
            min = graph1.degree(node)
            max = graph1.degree(node)
            first = False
        
        if len(top10) < 10: #Question 5
            top10.append(node)
            top10.sort(key = lambda node: graph1.degree(node), reverse = False)
        
        elif graph1.degree(node) > graph1.degree(top10[0]): #Question 5
            top10[0] = node
            top10.sort(key = lambda node: graph1.degree(node), reverse = False)

        cur_country = lookUpCountrtryOne(node) #Question 6r

        cur_country = cur_country.strip()



        if countries.get(cur_country) is None and not len(cur_country) == 0:
            count+=1
            countries[cur_country] = []
            countries.get(cur_country).append(node)
        
        elif len(cur_country) != 0:
            countries.get(cur_country).append(node)

        if graph1.degree(node) > max: #Question 3
            max = graph1.degree(node)
            max_set.clear()

        if graph1.degree(node) == max: #Question 3
            max_set.append(node)

        if graph1.degree(node) < min: #Question 4
            min = graph1.degree(node)
            min_set.clear()

        if graph1.degree(node) == min: #Question 4
            min_set.append(node)

    top10.sort(key = lambda node: graph1.degree(node), reverse = True)

    print("3. What is the largest node degree? Which nodes have this degree?")
    print("    ", max)
    for x in range(len(max_set)):
        print ("    ", max_set[x])
    print("\n")

    print("4. What is the smallest node degree? Which nodes have this degree?")
    print("    ", min)
    print("    ", end="")
    for x in range(len(min_set)):
        print (min_set[x] + " , ", end = "")
    print("\n")
    

    # print("----------------------------------------")
    print("5. Find out the 10 nodes that have the highest degrees. Print out, in the descending order of degrees,\n (IP address, Degree, Country)")
    for x in top10:
        print("    ", x , ", ", end="")
        print(graph1.degree(x), ", ", end="")
        print(lookUpCountrtryOne(x))
    print("\n")
    # print("----------------------------------------")
    print("6. Find the five countries that have the highest number of Bitcoin nodes. Print out, in the descending order of node numbers,\n (Country: # of nodes in country)")
    top5 = []
    for country in countries:
        if len(top5) < 5:
            top5.append(country)
            top5.sort(key = lambda currentCurrentCount: len(countries.get(currentCurrentCount)), reverse=False)
        elif len(countries.get(country)) > len(top5[0]):
            top5[0] = country
    top5.sort(key = lambda currentCurrentCount: len(countries.get(currentCurrentCount)), reverse=True)  
    for x in top5:
        if x is None:
            print("N/A")
        else:
            print("    ", x, ": ", end="")
        
        print(len(countries.get(x)))

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

if __name__ == "__main__":
    main()
