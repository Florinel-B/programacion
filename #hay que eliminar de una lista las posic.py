#hay que eliminar de una lista las posiciones pared de la misma es decir hay que recorrer la lista entera 
#coger los impares o eliminar los pares y ponerlos en una nueva lista
def eliminarpospar (x):
    lista=[]
    for i in range(0,len(x),2):
        lista.append(x[i])
    return lista







lista = [1, 2, 4, 5,6, 7, 7,9, 7, 4,234,532,3,243,54346,34,34,6]
imparlista = eliminarpospar(lista)
print(imparlista)