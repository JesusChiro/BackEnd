"""
Ejercicio 2:
Ingrese un texto y un divisor y luego muestre el mismo
texto dividido por el divisor
ejemplo:
ingreso
Texto=abcdefg
divisor=2
resultado: 
ab
cd
ef
g
"""

texto = input("Ingrese Texto: ")
divisor = int(input("Ingrese divisor: "))

# resultado = len(texto)/divisor

# while (resultado > 0):
#     print(texto[:divisor])
#     texto = texto[divisor:]
#     resultado = resultado - 1

for contador in range(0, len(texto), divisor):
    # salida
    salida = texto[contador:contador+divisor]
    print(salida)
