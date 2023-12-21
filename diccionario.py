def contarletras(cadena):
    cadena = cadena.lower()
    d={}
    for caracter in cadena:
        if caracter not in ".,¿?!¡:;-/ ": 
            if caracter in d:
                d[caracter] += 1
            else:
               d[caracter] = 1 
    return d
def imprimir(ocurrencias):
    print("EL NUMERO DE OCURRENCIAS DE CADA LETRA EN ESTA FRASE ES: ")
    for k in ocurrencias.keys():
        print(k,":",ocurrencias[k])



print("este programa calcula el nunmero de ocurrencias de cada letra en una frase ")
frase= input("dame una frase cualquiera: ")
ocurrencias= contarletras(frase)
imprimir(ocurrencias)