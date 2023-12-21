mes = int(input("mes :"))
dia = int(input("dia :"))
if mes < 1 or mes > 12 :
     print("mal")
else :
    dia_max= 30
    if mes <= 7 and mes%2 != 0 :  
        dia_max = 31
        if mes == 2 and bisiesto :
            dia_max = 29
        else:
            dia_max = 28
    if mes >= 8 and mes%2 == 0 :
        dia_max = 31
