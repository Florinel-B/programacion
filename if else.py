a= float(input("valor: "))
b= float(input("valor: "))

def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        else:
            return "No solutions"
    else:
        x = -b / a
        return x

x = solve_linear_equation(a, b)
print(f"The solution for 'x' is: {x}")
