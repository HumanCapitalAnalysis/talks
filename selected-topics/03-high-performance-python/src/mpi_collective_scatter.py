"""" Example script MPI collective communication.

    This module illustrates the MPI scattering of a list. Its elements are send from a root
    process to all processes in the communicator. However, not all data is send to all processes.
    Instead, it is distributed in chunks.

    References
    ----------

    [1] https://mpi4py.readthedocs.io

    Examples
    --------

    mpiexec -n 5 python mpi_collective_scatter.py

"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = [(i+1)**2 for i in range(size)]
else:
    data = None
data = comm.scatter(data, root=0)
assert data == (rank+1)**2