import numpy as np
import math

a = 5.8
x = 0.24

z = np.arctan(np.power(x, 2)) - np.sqrt(x + np.power(1.43, 3)) + np.power(np.cos(math.pi/2*a), 3) / abs(x-np.power(a,0.2))

print(z)