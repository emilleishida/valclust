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

    intra_sampler()
    inter_sampler()

    """

    def __init__(self, X, y):
        self.set_data(X, y)

    def intra_sampler(self, cinx, size=None, method='euclidean', return_ind=False, outfile=None):
	"""
	Sampling intra-cluster pairwise distances.

	Arguments: 
		X (feature vectors/data)
		y (cluster memberships)
		cinx (distinct cluster index) to run sampling for a particular cluster
		size (amount of sampling), if None, all exclusive pairwise distances are computed.
		method: distance method, such as 'euclidean', 'mahalanobis', ...

	"""

	X_clust = self.X[self._get_members(cinx)]

        nsize = X_clust.shape[0]

	totpw = size
	if totpw is None:
	   totpw = nsize*(nsize-1)/2
	sys.stderr.write("##\tCluster %s  --> Size: %d\n" %(cinx, nsize))


	rand_pair_ind = np.random.randint(low=0, high=nsize, size=(totpw,2))

	if outfile is None:
	    dary = np.zeros(shape=totpw, dtype='float')
	    n = 0
	    for i,j in rand_pair_ind:
		dary[n] = cal_distance(X_clust[i], X_clust[j], method=method)
        	n += 1
	    return(dary)
	else:
	    with open(outfile, 'w') as fp:
		for i,j in rand_pair_ind:
		   dist_ij = cal_distance(X_clust[i], X_clust[j], method=method)
		   fp.write("%-d %-d %.4f\n" %(i, j, dist_ij))

	return(None)




    def inter_sampler(self, cinx, size=None, method='euclidean', return_ind=False, outfile=None):
	"""
	Sampling inter-cluster pairwise distances 
	for a particular cluster (cinx) with respect to all other clusters.


	"""
        memb_indx = self._get_members(cinx)
	rest_indx = self._get_non_members(cinx)

        nsize_memb = memb_indx.shape[0]
	nsize_rest = rest_indx.shape[0]

	totpw = size
	if totpw is None:
	    totpw = nsize_memb * nsize_rest

	sys.stderr.write("##\tCluster %s w.r.t. rest --> Size: %d x %d  Total pairs: %d\n" 
		%(cinx, nsize_memb, nsize_rest, totpw))

	rand_memb_ind = memb_indx[np.random.randint(low=0, high=nsize_memb, size=totpw)]
	rand_rest_ind = rest_indx[np.random.randint(low=0, high=nsize_rest, size=totpw)]

	
	if outfile is None:
	    # No file is given, so save the output in a numpy array
	    dary = np.zeros(shape=totpw, dtype='float')
            n = 0 
            for i,j in zip(rand_memb_ind, rand_rest_ind):
                dary[n] = self.distance(i, j) #, method=method)
                n += 1
	    return(dary)
	
	else:
	    # Save the output in the given file
	    with open(outfile, 'w') as fp:
	       for i,j in zip(rand_memb_ind, rand_rest_ind):
	          dist_ij = self.distance(i, j, method=method)
	          fp.write("%-d %-d %.4f\n" %(i, j, dist_ij))

	    return(None)
