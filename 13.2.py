print ("calcular 1")
print ("calcular 2")
print ("calcular 3")
opcion= input("opciones: ")
if opcion.lower()== "a" :
    r= float(input("resistencia: "))
    v = float(input("voltaje: "))
    i = v/r
    print ("la intensidad es : ", i )
elif  opcion.lower()== "b" :
    i= float(input("intesidad: "))
    v = float(input("voltaje: "))
    r = v/i
    print ("la intensidad es : ", r )
elif  opcion.lower()== "c" :
    r= float(input("resistencia: "))
    i = float(input("intesidad: "))
    v = i*r
    print ("la intensidad es : ", v )
else :
    print("opcion no valida")