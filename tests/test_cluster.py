import numpy as np
import valclust
import sys

def test_get_members():
    a = np.array([1,1,1,2,3,1,1,2,3])

    cobj = valclust.cluster.Cluster()

    a1 = cobj._get_members(a, 1)
    
    assert(a1.shape[0] == 5)

    a1_true = [0,1,2,5,6]
    for i in range(5):
	assert(a1[i] == a1_true[i])

def test_get_non_members():
    a = np.array([1,1,1,2,3,1,1,2,3])

    cobj = valclust.cluster.Cluster()

    anot1 = cobj._get_non_members(a, 1)

    assert(anot1.shape[0] == 4)

    anot1_true = [3,4,7,8]
    for i in range(4):
        assert(anot1[i] == anot1_true[i])
