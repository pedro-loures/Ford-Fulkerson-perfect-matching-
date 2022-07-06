# AUTHORS 
# Pedro Loures Alzamora
# Description: implementation of ford fulkerson with bfs to generate perfect matchings in a bipartite grapgh
# TODO LIST
# -0 TODO implement graph structure
# -1 OK Read entry
# -2 TODO implement bfs
# -3 TODO implement ford fulkerson
# -4 TODO check perfect matching
# -5 TODO output padronization

# External imports
import numpy as np
import scipy

# Local imports
import ford_fulkerson as ff
import graph_search as gs
import utils as ut


def main():
  graph = ut.read_input()
  gs.make_bipartite(graph, 0)
  pass


if __name__ == "__main__":
    main()