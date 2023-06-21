# for num in range(1, 11, 1):
#     if num % 2 == 0:
#         print(num, 'es par')
#     else:
#         print(num, 'no es par')

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
par = []

for num in numeros:
    if (num % 2 == 0):
        par.append(num)
print(par)

# usando list comprehensions
impares = [num for num in numeros if num % 2 != 0]
print(impares)


paises = ['ECUADOR', 'Brasil', 'Honduras']
print(paises)
paises_minuscula = [pais.lower() for pais in paises]
print(paises_minuscula)

numeros = [num for num in range(50)]
print(numeros)
pares = [num for num in range(1, 101, 1) if num % 2 == 0]
print(pares)
