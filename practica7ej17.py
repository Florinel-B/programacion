#Se desea “dar la vuelta” a los valores de una matriz de dimensión n×n . ”Dar
#la vuelta” significa que la matriz transformada se lea de derecha a izquierda y de abajo hacia arriba igual que
#la matriz inicial leída de izquierda a derecha y de arriba abajo. A continuación se da un ejemplo de lo que
#significa “dar la vuelta” a una matriz 3×3 :
def inicializarmatriz(orden):
    matriz=[]
    for i in range(orden):
        matriz.append([0]*orden)
    return matriz


def invertir(matriz):
    matrizini=[]
    medida=len(matriz)-1
    while medida >= 0:
        matrizini.append(matriz[medida][::-1])
        medida = medida - 1

    return matrizini



matriz=[[1,2,3],[4,5,6],[7,8,9]]
matrizinvertida=invertir(matriz)
print(matrizinvertida)