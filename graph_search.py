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



def make_graph(lines, columns, matrixQ, cost):
  np_matrixQ = np.array(matrixQ).transpose()
  print(np_matrixQ)
  graph = {}
  print(cost)
  for _counter, edge in enumerate(matrixQ):
    print(_counter)
    print(cost[_counter])
    for _node in edge:
      if _node == 1:
        pass
      
  # print(lines, columns)
  # print(matrixQ)
  # print(cost)
  pass