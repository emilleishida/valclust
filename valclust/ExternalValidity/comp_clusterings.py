# Vahid Mirjalili
# Clustering Validation and Analysis

import numpy as np
import pyprind
import sys
from ..cluster import Cluster
import editdist


class CompareCluster(Cluster):


    def __init__(self, X, y):
        self.set_data(X, y)

    def clusterPurity(self, cinx, g):
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

	largest = np.max(sdict.values())
	return (largest / float(memg.shape[0]))


    def totalPurity(self, cinx, g, singleton=-1):
        """ Compute the total purity measure w.r.t. g partitioning
		singleton is the indicator for singletons.
	"""
	
	for k in np.unique(y_arr):
	   sys.stderr.write("%d %f\n"%(k, obj.clusterPurity(k, g_arr)))
