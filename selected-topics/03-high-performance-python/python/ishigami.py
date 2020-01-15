import numpy as np

def ishigami_readable(x, a=0.7, b=0.1):
    return np.sin(x[0]) + a * np.sin(x[1]) ** 2 + b * x[2] ** 4 * np.sin(x[0])

def ishigami_fast(x, a=0.7, b=0.1):
    x0, x1, x2 = x[:, 0], x[:, 1], x[:, 2]
    return np.sin(x0) + a * np.sin(x1) ** 2 + b * x2 ** 4 * np.sin(x0)
