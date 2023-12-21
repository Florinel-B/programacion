print("este programa te dice los años bisiestos")
años= int(input("año es: "))
if años > 1582:
    if años%4 == 0 :
        if años%100 == 0 and años%400 != 0 :
            print("no es bisiesto")
        else :
            print ("es bisiesto")
    else:
        print("no es bisiesto")
        
else:
    print("no es bisiestos")