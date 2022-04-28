from matplotlib import pyplot as plt
import numpy as np
data=np.loadtxt('lab6.txt')
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_xlim(-1.0,5.0)
ax.set_ylim(-0.5,1000)
ax.set_xlabel(r'Месяца')
ax.set_ylabel('Регионы России')
ax.set_title(u'Статистика привитых COVID-19 по данным МИНФИН за июнь 2021 по России')
ax.plot(data[:,0],data[:,1]/1000,'ko-',color='blue',label=r'$Ростовская область$')
ax.legend(loc='best')
fig.show()
