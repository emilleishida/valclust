import numpy as np
import valclust
import sys

def test_get_members():
    X = np.array([1,1,1,1,1,1,1,1,1])
    a = np.array([1,1,1,2,3,1,1,2,3])

    cobj = valclust.cluster.Cluster(X, a)

    a1 = cobj._get_members(1)
    
    assert(a1.shape[0] == 5)

    a1_true = [0,1,2,5,6]
    for i in range(5):
	assert(a1[i] == a1_true[i])


def test_get_members_string():
    X = np.array(['TATT', 'TTTA', 'GACG', 'GCGT', 'ATTA', 'TAAT', 'GCGG'])
    y = np.array(['c1', 'c1', 'c2', 'c2', 'c1', 'c1', 'c2'])

    cobj = valclust.cluster.Cluster(X, y)
    a1 = cobj._get_members('c1')
    a2 = cobj._get_members('c2')

    assert (a1.shape[0] == 4)
    assert (a2.shape[0] == 3)

    a1_true = [0,1,4,5]
    for i in range(4):
       assert(a1[i] == a1_true[i])

    a2_true = [2,3,6]
    for i in range(3):
       assert(a2[i] == a2_true[i])


def test_get_non_members():
    X = np.array([1,1,1,1,1,1,1,1,1])
    a = np.array([1,1,1,2,3,1,1,2,3])

    cobj = valclust.cluster.Cluster(X, a)

    anot1 = cobj._get_non_members(1)

    assert(anot1.shape[0] == 4)

    anot1_true = [3,4,7,8]
    for i in range(4):
        assert(anot1[i] == anot1_true[i])


def test_get_num_singletons():
    X = np.array([1,1,1,1,1,1,1,1,1,1,1,1])
    a = np.array([1,1,0,2,-1,0,1,0,-1,0,1,2])

    cobj = valclust.cluster.Cluster(X, a)
    nsing = cobj._num_singletons()
    assert (nsing == 2)

    nsing = cobj._num_singletons(indicator=0)
    assert (nsing == 4)

    cobj.summary()
