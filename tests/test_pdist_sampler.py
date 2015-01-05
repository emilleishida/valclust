import numpy as np
import sys
from valclust.ExternalValidity import PairwiseDistanceSampler as pds


def test_intra_sampling():

    np.random.seed(1234)

    d1 = np.random.multivariate_normal(mean=[-1,1], cov=[[1, 0],[0, 1]], size=3)
    d2 = np.random.multivariate_normal(mean=[2,-2], cov=[[1, 0],[0, 1]], size=4)

    d = np.vstack((d1, d2))
    y = np.array([1,1,1, 2,2,2,2])

    sam_obj = pds(d, y)

    ds1 = sam_obj.intra_sampler(1, size=None)
    assert(ds1.shape[0]) == 3

    ds2 = sam_obj.intra_sampler(2, size=None)
    assert(ds2.shape[0]) == 6


    d = np.array(["TTTA", "TGTT", "TAAT", "GTTA", "GGCG"])
    y = np.array(["c1", "c1", "c1", "c1", "c2"])
    ds3 = sam_obj.intra_sampler("c1", size=None, method="editdist")
    sys.stderr.write("**** %d\n" %(ds3.shape[0]))
    assert(ds3.shape[0]) == 6


def test_inter_sampling():

    np.random.seed(1234)

    d1 = np.random.multivariate_normal(mean=[-1,1], cov=[[1, 0],[0, 1]], size=3)
    d2 = np.random.multivariate_normal(mean=[2,-2], cov=[[1, 0],[0, 1]], size=4)

    d = np.vstack((d1, d2))
    y = np.array([1,1,1, 2,2,2,2])

    sam_obj = pds(d, y)

    ds1 = sam_obj.inter_sampler(1, size=None)
    assert(ds1.shape[0]) == 12




if __name__ == '__main__':
    test_intra_sampling()
