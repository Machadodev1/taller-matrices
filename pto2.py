"""2. Lista de Asistencia Simple:
Crea un programa que permita gestionar una lista de asistencia para un curso. Inicializa una lista vacía llamada
estudiantes . El programa debe presentar un menú al usuario con las siguientes opciones:
1. Agregar estudiante
2. Ver lista de estudiantes
3. Eliminar estudiante
4. Salir
El programa debe permitir al usuario seleccionar una opción y ejecutar la acción correspondiente. Para la opción
"Eliminar estudiante", el usuario debe ingresar el nombre del estudiante a eliminar. Si el estudiante no se
encuentra en la lista, el programa debe informarlo. Utiliza un ciclo while para mantener el menú activo hasta
que el usuario elija "Salir"."""
print("Bienvenido al sistema de asistencia")
programOn = True
estudents = []

while programOn:
    menu = input("Ingrese una opción a ejecutar:\n[1] Agregar estudiante\n[2] Ver lista de estudiantes\n[3] Eliminar estudiante\n[4] Salir\n")

    if menu == "1":
        nomus = input("Ingrese el nombre del estudiante: ")
        existe = False
        for i in estudents:
            if i == nomus:
                existe = True
                break
        if existe == False:
            estudents.append(nomus)
        else:
            print("El estudiante ya existe.")

    elif menu == "2":
        cont = 0
        for i in estudents:
            cont += 1
            print(f"{cont} - {i}")

    elif menu == "3":
        nomus = input("Ingrese el nombre del estudiante: ")
        encontrado = False
        for i in estudents:
            if i == nomus:
                estudents.remove(i)
                encontrado = True
                break
        if encontrado == False:
            print("Estudiante no encontrado")
        elif encontrado == True:
            print("Estudiante eliminado con éxito")

    elif menu == "4":
        print("Saliendo del sistema.")
        programOn = False



