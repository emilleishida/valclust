import numpy as np
import valclust
import valclust.external as exv
import sys

def test_purity():
    y = np.array([1,1,1,2,2,2,2])
    g = np.array([5,5,5,7,7,9,9])

    obj = exv.CompareCluster(X=None, y=y, g=g)


    r1 = obj.clusterPurity(1)
    assert (r1 == 1.0)

    r2 = obj.clusterPurity(2)
    assert (r2 == 0.5)

    tot = obj.totalPurity()
    assert (tot == 0.75)

def test_NMI():
    y = np.array([1,1,1,2,2,2,2,3])
    g = np.array([5,5,5,7,7,5,5,7])

    obj = exv.CompareCluster(X=None, y=y, g=y)

    nmi = obj.normalizedMutualInfo() ## Comparre with itself
    sys.stderr.write("NMI : %f"%(nmi))
    assert (nmi == 1.0)

    obj = exv.CompareCluster(X=None, y=y, g=g)
    nmi = obj.normalizedMutualInfo()
    sys.stderr.write("NMI : %f"%(nmi))
    assert(int(nmi*10000) == 3851)

def test_contingency():
    y = np.array([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3])
    g = np.array([4,4,4,4,5,4,4,5,5,5,7,5,4,4,7,7,7])

    obj = exv.CompareCluster(X=None, y=y, g=g)
    obj._contingency()

    #sys.stderr.write("TP:  %f\tFP:  %f\n"%(obj.tp, obj.fp))
    #sys.stderr.write("FN:  %f\tTN:  %f\n"%(obj.fn, obj.tn))
    assert(obj.tp == 20)
    assert(obj.fp == 20)
    assert(obj.fn == 24)
    assert(obj.tn == 72)

    obj = exv.CompareCluster(X=None, y=y, g=y)
    obj._contingency()
    assert(obj.tp == 40)
    assert(obj.fp == 0)
    assert(obj.fn == 0)
    assert(obj.tn == 96)

def test_MCC():
    y = np.array([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3])
    g = np.array([4,4,4,4,5,4,4,5,5,5,7,5,4,4,7,7,7])

    obj = exv.CompareCluster(X=None, y=y, g=g)
    res = obj.MCC()

    assert(int(res*10000) == 2434)
