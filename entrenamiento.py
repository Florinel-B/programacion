def repes (frase):
    d={}
    for i in range(len(frase)):
        if frase[i] not in(d):
            d[frase[i]]=[i, i]
        else:
            d[frase[i]][1]= i
    return d

def imprimir(letras, frase):
    for i in range (len(frase)):
        print("aparece por primera vez en",letras[frase[i]][0], "y por ultima vez en", letras[frase[i]][1])

frase=input("dame un frase y te digo la primera y ultima posicion: ")
letras=repes(frase)
imprimir(letras, frase)