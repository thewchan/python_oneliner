"""K-Means clustering one-liner example."""
import numpy as np
from sklearn.cluster import KMeans


X = np.array([[35, 7000], [45, 6900], [70, 7100],
              [20, 2000], [25, 2200], [15, 1800]])

# One-liner
kmeans = KMeans(n_clusters=2).fit(X)

print('Input data: [Work hours, Salary $]')
print(X)
print('K-means fit:')
print(kmeans.cluster_centers_)
