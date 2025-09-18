import numpy as np
 import matplotlib.pylab as plt
 def step_function(x):
 return np.array(x > 0, dtype=np.int64)
 x = np.arange(-5.0, 5.0, 0.1)
 y = step_function(x)
 plt.plot(x, y)
 plt.ylim(-0.1, 1.1)
 plt.show()
시그모이드 함수 구현
def sigmoid(x):
 return1 / (1 + np.exp(-x))
시그모이드 함수 그래프
x = np.arange(-5.0, 5.0, 0.1)
 y = sigmoid(x)
 plt.plot(x, y)
 plt.ylim(-0.1, 1.1)
 plt.show()
