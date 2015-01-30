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

    def MCC(self, g):
	""" Compute Matthew's Correlation Coefficient:
		MCC = (TP*TN - FP*FN) / sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
	"""
	self.contingency(g)
	tp,fp,tn,fn = self.tp, self.fp, self.tn, self.fn
	return ((tp*tn - fp*fn)/sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)))

    def _contingency(self, g):
	""" Compute TP, FP, TN, and FN
		for any pair of points.
	"""
	tp_fp, tp = 0.0, 0.0
	tn_fn, fn = 0.0, 0.0
	for i,v1 in enumerate(self.clsize[:,:]):
	    c1,n1 = v1
	    imemb1 = self._get_members(c1)
	    gsub1 = g[imemb1]
	    if n1 >=2:
		tp_fp += sp.binom(n1, 2)
		for j in np.unique(gsub1):
		    size_ij = np.sum(gsub1 == j)
		    if size_ij >= 2:
			tp += sp.binom(size_ij, 2)
	    
	    for v2 in self.clsize[i+1:,:]:
		c2,n2 = v2
		tn_fn += n1 * n2
		imemb2 = self._get_members(c2)
		gsub2 = g[imemb2]
		for j1 in np.unique(gsub1):
		    for j2 in np.unique(gsub2):
			if j1 == j2:
			    c1g1 = np.sum(gsub1 == j1)
			    c2g2 = np.sum(gsub2 == j2)
			    fn += c1g1*c2g2


	self.tp = tp
	self.fp = tp_fp - tp

	self.tn = tn_fn - fn
	self.fn = fn

	return (None)
