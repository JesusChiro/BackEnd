contador = 1
while (contador <= 12):
    print(contador)
    contador += 1

resultado = 0
continuar = 'si'
while (continuar == 'si'):
    numero = int(input("ingrese un numero: "))
    resultado += numero
    continuar = input("¿Desea ingresar mas números?")

print(resultado)
