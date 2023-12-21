def posicion(frase):
    d={}
    lista=[]

    for caracter in frase:
        if caracter in d:
            lista.append(caracter)
            d[caracter] = [1,len(lista)]
        else:
            d[caracter] = [len(lista),len(lista)]
            lista.append(caracter)
    return (d,lista)

entrada= input("dame un frase random: ")
firstandlast= posicion(entrada)
print(firstandlast)
