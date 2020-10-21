import random
import math
x, f, n, xf, xsf = [], [], 0, 0, 0
for i in range(50):
    x.append(random.randint(0, 500))
    f.append(random.randint(0, 500))
for i in f: n = n + i
for pl, i in enumerate(x): xf = xf + (i * f[pl])
mean = xf / n
for pl, i in enumerate(x): xsf = xsf + (i * i * f[pl])
sd = int(math.sqrt(((xsf) / n) - (mean * mean)))
x.sort()
