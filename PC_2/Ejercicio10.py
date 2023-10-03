'''Problema 10:
Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
8/9/1636 o Septiembre 8, 1636, donde el mes en este último podría ser cualquiera de los valores en
la lista abajo:
["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
"Noviembre", "Diciembre"]
Luego, genere esa misma fecha en formato AAAA-MM-DD.'''

meses={ #Diccionario para identificar con facilidad cada mes con su respectivo numero
    "Enero": "01",
    "Febrero": "02",
    "Marzo": "03",
    "Abril": "04",
    "Mayo": "05",
    "Junio": "06",
    "Julio": "07",
    "Agosto": "08",
    "Septiembre": "09",
    "Octubre": "10",
    "Noviembre": "11",
    "Diciembre": "12"
}

def convertir_fecha(fecha):
    for mes, numero_mes in meses.items():
        fecha=fecha.replace(mes,numero_mes)

    componentes=fecha.split() #Separamos en componentes
    if len(componentes)==3:
        mes=componentes[0].zfill(2)
        dia=componentes[1].rstrip(',').zfill(2)
        anio=componentes[2]
    else:
        mes=fecha.split("/")[0].zfill(2)
        dia=fecha.split("/")[1].zfill(2)
        anio=fecha.split("/")[2]

    return f"{anio}-{mes}-{dia}"

print("\t10. REORDENAMIENTO DE FECHA.")
fecha=input("Por favor, ingrese una fecha en el orden (mes-dia-anio) o (Mes dia, anio). \nEjemplo: 11/15/2003 o Noviembre 15,2003. \nIngrese la fecha: ")
fecha_printable=convertir_fecha(fecha)
print(f"\nLa fecha en formato AAAA-MM-DD es:{fecha_printable}")