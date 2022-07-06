# External imports
import string
from typing_extensions import assert_type
import numpy as np
import scipy

# Local imports
import ford_fulkerson as ff
import graph_search as gs
import utils as ut

# graph structure
'''
  2 3   # lines, coluna
  1 1 0 # matrixQ
  0 0 1
  1 0 1
  0 1 0
  2 3 5 # cost

{
  0 : [(2, 2), (3, 3)]
  1 : [(2, 5)]
  2 : [(0, 2), (1, 5)]
  3 : [(0, 3)]
}

'''

def assert_matrix(matrixQ):
  # asssert 1 in more than one columns
  pass


# make graph structure from the matrix given before (can be optimized)
def make_graph(matrixQ, cost, lines=None, columns=None):
  np_matrixQ = np.array(matrixQ).transpose()
  graph = {}
  
  # Iterate through Edges 
  for _counter, edge in enumerate(np_matrixQ):
    _from = None
    _to = None

    # Iterate throu vertices - vertix = current_vertix, node = check if they are conected
    for vertix, _node in enumerate(edge):

      # If they are conected save their position
      if  _node == 1:
        if _from == None:
          _from = vertix
        else:
          _to = vertix
    
    # Add edges to graph
    if _from not in graph:
      graph[_from] = [(_to, cost[_counter])]
    else:
      graph[_from].append((_to, cost[_counter]))

    if _to not in graph:
      graph[_to] = [(_from, cost[_counter])]
    else:
      graph[_to].append((_from, cost[_counter]))
  
  return graph

# Implementation of Breadth First Search
def make_bipartite(graph, root, target=None):
  print(graph)

  # Prepare root edges
  edges=[(root, *node_cost) for node_cost in graph[root]]
  graph[root].append('blue')

  # Pass through all the edges
  while(len(edges)> 0):

    previous_node, current_node, _ = edges.pop(0) # current edge

    assert type(graph[current_node][-1]) != str, "node " + str(current_node) + "already explored:" + str(graph[current_node]) # catch if repeating nodes
    
    prev_color = graph[previous_node][-1]  # update color of the next next_node
    assert type(prev_color) == str, "COLOR " + str(color) + " NOT A STRING"
    if prev_color == 'red': color = 'blue'
    else: color = 'red'
    graph[current_node].append(color)

    # print(current_node, graph[current_node])

    # append the ones that hasnt been visited
    for next_node, cost  in graph[current_node][:-1]:
      if type(graph[next_node][-1]) == str:  # if already visited check if bipartite and skip (previous color == next_color)
        assert prev_color == graph[next_node][-1], "GRAPH MUST BE BIPARTITE:" + prev_color + "==" +  graph[next_node][-1]
        continue
      edges.append((current_node, next_node, cost))
      
    
  # print(graph)
  return edges
  

    

