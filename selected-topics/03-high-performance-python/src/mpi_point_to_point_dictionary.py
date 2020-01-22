"""" Example script MPI point-to-point communication.

    This module illustrates the MPI point-to-point communication for a dictionary.

    References
    ----------

    [1] https://mpi4py.readthedocs.io

    Examples
    --------

    mpiexec -n 2 python mpi_point_to_point_dictionary.py

"""
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    comm.send(data, dest=1, tag=11)
    data = {'a': 8, 'b': 3.14}

elif rank == 1:
    data = comm.recv(source=0, tag=11)

print(f"rank {rank}, data: {data}")

