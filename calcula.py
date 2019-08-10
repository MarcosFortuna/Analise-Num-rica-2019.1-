#retorna o valor dos pontos nas funções dadas
def calcula(funcao, intervalo):
    
    q_funcao = len(funcao)
    n_x = len(funcao[0])
    q_intervalo = len(intervalo)
   
    vetorfinal = []
    
    for i in range(0,q_funcao):
        res = []
        for j in range(0,q_intervalo):
            soma = 0
            for k in range(0,n_x):
                 soma += funcao[i][k] *(intervalo[j]** k)    
            res.append(soma)
        vetorfinal.append(res)
    return vetorfinal             