#!/usr/bin/env python
"""This module compiles the lecture notes."""
import subprocess
import argparse
import shutil
import glob
import os


for task in ['pdflatex', 'bibtex', 'pdflatex', 'pdflatex']:
    subprocess.check_call(task + ' main', shell=True)
