# Vahid Mirjalili
# Clustering Validation and Analysis

import numpy as np
import scipy.special as sp
import pyprind
import sys
from .cluster import Cluster
import editdist


class CompareCluster(Cluster):

    def __init__(self, X, y, g):
        assert (y.shape == g.shape)
        self.set_data(X, y)
	self.g = g
	self.gsize, self.gdict = self.cluster_sizes(g)

    def clusterPurity(self, cinx):
	""" Compute the purity of an individual cluster cinx 
	with respect to a given clustering solution 
	g (which could be the ground-truth partitioning).
	"""
	cmembers = self._get_members(cinx)
	memg = self.g[cmembers]
	sdict = {}
	for k in memg:
	    if k in sdict.keys():
	        sdict[k] += 1
	    else:
		sdict[k] = 1

	largest = np.max(sdict.values())
	return (largest / float(memg.shape[0]))


    def totalPurity(self):
        """ Compute the total purity measure w.r.t. g partitioning
	"""
	res, n = 0.0, 0
	wres, wsum = 0.0, 0.0
	for k in np.unique(self.y):
	    p = self.clusterPurity(k)
	    res += p
	    n += 1
	    ksize = self.ydict[k]
	    wres += p*ksize
	    wsum += ksize
	return (res/n, wres/wsum)


    def normalizedMutualInfo(self):
	""" Compute Normalized Mutual Information (NMI) 
		w.r.t. ground truth partitioning.
	"""
	n = self.n

	gc = Cluster(X=None, y=self.g)
	y_uniq = self.unique()

	sval = 0.0
	for i in y_uniq:
	    imembers = self._get_members(i)

	    isize = self.ydict[i]
	    gsub = self.g[imembers]

	    for j in np.unique(gsub):
		size_ij = np.sum(gsub == j)
		jsize = self.gdict[j]
		#print("%d %d \t %d %d --> %d  %f" %(i, isize, j, jsize, size_ij, size_ij * n/float(isize * jsize)))
		sval += size_ij/float(n) * np.log(size_ij * n/float(isize * jsize))

	return(2.0 * sval / (self.entropy() + gc.entropy()))

    def MCC(self):
	""" Compute Matthew's Correlation Coefficient:
		MCC = (TP*TN - FP*FN) / sqrt((TP+FP)*(TP+FN)*(TN+FP)*(TN+FN))
	"""
	self._contingency()
	tp,fp,tn,fn = self.tp, self.fp, self.tn, self.fn
	return ((tp*tn - fp*fn)/np.sqrt((tp+fp)*(tp+fn)*(tn+fp)*(tn+fn)))

    def _contingency(self):
	""" Compute TP, FP, TN, and FN
		for any pair of points.
	"""
	tp_fp, tp = 0.0, 0.0
	tn_fn, fn = 0.0, 0.0
	for i,v1 in enumerate(self.ysize[:,:]):
	    c1,n1 = v1
	    imemb1 = self._get_members(c1)
	    gsub1 = self.g[imemb1]
	    if n1 >=1:
		tp_fp += sp.binom(n1, 2)
		for j in np.unique(gsub1):
		    size_ij = np.sum(gsub1 == j)
		    if size_ij >= 2:
			tp += sp.binom(size_ij, 2)
		    size_j = np.sum(self.g == j)
		    fn += size_ij * (size_j - size_ij)
		    #print("%d %d %d   %d\t\t%d"%(j, size_j, size_ij, size_ij*(size_j-size_ij), fn))
	
	    if (i < self.ysize.shape[0] - 1): 
		tn_fn += n1 * np.sum(self.ysize[i+1:,1])


	self.tp = tp
	self.fp = tp_fp - tp

	fn = fn / 2
	self.tn = tn_fn - fn
	self.fn = fn

	#sys.stderr.write("TP: %.0f  FP: %.0f \t TN: %.0f  FN: %.0f\n"%(self.tp,self.fp,self.tn,self.fn))
	return (None)
