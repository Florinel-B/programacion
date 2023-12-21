def generarmatriz(grafo):
    maximo=0
    lista=[]
    for m in grafo:
        if m[0] not in lista:
            lista.append(m[0])
        if m[1] not in lista:
            lista.append(m[1])
    maximo=len(lista)

    matriz=[]
    for i in range(maximo):
        matriz.append([0]*maximo)
    return matriz
def obtenerposicion(matriz):
    pos=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            pos.append([i,j])
    return pos




def adyacente(grafo):
    matriz=generarmatriz(grafo)
    pos=obtenerposicion(matriz)
    for elementos in pos:
        if elementos in grafo:
            matriz[elementos[0]][elementos[1]]=1
            matriz[elementos[1]][elementos[0]] = 1
    return matriz
def imprimir(matriz):
    for i in range(len(matriz)):
        print(matriz[i])



conexionesgrafos=[[0,2],[1,2],[2,3]]
matrizadyancente=adyacente(conexionesgrafos)
imprimir(matrizadyancente)