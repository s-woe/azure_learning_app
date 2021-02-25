import numpy as np
from .context import processing


def test_process():
    data = 1
    assert(2==processing.process(data))