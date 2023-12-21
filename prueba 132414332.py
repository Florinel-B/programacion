n = 100
i= 1 
def sumatorio(n):
  """Calcula el sumatorio de los primeros n números naturales."""
  suma = 0
  for i in range(1, n + 1):
    suma += i
  return suma