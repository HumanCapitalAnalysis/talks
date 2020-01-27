#!/usr/bin/env python
"""This script creates a set of slides."""
import subprocess as sp
import shutil
import os

if not os.path.exists("main.tex"):
    raise SystemExit("\n .. no source file available\n")


for task in ['pdflatex', 'bibtex', 'pdflatex', 'pdflatex']:
    sp.check_call(task + ' main', shell=True)

shutil.copy("main.pdf", "../slides.pdf")