'''Problema 9:
Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
por ejemplo, omitiendo las vocales.
Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
minúsculas. '''

def omitir_vocales(cadena):
    nueva_palabra=""
    for letra in cadena:
        letra=letra.lower()
        if letra not in "aeiou":
            nueva_palabra+=letra
    return nueva_palabra

print("\t9. OMITIR VOCALES")
texto=input("Ingrese una cadena de texto: ")
nueva_palabra=omitir_vocales(texto)
print("El texto con las vocales omitidas es:",nueva_palabra)