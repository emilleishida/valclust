# Vahid Mirjalili
# Clustering Validation and Analysis

import numpy as np
import pyprind
import sys
from ..cluster import Cluster
import editdist

def cal_distance(x1, x2, method='euclidean'):
    if method == 'euclidean':
        diff = x1 - x2
        sq_diff = diff * diff
        return(np.sqrt(np.sum(sq_diff)))
    elif method == 'editdist':
	return(editdist.distance(x1, x2))


class PairwiseDistanceSampler(Cluster):
    """
    Class for sampling intra and inter cluster pairwise distances

    Class Methods:



    """

    def intra_sampler(self, X, y, cinx, size=None, method='euclidean', return_ind=False):
	"""
	Sampling intra-cluster pairwise distances.

	Arguments: 
		X (feature vectors/data)
		y (cluster memberships)
		cinx (distinct cluster index) to run sampling for a particular cluster
		size (amount of sampling), if None, all exclusive pairwise distances are computed.

	"""

	X_clust = X[self._get_members(y, cinx)]

        nsize = X_clust.shape[0]

	totpw = nsize*(nsize-1)/2
	sys.stderr.write("##\tCluster %s  --> Size: %d  Total pairs: %d\n" %(cinx, nsize, nsize*(nsize-1)/2))

	dary = np.zeros(shape=totpw, dtype='float')

	if size is None:
	    sys.stderr.write("##\tComputing all intra-cluster pairwise distances ...\n")

	    n = 0
	    for i in range(nsize):
		for j in range(i+1, nsize):
		    dary[n] = cal_distance(X_clust[i], X_clust[j], method=method)
		    n += 1
	else:
	    sys.stderr.write("##\tSampling %d intra-cluster pairwise distances ...\n" %size)

	return(dary)




    def inter_sampler(self, X, y, cinx, size=None, method='euclidean', return_ind=False):
	"""
	Sampling inter-cluster pairwise distances 
	for a particular cluster (cinx) with respect to all other clusters.


	"""
        memb_indx = self._get_members(y, cinx)
	rest_indx = self._get_non_members(y, cinx)

        nsize_memb = memb_indx.shape[0]
	nsize_rest = memb_indx.shape[0]

	totpw = size
	if totpw is None:
	    totpw = nsize_memb * nsize_rest

	sys.stderr.write("##\tCluster %s w.r.t. rest --> Size: %d x Size: %dTotal pairs: %d\n" 
		%(cinx, nsize_memb, nsize_rest, totpw)

	rand_memb_ind = np.random.randint(low=0, high=nsize_memb, size=size)
	rand_rest_ind = np.random.randint(low=0, high=nsize_memb, size=size)
	
	
