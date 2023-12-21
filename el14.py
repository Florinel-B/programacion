ventas= float(input("las ventas anuales: "))
salario= 1500
salario_bruto = (salario+ventas*0.03)
salario_neto= (salario_bruto*0.78)
irpf= (salario_bruto-salario_neto)
print (salario_bruto, salario_neto, irpf)