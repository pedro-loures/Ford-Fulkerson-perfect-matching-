# External imports
import numpy as np
import scipy

# Local imports
import ford_fulkerson as ff
import graph_search as gs
import utils as ut


def _ford_fulkerson(graph, begining, end):
  pass

def perfect_matching(graph, red_set, blue_set):

  # create root vertix conectiong to red_set
  graph['root'] = [(node, 1, 1) for node in red_set]
  graph['root'].append('root')
  # create target vertix conecting to blue_set
  graph['target'] = [(node, 1, 1) for node in blue_set]
  graph['target'].append('target')
  # implement _ford_fulkerson()
  path = gs.bfs_flux(graph, 'root', 'target')
  pass  
