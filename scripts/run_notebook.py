#!/usr/bin/env python
"""This module executes all notebooks. It serves the main purpose to ensure that all can be
executed and work proper independently."""
import subprocess as sp
import glob
import os

def run_notebook(notebook):
    cmd = ' jupyter nbconvert --execute %s --ExecutePreprocessor.timeout=-1 --to notebook' %notebook
    sp.check_call(cmd, shell=True)


if __name__ == '__main__':

    for fname in glob.glob("*.ipynb"):
        run_notebook(fname)
