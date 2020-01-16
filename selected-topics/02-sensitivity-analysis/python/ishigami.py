""" This module provides some capabilities around the Ishigami equation.

    The Ishigami function of Ishigami and Homma (1990) is used as an example for uncertainty and
    sensitivity analysis methods, because it exhibits strong nonlinearity and nonmonotonicity. It
    also has a peculiar dependence on x 3 , as described by I. M. Sobol and Levitan (1999).

    .. math::

        f(x) = \sin(x_1) + a\, \sin^2 (x_2) + b\, x_3^4\, \sin(x_1)

    The independent distributions of the input random variables are usually:
    :math:`x i ∼ Uniform[−π, π]`, for all :math:`i = 1, 2, 3`.

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


def ishigami_readable(x, a=0.7, b=0.1):
    """Evaluate Ishigami equation with a focus on readability

    Parameters
    ----------

    x : numpy.ndarray
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
    return np.sin(x[0]) + a * np.sin(x[1]) ** 2 + b * x[2] ** 4 * np.sin(x[0])


def ishigami_fast(x, a=0.7, b=0.1):
    """ Evaluate Ishigami equation with a focus on speed.

    This function is a vectorized implementation for the evaluation of the Ishigami equation.

    Parameters
    ----------

    x : numpy.ndarray
        evaluation points for Ishigami equation.

    a : float, optional
        first parameter in Ishigami equation (default is 0.7).

    b : float, optional
        second parameter in Ishigami equation (default is 0.1).

    Returns
    -------

    rslt : numpy.ndarray
        evaluations of the Ishigami equation

    Notes
    -----

    [1] https://www.oreilly.com/library/view/python-for-data/9781449323592/ch04.html

    """

    x0, x1, x2 = x[..., 0], x[..., 1], x[..., 2]
    rslt = np.sin(x0) + a * np.sin(x1) ** 2 + b * x2 ** 4 * np.sin(x0)

    return rslt


def get_ishigami_overall_variance(a=0.7, b=0.1):
    """Compute overall variance.

    Parameters
    ----------

    a : float, optional
        first parameter in Ishigami equation (default is 0.7).

    b : float, optional
        second parameter in Ishigami equation (default is 0.1).

    Returns
    -------

    rslt : float
        overall variance.

    """

    rslt = (a ** 2 / 8.0) + (b * (np.pi ** 4)) / 5.0 + (b ** 2 * (np.pi ** 8)) / 18.0 + 0.5

    return rslt


def get_ishigami_main_effects(a=0.7, b=0.1):
    """Compute main effect indices.

    Parameters
    ----------

    a : float, optional
        first parameter in Ishigami equation (default is 0.7).

    b : float, optional
        second parameter in Ishigami equation (default is 0.1).

    Returns
    -------

    rslt : numpy.ndarray
        main effect indices.

    """

    scale = get_ishigami_overall_variance(a, b)

    effects = list()
    effects += [0.5 * (1 + (b * np.pi ** 4 / 5)) ** 2]
    effects += [a ** 2 / 8]
    effects += [0]

    rslt = np.array(effects) / scale

    return rslt


def get_ishigami_total_effects(a=0.7, b=0.1):
    """Compute total effect indices.

    Parameters
    ----------

    a : float, optional
        first parameter in Ishigami equation (default is 0.7).

    b : float, optional
        second parameter in Ishigami equation (default is 0.1).

    Returns
    -------

    rslt : numpy.ndarray
        total effect indices.

    """

    scale = get_ishigami_overall_variance(a, b)
    
    effects = list()
    effects += [0.5 * (1 + (b * np.pi ** 4 / 5)) ** 2 + (8 * b ** 2 * np.pi ** 8) / 225]
    effects += [(a ** 2) / 8]
    effects += [(8 * (b ** 2) * (np.pi ** 8)) / 225]

    rslt = np.array(effects) / scale
    
    return rslt
