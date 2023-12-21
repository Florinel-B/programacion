def verdad(x):  
    if x >= 0 : 
        result = True
    else : 
        result = False
    return result

num= float(input("dame uno numero :"))

if verdad(num):
    print(num, "es positivo" )
else : 
    print (num, "es negativo")