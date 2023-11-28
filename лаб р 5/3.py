import numpy as np
import matplotlib.pyplot as plt

x = 3.567
a_values = (3.5,25.5,0.75)
arg_values = []
func_values = []
for a in a_values:
    cotanget = 1 / np.tan(x)
    func_value = np.power(cotanget, 3) + 2,24*a*x
    arg_values.append(x)
    func_values.append(func_value)


arg_values = np.array(arg_values)
func_values= np.array(func_values)
max_value = func_values.max()
min_value= func_values.min()
mean_value = func_values.mean()
num_elements = func_values.size

print("qantity:", num_elements)
print("mean:", mean_value)
print("Max:", max_value)
print("min:", min_value)

plt.plot(a_values,func_values,'o-', label = 'f(x)')
plt.axhline(mean_value,color='r', linestyle = '--', label='mean')

plt.xlabel('a')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.title('change f(x)')
plt.show()

