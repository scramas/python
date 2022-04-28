#лаба 3
from  math import *
flag=0
print('Введите координаты X и Y для точки: ')
x=float(input('X= '))
y=float(input('Y= '))
if(x<-1) or (x>4):
    flag=0
if((x>=-1)and (x<1) and(y>=2*x+2)and (y<x**3-4*x**2+x+6)or (x>=1) and(x<=4)and (y>=x**3-4*x**2+x+6)and(y<=2*x+2)):
    flag=1
else:
    flag=0
print('Точка Х={0:6.2f} Y={1:6.2f}'.format(x,y),end=" ")
if flag:
    print('попадает',end=" ")
else:
    print('не попадает',end=" ")
    print('в область.')
#лаба 4
import matpplotlib.pyplot as plt
import numpy as np
x=np.linspace(0.0,10.0,30)
y=2+np.sin(x)**3
y1=np.abs(2+np/sin(x)**3)
plt.plot(x,y,y1)
plt.show()
#лаба 5
import numpy as np
import matpplotlib.pyplot as plt
fsize=12
plt.rcParams['axes.titlesize']=fsize
plt.rcParams['axes.labelsize']=fsize
plt.rcParams['xtick.labelsize']=fsize
plt.rcParams['ytick.labelsize']=fsize
plt.rcParams['legend.fontsize']=fsize
x=np.linspace(0.0,10.0,50)
fig=plt.figure()
ax.plot(x,np.sin(x),'ko-',label='1')
ax.plot(x,np.cos(x),'ks-',color='orange',linwidth=1,markersize=3.0,label='2')
ax.plot(x,np.sin(x)**2.0,'k^-',color='magenta',linwidth=1,label='3')
ax.plot(x,(x)**0.15,'k--',linwidth=1,label=r'$x^2$')
ax.legend(loc='best')
ax.set_xlim(-1.0,11.0)
ax.set_ylim(-1.5,1.5)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_title('Мой первый рисунок')
ax.grid()
fig.savefig("fig1.png",orientation='landscape',dpi=300)
#лаба 6
import numpy as np
import matpplotlib.pyplot as plt
data=np.loadtxt('data.txt')
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.set_xlim(-1.0,11.0)
ax.set_ylim(-1.1,1.1)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_title(u'Данные из файла')
ax.plot(data[:,0],data[:,1],'ko-',color='grey',label=r'$d_1$')
ax.plot(data[:,0],data[:,2],'gs-',label=r'$d_2$')
ax.legend(loc='best')
fig.show()