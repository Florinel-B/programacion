def aclararPantalla(N):
    for i in range(N):
        print()
def inicializarPalabraObjetivo(N):
    cadena = "*"*N
    return cadena

def actualizar (palabraMisteriosa, letra, PalabraObjetivo, intentos):
    if letra in palabraMisteriosa:
        for i in range (len(palabraMisteriosa)):
            if letra == palabraMisteriosa[i]:
                PalabraObjetivo = PalabraObjetivo[:i] + letra + PalabraObjetivo[i+1:]
    else  :
        intentos -= 1
    return PalabraObjetivo, intentos



print("este juego va de jugar al ahorcado")
palabraMisteriosa = input("dame la palabraque tiene que adivinar")
aclararPantalla(20)
PalabraObjetivo = inicializarPalabraObjetivo(len(palabraMisteriosa))
intentos = len(palabraMisteriosa)
while intentos > 0 and PalabraObjetivo != palabraMisteriosa:
    print("intentos", intentos)
    print("la palabra a adivinar es", PalabraObjetivo)
    letra = input("dame una letra")
    PalabraObjetivo, intentos = actualizar(palabraMisteriosa, letra, PalabraObjetivo, intentos)
if intentos > 0 :
    print("felicidades no te ahorcaste", palabraMisteriosa)
else:
    print("felicidades lo ahoracaste", palabraMisteriosa)
