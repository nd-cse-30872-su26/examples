#!/usr/bin/env python3

import collections
import sys

# Type Aliases

Graph = dict[int, dict[int, int]]
Edge  = tuple[int, int]

# Read Graph

def read_graph() -> Graph:
    graph: Graph = collections.defaultdict(dict)

    for edge, line in enumerate(sys.stdin):
        s, t = map(int, line.split())
        graph[s][t] = edge
        graph[t][s] = edge

    return graph

# Find Circuit

def find_circuit(graph: Graph, edge: Edge, visited: set[int], path: list[Edge]) -> list[Edge]:
    ''' Recursive DFS traversal '''
    pass

# Find Eulerian Circuit

def find_euler_circuit(graph: Graph) -> list[Edge]:
    ''' Iteratively compute subcircuit until all edges have been travsrsed or
    no circuit is possible '''
    visited: set[int]   = set()                 # Visited edges (set of edge ordinals)
    circuit: list[Edge] = []                    # Eulerian circuit (list of edges)
    origin : int        = list(graph.keys())[0] # Starting vertex
    start  : Edge       = (origin, list(graph[origin].items())[0][0]) # Starting edge
    index  : int        = 0                     # Where in circuit to insert subcircuit

    while start:
        # Find subcircuit and insert it after current component
        path    = find_circuit(graph, start, visited, [])
        circuit = circuit[0:index] + path + circuit[index:]

        # Check if any nodes in current circuit have an unused edge, if so, set
        # start so we search for subcircuit beginning at that vertex
        start = None
        for index, vertex in enumerate(source for source, target in circuit):
            for neighbor, edge in graph[vertex].items():
                if edge not in visited:
                    start = (vertex, neighbor)
                    break

    return circuit

# Main Execution

def main() -> None:
    graph   = read_graph()
    circuit = find_euler_circuit(graph)

    for source, target in circuit:
        print(source, target)

if __name__ == '__main__':
    main()
