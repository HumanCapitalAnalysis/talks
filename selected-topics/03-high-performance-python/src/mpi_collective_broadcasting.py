"""" Example script MPI collective communication.

    This module illustrates the MPI broadcasting of a dictionary. The dictionary is send to all
    other processes in the communicator.

    References
    ----------

    [1] https://mpi4py.readthedocs.io

    Examples
    --------

    mpiexec -n 5 python mpi_collective_broadcasting.py

"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'key1': [7, 2.72, 2+3j],
            'key2': ('abc', 'xyz')}
else:
    data = None
data = comm.bcast(data, root=0)
