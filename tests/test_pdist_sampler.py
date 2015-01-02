import numpy as np
import sys
from valclust.clusterSeparation import PairwiseDistanceSampler as pds


def test_intra_sampling():

    np.random.seed(1234)

    d1 = np.random.multivariate_normal(mean=[-1,1], cov=[[1, 0],[0, 1]], size=3)
    d2 = np.random.multivariate_normal(mean=[2,-2], cov=[[1, 0],[0, 1]], size=4)

    d = np.vstack((d1, d2))
    y = np.array([1,1,1, 2,2,2,2])
    sam_obj = pds()

    ds1 = sam_obj.intra_sampler(d, y, 1, size=None)
    assert(ds1.shape[0]) == 3

    ds2 = sam_obj.intra_sampler(d, y, 2, size=None)
    assert(ds2.shape[0]) == 6

if __name__ == '__main__':
    unittest.main()
