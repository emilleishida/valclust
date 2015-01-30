# Vahid Mirjalili
# Clustering Validation and Analysis

import numpy as np
import scipy.special as sp
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


    def totalPurity(self, g, singleton=-1):
        """ Compute the total purity measure w.r.t. g partitioning
		singleton is the indicator for singletons.
	"""
	res, n = 0.0, 0
	for k in np.unique(self.y):
	   if (k != singleton):
	       res += self.clusterPurity(k, g)
	       n += 1
	return (res/n)

    def normalizedMutualInfo(self, g):
	""" Compute Normalized Mutual Information (NMI) 
		w.r.t. ground truth partitioning.
	"""
	n = self.n

	y_uniq = self.unique()

	gc = Cluster(X=None, y=g)
	g_uniq = gc.unique()

	y_csize = self.cluster_sizes()
	g_csize = gc.cluster_sizes()


	sval = 0.0
	for i in y_uniq:
	    imembers = self._get_members(i)

	    isize = y_csize[y_csize[:,0]==i,1]
	    gsub = g[imembers]

	    for j in np.unique(gsub):
		size_ij = np.sum(gsub == j)
		jsize = g_csize[g_csize[:,0]==j,1]
		#print("%d %d \t %d %d --> %d  %f" %(i, isize, j, jsize, size_ij, size_ij * n/float(isize * jsize)))
		sval += size_ij/float(n) * np.log(size_ij * n/float(isize * jsize))

	return(2.0 * sval / (self.entropy() + gc.entropy()))

    def _calContingency(self, g):
	""" Compute TP, FP, TN, and FN
		for any pair of points.
	"""
	tp_fp, tp = 0.0, 0.0
	for i,n in self.clsize[:,:]:
	    if n >=2:
		tp_fp += sp.binom(n, 2)
		imemb = self._get_members(i)
		gsub = g[imemb]
		for j in np.unique(gsub):
		    size_ij = np.sum(gsub == j)
		    if size_ij >= 2:
			tp += sp.binom(size_ij, 2)
	self.tp = tp
	self.fp = tp_p - tp

