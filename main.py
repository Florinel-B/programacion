from math import sqrt

a= float(input("lado 1 :"))
b= float(input("lado 2 :"))
c= float(input("lado 3 :"))
s= (a+b+c)/2
area = sqrt (( s*(s-a)*(s-b)*(s-c) ))
print("el area es :", area)

