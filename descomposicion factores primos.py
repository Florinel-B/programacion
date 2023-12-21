def factores (x):
    descompocion = []
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            descompocion.append(divisor)
            x = x // divisor
        else : 
            divisor += 1 
    return descompocion
numero = int(input("dame un numero: "))
descompocion = factores(numero)
print (numero,"puede desconmponerse en estoss factores: ", descompocion)