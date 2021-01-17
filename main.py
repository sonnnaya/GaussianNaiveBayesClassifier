import numpy as np
from typing import List
from cluster import Cluster
from data import test_images, clusters
from probabilities import posterior_probability


def classify(image: np.ndarray, clusters: List[Cluster]):
    probabilities = [np.log(10 ** 30 * posterior_probability(image, clusters, cluster)) for cluster in clusters]
    maximum = max(probabilities)
    index = probabilities.index(maximum)
    clusters[index].add(image)


for each in test_images:
    classify(each, clusters)

if __name__ == '__main__':
    for i, each in enumerate(clusters):
        print(f'Class {i + 1}: {[x.tolist() for x in each.images]}')
