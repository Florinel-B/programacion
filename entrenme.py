def inicializar(num):
    m=[]
    for i in range(num):
        m.append([0]*num)
    return m
def floid(matriz,max):
    columna=0
    fila=len(matriz)-1
    long=1


def imprimir(matriz):
    N = len(matriz)
    M = len(matriz[0])
    for f in range(N):
        for c in range(M):
            print(matriz[f][c], end="")
        print()





tamanomat=5
maximonum=int(input("dame el tamaño de la matriz"))
matriz=inicializar(tamanomat)
triangulo=floid(matriz,maximonum)
imprimir(triangulo)