a = int(input("dame un puto numero ya: "))

menor = a 

while a != 0 :
    a = int(input("otro numero, para acabar ponemos el 0 : "))
    if menor > a and a != 0 : 
        menor =  a 

if menor == 0 :
    print ("no se ha introducido ningun valor")
else :
    print ("el menor es", menor)

