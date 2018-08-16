#!/usr/bin/env python
"""This module creates the full project. This is useful for the continuous integration workflow."""
import subprocess
import os

# We build all lectures and update the distribution.
os.chdir('../seminal_papers')
subprocess.check_call(['./create_slides', '--update'])
os.chdir('../')




