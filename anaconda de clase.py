def inicializar(num):
    m=[]
    for i in range(num):
        m.append([0]*num)
    return m
def rellenar(matriz):
    N=len(matriz)
    M=len(matriz[0])
    for f in range (N):
        for c in range(M):
            matriz[f][c]= min(f,c,N-1-f,M-1-c)
    return matriz

def imprimir(matriz):
    N = len(matriz)
    M = len(matriz[0])
    for f in range(N):
        for c in range(M):
            print(matriz[f][c], end="")
        print()


numero=int(input("dame el tamañp matriz"))
matriz = inicializar(numero)
cosita=rellenar(matriz)
imprimir(matriz)