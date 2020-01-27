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

procs = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    for proc in range(1, procs):
        comm.send(data, dest=proc, tag=proc)
    data = {'a': 8, 'b': 3.14}
else:
    data = comm.recv(source=0, tag=rank)

print(f"rank {rank}, data: {data}")

