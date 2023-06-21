numero1 = input("Numero 1: ")
numero2 = input("Numero 2: ")
operacion = input("Operacion(suma,resta): ")

if (operacion == "suma"):
    resultado = int(numero1) + int(numero2)
elif (operacion == "resta"):
    resultado = int(numero1) - int(numero2)
else:
    print("No se encontró la operación solicitada")
    exit()

print("Resultado: " + str(resultado))
