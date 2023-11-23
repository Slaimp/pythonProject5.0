import numpy as np

a = 1.21
b = 0.371

w = np.tan(np.power(a + b, 2)) - np.cbrt(a + 1.5) + a * np.power(a, 5) - b / np.log(np.power(a, 2))

print(w)