'''Problema 7:
Escriba una función de Python que tome un número como parámetro y verifique que el número sea
primo o no.'''
import math #Agregamos el modulo math
def es_primo(numero):
    if numero==1: #El 1 no es primo
        return False
    if numero==2 or numero==3: #Los números 2 y 3 son primos
        return True

    raiz_cuadrada=math.isqrt(numero) #Aplicamos la funcion del modulo math para calcular la raiz cuadrada
    for i in range(2, raiz_cuadrada+1):
        if numero%i==0:
            return False
    return True

print("\t7. EVALUAR NUMEROS PRIMOS.")
numero=int(input("Ingrese un número: "))
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
