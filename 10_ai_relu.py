import numpy as np
import matplotlib.pyplot as plt

def relu(x):
    return np.maximum(0, x)

x = np.arange(-10, 10, 0.1)
print(x)
y = relu(x)
print(y)
plt.plot(x, y)
plt.title('ReLU Function')
plt.show()