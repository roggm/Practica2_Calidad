
def crearCriteriosYAlumnos(nCriterios, hoja, nAlumnos):
    listaCriterios = []
    listOfValuesCrit = []
    listDeCalificaciones = []
    for k in range(nCriterios):
        print(":::Escribe el criterio de evaluación", k+1, ":::")
        nombreCriterio = input("criterio de evaluación: ")
        valorCriterio = int(input("valor del criterio de evaluación respecto a 100: "))
        y = k+2
        hoja.cell(2,y).value = nombreCriterio
        hoja.cell(1,y).value = valorCriterio
        listaCriterios.append(nombreCriterio)
        listOfValuesCrit.append(valorCriterio)


    filas = hoja.max_column
    hoja.cell(1,filas+1).value = "100"
    hoja.cell(2,filas+1).value = "Total"


    for i in range(nAlumnos):
        print(":::Escribe el nombre del alumno", i+1, ":::")
        nombreAlumno = input("nombre del alumno: ")
        x = i+3
        y = 2
        hoja.cell(x,1).value = nombreAlumno
        listC = []
        print(":::Establecer calificaciones del alumno", nombreAlumno,":::")
        for j in listaCriterios:
            print("Esribe calificación del alumno en", j)
            calificacionAlumno = eval(input("calificación del alumno: "))
            hoja.cell(x,y).value = calificacionAlumno
            listC.append(calificacionAlumno)
            y+=1

        listDeCalificaciones.append(listC)


    calificacionesTotales = []
    for index, calificaciones in enumerate(listDeCalificaciones):
        listOfGrades = []
        for i, c in enumerate(calificaciones):
            p = c/100
            crit = listOfValuesCrit[i]
            cal = p*crit
            listOfGrades.append(cal)

        totalCalificaciones = sum(listOfGrades)
        hoja.cell((2+(index+1)),filas+1).value = totalCalificaciones
        calificacionesTotales.append(totalCalificaciones)



    print(f"Valores criterios: {listOfValuesCrit}")
    print(f"Calificaciones de criterios por alumno: {listDeCalificaciones}")
    print(f"Calificaciones totales por alumno: {calificacionesTotales}")
