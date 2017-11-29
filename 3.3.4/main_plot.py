import matplotlib.pyplot as plt
import math
import pandas as pd

a = pd.read_excel('./a.xls', header=None)
x = a[[0]] #B
y1 = a[[1]] #emf1
y2 = a[[2]] #emf2
y3 = a[[3]] #emf3
y4 = a[[4]] #emf4
y5 = a[[5]] #emf5
y6 = a[[6]] #emf6
plt.title('EMF=f(B)')
plt.plot(x, y1, 'bo', color='green', label = u'I=0.3', markersize=5, linestyle='-')
plt.plot(x, y2, 'bo', color='black', label = u'I=0.4', markersize=5, linestyle='-')
plt.plot(x, y3, 'bo', color='blue', label = u'I=0.5', markersize=5, linestyle='-')
plt.plot(x, y4, 'bo', color='red', label = u'I=0.7', markersize=5, linestyle='-')
plt.plot(x, y5, 'bo', color='grey', label = u'I=0.9', markersize=5, linestyle='-')
plt.plot(x, y6, 'bo', color='brown', label = u'I=1.0', markersize=5, linestyle='-')
plt.legend(loc='best')
plt.xlabel('B, Tl')
plt.ylabel('EMF, mV')
plt.grid(True)
plt.show()