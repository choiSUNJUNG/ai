import numpy as np
import matplotlib.pyplot as plt

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x))

x = np.arange(-10, 10, 0.1)
print(x)
y = softmax(x)
print(y)
plt.plot(x, y)
plt.title('Softmax Function')
plt.show()