# Rotina sucessores para Grade de Ocupação
def sucessores(atual,mapa,dim_x,dim_y):
    f = []
    x = atual.xa
    y = atual.ya
    
    if x+1!=dim_x:
        if mapa[x+1][y]==1:
            linha = []
            linha.append(x+1)
            linha.append(y)
            f.append(linha)
    
    if y+1!=dim_y:
        if mapa[x][y+1]==1:
            linha = []
            linha.append(x)
            linha.append(y+1)
            f.append(linha)
    
    if x-1>=0:
        if mapa[x-1][y]==1:
            linha = []
            linha.append(x-1)
            linha.append(y)
            f.append(linha)
    
    if y-1>=0:
        if mapa[x][y-1]==1:
            linha = []
            linha.append(x)
            linha.append(y-1)
            f.append(linha)
    return f

# Carrega Grafo para Lista de Adjacência e Lista de Nós
def Gera_Problema(arquivo):
    f = open(arquivo,"r")
    
    i=0
    nos = []
    grafo = []
    for str1 in f:
        str1 = str1.strip("\n")
        str1 = str1.split(",")
        if i==0:
            nos = str1
        else:
            grafo.append(str1)
        i += 1       
    
    return nos, grafo