import numpy as np
import matplotlib.pyplot as plt

def stepfunc(x):
    return np.where(x <= 0, 0, 1)

x = np.arange(-10, 10, 0.1)
print(x)
y = stepfunc(x)
print(y)
plt.plot(x, y)
plt.title('Step Function')
plt.show()