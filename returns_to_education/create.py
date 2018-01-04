#!/usr/bin/env python
"""This module compiles the notes with the figures."""
import subprocess
import shutil
import os

if __name__ == '__main__':

    os.chdir('slides')
    subprocess.check_call('./create.py', shell=True)
    os.chdir('../')

    shutil.copy('slides/main.pdf', 'slides.pdf')
    subprocess.check_call('git clean -d -f', shell=True)
