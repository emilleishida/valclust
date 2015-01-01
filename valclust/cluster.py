import numpy as np

class Cluster(object):
    """
    Class to find distinct clusters.

    Class Metods:

	n_distnict()

    """

    def __init__(self):
        self.ary = None

    def n_distinct(self, y):
        return(np.unique(y).shape[0])

    def cluster_sizes():
	tup = np.unique(y, return_counts = T)
	return(np.asarray(tup).T)

    def members(self, y, cinx):
	"""
	Return a numpy array for the indecies of all 
	members for a specific cluster indexed by cinx.
	
	"""
	
        
