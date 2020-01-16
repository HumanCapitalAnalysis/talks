import numpy as np
#https://uqworld.org/t/ishigami-function/55

def ishigami_readable(x, a=0.7, b=0.1):
    return np.sin(x[0]) + a * np.sin(x[1]) ** 2 + b * x[2] ** 4 * np.sin(x[0])

def ishigami_fast(x, a=0.7, b=0.1):
    x0, x1, x2 = x[..., 0], x[..., 1], x[..., 2]
    return np.sin(x0) + a * np.sin(x1) ** 2 + b * x2 ** 4 * np.sin(x0)


def get_ishigami_unconditional_variance(a=0.7, b=0.1):
    
    return a ** 2 / 8 + b * (np.pi ** 4) / 5 + b ** 2 * np.pi ** 8 / 18 + 1 / 2 

def get_ishigami_conditional_variances(a=0.7, b=0.1):
    
    
    return 0.5 * (1 + (b * np.pi ** 4 / 5)) ** 2, a ** 2 / 8, 0.0