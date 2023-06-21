"""
Crear un programa que ingrese un texto e indique 
si es palindromo que es cuando se lee igual al
derecho y al reves
ejemplo:
ana
oso
anita lava la tina
atar la rata
"""

texto = input("ingrese un texto: ").lower()
texto = texto.replace(' ', '')
inverso = texto[::-1]

if texto == inverso:
    print("La palabra o frase es palindromo")
else:
    print("La palabra no es palindroma")
