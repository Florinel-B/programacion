# ] Escribe un programa que reciba una frase por teclado y que construya e imprima por
# pantalla un diccionario en el que se guarde, para cada símbolo, una lista de las posiciones en la que aparece
# en la frase. Por ejemplo: si la frase fuera ‘hola hola!’, el diccionario que se imprimiría por pantalla es: {'h':
# [0, 5], 'o': [1, 6], 'l': [2, 7], 'a': [3, 8], ' ': [4], '!': [9]}
def contadorletras(frase):
    d={}
    a=[]
    for i in frase:
        if i in d:
            a.append(i)
            d[i]= d[i]+[len(a)]
        else :
            a.append(i)
            d[i]= [len(a)]
    return d

def imprimir(letra):
    for i in letra:
        if len(letra[i]) == 1:
            a = "vez"
        else:
            a = "veces"
        print("posicion de la letra",i , letra[i],"se repite",len(letra[i]), a)

frase=input('dame un frase para decirte cuantas veces aparece una letras en la misma')
frase=frase.lower()
Letras = contadorletras(frase)
imprimir(Letras)