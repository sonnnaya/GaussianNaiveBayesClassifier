import numpy as np
from cluster import Cluster


np.random.seed(0)
clusters = [Cluster([np.random.normal(5, 1.9, size=2) for x in range(10)]),
            Cluster([np.random.normal(4, 1.7, size=2) + 10 for y in range(8)]),
            Cluster([np.random.normal(6, 1.6, size=2) - 10 for z in range(12)])]

test_images = np.genfromtxt('test_data.csv', delimiter=',')
