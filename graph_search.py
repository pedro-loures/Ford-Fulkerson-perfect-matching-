# External imports
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
  0 : [[2, 2], [3, 3]]
  1 : [[2, 5]]
  2 : [[0, -2], [1,-5]]
  3 : [[3,-0]]
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
      graph[_to] = [(_from, -cost[_counter])]
    else:
      graph[_to].append((_from, -cost[_counter]))
  
  return graph

# Implementation of Breadth First Search
def bfs(graph, root, target=None):
  edges=graph[root]
  while(len(edges)> 0):
    print(edges)
    node, _ = edges.pop(0)
    for edge, cost in graph[node]:
      if cost<0: continue
      edges.append((edge, cost))
  pass
  

    

