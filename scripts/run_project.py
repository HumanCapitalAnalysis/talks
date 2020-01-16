#!/usr/bin/env python
"""This module creates the full project. This is useful for the continuous integration workflow."""
import subprocess
import glob
import os

DIRNAMES = ["overviews", "research-skills", "selected-topics", "seminal-papers"]

os.chdir(os.environ["PROJECT_ROOT"])

# We build all lectures and update the distribution.
for dirname in DIRNAMES:
    os.chdir(dirname)

    for subdir in glob.glob("*"):
        os.chdir(subdir)

        # run slides
        os.chdir("slides")
        subprocess.check_call(["run-slides"])
        os.chdir("../")

        # run notebook
        subprocess.check_call(["run-notebook"])

        os.chdir("../")

    os.chdir("../")

# run pytest
subprocess.check_call(["pytest"])
