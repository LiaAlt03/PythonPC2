'''Problema 8:
Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
función acepta el número como argumento.
'''
def factorial(numero):
    if numero==0: #caso especial de factorial de 0
        return 1
    resultado=1
    for i in range(1,numero+1):
        resultado*=i
    return resultado

print("\t8. CALCULO DEL FACTORIAL DE UN NUMERO.")
numero=int(input("Ingrese un numero entero positivo: "))
if numero<0:
    print("El numero NO debe ser negativo, reinicie el programa.")
else:
    resultado=factorial(numero)
    print(f"El factorial de {numero} es {resultado}.")