import numpy as np
from .context import processing


def test_process():
    data = np.random.rand(10,10)
    data_count = sum(data)
    assert(data_count==processing.process(data))