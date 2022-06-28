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
  lines, columns = [int(valor) for valor in input(text).split(' ')]
  matrixQ=[]
  for _ in range(lines*2):
    linha = input().split(' ')
    matrixQ.append(linha)
  cost = input().split(' ')
  gs.make_graph(lines, columns, matrixQ, cost)
  return

