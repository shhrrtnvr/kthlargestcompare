from value_generators import *
from kthlargest import *
import time
import matplotlib.pyplot as plt

k, t = [], []

for i in range(10,50000, 50):
    k.append(i)
    data = generate_random(1000000)
    start = time.time()
    algorithm2(data,i)
    end = time.time()
    t.append(end-start)

fig, ax = plt.subplots()
ax.plot(k, t)
ax.set_xlabel('k --->')
ax.set_ylabel('time, t')
ax.set_title('Runtime for changing k in algorithm 2')
plt.show()
