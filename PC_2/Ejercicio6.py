'''Problema 6:
Escriba un programa en Python para obtener la serie de Fibonacci entre 0 y 50.
Nota: La secuencia de Fibonacci es la serie de números:
0, 1, 1, 2, 3, 5, 8, 13, 21,. ...
Cada número siguiente se obtiene sumando los dos números anteriores.'''

def fibonacci(numero):
    secuencia=[0,1]

    while secuencia[-1]<=numero:
            num_siguiente=secuencia[-1]+secuencia[-2]
            secuencia.append(num_siguiente)
    secuencia.pop()#Se utiliza para eliminar el último número que excede el valor de "numero"
    return secuencia

secuencia=fibonacci(50)
print("\t6. SERIE FIBONACCI")
print("La serie de Fibonacci entre los numeros 0 y 50 es la siguiente: ")
print(secuencia)