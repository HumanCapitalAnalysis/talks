from mpi4py.futures import MPIPoolExecutor


from mpi4py import MPI


if __name__ == '__main__':

    print(MPI.COMM_WORLD.size)

    executor = MPIPoolExecutor(max_workers=3)
    task_partial = partial(task_mp_no_communication, num_outer, num_inner)

    
    
    for result in executor.map(pow, [2]*32, range(32)):
        print(result)