#!/usr/bin/python

# import re
# import json
import numpy as np
from matplotlib import pyplot as plt

INDEX_NAME = "index_file.csv"

f = open(INDEX_NAME, "r")

line = f.readline()

xs = []
ys = []

y_c = 0
while line:
    kv = line.split(",")
    x = long(kv[0].ljust(24, '0'))
    y = long(kv[1].replace("\n",""),16)
    
    # if y_c > y:
    #     print kv[1].replace("\n","")
    #     break

    xs.append(x)
    ys.append(y)
    line = f.readline()
    y_c = y
fig = plt.figure()

axes = fig.subplots(1)
ys.sort()

axes.plot(ys)

plt.show()