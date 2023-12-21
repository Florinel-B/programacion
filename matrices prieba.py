def cuadradomag(x):
    d1=0
    d2=0
    c1=0
    c2=0
    c3=0
    f1=0
    f2=0
    f3=0
    for i in range(len(x)):
        d1=d1+x[i][i]
    for j in range (len(x)):
        d2= d2+x[i][len(M)-1-j]
    if d1==d2:
        for columna in range(len(x)):
          c1=x[columna][0] + c1
          c2=x[columna][1] + c2
          c3=x[columna][2] + c3
    if c1==c2==c3 and d2==c1:
        for fila in range (len(x)):
            f1 = x[0][fila]+f1
            f2 = x[1][fila]+f2
            f3 = x[2][fila]+f3
    if f1==f2==f3 and f1==d2:
        return True
    else :
        return False
    
        
a=False
M= [[4,9,2],[3,5,7],[8,1,6]]
a=cuadradomag(M)
if a:
    print("Es un cuadrado magico")
else :
    print("no es cuadrado magico")
