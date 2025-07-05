programOn = True
listaestud = []

while programOn:
    accionuser = input("Ingrese el número de la acción a tomar:\n[1] Agregar estudiante\n[2] Ver actividades de estudiante\n[3] Agregar actividad\n[4] Eliminar actividad\n[5] Salir\n")
    if accionuser == "1":
        nom = input("Ingrese el nombre del estudiante a agregar: ")
        existe = False
        for i in listaestud:
            if i[0] == nom:
                existe = True
                break
        if existe == True:
            print("Usuario repetido, intente nuevamente")
        elif existe == False:
            listaestud.append([nom, []])
    elif accionuser == "2":
        nom = input("Ingrese el nombre del estudiante para ver actividades: ")
        existe = False
        for i in listaestud:
            if i[0] == nom:
                print(f"actividades de {nom}: {i[1]}")
                existe = True
        if existe == False:
            print("Estudiante no encontrado")
    elif accionuser == "3":
        nom = input("Ingrese el nombre del estudiante para agregar actividades: ")
        existe = False
        for i in listaestud:
            if i[0] == nom:
                tar = input("Ingrese la actividad a agregar: ")
                i[1].append(tar)
                existe = True
        if existe == False:
            print("Estudiante no encontrado")
    elif accionuser == "4":
        nom = input("Ingrese el nombre del estudiante para eliminar actividades: ")
        estudiante_encontrado = False
        for i in listaestud:
            if i[0] == nom:
                estudiante_encontrado = True
                tar = input("Ingrese la tarea a eliminar: ")
                tarea_encontrada = False
                for j in range(len(i[1])):
                    if i[1][j] == tar:
                        i[1].pop(j)
                        print("Tarea eliminada correctamente")
                        tarea_encontrada = True
                        break
                if tarea_encontrada == False:
                    print("Tarea no encontrada en la lista de actividades")
                break
        if estudiante_encontrado == False:
            print("Estudiante no encontrado")
    elif accionuser == "5":
        print("Saliendo del sistema...")
        programOn = False