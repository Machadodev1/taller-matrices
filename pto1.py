"""Desarrolla un programa que simule la evaluación de una tarea. El programa debe solicitar al usuario que ingrese
las calificaciones para **tres criterios diferentes** (por ejemplo, "Claridad", "Contenido", "Originalidad"). Cada
calificación debe ser un número entero entre 0 y 10. Utiliza un ciclo while para asegurar que cada calificación
ingresada esté dentro del rango válido. Una vez obtenidas las tres calificaciones válidas, calcula el **promedio**
de la tarea. Finalmente, imprime un mensaje indicando el rendimiento general de la tarea basándose en el
promedio:
"Excelente Tarea" si el promedio es mayor o igual a 9.
"Buena Tarea" si el promedio es mayor o igual a 7 y menor a 9.
"Necesita Mejorar" si el promedio es mayor o igual a 5 y menor a 7.
"Deficiente" si el promedio es menor a 5."""
programOn = True
items = ["Claridad", "Contenido", "Originalidad"]
notas = []
sumanotas = 0

print("Bienvenido al sistema de tareas\nLos items a calificar son: Claridad, Contenido y Originalidad")

for i in items:
    notaact = int(input(f"Ingrese la nota para {i}: "))
    if 0 <= notaact <= 10:
        notas.append(notaact)
    else:
        print("Nota fuera de rango. Debe ser entre 0 y 10.")

for i in range(len(items)):
    print(f"{items[i]}: {notas[i]}")

for i in notas:
    sumanotas += i

promedionotas = sumanotas // len(notas)

if promedionotas >= 9:
    print(f"Excelente tarea, su promedio fue: {promedionotas}")
elif promedionotas >= 7:
    print(f"Buena tarea, su promedio fue: {promedionotas}")
elif promedionotas >= 5:
    print(f"Necesita mejorar, su promedio fue: {promedionotas}")
else:
    print(f"Deficiente, su promedio fue: {promedionotas}")