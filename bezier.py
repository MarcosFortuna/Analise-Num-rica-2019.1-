def Bezier(pontos,neg, pos):
     res = []
     i=0
     while i < len(pontos):
           a0 = pontos[i][0]
           b0 = pontos[i][1]
           a1 = 3*(pos[i][0] - pontos[i][0])
           b1 = 3*(pos[i][1] - pontos[i][1])
           a2 = 3*(pontos[i][0] + neg[i+1][0] - (2*pos[i][0]))
           b2 = 3*(pontos[i][1] + neg[i+1][1] - (2*pos[i][1]))
           a3 = pontos[i+1][0] - pontos[i][0] + (3*pos[i][0]) - (3*neg[i+1][0])
           b3 = pontos[i+1][1] - pontos[i][1] + (3*pos[i][1]) - (3*neg[i+1][1])
           i+=1
           a = [a0, a1, a2, a3]
           b = [b0, b1, b2, b3]   
           
           res.append([a,b])
     return res