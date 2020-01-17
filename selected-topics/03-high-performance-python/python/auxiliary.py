import sys

import numpy as np

sys.path.insert(0, "../02-sensitivity-analysis/python")

from ishigami import compute_simulation_total_effect

from ishigami import compute_simulation_main_effect
from ishigami import evaluate_ishigami_readable


def evaluate_ishigami_loop(inputs):
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
    print(f"... started on input parameter {which}")
    rslt = compute_simulation_main_effect(num_outer, num_inner, which)
    print(f"... finished input parameter {which}")


def task_mp_queue(num_outer, num_inner, qout, which):
    """Compute main effect by simulation.

    This function computes the main effects by simulation for
    one input parameter and puts the result into `qout` container.

    Parameters
    ----------

    num_outer : integer
        Number of draws for outer simulation loop.

    num_inner : integer
        Number of draws for inner simulation loop.

    which : integer
        Position of main effect variable.

    qout : multiprocessing.Queue
        Queue container to collect results. A tuple
        with the identifier of the input parameter
        and the main effect is put into the quque.

    Returns
    -------

    None

    """
    rslt = compute_simulation_main_effect(num_outer, num_inner, which)
    qout.put((which, rslt))

def task_mp_management(num_outer, num_inner, task):
    label, which = task
    print(f"working on {label} effect for input {which}")
    if label == "main":
        return compute_simulation_main_effect(num_outer, num_inner, which)
    elif label == "total":
        return compute_simulation_total_effect(num_outer, num_inner, which)
    else:
        raise NotImplementedError