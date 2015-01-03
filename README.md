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


## clusterSeparation

  * Falls within the category of internal indecies
  * Separability and compactness of clusters

Measuring te quality of clusterings by calculating the intra-cluster and inter-cluster distances.



   Example

```
from valclust.clustDistAnalysis import ClusterDistanceSampler as cds

```
