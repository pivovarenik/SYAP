import random

tupl = tuple((random.randint(-10, 10) for i in range(10)))
print(tupl)
Alex = -1
Alex = min(i for i in tupl if i % 2 == 0 and i >= 0)
if Alex == -1:
    print(tupl[0])
else:
    print(Alex)
