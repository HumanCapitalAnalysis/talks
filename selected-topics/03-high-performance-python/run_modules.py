"""" Run MPI illustrations.

    This script runs all MPI illustrations to ensure a proper functioning throughout.

    Examples
    --------

    python run.py

"""
import subprocess as sp
import glob
import sys
import os

if __name__ == '__main__':

    os.chdir("src")
    for fname in glob.glob("mpi_*.py"):
        sp.check_call(f"mpiexec -n 5 {sys.executable} {fname} > /dev/null", shell=True)

