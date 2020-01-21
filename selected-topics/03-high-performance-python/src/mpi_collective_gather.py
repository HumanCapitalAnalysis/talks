"""" Example script MPI collective communication.

    This module illustrates the MPI gathering of a list. This is the inverse of gather().

    References
    ----------

    [1] https://mpi4py.readthedocs.io

    Examples
    --------

    mpiexec -n 5 python mpi_collective_gather.py

"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

data = (rank + 1) ** 2
data = comm.gather(data, root=0)
if rank == 0:
    for i in range(size):
        assert data[i] == (i + 1) ** 2
else:
    assert data is None
