import numpy as np

n =2
x = np.column_stack((np.ones(12), np.arange(n, n+12), np.random.randint(60,83, 12)))

y = np.random.uniform(13.5, 18.6, 12)

a = np.linalg.inv(x.T @ x) @ x.T @ y

y_predicted = x @ a

print("mark ccof", a)
print("primary", y)
print("acstrasens", y_predicted)

