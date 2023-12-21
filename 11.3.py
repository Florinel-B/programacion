#aproximacion de pi
from math import sqrt
pito= 0 
i= 1
numero= int(input("dame un puto numero coño: "))
while i <= numero:
    pito = (24/(i**2))+ pito 
    i = i + 1 
pito= sqrt(pito)/2
print ("valor de pi aprox es :", pito, "en serie de", i)