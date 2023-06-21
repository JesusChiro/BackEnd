# Entrada
lado = int(input("Ingrese lado del cuadrado: "))

# Proceso
for contador in range(lado):
    # Salida
    if (contador == 0 or contador == (lado-1)):
        print('* ' * lado)
    else:
        print('*' + '  ' * (lado - 2) + ' *')
