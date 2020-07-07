from value_generators import *
from kthlargest import *
import time
import random
import statistics
import matplotlib.pyplot as plt

n, t1, t2 = [], [], []

for i in range(10000, 1000000,5000):
    n.append(i)
    data = generate_sorted(i)
    k = 10

    start = time.time()
    val1 = algorithm1(data, k)
    end = time.time()
    t1.append(end-start)

    start = time.time()
    val2 = algorithm2(data, k)
    end = time.time()
    t2.append(end-start)
m1, m2 = statistics.median(t1), statistics.median(t2)
print((m1-m2)/m2 *100)
    
fig, ax = plt.subplots()
ax.plot(n, t1, label = 'algorithm 1')
ax.plot(n, t2, label = 'algorithm 2')
ax.set_xlabel('Array size, n')
ax.set_ylabel('Time, t')
ax.set_title('Random generated input, k = %d' %k)
ax.legend()
plt.show()

    


