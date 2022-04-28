#лаба 5 
import numpy as np
import matplotlib.pyplot as plt
fsize=12
plt.rcParams['font.family']='serif'
plt.rcParams['font.serif']='Times New Roman'
plt.rcParams['axes.titlesize']=fsize
plt.rcParams['axes.labelsize']=fsize
plt.rcParams['xtick.labelsize']=fsize
plt.rcParams['ytick.labelsize']=fsize
plt.rcParams['legend.fontsize']=fsize
x=np.linspace(0.0,10.0,50)
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(x,np.sin(x),'ko-',label='1')
ax.plot(x,np.cos(x),'ks-',color='orange',linewidth=1,markersize=3.0,label='2')
ax.plot(x,np.sin(x)**2.0,'k^-',color='magenta',linewidth=1,label='3')
ax.plot(x,(x)**0.15,'k--',linewidth=1,label=r'$x^2$')
ax.legend(loc='best')
ax.set_xlim(-1.0,11.0)
ax.set_ylim(-1.5,1.5)
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x)$')
ax.set_title('Мой первый рисунок')
ax.grid()
fig.savefig("fig1.png",orientation='landscape',dpi=300)
