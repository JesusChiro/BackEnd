# for contador in range (1):
#     print(contador)

# crear un programa que pida crear ingresar un numero
# y muestre la tabla de multiplicar de este del 1 al 12
tabla = input("Ingrese tabla a multiplicar: ")
for contador in range(1, 13, 1):
    resultado = contador*int(tabla)
    print(tabla, " x ", contador, " = ", resultado)
