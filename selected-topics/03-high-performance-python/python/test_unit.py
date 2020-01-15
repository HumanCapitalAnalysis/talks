import numpy as np

from auxiliary import * 
from ishigami import * 

def test_1():
    
    for _ in range(10):
        num_outer, num_inner, seed = np.random.randint(6, 10, size=3)
        which = np.random.choice(range(3))

        stat_1 = get_conditional_variance_fast(num_outer, num_inner, which, seed)
        stat_2 = get_conditional_variance_readable(num_outer, num_inner, which, seed)      

        np.testing.assert_equal(stat_1, stat_2)
        
def test_2():
    num_draws = np.random.randint(6, 10)
    inputs =  np.random.uniform(low=-np.pi, high=np.pi, size=(num_draws, 3))

    rslt = list()
    for input_ in inputs:
        rslt.append(ishigami_readable(input_))

    np.testing.assert_equal(ishigami_fast(inputs), rslt)