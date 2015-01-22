import numpy as np
import valclust
import valclust.ExternalValidity as EV
import sys

def test_purity():
    y = np.array([1,1,1,2,2,2,2])
    g = np.array([5,5,5,7,7,9,9])

    obj = EV.CompareCluster(X=None, y=y)


    r1 = obj.clusterPurity(1, g)
    assert (r1 == 1.0)

    r2 = obj.clusterPurity(2, g)
    assert (r2 == 0.5)
