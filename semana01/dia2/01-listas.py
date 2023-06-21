dias = ['lunes', 'martes', 'miercoles']
print(dias)
print(dias[0])
print(dias[0:2])

# agregar valor a una lista
dias.append('jueves')
print(dias)
dias.append(5)
print(dias)

# eliminar un valor de la lista
dias.pop(1)
del dias[1:3]
print(dias)

# actualizar un valor de la lista
dias[1] = "martes"
print(dias)

# recorre una lista
for contador in range(len(dias)):
    print(dias[contador])

for dia in dias:
    print(dia)
