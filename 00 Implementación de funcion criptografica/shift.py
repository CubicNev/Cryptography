# c = ap + b mod n

lenguaje = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alfa = 0
beta = 0
n = 1

def elegir():
    while True:
        try:
            opc = int(input(" 1: Caracter, 2: Ver todo, Opcion: "))
        except:
            continue

        if opc == 1:
            car = input(" Ingresa el caracter: ")
            cifrar(car)
        elif opc == 2:
            lengCifrado()
        else:
            break

def cifrar(caracter):
    indice = lenguaje.index(caracter.upper())
    opPrim = alfa*indice + beta
    cifrado = opPrim % n
    return cifrado
    #print(" El indice es " + str(cifrado) + " = " + lenguaje[cifrado])

def lengCifrado():
    i=0
    for car in lenguaje:
        cifrado = cifrar(car)
        print(" " + str(i) + " " + car + " - " + str(cifrado) + " " + lenguaje[cifrado])

alfa = int(input(" Ingresa alfa: "))
beta = int(input(" Ingresa beta: "))
n = len(lenguaje)
print(" El tamaño del lenguaje es: " + str(n))

elegir()
