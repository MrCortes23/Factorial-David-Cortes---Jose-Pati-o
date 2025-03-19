"""
Calculador de Factorial
Autor: David Cortes - Jose Patiño
Licencia: MIT - Este código es libre y puede ser modificado y distribuido

"""

num = int(input("Ingrese un número positivo: "))

if num < 0:
    print("El número debe ser positivo.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es: {factorial}")
