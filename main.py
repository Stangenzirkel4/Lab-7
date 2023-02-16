import random
import numpy as np
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Задание №1
# Стандартные списки
default_list_a = [random.randint(1, 99) for i in range(10^6)]
default_list_b = [random.randint(1, 99) for i in range(10^6)]

t1_start = time.perf_counter()
for i in range(len(default_list_a)):
    default_list_a[i] *= default_list_b[i]
all_time1 = time.perf_counter() - t1_start

# Массивы NumPy
numpy_list_a = np.random.randint(1, 100, 10^6)
numpy_list_b = np.random.randint(1, 100, 10^6)

t2_start = time.perf_counter()
numpy_list_a = np.multiply(numpy_list_a,numpy_list_b)
all_time2 = time.perf_counter() - t2_start

print("Время, затраченное на умножение стандартных списков: %s"%(all_time1))
print("Время, затраченное на умножение массивов NumPy: %s"%(all_time2))

# Задание №3

x = np.linspace(-np.pi*3, np.pi*3, 100)
y = x * np.cos(x)
z = np.sin(x)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='parametric curve')
plt.show()