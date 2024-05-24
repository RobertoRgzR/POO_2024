alumnos = []

respuesta = input("Deseas ingresar un alumno?y/n: ").lower()

while respuesta == "y":
    alumno = {}
    alumno ["Nombre"] = input("Ingresa el nombre del alumno: ")
    alumno ["carrera"] = input(f"Ingresa la carrera: ")
    alumno ["calificaciones"] = []
    alumno ["calificaciones"].append (float(input("Ingresa la calificacion para el parcial 1: ")))
    alumno ["calificaciones"].append (float(input("Ingresa la calificaion para el parcial 2: ")))
    alumno ["calificaciones"].append (float(input("Ingresa la calificacion para el parcial 3: ")))
    alumno ["Proyecto"] = float(input("ingresa la calificacion del proyecto final: "))

    promedio_parciales = sum(alumno["calificaciones"]) / (len(alumno["calificaciones"]))
    promedio_final = (promedio_parciales + alumno["Proyecto"]) / 2

    alumno["Promedio Final"] = promedio_final

    if alumno["Proyecto"] > 50 and promedio_parciales < 80:
        alumno["Extraordinario"] = True
    else:
        alumno["Extraordinario"] = False

    alumnos.append(alumno)

    respuesta = input("¿Deseas otra captura: (y/n)").lower()

    for alumno in alumnos:
        print(f"Nombre: {alumno['Nombre']}, Carrera: {alumno['carrera']}, Promedio Final: {alumno['Promedio Final']:.2f}")
        if alumno["Extraordinario"]:
            print("Debe presentar examen extraordinario.")
        else:
            print("No requiere examen extraordinario.")

    
