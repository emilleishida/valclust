import numpy as np

class Cluster(object):
    """
    Class to find distinct clusters.

    Class Metods:

	n_distnict(self, y): the number of distinct clusters
	cluster_sizes(self, y): the sizes of each cluster in a numpy ndarray
	get_members(self, y, cinx): the indeces of members of a particular cluster cinx

    """

    def __init__(self):
        self.ary = None

    def n_distinct(self, y):
	"""
	Returns  the number of distinct clusters.
	"""
        return(np.unique(y).shape[0])

    def cluster_sizes(self, y):
	"""
	Returns the sizes of each cluster in a numpy ndarray.
	"""
	tup = np.unique(y, return_counts = T)
	return(np.asarray(tup).T)

    def get_members(self, y, cinx):
	"""
	Returns a numpy array for the indecies of all 
	members for a specific cluster indexed by cinx.
	
	"""
	allindx = np.arange(0, y.shape[0])
	return (allindx[y == cinx])
        
