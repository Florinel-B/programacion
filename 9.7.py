def crea_matriz(n):
    matriz=[]
    for i in range(n):
        a=[0]*n
        matriz.append(a)
    return matriz
def rellenar_matriz(b,a):
    c=a**2
    for i in range (len(b)): #si se quiere ir al reves en la lista/matriz tenemos que darle los parametros (tamaño-1,-1,-1)
        for j in range (len(b[0])):
            b[i][j]=c
            c -= 1
            
    return b
def imprimirfila(b):
    for fila in range (len(b)):
        for col in range (len(b[0])):
            print(b[fila][col], end="\t")
        print()


a=int(input("dame un numero del 1 al 10 para crear una matriz cuiadrada de ese tamaño: "))
b=crea_matriz(a)
c=(rellenar_matriz(b,a))
imprimirfila(c)