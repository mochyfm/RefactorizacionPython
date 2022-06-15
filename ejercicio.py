#!/usr/bin/env python3

# Crea una función "calcularMaxMix" que recibe una lista con valores numéricos y
# devuelve el valor máximo y el mínimo. Crea un programa que pida números por
# teclado y muestra el máximo y el mínimo, utilizando la función anterior.
# A continuación pide un número (entre 1 y 100) y el programa debe decir si está en la lista.

import random

def isNumberOnList(num):
    try:
        num = int(num)
    except ValueError:
        return False;
    if num in numeros:
        return True;
    else:
        return False;

def askForNumber():
    try:
        numero = int(input("Dime un número del 1 al 100: "))
    except ValueError:
        numero = -1
    return numero;


def CalcularMaxMin(lista):
    return (max(lista), min(lista))

numeros = []
# Inicializo la lista con valores aleatorios
for i in range(10):
    numeros.append(random.randint(1,100))
vmax, vmin = CalcularMaxMin(numeros)
print("El valor máximo es ", vmax)
print("El valor mínimo es ", vmin)

userNumber = askForNumber()
onList = isNumberOnList(userNumber);

while userNumber < vmin or userNumber > vmax or onList == False:
    if (userNumber < vmin or userNumber > vmax):
        print(f'El número de estar entre {vmax} y {vmin}')
    else:
        print('El número no está en la lista')
    userNumber = askForNumber()
    onList = isNumberOnList(userNumber)