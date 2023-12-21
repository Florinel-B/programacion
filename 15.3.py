i = int(input("dios")) 
counter = 1
numero = 1 
while counter <= i:
    stars = 1
    while stars <= counter:
        print(numero,"" , end="")
        stars += 1
        numero += 1 
    print()
    
    counter += 1
    
        