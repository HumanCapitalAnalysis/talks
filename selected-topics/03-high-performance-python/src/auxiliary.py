import glob
import sys
import os

from numpy import f2py
from numba import jit
import numpy as np

sys.path.insert(0, "../../02-sensitivity-analysis/python")

from ishigami import compute_simulation_total_effect
from ishigami import compute_simulation_main_effect
from ishigami import evaluate_ishigami_readable
from ishigami import evaluate_ishigami_numba

cwd = os.getcwd()

os.chdir(os.path.dirname(__file__))
if not glob.glob("ishigami_f2py*"):
    src = open('ishigami.f90', 'rb').read()
    f2py.compile(src, 'ishigami_f2py', "", extension='.f90')
    from ishigami_f2py import evalute_ishigami_f2py
    os.chdir(cwd)


@jit(nopython=True)
def evaluate_ishigami_numba_loop(inputs):
    """Evaluate Ishigami function.

    Parameters
    ----------

    inputs : numpy.ndarray
        Evaluation points for Ishigami equation.

    Returns
    -------

    results : numpy.ndarray
        Results from evaluation of `inputs`.

    """
    results = np.empty(inputs.shape[0])

    for i in range(inputs.shape[0]):
        results[i] = evaluate_ishigami_numba(inputs[i, :])

    return results


def evaluate_ishigami_f2py_loop(inputs):
    """Evaluate Ishigami function.

    Parameters
    ----------

    inputs : numpy.ndarray
        Evaluation points for Ishigami equation.

    Returns
    -------

    results : numpy.ndarray
        Results from evaluation of `inputs`.

    """

    results = evalute_ishigami_f2py(inputs, inputs.shape[0])

    return results


def evaluate_ishigami_readable_loop(inputs):
    """Evaluate Ishigami function.

    Parameters
    ----------

    inputs : numpy.ndarray
        Evaluation points for Ishigami equation.

    Returns
    -------

    results : numpy.ndarray
        Results from evaluation of `inputs`.

    """
    results = list()

    for input_ in inputs:
        results.append(evaluate_ishigami_readable(input_))

    return np.array(results)


def task_mp_no_communication(num_outer, num_inner, which):
    """Compute main effect by simulation.

     This function computes the main effects by simulation for one input parameter but does not
     return anything.

     Parameters
     ----------

     num_outer : integer
         Number of draws for outer simulation loop.

     num_inner : integer
         Number of draws for inner simulation loop.

     which : integer
         Position of main effect variable.

     Returns
     -------

     None

     """
    _ = compute_simulation_main_effect(num_outer, num_inner, which)


def task_mp_queue(num_outer, num_inner, qout, which):
    """Compute main effect by simulation.

    This function computes the main effects by simulation for one input parameter and puts the
    result into `qout` container.

    Parameters
    ----------

    num_outer : integer
        Number of draws for outer simulation loop.

    num_inner : integer
        Number of draws for inner simulation loop.

    which : integer
        Position of main effect variable.

    qout : multiprocessing.Queue
        Queue container to collect results. A tuple with the identifier of the input parameter
        and the main effect is put into the queue.

    Returns
    -------

    None

    """
    rslt = compute_simulation_main_effect(num_outer, num_inner, which)
    qout.put((which, rslt))


def task_mp_management(num_outer, num_inner, task):
    """Compute sensitivity indices by simulation.

     This function computes the sensitivity indices for one input parameter but does not return
     anything.

     Parameters
     ----------

     num_outer : integer
         Number of draws for outer simulation loop.

     num_inner : integer
         Number of draws for inner simulation loop.

     task : tuple
         Task information. The first element determines whether to simulate the main or total
         effect, while the second indicates the input parameters.

     Returns
     -------

     None

     """
    label, which = task
    if label == "main":
        return compute_simulation_main_effect(num_outer, num_inner, which)
    elif label == "total":
        return compute_simulation_total_effect(num_outer, num_inner, which)
    else:
        raise NotImplementedError
