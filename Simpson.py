
def Regra_simpson(n,a,b):
    h = (b-a)/n
    XI0 = a + b
    XI1 = 0
    XI2 = 0 

    for i in range(1,n-1):
        X = a + ( i * h )
        if i%2 == 0:
            XI2 += X
        else:
            XI1 += X
    
    XI = h*(XI0 + (2*XI2) + (4*XI1))/3
    
    return XI