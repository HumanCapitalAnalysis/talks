import numpy as np
from ishigami import *

def get_unconditional_variance_fast(num_draws, seed=123):
    
    np.random.seed(seed)
    inputs =  np.random.uniform(low=-np.pi, high=np.pi, size=(num_draws, 3))

    return np.var(ishigami_fast(inputs))

    
def get_unconditional_variance_readable(num_draws, seed=123):
    
    np.random.seed(seed)
    inputs =  np.random.uniform(low=-np.pi, high=np.pi, size=(num_draws, 3))

    rslt = list()
    for x in inputs:
        rslt.append(ishigami_readable(x))

    return np.var(rslt)
    
def get_conditional_variance_fast(num_outer, num_inner, which, seed=123):
    
    np.random.seed(seed)
    
    rslt = np.random.uniform(low=-np.pi, high=np.pi, size=(num_outer, num_inner, 3))
    rslt[:, :, which] = rslt[:, 0, which].reshape(num_outer, 1)
    return np.var(np.apply_along_axis(np.mean, 1, np.apply_along_axis(ishigami_readable, 2, rslt)))


def get_conditional_variance_readable(num_outer, num_inner, which, seed=123):
    
    np.random.seed(seed)

    rslt = np.random.uniform(low=-np.pi, high=np.pi, size=(num_outer, num_inner, 3))

   
    rslt_outer = list()
    for i in range(num_outer):
        x0 = np.random.uniform(low=-np.pi, high=np.pi, size=1)
        
        rslt[i, :, which] = rslt[i, 0, which]
        
        rslt_inner = list()
        for j in range(num_inner):
            x = rslt[i, j, :]
            rslt_inner.append(ishigami_readable(x))

        rslt_outer.append(np.mean(rslt_inner))

    return np.var(rslt_outer) 