valclust
========

Clustering Validation and Analysis


  * Different Types of Cluster Validity Indecies:

    1. External Indecies: comparing the clustering results with the *a priori* known clusters
    2. Internal indecies: measuring the quality of clusterings without comparing to any other clustering solution
    3. Relative indecies: comparing the clustering results obtained from different algorithms, or dissimilarity measures 


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



   Example

```
from valclust.clusterSeparation import ClusterDistanceSampler as cds

```

  **Example: External Validaity Indecies**

```
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
