def crearconjuntovacio (): 
    x= []
    return x
def anadirelem (lis, elem): 
    if elem not in lis:
        lis.append(elem)
    return lis

def eliminarelem (lis, elem): 
    encontrado = False
    i=0  
    while not encontrado and i<len(lis):
        if lis[i] == elem:
            del lis[i]
            encontrado= True
            i+=1
        else: 
            i+=1
    return lis
def union (lis, lis1):
    a = lis[:]
    for elem in lis1: 
        a = anadirelem(lis, elem)
    return a
def intersecion (lis, lis1):
    a = crearconjuntovacio()
    for elem in lis1: 
        a = eliminarelem(lis, elem)
    return a


lista = [1,2,3,4,5]
lista1 = [3,4,5,6,7,8]
#elemento = int(input("dame un elemento"))
#elementolist= eliminarelem(lista, elemento)
unionlistas= union(lista,lista1)
#print (elementolist)
print (unionlistas)