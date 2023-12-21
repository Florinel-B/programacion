# Implemente un programa en Python que utilice un diccionario para traducir a valores
#numéricos las palabras que hacen referencia a números de una frase introducida por teclado.
#Nota 1: Se puede suponer que la frase no contiene símbolos de puntuación y que hay exactamente un espacio
#en blanco entre palabras consecutivas.
#Nota 2: Es suficiente con traducir del ‘un’/‘uno’ al ‘nueve’
def cambio(frase):
    f={}
    d={}
    g={}
    numero=""
    palabra=""
    contador=0
    d['un']=1
    d['uno'] = 1
    d['dos'] = 2
    d['tres'] = 3
    d['cuatro'] = 4
    d['cinco'] = 5
    d['seis'] = 6
    d['siete'] = 7
    d['ocho'] = 8
    d['nueve'] = 9
    for i in frase:
        if i!= " ":
            palabra = palabra+i
        else:
            f[contador]=palabra
            contador+=1
            palabra=""
    for clave in f :
       if f[clave] in d:
         numero=d[f[clave]]
         g[clave]= numero
       else:
         g[clave] = f[clave]
    return g
def imprimir(frase):
    for k in frase.keys():
        print(frase[k], end=" ")
frase=input('dame una frase para cambiar de ordinales a cardinales')
frase = frase + " "
cardinales=cambio(frase)
imprimir(cardinales)