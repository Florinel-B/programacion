a= float(input("a: "))
b= float(input("b: "))
c= float(input("c: "))
d= float(input("d: "))
e= float(input("e: "))

c1= abs(b - a)
c2= abs(c - a)
c3= abs(d - a)
c4= abs(e - a)
peque = c1
nr = b 
if (c2 < peque):
    nr = c
if (c3 < peque):
    nr = d
if (c4 < peque):
    nr = e 

print ("el mas cercano es: ", nr)