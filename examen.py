#ejercicio 1
#plemente un programa que pida al usuario un número y diga si es o no feliz. Un
#número feliz es aquel que llega a 1 después de elevar al cuadrado y sumar cada una de sus cifras un
#cierto número de veces.
def descomposicion(num):
    lista=[]
    while num >= 1:
        a = num % 10
        num = num//10
        lista.append(a)
    return lista

def feliz(num):
    lista = []
    listanumeros = []
    numinicial=num
    while num > 1 :
        lista=descomposicion(num)
        num=0
        for i in range (len(lista)):
            num= num+lista[i]**2
        listanumeros.append(num)
        if listanumeros[-1]==numinicial:
            return False
    return True

numero=int((input("dame un numero y te digo si es feliz")))
esfeliz = feliz(numero)
print(esfeliz)