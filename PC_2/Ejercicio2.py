'''Problema 2:
Escriba un programa en Python para construir el siguiente patrón.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
print("\t2. TRIANGULO")
numero=int(input("Digite un numero entero positivo: "))

# Parte superior
for i in range(1,numero+1):
    for j in range(i):
        print("*",end=" ")
    print()

# Parte inferior
for i in range(numero-1, 0, -1):
    for j in range(i):
        print("*",end=" ")
    print()
