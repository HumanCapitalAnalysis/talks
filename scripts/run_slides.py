#!/usr/bin/env python
"""This script creates a set of slides."""
import subprocess as sp
import shutil


for task in ['pdflatex', 'bibtex', 'pdflatex', 'pdflatex']:
    sp.check_call(task + ' main', shell=True)

shutil.copy("main.pdf", "../slides.pdf")