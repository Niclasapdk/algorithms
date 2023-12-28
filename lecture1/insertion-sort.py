import time
import matplotlib.pyplot as plt
import random

def insertionsort(ar):
    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > key:
            ar[j+1] = ar[j]
            j -= 1
        ar[j+1] = key
    return ar

def time_execution(ar):
    t0 = time.time()
    insertionsort(ar)
    t1 = time.time()
    return t1-t0

SIZE_MAX = 200
inputs = [[[random.randint(0, 30) for _ in range(i)] for _ in range(5)] for i in range(SIZE_MAX)]
ns = [i for i in range(SIZE_MAX)]
exec_times = [[time_execution(inputs[size][idx]) for idx in range(5)] for size in range(SIZE_MAX)]
plt.plot(ns, exec_times)
plt.show()