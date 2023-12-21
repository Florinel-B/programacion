def cuadradro (N):
    cuadradro = [a**2 for a in N]
    return cuadradro

a = list(range(1,7))
b = cuadradro(a)
suma= sum(b)

v= []
c= list(range(1,7))
for i in range(1,len(c)+1):
    v= v + [(i**2)]
print(v)
print(b)