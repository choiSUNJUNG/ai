import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.arange(-10, 10, 0.1)
print(x)
y = sigmoid(x)
print(y)
plt.plot(x, y)
plt.title('Sigmoid Function')
plt.show()