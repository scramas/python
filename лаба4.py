#лаба 4 вариант 10
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0.0,10.0,30)
y=np.cos(x)-1
y1=np.abs(np.cos(x)-1)/(np.cos(x)-1)
plt.plot(x,y,y1)
plt.show()
