import numpy as np

class Cluster(object):
    """
    Class to find distinct clusters.

    Class Metods:

	n_distnict(self, y): the number of distinct clusters
	cluster_sizes(self, y): the sizes of each cluster in a numpy ndarray
	get_members(self, y, cinx): the indeces of members of a particular cluster cinx

    """

    def __init__(self, X=None, y=None, g=None):
	self.set_data(X, y, g)

    def set_data(self, X, y, g=None):
        self.X = X
        self.y = y
	self.g = g
        self.n = y.shape[0]
	#if conv_singletons:
	#    self.convert_singletons()

	self.ysize, self.ydict = self.cluster_sizes()

    def convert_singletons(self):
	"""
	Convert non-clusters (-1) to singletons
	"""
	cmax = np.max(self.y)
	for i,y in enumerate(self.y):
	   if y == -1:
		self.y[i] = cmax + i
	gmax = np.max(self.g)
        for i,g in enumerate(self.g):
           if g == -1:
                self.g[i] = gmax + i


    def n_distinct(self):
	"""
	Returns  the number of distinct clusters.
	"""
        return(np.unique(self.y).shape[0])

    def unique(self):
	return(np.unique(self.y))

    def cluster_sizes(self, arr=None):
	"""
	Returns the sizes of each cluster in a numpy ndarray.
	(or a dictionary)
	"""
	if arr is None:
	    arr = self.y
	tup = np.unique(arr, return_counts = True)

	asize = np.asarray(tup).T
	dsize = dict(asize)
	return(asize, dsize)

    def _get_members(self, cinx):
	"""
	Returns a numpy array for the indecies of all 
	members for a specific cluster indexed by cinx.
	
	"""
	allindx = np.arange(0, self.n)
	return (allindx[self.y == cinx])
        

    def _get_non_members(self, cinx):
	"""
	Returns a numpy array for the indecies of all
	data points that DO NOT belong to cluster cinx.

	"""
	allindx = np.arange(0, self.n)
	return (allindx[self.y != cinx])

    def distance(self, i, j, method='euclidean'):
        x1 = self.X[i]
        x2 = self.X[j]
        if method == 'euclidean':
            diff = x1 - x2
            sq_diff = diff * diff
            return(np.sqrt(np.sum(sq_diff)))
        elif method == 'editdist':
            return(editdist.distance(x1, x2))

    def _num_singletons(self):
	"""Finding the number of singletons
	   specified by indicator [default=-1]
	"""
        return (np.sum(np.array(self.ysize[:,1]) == 1))

    def entropy(self):
	""" Computing the entropy of a clustering.
	"""
	s = 0.0
	nt = float(self.n)
	for k in self.ysize[:,1]:
	    s -= k/nt * np.log(k/nt)
	return(s)

    def summary(self):
        """ Gives a summary statistics on clusters.
	"""
	print ("Number of singletons: %d"%(self._num_singletons()))
	print ("Number of clusters: %d"%(self.n_distinct()))

	return (None)
