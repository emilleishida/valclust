# Vahid Mirjalili
# Clustering Validation and Analysis

import numpy as np
import pyprind
import sys
from ..cluster import Cluster

class PairwiseDistanceSampler(Cluster):
    """
    Class for sampling intra and inter cluster pairwise distances

    Class Methods:



    """

    def intra_sampler(self, X, y, cinx, size=None):
	"""
	Sampling intra-cluster pairwise distances.

	Arguments: 
		X (feature vectors/data)
		y (cluster memberships)
		cinx (distinct cluster index) to run sampling for a particular cluster
		size (amount of sampling), if None, all exclusive pairwise distances are computed.

	"""
	print ("Calling sample function!")

	X_clust = X[self.get_members(y, cinx),:]
	nsize,ndim = X_clust.shape
	print("Cluster Size: %d   Numb. of Dimensions: %d" %(nsize, ndim))

