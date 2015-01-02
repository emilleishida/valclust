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

    def intra_sampler(self, X, y, cinx, size=None, return_ind=False):
	"""
	Sampling intra-cluster pairwise distances.

	Arguments: 
		X (feature vectors/data)
		y (cluster memberships)
		cinx (distinct cluster index) to run sampling for a particular cluster
		size (amount of sampling), if None, all exclusive pairwise distances are computed.

	"""

	X_clust = X[self.get_members(y, cinx),:]
	nsize,ndim = X_clust.shape
	totpw = nsize*(nsize-1)/2
	sys.stderr.write("##\tCluster %s  --> Size: %d   NumDim.: %d  Total pairs: %d\n" %(cinx, nsize, ndim, nsize*(nsize-1)/2))

	dary = np.zeros(shape=totpw, dtype='float')

	if size is None:
	    sys.stderr.write("##\tComputing all intra-cluster pairwise distances ...\n")

	    n = 0
	    for i in range(nsize):
		for j in range(i+1, nsize):
		    dary[n] = cal_distance(X_clust[i,:], X_clust[j,:], method='euclidean')
		    n += 1
	else:
	    sys.stderr.write("##\tSampling %d intra-cluster pairwise distances ...\n" %size)


	return(dary)

