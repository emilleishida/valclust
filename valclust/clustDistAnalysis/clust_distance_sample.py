# Vahid Mirjalili
# Clustering Validation and Analysis

import numpy as np
import pyprind
import sys
from ..cluster import Cluster

class ClusterDistanceSampler(Cluster):
    """
    Class for sampling intra and inter cluster distances

    Class Methods:



    """

    def intra_sampler(self, X, y, size=None):
       """
       Sampling intra-cluster distances.

       Arguments: 
		X (feature vectors/data)
		y (cluster memberships)
		size (amount of sampling), if None, all exclusive pairwise distances are computed.

       """
       print ("Calling sample function!")
