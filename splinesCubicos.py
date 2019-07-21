import numpy  as np 
import matplotlib as plt
import scipy as sp 

h = [1]*num
l = []
mi = []
z = []
alpha = [0]*num
c = [0]*num
b = [0]*num
d = [0]*num
for i in range(0,num-1):
  h.append(x[i+1] - x[i])
for i in range(1,num-1):
  alpha[i] = ((3/h[i]) * (a[i+1]- a(i))) - (3/h[i-1] *(a[i])-a[i-1]) 

l.append(1)
mi.append(0)
z.append(0)

for i in range(1,num-1):
  aux = 2(x[i+1] - x[i-1]) - h[i-1]*mi[i-1]
  l.append(aux)
  mi.append(h[i]*l[i])
  aux = (alpha[i] - h[i-1] * z[i-1])/l[i]
  z.append(aux)

l.append(1)
z.append(0)

for j in range(num-1,0,-1):
  c[j] = z[j]-mi[j]*c[j+1]
  b[j] = ((a[j+1]-a[j])/h[j]) - (h[j]*(c[j+1] + 2*c[j]))/3
  d[j] = (c[j+1] - c[j])/3*h[j]

print(a,b,c,d)  
