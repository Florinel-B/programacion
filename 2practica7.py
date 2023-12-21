def encontrarmax(n,x):
    j= 0
    for i in range (len(n)):
        j= 0
        while j < 5: 
            if n[i][j] > x:
                x = n[i][j]
                j+=1
            else :
                j+=1
    return x
def posicionmaximo(lis1, maximo):
    maxfila = 0
    maxcolumna= 0 
    for i in range (len(lis1)):
        j= 0
        while j < 5: 
            if lis1[i][j] > maximo:
                maximo = lis1[i][j]
                j+=1
                maxfila = i
                maxcolumna = j
            else :
                j+=1
    return maxcolumna, maxfila
#tambien se puede utilizar for columna in range (len(n)) y luego para las filas se puede utilizar un for filas in range (len(m(n)))
def repeticion(lis1,maximo):
    maxfila = 0
    maxcolumna= 0 
    lis2= []
    for i in range (len(lis1)):
        j= 0
        while j < 5: 
            if lis1[i][j] > maximo:
                lis2= []
                maximo = lis1[i][j]
                j+=1
                maxfila = i
                maxcolumna = j
                lis2.append([maxfila,maxcolumna])
            else :
                j+=1
            if maximo == lis1[i][j]:
                lis2.append([maxfila,maxcolumna])
    return lis2


maximo=0
liston= [[1,2,46,34,3],[2,5,12,533,12],[12,32,4342,231,4],[123,1543,431,4342,213]]
f = encontrarmax (liston,maximo)
posicion= posicionmaximo(liston,maximo)
m= repeticion(liston,maximo)
print (f)
print (posicion)
print (m)