a= float(input("valor a: "))
b= float(input("valor b: "))
c= float(input("valor c: "))
def solve_second_equation(a, b, c):
    if (-4*a*c)> b**2 or a != 0 :   
        return "No solutions"

    else:
        x = (-b+(b**2+(-4*a*c))**0.5)/(2*a)
        x_1 = (-b-(b**2+(-4*a*c))**0.5)/(2*a)
        return x, x_1
     
     

x = solve_second_equation(a, b, c)

print(f"The solution for 'x' is: {x}")
