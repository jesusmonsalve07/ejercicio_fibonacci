#!/usr/bin/env python3
# Determinar e imprimir si una palabra dada es palíndromo o no


def palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False


# O tambien se puede revertir la lista y comparar la lista revertida con la normal
# for i in reversed(palabra):
#    print(i)

palabra = str(input("Ingrese una palabra que desee: "))

if palindromo(palabra) == True:
    print("SÍ es un palíndromo")
else:
    print("NO es un palíndromo")
