import numpy as np
import matplotlib.pyplot as pp



x = np.array(((2,3), (3,5)))
y = np.array(((1,2), (5,-1)))

print (x)
print (y)

print (x + y)
print (np.dot(x, y))

z = np.zeros((2,2))
print (z)

sum = z + x

print (sum)

print("B\n", np.linspace(2, 3, num=5, retstep=True), "\n")

