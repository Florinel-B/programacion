#: Implementa un programa que pida al usuario un número N entre 1 y 10 y que genere e
#imprima por pantalla una matriz de tamaño NxN en el que los elementos se rellenan con números
#consecutivos, comenzando con el valor 1 en la primera posición de la matriz y siguiendo el orden de
#las filas. Ejemplo: Para un valor de la entrada de 4, la matriz generada debe ser la mostrada en al
def genmat(num):
    matriz=[]
    for i in range(num):
        matriz.append([0]*num)
    return matriz
def rellenarmat(matriz,num):
    j=0
    k=0
    for i in range (1,len(matriz)**2+1):
        matriz[j][k] = i
        if i%num==0:
            j+=1
            k=0
        else:
            k+=1
    return matriz


tamanomat=int(input("dame un numero para hacer la matriz de tamaño N "))
a=genmat(tamanomat)
matriz=rellenarmat(a,tamanomat)
print(matriz)