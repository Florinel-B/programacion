#f = x**5 - 50*x**2 +2
a= int(input("numero"))
b= int(input("numero"))
c= 0
n= 100
ala = 0
for i in range (1,n):
    c= a+i*((b-a)/n)
    ala= ala+c
sumatorio  = c**5 - 50*c**2 +2
integral = ((b-a)/n)*(((a**5 - 50*a**2 +2)+(b**5 - 50*b**2 +2))/2)+sumatorio
print ("la integral es: ", integral)
