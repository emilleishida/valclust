# Vahid Mirjalili
# Clustering Validation and Analysis

import numpy as np
import pyprind
import sys
from ..cluster import Cluster
import editdist

def clusterPurity(Cluster, cinx, g):
    """ Compute the purity of an individual cluster cinx 
	with respect to a given clustering solution 
	g (which could be the ground-truth partitioning).
    """
    cmembers = self._get_members(cinx)
    memg = g[cmembers]
    sdict = {}
    for k in memg:
	if k in sdict.keys():
	    sdict[k] += 1
	else:
	    sdict[k] = 1

    largest = np.max(sdict.value())
    return (largest, memg.shape[0])


def totalPurity(Cluster, cinx, g):
   pass
