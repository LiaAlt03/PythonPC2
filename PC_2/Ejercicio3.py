'''Problema 3:
Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
números.
Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
números pares e impares.'''

print("\t3. NUMEROS PARES E IMPARES. \nNOTA: Digite '000' para salir del bucle.\n")
pares=0
impares=0

while True:
    numero=int(input("Digite un número: "))
    if numero==000:
        break
    if numero%2==0:
        pares+=1
    else:
        impares+=1

print(f"\nCantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")