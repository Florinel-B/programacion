a = int(input("dame un puto numero ya: "))
i= 1
media = a 

while a != 0 :
    a = int(input("otro numero, para acabar ponemos el 0 : "))
    media = media + a 
    if a != 0 :
        i = i+1

media = media / i 
if media == 0 :
    print ("no se ha introducido ningun valor")
else :
    print ("el media es", media)