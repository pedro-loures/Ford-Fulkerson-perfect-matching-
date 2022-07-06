# External imports
import numpy as np
import scipy
import string

# Local imports
import ford_fulkerson as ff
import graph_search as gs
import utils as ut


# Read input and create graph
def read_input(text=''):
  # First line [0] - lines, columns
  lines, columns = [int(valor) for valor in input(text).split(' ')]
  
  # Second to Second to last [1:-1] - matrix
  matrixQ=[]
  for _ in range(lines*2):
    linha = input().split(' ')
    # print(linha)
    linha = [int(valor) for valor in linha]
    matrixQ.append(linha)

  # Last line [-1] - capacity of edges
  capacity = [int(valor) for valor in input().split(' ')]

  # Make a graph
  graph = gs.make_graph(matrixQ, capacity, lines, columns)
  return graph

  

