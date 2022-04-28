#лаба 2 вариант 10
import math
def ctg(x):
    return math.cos(x)/math.sin(x)
a=float(input('Введите a '))
z1=(math.sin(math.pi/2+3*a))/(1-math.sin(3*a-math.pi))
z2=ctg((5/4)*math.pi+(3/2)*a)
print()
print('Формула z1',z1)
print()
print('Формула z2',z2)
