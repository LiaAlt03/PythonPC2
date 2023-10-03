'''Problema 5:
Genere una función que tenga como parámetros el ingreso de un número entero y un dígito.
Verifique la cantidad de veces que se usa dicho número en el dígito solicitado.
Ejemplo:
Número ingresado: 15789000 y Dígito: 0
Cantidad de veces 0 en el número: 4 '''

def contador(numero,digito):
    numero=str(numero)
    num_veces=numero.count(str(digito))
    return num_veces

print("\t5. CONTADOR DE DIGITOS")
numero_principal=int(input("Ingrese un numero: "))
digito_d=int(input("Ingrese el digito que desee contabilizar: "))

cantidad=contador(numero_principal, digito_d)
print(f"Cantidad de veces que se repite el numero {digito_d} en el numero {numero_principal} es de: {cantidad}")