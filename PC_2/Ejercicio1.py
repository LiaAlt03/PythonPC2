'''Problema 1:
Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
en el rango de 1500 y 2700 (ambos incluidos).'''

num_divisibles=[] #Lista vacia para almacenar datos

for numero in range(1500, 2701):
    if numero%7==0 and numero%5==0:
        num_divisibles.append(numero)

print("\t1. NUMEROS DIVISIBLES Y MÚLTIPLOS. \nLos números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(num_divisibles)