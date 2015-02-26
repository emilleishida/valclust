valclust
========

Clustering Validation and Analysis


  * Different Types of Cluster Validity Indecies:

    1. External Indecies: comparing the clustering results with the *a priori* known clusters
    2. Internal indecies: measuring the quality of clusterings without comparing to any other clustering solution
    3. Relative indecies: comparing the clustering results obtained from different algorithms, or dissimilarity measures 


## External Indecies:

  * Purity	
  * NMI (Normalized Mutual Information - information theoretic)
  * NID 
  * MCC (Mathew's Correlation Coefficient)

## Internal Indecies:

  * Silhouette Index
  * Davis-Bouldin Index
  * Calinski-Harabasz Index
  * Dunn Index
  * RMSSTD Index
  * Gap Statistic (finding the number of clusters)


### Similarity Measures between Different Groupings

  * Cosine Similarity or Correlation 
  * Matching Coefficient
  * Jaccard Coefficient
  

## clusterSeparation

  * Falls within the category of internal indecies
  * Separability and compactness of clusters

Measuring te quality of clusterings by calculating the intra-cluster and inter-cluster distances.



  **Example: Internal Validity**

```
import numpy as np
from valclust.InternalValidity import PairwiseDistanceSampler as pds

np.random.seed(1234)

d1 = np.random.multivariate_normal(mean=[-1,1], cov=[[1, 0],[0, 1]], size=3)
d2 = np.random.multivariate_normal(mean=[2,-2], cov=[[1, 0],[0, 1]], size=4)

d = np.vstack((d1, d2))
y = np.array([1,1,1, 2,2,2,2])

sam_obj = pds(d, y)  # sampler object

# distance among points within cluster 1
ds1_intra = sam_obj.intra_sampler(1, size=None) 
# distance bwtween points from cluster 1 and the rest
ds1_inter = sam_obj.inter_sampler(1, size=None)

```
Output:
```
>>> ds1_intra
array([ 0.        ,  2.46500264,  0.        ])

>>> ds1_inter
array([ 4.17855077,  5.17794181,  5.176349  ,  7.17877856,  4.17855077,
        4.11556509,  6.43752761,  5.17794181,  7.17877856,  4.78430904,
        7.53358227,  7.17877856])
```


  **Example: External Validaity Indecies**

```
import numpy as np
import valclust
import valclust.ExternalValidity as EV

y = np.array([1,1,1,2,2,2,2,-1])
g = np.array([5,5,5,7,7,9,9,2])

obj = EV.CompareCluster(X=None, y=y)

for i in np.unique(y):
   res = obj.clusterPurity(i, g)
   print("Purity for cluster %d ==> %.4f"%(i, res))
```
Output: 
```
Purity for cluster -1 ==> 1.0000
Purity for cluster 1 ==> 1.0000
Purity for cluster 2 ==> 0.5000


```
