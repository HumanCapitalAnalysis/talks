"""" Example script MPI dynamic process management.

    This example computes the sensitivity indices using the executor.map() command.

    Notes
    -----

    [1] See https://mpi4py.readthedocs.io/en/stable/tutorial.html#dynamic-process-management for
    a more involved example using the master - worker paradigm.

    Usage
    -----

    mpiexec -n 1 -usize 2 python mpi_dynamic_process_map.py

"""
from functools import partial
import itertools

from mpi4py.futures import MPIPoolExecutor
from auxiliary import task_mp_management

if __name__ == '__main__':

    num_outer = num_inner = 1000

    # Note that we can use exactly the same function as for the MP example.
    task_partial = partial(task_mp_management, num_outer, num_inner)

    tasks = list(itertools.product(["main", "total"], range(3)))

    with MPIPoolExecutor() as executor:
        results = executor.map(task_partial, tasks)

    for i, rslt in enumerate(results):
        print(rslt, tasks[i])
