#!/usr/bin/env python
"""This module creates the full project. This is useful for the continuous integration workflow."""
import subprocess
import shutil
import glob
import os

DIRNAMES = ["overviews", "research-skills", "selected-topics", "seminal-papers"]

os.chdir(os.environ["PROJECT_ROOT"])

# We build all lectures and update the distribution.
for dirname in DIRNAMES:
    os.chdir(dirname)

    for subdir in glob.glob("*"):
        os.chdir(subdir)
        os.chdir("slides")

        for task in ['pdflatex', 'bibtex', 'pdflatex', 'pdflatex']:
            subprocess.check_call(task + ' main', shell=True)

        shutil.copy("main.pdf", "../slides.pdf")

        os.chdir("../../")
    os.chdir("../")
