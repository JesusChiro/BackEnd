capitales = {
    'Perú': 'Lima',
    'Ecuador': 'Quito',
    'Chile': 'Santiago',
    'Uruguay': 'Montevideo'
}
print(capitales)

nuevaCapital = {
    'Brasil': 'Brasilia'
}
capitales.update(nuevaCapital)
print(capitales)

"""
pais = input('Ingrese el país: ')
capital = capitales.get(pais)
print(' capital de '+pais + ' es '+capital)
"""

capitales.update({'Chile': 'Arica'})
print(capitales)

# eliminar valores
capitales.pop('Chile')
print(capitales)
"""
pais = input('Ingrese pais a eliminar:')
capitalEliminada = capitales.pop(pais, 'no existe')
print('capital eliminada ' + capitalEliminada)
print(capitales)
"""

# recorrer diccionarios
# recorrer claves
print('*'*20)
print("paises: ")
print('*'*20)
for clave in capitales.keys():
    print(clave)

# recorrer los valores
print('*'*20)
print("capitales: ")
print('*'*20)
for valor in capitales.values():
    print(valor)
print('*'*20)

for clave, valor in capitales.items():
    print('La capital de ' + clave + ' es ' + valor)
