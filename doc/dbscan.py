import numpy as np
import scipy
import scipy.spatial
import sklearn.cluster


def DBSCAN(data, eps, min_pts):
    """ Clustering data using DBSCAN algorithm.
    """
    
    #kd-tree for quick nearest-neighbor lookup
    tree = scipy.spatial.cKDTree(data)
    neighbors = tree.query_ball_point(data, eps)
    clusters = [] # list of (set, set)'s, to distinguish 
                  # core/reachable points
    visited = set()
    for i in xrange(len(data)):
        if i in visited: 
            continue
        visited.add(i)
        if len(neighbors[i]) >= min_pts:
            clusters.append(({i}, set())) # core
            to_merge_in_cluster = set(neighbors[i])
            while to_merge_in_cluster:
                j = to_merge_in_cluster.pop()
                if j not in visited:
                    visited.add(j)
                    if len(neighbors[j]) >= min_pts:
                        to_merge_in_cluster |= set(neighbors[j])
                if not any([j in c[0] | c[1] for c in clusters]):
                    if len(neighbors[j]) >= min_pts:
                        clusters[-1][0].add(j) # core
                    else:
                        clusters[-1][1].add(j) # reachable
    return np.array(clusters)


import networkx as nx

colors = 'rbgycm' * 10

def ConnectedComponents(data, eps):

   tree = scipy.spatial.cKDTree(data)
   neighbors = tree.query_ball_point(data, eps)

   g = nx.Graph()
   g.add_nodes_from(xrange(len(data)))
   nx.draw_networkx(g, data, with_labels=False, node_size=5, \
                 node_color=[.5] * 3, width=.5)   
   g = nx.Graph()
   for i in xrange(len(data)):
       if len(neighbors[i]) >= 10:
           g.add_edges_from([(i, j) for j in neighbors[i]])

   for i, comp in enumerate(nx.connected_component_subgraphs(g)):
        nx.draw_networkx(comp, data, with_labels=False, node_size=5, \
                     node_color=[.5] * 3, edge_color=colors[i], width=.5)




def main():

    np.random.seed(seed=1234)

    m1 = np.array([-2,-2])
    m2 = np.array([0,1.5])
    m3 = np.array([1.7,-1.8])
    S1 = np.array([[0.4,0.1],[0.1,0.4]])
    S2 = np.array([[0.5,-0.05],[-0.05,0.5]])
    S3 = np.array([[0.56,0],[0,0.56]])
    d1 = np.random.multivariate_normal(mean=m1, cov=S1, size=1000)
    d2 = np.random.multivariate_normal(mean=m2, cov=S2, size=1000)
    d3 = np.random.multivariate_normal(mean=m3, cov=S3, size=1000) 

    d = np.concatenate([d1, d2, d3])
    print(d.shape)

    #np.savetxt('zzz/data.3clusters.dat', d)


    import time
   
    start = time.time()
    cl = DBSCAN(d, eps=0.2, min_pts=20)
    end = time.time()

    print(end-start, cl.shape)
    for i, (core, neighb) in enumerate(cl):
	print (i, len(core), len(neighb), len(core) + len(neighb))


    dbs = sklearn.cluster.DBSCAN(eps=0.2, min_samples=20, metric='euclidean', algorithm='kd_tree', leaf_size=100)
    start = time.time()
    cl2 = dbs.fit_predict(d)
    end = time.time()
    print(end-start, cl2.shape)
    for i in np.unique(cl2):
        print (i, np.sum(cl2 == i))

    dbs = sklearn.cluster.DBSCAN(eps=0.2, min_samples=20, metric='euclidean', algorithm='brute')
    start = time.time()
    cl2 = dbs.fit_predict(d)
    end = time.time()
    print(end-start, cl2.shape)

    #ConnectedComponents(d, 0.2)

if __name__ == "__main__":
    main()


