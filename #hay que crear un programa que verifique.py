#hay que crear un programa que verifique todos los numeros de una lista y elimine los numeros que nos divisibles por 2
#es decir impares
def pares(x):
    par= []
    i = 0
    while i < len(x):
        if x[i] % 2 == 0 : 
            par.append(x[i])
            i +=1
        else :
            i +=1
    return par 



lista = [1,2,3,4,5,6,6,7,8,9,10,11,12,13,14,15,16,100,55,64,121]
listapar = pares(lista)
print(listapar)