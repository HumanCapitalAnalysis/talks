""" This module provides some capabilities around the Ishigami equation.

    The Ishigami function of Ishigami and Homma (1990) is used as an example for uncertainty and
    sensitivity analysis methods, because it exhibits strong nonlinearity and nonmonotonicity. It
    also has a peculiar dependence on x 3 , as described by I. M. Sobol and Levitan (1999).

    .. math::

        f(x) = \sin(x_1) + a\, \sin^2 (x_2) + b\, x_3^4\, \sin(x_1)

    The independent distributions of the input random variables are usually:
    :math:`x i ∼ Uniform[−π, π]`, for all :math:`i = 1, 2, 3`.

    There are default values for the two parameters of the function with a = 7 and b = 0.1 as
    these are the values used in Crestaux et al. (2007) and Marrel et al. (2009). The research in
    Sobol & Levitan (1999) is based on a = 7 and b = 0.05.

    This module contains the following main elements in this order:

    [1] evaluation of Ishigami function

    [2] analytical solutions to overall variance and sensitivity indices

    [3] simulated solutions to overall variance and sensitivity indices


    References
    ----------

    [1] https://uqworld.org/t/ishigami-function/55

    [2] https://www.sfu.ca/~ssurjano/ishigami.html

    [3] T. Ishigami and T. Homma, “An importance quantification technique in uncertainty analysis
    for computer models,” In the First International Symposium on Uncertainty Modeling and
    Analysis, Maryland, USA, Dec. 3–5, 1990.

    [4] I. M. Sobol’ and Y. L. Levitan, “On the use of variance reducing multipliers in Monte Carlo
    computations of a global sensitivity index,” Computer Physics Communications, vol. 117, no. 1,
    pp. 52–61, 1999.

    [5] Marrel, A., Iooss, B., Laurent, B., & Roustant, O. (2009). Calculations of sobol indices
    for the gaussian process metamodel. Reliability Engineering & System Safety, 94(3), 742-751.

"""
import numpy as np


def evaluate_ishigami_readable(input, a=7, b=0.1):
    """Evaluate Ishigami equation with a focus on readability

    Parameters
    ----------

    inputs : numpy.ndarray
        evaluation points for Ishigami equation.

    a : float, optional
        first parameter in Ishigami equation (default is 0.7).

    b : float, optional
        second parameter in Ishigami equation (default is 0.1).

    Returns
    -------

    rslt : float
        evaluation of the Ishigami equation

    """
    x1, x2, x3 = input
    rslt = np.sin(x1) + a * np.sin(x2) ** 2 + b * x3 ** 4 * np.sin(x1)

    return rslt


def evaluate_ishigami(inputs, a=7, b=0.1):
    """ Evaluate Ishigami equation with a focus on speed.

    This function is a vectorized implementation for the evaluation of the Ishigami equation.

    Parameters
    ----------

    inputs : numpy.ndarray
        Evaluation points for Ishigami equation.

    a : float, optional
        First parameter in Ishigami equation (default is 0.7).

    b : float, optional
        Second parameter in Ishigami equation (default is 0.1).

    Returns
    -------

    rslt : numpy.ndarray
        Evaluations of the Ishigami equation

    Notes
    -----

    [1] https://www.oreilly.com/library/view/python-for-data/9781449323592/ch04.html

    """
    x0, x1, x2 = inputs[..., 0], inputs[..., 1], inputs[..., 2]
    rslt = np.sin(x0) + a * np.sin(x1) ** 2 + b * x2 ** 4 * np.sin(x0)

    return rslt


def compute_analytically_overall_variance(a=7, b=0.1):
    """Compute overall variance analytically.

    Parameters
    ----------

    a : float, optional
        First parameter in Ishigami equation (default is 0.7).

    b : float, optional
        Second parameter in Ishigami equation (default is 0.1).

    Returns
    -------

    rslt : float
        Overall variance.

    """
    rslt = (a ** 2 / 8.0) + (b * (np.pi ** 4)) / 5.0 + (b ** 2 * (np.pi ** 8)) / 18.0 + 0.5

    return rslt


def compute_analytically_main_effects(a=7, b=0.1):
    """Compute main effect indices analytically.

    Parameters
    ----------

    a : float, optional
        First parameter in Ishigami equation (default is 0.7).

    b : float, optional
        Second parameter in Ishigami equation (default is 0.1).

    Returns
    -------

    rslt : numpy.ndarray
        Main effect indices.

    """

    scale = compute_analytically_overall_variance(a, b)

    effects = list()
    effects += [0.5 * (1 + (b * np.pi ** 4 / 5)) ** 2]
    effects += [a ** 2 / 8]
    effects += [0]

    rslt = np.array(effects) / scale

    return rslt


def compute_analytically_total_effects(a=7, b=0.1):
    """Compute total effect indices analytically.

    Parameters
    ----------

    a : float, optional
        First parameter in Ishigami equation (default is 0.7).

    b : float, optional
        Second parameter in Ishigami equation (default is 0.1).

    Returns
    -------

    rslt : numpy.ndarray
        Total effect indices.

    """
    scale = compute_analytically_overall_variance(a, b)
    
    effects = list()
    effects += [0.5 * (1 + (b * np.pi ** 4 / 5)) ** 2 + (8 * b ** 2 * np.pi ** 8) / 225]
    effects += [(a ** 2) / 8]
    effects += [(8 * (b ** 2) * (np.pi ** 8)) / 225]

    rslt = np.array(effects) / scale
    
    return rslt


def compute_simulation_overall_variance(num_draws, seed=123):
    """Compute overall variance by simulation.

    Parameters
    ----------

    num_draws : integer
        Number of draws for simulation.

    seed : integer, optional
        Seed value for random number generator.

    Returns
    -------

    rslt : numpy.float
        Overall variance of model output.

    """
    np.random.seed(seed)
    inputs = np.random.uniform(low=-np.pi, high=np.pi, size=(num_draws, 3))

    return np.var(evaluate_ishigami(inputs))


def compute_simulation_main_effect(num_outer, num_inner, which, seed=123):
    """Compute main effect by simulation.

    Parameters
    ----------

    num_outer : integer
        Number of draws for outer simulation loop.

    num_inner : integer
        Number of draws for inner simulation loop.

    which : integer
        Position of main effect variable.

    seed : integer, optional
        Seed value for random number generator.

    Returns
    -------

    rslt : numpy.float
        Main effect parameter.

    """
    np.random.seed(seed)

    inputs = np.random.uniform(low=-np.pi, high=np.pi, size=(num_outer, num_inner, 3))
    unconditional_variance = np.var(evaluate_ishigami(inputs.reshape(num_outer * num_inner, 3)))

    inputs[:, :, which] = inputs[:, 0, which].reshape(num_outer, 1)
    rslt = np.var(np.mean(evaluate_ishigami(inputs), axis=1)) / unconditional_variance

    return rslt


def compute_simulation_main_effect_readable(num_outer, num_inner, which, seed=123):
    """Compute main effect by simulation with a focus on readability.

    Parameters
    ----------

    num_outer : integer
        Number of draws for outer simulation loop.

    num_inner : integer
        Number of draws for inner simulation loop.

    which : integer
        Position of main effect variable.

    seed : integer, optional
        Seed value for random number generator.

    Returns
    -------

    rslt : numpy.float
        Main effect parameter.

    """
    np.random.seed(seed)

    inputs = np.random.uniform(low=-np.pi, high=np.pi, size=(num_outer, num_inner, 3))
    unconditional_variance = np.var(evaluate_ishigami(inputs.reshape(num_outer * num_inner, 3)))

    rslt_outer = list()

    for i in range(num_outer):
        inputs[i, :, which] = inputs[i, 0, which]

        rslt_inner = list()
        for j in range(num_inner):
            x = inputs[i, j, :]
            rslt_inner.append(evaluate_ishigami(x))

        rslt_outer.append(np.mean(rslt_inner))

    rslt = np.var(rslt_outer) / unconditional_variance

    return rslt


def compute_simulation_total_effect(num_outer, num_inner, which, seed=120):
    """Compute total effect by simulation.

    Parameters
    ----------

    num_outer : integer
        Number of draws for outer simulation loop.

    num_inner : integer
        Number of draws for inner simulation loop.

    which : integer
        Position of main effect variable.

    seed : integer, optional
        Seed value for random number generator.

    Returns
    -------

    rslt : numpy.float
        Main effect parameter.

    """
    np.random.seed(seed)

    inputs = np.random.uniform(low=-np.pi, high=np.pi, size=(num_outer, num_inner, 3))
    unconditional_variance = np.var(evaluate_ishigami(inputs.reshape(num_outer * num_inner, 3)))

    for not_which in set(range(3)).difference([which]):
        inputs[:, :, not_which] = inputs[:, 0, not_which].reshape(num_outer, 1)
    conditional_variance = np.var(np.mean(evaluate_ishigami(inputs), axis=1))

    rslt = 1 - conditional_variance / unconditional_variance

    return rslt
