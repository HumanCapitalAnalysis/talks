import subprocess as sp
from ishigami import *
from auxiliary import *

sp.check_call("py.test", shell=True)
sp.check_call("jupyter nbconvert --execute Untitled.ipynb", shell=True)

stat = get_ishigami_total_effects()
print(stat)

num_outer = 1000
num_inner = 1000

stat = list()
for which in range(3):
    stat.append(get_total_effect(num_outer, num_inner, which))
print(stat)