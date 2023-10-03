'''Problema 4:
Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
materias.
Puede usar el siguiente esquema a manera de ejemplo
{ Alumno: Juan, Notas: [10, 12, 15] }
Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
completo de los alumnos.'''

def sistema(num_alumnos):
    alumnos=[] #Vacio, para almacenar nombres
    
    for i in range(num_alumnos):
        nombre=input(f"Ingrese el nombre del {i+1}° alumno: ")
        notas=[] #Almacenar las calificaciones
        
        for j in range(3):
            nota=float(input(f"\tIngrese la {j+1}° nota: "))
            notas.append(nota)
        
        datos={"Alumno": nombre, "Notas": notas}
        alumnos.append(datos)
    
    return alumnos

def listado(alumnos):
    print("\nListado de Alumnos y Notas: \nALUMNOS\t\tNOTAS:")
    for datos in alumnos:
        print(f"{datos['Alumno']}\t\t{datos['Notas']}")

print("\t4. SISTEMA DE NOTAS.")
num_alumnos=int(input("Ingrese la cantidad de alumnos que desea subir notas al sistema:\n"))
lista_alumnos=sistema(num_alumnos)
listado(lista_alumnos)