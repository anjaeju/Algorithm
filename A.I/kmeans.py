import numpy as np
import matplotlib.pyplot as plt

from numpy.linalg import norm

# https://towardsdatascience.com/k-means-clustering-algorithm-applications-evaluation-methods-and-drawbacks-aa03e644b48a
# 해당 게시글 보고 연습

class Kmeans(object):
    '''implementing Kmean'''

    def __init__(self, n_clusters, max_iter=100, random_state=123):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.random_state = random_state

    def init_centroids(self, X):
        np.random.RandomState(self.random_state)
        random_idx = np.random.permutation(X.shape[0])
        centroids = X[random_idx[:self.n_clusters]]
        return centroids

    def compute_distance(self, X, centroids):
        
        distance = np.zeros((X.shape[0], self.n_clusters))
        
        for k in range(self.n_clusters):
            row_norm = norm(X - centroids[k, :], axis=1)
            distance[:, k] = np.square(row_norm)     
        return distance

    def find_closest_cluster(self, distance):
        return np.argmin(distance, axis=1)

    def compute_centroids(self, X, labels):
        centroids = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            centroids[k, :] = np.mean(X[labels == k, :], axis=0)
        return centroids

    def compute_sse(self, X, labels, centroids):
        distance = np.zeros(X.shape[0])
        for k in range(self.n_clusters):
            distance[labels == k] = norm(X[labels == k] - centroids[k], axis=1)
        return np.sum(np.square(distance))            

    def fit(self, X):
        self.centroids = self.init_centroids(X)

        for i in range(self.max_iter):
            old_centroids = self.centroids
            distance = self.compute_distance(X, old_centroids)
            self.labels = self.find_closest_cluster(distance)
            print(self.labels)
            self.centroids = self.compute_centroids(X, self.labels)

            if np.all(old_centroids == self.centroids):
                break
        self.error = self.compute_sse(X, self.labels, self.centroids)




if __name__ == '__main__':

    Random = 1
    X = np.vstack((np.random.rand(30), np.random.rand(30))).reshape(-1, 2)

    print(X)
    
    plt.scatter(X[:,0], X[:,1])
    plt.show()

    km = Kmeans(n_clusters = 2, max_iter = 100, random_state=Random)
    km.fit(X)

    centroids = km.centroids

    fig, ax = plt.subplots(figsize=(6,6))

    plt.scatter(X[km.labels == 0, 0], X[km.labels == 0, 1], c='lightgreen', label='cluters 1')
    plt.scatter(X[km.labels == 1, 0], X[km.labels == 1, 1], c='lightblue', label='cluters 1')
    plt.scatter(centroids[:,0], centroids[:,1], marker='*', s=300, c='r', label='centroid')

    plt.legend()

    ax.set_aspect('equal')
    plt.show()
