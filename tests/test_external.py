import numpy as np
import valclust
import valclust.ExternalValidity as EV
import sys

def test_purity():
    y = np.array([1,1,1,2,2,2,2,-1])
    g = np.array([5,5,5,7,7,9,9,2])

    obj = EV.CompareCluster(X=None, y=y)


    r1 = obj.clusterPurity(1, g)
    assert (r1 == 1.0)

    r2 = obj.clusterPurity(2, g)
    assert (r2 == 0.5)

    tot = obj.totalPurity(g, singleton=-1)
    assert (tot == 0.75)

def test_NMI():
    y = np.array([1,1,1,2,2,2,2,3])
    g = np.array([5,5,5,7,7,5,5,7])

    obj = EV.CompareCluster(X=None, y=y)

    nmi = obj.normalizedMutualInfo(y) ## Comparre with itself
    sys.stderr.write("NMI : %f"%(nmi))
    assert (nmi == 1.0)

    nmi = obj.normalizedMutualInfo(g)
    sys.stderr.write("NMI : %f"%(nmi))
    assert(int(nmi*10000) == 3851)

def test_contingency():
    y = np.array([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3])
    g = np.array([4,4,4,4,5,4,4,5,5,5,7,5,4,4,7,7,7])

    obj = EV.CompareCluster(X=None, y=y)
    obj._contingency(g)

    #sys.stderr.write("TP:  %f\tFP:  %f\n"%(obj.tp, obj.fp))
    assert(obj.tp == 20)
    assert(obj.fp == 20)
    

    obj._contingency(y)
