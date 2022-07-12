# External imports
import string
from typing_extensions import assert_type
from anyio import current_effective_deadline
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
  2 3 5 # capacity

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
def make_graph(matrixQ, capacity, lines=None, columns=None):
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
      graph[_from] = [(_to, capacity[_counter], capacity[_counter])]
    else:
      graph[_from].append((_to, capacity[_counter], capacity[_counter]))

    if _to not in graph:
      graph[_to] = [(_from, capacity[_counter], capacity[_counter])]
    else:
      graph[_to].append((_from, capacity[_counter], capacity[_counter]))
  
  return graph # node:[(edge_target, edge_capacity, remaining_capacity), ..., edge]

# Implementation of Breadth First Search
def make_bipartite(graph, root, return_graph=False, ):
  
  blue=[] # subset1
  red=[]  # subset2

  # Prepare root edges
  edges=[(root, *node_capacity) for node_capacity in graph[root]]
  graph[root].append('blue')
  blue.append(root)

  # Pass through all the edges
  while(len(edges)> 0):

    previous_node, current_node, _, _ = edges.pop(0) # current edge
    
    assert type(graph[current_node][-1]) != str, "node " + str(current_node) + "already explored:" + str(graph[current_node]) # catch if repeating nodes
    prev_color = graph[previous_node][-1]  # get previous color
    assert type(prev_color) == str, "COLOR " + str(color) + " NOT A STRING"
    
    # update color of the next next_node and add to group
    if prev_color == 'red': 
      color = 'blue' 
      blue.append(current_node)
    else: 
      color = 'red'
      red.append(current_node)
    graph[current_node].append(color)

    # append the ones that hasnt been visited
    for next_node, capacity, _  in graph[current_node][:-1]:
      if type(graph[next_node][-1]) == str:  # if already visited check if bipartite and skip (previous color == next_color)
        assert prev_color == graph[next_node][-1], "GRAPH MUST BE BIPARTITE:" + prev_color + "==" +  graph[next_node][-1]
        continue
      edges.append((current_node, next_node, capacity, capacity))
  if return_graph: return graph, red, blue
  return red, blue # Equivalent to both sets
  

def bfs_flux(graph, root, target):
  graph_ = graph.copy()
  edges=[(root, *node_capacity) for node_capacity in graph[root][:-1]]
  flux = [[edge[1]] for edge in edges]
  visited = []

  print(graph_)
  print(edges)
  # print(flux)
  while len(edges) > 0:
    previous_node, current_node, _, _ = edges.pop(0)

    for next_node, total_cap, remaining_cap  in graph[current_node][:-1]:
      print(current_node, graph_[current_node])
      if remaining_cap > 0 and next_node not in visited:
        edges.append((current_node, next_node, total_cap, remaining_cap))
    
        # Add to flux
        for i, flux_i in enumerate(flux):
          if current_node in flux_i: flux[i].append(next_node)
        # Add to visited
        visited.append(next_node)
        # Check if target
        if next_node == target:
          break
        # update graph
        for index, edge in enumerate(graph_[current_node]):
          if edge[0] == next_node:
            graph_[current_node][index] = (next_node, total_cap, remaining_cap-1)

  print(flux)
  print(graph_)




  pass


