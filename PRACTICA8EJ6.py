 #Escribe un programa que pida al usuario dos palabras. El programa deberá generar e
#imprimir por pantalla un diccionario en el que, para cada letra de la primera palabra se almacene un valor de
#1 si la letra está también en la segunda palabra, o un 0 en caso contrario. Ejemplo: si la primera palabra es
#‘caro’ y la segunda es ‘otras’, el diccionario que se genera y que se imprime es: {'c': 0, 'a': 1, 'r': 1, 'o': 1}.
def buscarletras(palabra):
    d={}
    for i in range(len(palabra)):
        if i not in d:
            d[palabra[i]]=""
    return d
def comparacionletras(l1,l2):
    letras={}
    for elementos in (l1):
        if elementos not in (" "):
            if elementos in l2:
                letras[elementos]=1
            else :
                letras[elementos]=0
    return letras

def imprimir(letras):
    print("estas son las diferentes letras iguales de las palabras",letras)



palabra1=input("dame una palabra")
palabra2=input("dame otra palabra para ver que letas de la primera esta contiene")
letras1=buscarletras(palabra1)
letras2=buscarletras(palabra2)
letrascontenidas=comparacionletras(letras1,letras2)
a=imprimir(letrascontenidas)
