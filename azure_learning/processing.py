import numpy as np

def process(data: np.ndarray) -> int:
    return sum(data.flatten())