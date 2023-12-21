numero= int(input("numerito: "))
numero2 = int(input("numerito 2: "))
amigos= False
divisores1 = 0
divisores2= 0 
i= 1
while numero/2 >= i :
    if (numero % i == 0):
        divisores1 = i + divisores1
    breakpoint()
    i += 1 

i= 1
while numero2/2 >= i :
    if (numero2 % i == 0):
        divisores2 = i + divisores2
    i += 1 

print("divisor1", divisores1,"divisor2", divisores2)
if divisores1 == numero2 and divisores2 == numero:  
    print("son amigos",)
else :
    print("no lo son ")