#!/usr/bin/env python3
# Ejercicio 4. Crear un programa para hacer la comparación entre dos números enteros

x = int(input("Ingrese el número x: "))
y = int(input("Ingrese el número y: "))

if x == y:
    print("Los números " + str(x) + " y " + str(y) + " son iguales")
elif x != y:
    print("Los números " + str(x) + " y " + str(y) + " no son iguales")