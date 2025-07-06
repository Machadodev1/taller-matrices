programOn = True
listaestud = []

while programOn:
    accionuser = input("Ingrese el número de la acción a tomar:\n[1] Agregar estudiante\n[2] Ver actividades de estudiante\n[3] Agregar actividad\n[4] Eliminar actividad\n[5] Salir\n")

    if accionuser == "1":
        nomus = input("Ingrese el nombre del estudiante: ")
        existe = False
        for i in listaestud:
            if i[0] == nomus:
                existe = True
                break
        if existe == False:
            listaestud.append([nomus, []])
        else:
            print("El estudiante ya existe.")

    elif accionuser == "2":
        selecest = input("Ingrese el nombre del estudiante para ver sus actividades: ")
        encontrado = False
        for i in listaestud:
            if i[0] == selecest:
                print(f"Actividades de {selecest}: {i[1]}")
                encontrado = True
                break
        if encontrado == False:
            print("Estudiante no encontrado.")

    elif accionuser == "3":
        while True:
            numest = input("Ingrese el nombre del estudiante para asignar actividad: ")
            tareaas = input("Ingrese el nombre de la actividad a agregar: ")
            encontrado = False
            for i in listaestud:
                if i[0] == numest:
                    i[1].append(tareaas)
                    encontrado = True
                    break
            if encontrado == False:
                print("Estudiante no encontrado.")
            cont = input("Agregar otra tarea?\n[1] Sí\n[2] No: ")
            if cont != "1":
                break
    elif accionuser == "4":
        while True:
            numest = input("Ingrese el nombre del estudiante para eliminar actividad: ")
            tareaas = input("Ingrese el nombre exacto de la actividad a eliminar: ")
            encontrado = False
            for i in listaestud:
                if i[0] == numest:
                    for j in range(len(i[1])):
                        if i[1][j] == tareaas:
                            i[1].pop(j)
                            print("Actividad eliminada correctamente.")
                            encontrado = True
                            break
                    break
            if encontrado == False:
                print("Estudiante o actividad no encontrada.")
            
            cont = input("¿Desea eliminar otra actividad?\n[1] Sí\n[2] No: ")
            if cont != "1":
                break
    elif accionuser == "5":
        print("Saliendo del sistema...")
        break