a=[[3,6,2],[8,5,4],[1,9,7]]  
v= (a[0][0]* a[1][1]* a[2][2])+(a[0][1]*a[1][2]*a[2][0])+(a[1][0]*a[2][1]*a[0][2])
b= -(a[0][2]* a[1][1]* a[2][0])-(a[0][0]*a[1][2]*a[2][1])-(a[1][0]*a[0][1]*a[2][2])
c= v+b
print(c)