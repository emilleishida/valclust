import numpy as np
from valclust.clusterSeparation import PairwiseDistanceSampler as pds


def test_intra_sampling():
    d = np.random.multivariate_normal(mean=[0,0], cov=[[1, 0],[0, 1]], size=10)
    y = np.ones(shape=(10,), dtype='int')
    sam_obj = pds()

    sam_obj.intra_sampler(d, y, 1, size=None)
