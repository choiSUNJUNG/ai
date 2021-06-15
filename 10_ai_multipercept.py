import numpy as np
x = np.array([10, 20])
w1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
b1 = np.array([1, 2, 3])
w2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
b2 = np.array([0.1, 0.2])
def sigmoid(x) :
    return 1 / (1 + np.exp(-x))

a1 = np.dot(x, w1) + b1
z1 = sigmoid(a1)
a2 = np.dot(z1, w2) + b2
y = sigmoid(a2)
print(a1)
print(z1)
print(a2)
print(y)
