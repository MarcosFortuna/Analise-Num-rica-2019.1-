a = b =[0]*4

for i in range(0,n-1):
    a[0] = x[i]
    b[0] = y[i]
    a[1] = 3*(x[i]-x[i])#primeiro x tem +
    b[1] = 3*(y[i] - y[i])#primeiro y tem +
    a[2] = 3*(x[i] + x[i+1] - (2*x[i]))#ultimo i tem o +
    b[2] = 3*(y[i] + y[i+1] - (2*y[i]))
    a[3] = x[i+1] - x[i] + 3*x[i] - 3*x[i+1] 
    b[3] = y[i+1] - y[i] + 3*y[i] - 3*y[i+1]  

    #deve retornar todos os as e bs de i
