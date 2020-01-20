import numpy as np

from ishigami import compute_simulation_main_effect_readable
from ishigami import compute_analytically_overall_variance
from ishigami import compute_simulation_overall_variance
from ishigami import compute_simulation_main_effect
from ishigami import evaluate_ishigami_vectorized
from ishigami import evaluate_ishigami_readable
from ishigami import evaluate_ishigami_numba


def test_1():
    """ Testing the equality of the fast and readable implementation of the Ishigami evaluations."""
    for _ in range(10):
        num_draws = np.random.randint(6, 10)
        inputs = np.random.uniform(low=-np.pi, high=np.pi, size=(num_draws, 3))

        rslt = [evaluate_ishigami_readable(input_) for input_ in inputs]
        np.testing.assert_equal(evaluate_ishigami_vectorized(inputs), rslt)

        rslt = [evaluate_ishigami_numba(input_) for input_ in inputs]
        np.testing.assert_almost_equal(evaluate_ishigami_vectorized(inputs), rslt)


def test_2():
    """Testing closed-form solution to its approximation."""
    num_draws = 10000000
    stat_1 = compute_simulation_overall_variance(num_draws)
    stat_2 = compute_analytically_overall_variance()

    np.testing.assert_almost_equal(stat_1, stat_2, decimal=2)


def test_3():
    """Testing equality of the fast and readable implementation of the main effects."""
    for _ in range(10):
        num_outer, num_inner, seed = np.random.randint(10, 100, size=3)
        which = np.random.choice(3)

        args = (num_outer, num_inner, which, seed)
        stat_1 = compute_simulation_main_effect_readable(*args)
        stat_2 = compute_simulation_main_effect(*args)

        np.testing.assert_almost_equal(stat_1, stat_2)