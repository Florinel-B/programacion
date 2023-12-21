p = False
otra= 0
def Primo(x):
    if x > 2:
        for z in range (1, int(x/2)+1):
            if x % z == 0:  
                p = False
            else :
                p= True
    else :
        p = True
    return p
#sacar numeros primos y ver si son parientes o no

num = int(input('dame un numerito maximo para calcular parientes: '))
for i in range (1, num+1):
    if Primo(i) :
        otro =int(i+4)
        if Primo(otro):
            print ('son parinetes', i, otro)

