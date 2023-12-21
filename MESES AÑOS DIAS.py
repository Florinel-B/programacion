años = int(input("año :"))
mes = int(input("mes :"))
dia = int(input("dia :"))
bisiesto = False
dia_max= 30

if años > 1582:
    if años%4 == 0 :
        if años%100 == 0 and años%400 != 0 :
            print("no es bisiesto")
        else :
            print ("es bisiesto")
            bisiesto = True
    else:
        print("no es bisiesto")
        
else:
    print("no es bisiestos")




if mes < 1 or mes > 12 :
     print("mes incorrecto")
else :
    if mes <= 7 and mes%2 != 0 :  
        dia_max = 31
    elif mes>= 8 and mes%2 == 0 :
        dia_max = 31
if mes == 2 and bisiesto == True :
        dia_max = 29
elif mes == 2 and bisiesto == False :
        dia_max = 28
breakpoint()
if dia < 1 or dia > dia_max :
    print("dia esta mal")
else :
    print("dia esta bien")