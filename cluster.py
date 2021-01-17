import numpy as np
from typing import List


class Cluster:
    def __init__(self, images: List[np.ndarray]):
        self.images: List[np.ndarray] = images

    def add(self, image: np.ndarray) -> None:
        self.images.append(np.array(image))
