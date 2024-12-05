import matplotlib.pyplot as plt
import numpy as np


x1 = np.arange(-5, 5.1, 0.1)
y1 = x1 * x1

x2 = np.arange(-2, 2.1, 0.1)
y2 = x2 * x2 + 2

rng = np.random.default_rng()
y3 = rng.uniform(-25, -1, 100)
x3 = np.linspace(-5, 5, 100)

fig, ax = plt.subplots()
ax.plot(x1, y1, label='Функция 1')
ax.plot(x2, y2, label='Функция 2')
ax.plot(x3, y3, label='Функция 3')
ax.set_title('Графики функций')
ax.set_xlabel('Ось Х')
ax.set_ylabel('Ось У')
ax.grid(True)
ax.legend()

plt.show()
