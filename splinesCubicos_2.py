def spline_Fixado(x,y,fpo,fpn):
    num = len(y)-1
    #fpo =  derivada de y[0]
    #fpn = derivada y[num]
    h = [0]*(num)
    alfa = [0]*(num)
    l = [0]*num
    mi = [0]*num
    z = [0]*num
    c = [0]*num
    b = [0]*num
    d = [0]*num
    
    for i in range(0,num-1):
        h[i] = x[i+1] - x[i]
    #faça
    #alfa[0] = (3*(y[1] - y[0]))/(h[0] - (3*fpo))
    #alfa[0] = 3*fpn - (3*(y[num] - y[num-1]))/h[num-1]
    
    #passo 3
    for i in range(1,num-1):
        alfa[i] = ((3/h[i])*(y[i+1] - y[i])) - ((3/h[i-1])*(y[i] - y[i-1]))
    
    #passo 4
    l[0] = 2*h[0]
    mi[0] = 0.5
    z[0] = alfa[0]/l[0]
    
    #passo5
    for i in range(1,num-1):
        
        l[i] = 2*(x[i+1] - x[i-1]) - (h[i-1]*mi[i-1])
        mi[i] = h[i]/l[i]
        z[i] = ( alfa[i] - (h[i-1]*z[i-1]) ) / l[i]
    
    #passo 6    
    l[num] = h[num-1]*(2-mi[n-1])
    z[num] = (alfa[num] - (h[num-1]*z[num-1]))/l[num]
    c[num] = z[num]
    
    #passo 7
    for j in range(num-1,0):
        c[j] = z[j] -( mi[j] * c[j+1])
        b[j] = (y[j+1]-y[j])/(h[j] - (h[j]*(c[j+1] + 2*c[j]))/3)
        d[j] = (c[j+1] - c[j])/(3*h[j])
        
