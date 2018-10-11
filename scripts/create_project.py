#!/usr/bin/env python
"""This module creates the full project. This is useful for the continuous integration workflow."""
import subprocess
import os

# We build all lectures and update the distribution.
for dirname in ['research_skills', 'seminal_papers', 'overviews']:
    os.chdir(dirname)
    subprocess.check_call(['./create', '--update'])
    os.chdir('../')
