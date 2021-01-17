import numpy as np
from functools import reduce
from typing import List
from scipy.stats import norm
from cluster import Cluster


def likelihood_function(x: np.ndarray, mean: np.ndarray, std: np.ndarray) -> float:
    return reduce(lambda i, j: i * j, norm.pdf(x, mean, std))


def prior_probability(total_images: int, cluster: Cluster) -> float:
    return len(cluster.images) / total_images


def posterior_probability(x: np.ndarray, clusters: List[Cluster], cluster: Cluster) -> float:
    total_images = sum(map(lambda x: len(x.images), clusters))

    mean = np.array(cluster.images).mean(axis=0)
    std = np.array(cluster.images).std(axis=0)

    return likelihood_function(x, mean, std) * prior_probability(total_images, cluster)
