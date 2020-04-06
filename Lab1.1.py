# var 23  n=8 w=1500 N=1024
import random
import math
import matplotlib.pyplot as plt
import time

n = 8
w = 1500
N = 1024
t = [i for i in range(N)]

time_start = time.time()

result = []
for i in range(0, n):
    A = random.random()
    fi = random.random() * math.pi
    res = [A * math.sin(w * t[j] * j + fi) for j in range(N)]
    result.append(res)

x_t = []
for i in range(N):
    x = 0
    for j in range(n):
        x += result[j][i]
    x_t.append(x)

Mx = 0
for i in range(len(x_t)):
    Mx += x_t[i]
Mx = Mx/N


Dx = 0
for i in range(len(x_t)):
    Dx += (x_t[i] - Mx) ** 2

time_fin = time.time()

print("Mx:", Mx, "\nDx:", Dx, "\nЧас: ", time_fin-time_start)

plt.plot(t, x_t)
plt.grid(True)
plt.show()
