a= int(input("dime numero: "))
b= int(input("dime numero: "))
menor = b

if a > b :
    menor = a
mcd = 1

for i in range (2,menor):
    if ((a % i) == 0) and ((b % i) == 0) :
       mcd = i 
       print (i)
print("mcd es:", mcd)
