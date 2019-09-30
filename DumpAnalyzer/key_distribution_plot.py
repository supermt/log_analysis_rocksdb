#!/usr/bin/python

# import re
# import json
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict


INDEX_NAME = "entry.csv"

f = open(INDEX_NAME, "r")

lines = f.readlines()

xs = []

for line in lines:
    line = line.replace("\n","")
    x = long(line.ljust(48,'0'))
    xs.append(x)

plt.plot(xs)

plt.show()