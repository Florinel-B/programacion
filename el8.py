from math import sin ,pi 
a =float( input ("lado: ") )
b =float( input ("lado: ") )
c =float ( input ("angulo en grados: ") )
angulo =c*pi/180
area =0.5*a*b*sin (angulo)
print ("area es:", area, "angulo es:", angulo) 