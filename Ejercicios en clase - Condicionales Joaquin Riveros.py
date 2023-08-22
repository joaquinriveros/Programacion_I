#Se le pide al usuario que ingrese la fecha actual
print("__________ Ingrese la fecha actual __________ ")
dia=str(input("Día de la semana: ")).lower()
fecha=int(input("DD(dia): "))
mes=int(input("MM(mes): ")) 
#Se determina que fecha ingreso el usuario para asi poder dirigirlo a las distintas actividades que han tenido los alumnos
if dia=="lunes" or dia=="martes" or dia=="miercoles" or dia=="jueves" or dia=="viernes":
    print("")
    if fecha>=1 and fecha<=31:
        print("")
        if mes>=7 and mes<=12:
            print("Fecha ingresada: " , dia , fecha , "/", mes )
            if dia=="lunes":
               #El dia lunes se tomo examen al nivel inicial, el usuario puede ver el porcentaje de alumnos que aprobaron y los que no
               print("__________ Hoy se tomaron examenes al nivel inicial __________")
               examenes_aprobados=int(input("_ Ingrese el número de alumnos aprobados: "))
               examenes_desaprobados=int(input("_ Ingrese el número de alumnos desaprobados:"))
               porcentaje_aprobados=(examenes_aprobados*100)/30
               print("- Aprobaron el ", porcentaje_aprobados, " porciento de los alumnos en nivel inicial -")
               porcentaje_desaprobados=(examenes_desaprobados*100)/30
               print("- Y desaprobaron el ", porcentaje_desaprobados, " porciento de los alumnos en nivel inicial -")
            else:
                #El dia martes se tomo examen al nivel intermedio, el usuario puede ver el porcentaje de alumnos que aprobaron y los que no
                if dia=="martes":
                  print("__________ Hoy se tomaron examenes al nivel intermedio __________")
                  examenes_aprobados=int(input("_ Ingrese el número de alumnos aprobados: "))
                  examenes_desaprobados=int(input("_ Ingrese el número de alumnos desaprobados: "))
                  porcentaje_aprobados=(examenes_aprobados*100)/60
                  print("- Aprobaron el ", porcentaje_aprobados, " porciento de los alumnos en nivel intermedio -")
                  porcentaje_desaprobados=(examenes_desaprobados*100)/60
                  print("- Y desaprobaron el ", porcentaje_desaprobados, " porciento de los alumnos en nivel intermedio -")
                else:
                    #El dia miercoles se tomo examen al nivel avanzado, el usuario puede ver el porcentaje de alumnos que aprobaron y los que no
                    if dia=="miercoles":
                       print("__________ Hoy se tomaron examenes al nivel avanzado __________")
                       examenes_aprobados=int(input("_ Ingrese el numero de alumnos aprobados: "))
                       examenes_desaprobados=int(input("_ Ingrese el numero de alumnos desaprobados: "))
                       porcentaje_aprobados=(examenes_aprobados*100)/60
                       print("- Aprobaron el ", porcentaje_aprobados, " porciento de los alumnos en nivel avanzado -")
                       porcentaje_desaprobados=(examenes_desaprobados*100)/60
                       print("- Y desaprobaron el ", porcentaje_desaprobados, " porciento de los alumnos en nivel avanzado -")
                    else:
                        #El dia jueves hubo practica hablada, el usuario puede ver la cantidad de alumnos que asistieron y los que no
                        if dia=="jueves":
                            print("__________ Hoy no se tomaron examenes hubo Practica Hablada __________")
                            alumnos_presentes=int(input("_ Ingrese el porcentaje de alumnos que asisterieron a clases: "))
                            if alumnos_presentes>=50:
                                print("- Asistio la mayoria de los alumnos -")
                            else:
                                print("- No asistio la mayoria de los alumnos -")
                        #El dia viernes hubo ingles para viajeros, el usuario puede igresar la cantidad de alumnos que ingresaron al nuevo ciclo y puede ver el ingreso total de la institucion
                        if dia=="viernes":
                            print("__________ Hoy no se tomaron examenes hubo Ingles para Viajeros __________")
                            if fecha==1 and mes==1 or mes==7:
                                print("Comienzo de nuevo ciclo")
                                cantidad_alumnos=int(input("_ Ingrese la cantidad de alumnos que ingresan al nuevo ciclo: "))
                                arancel_alumno=int(input("_ Ingrese el arancel en ($) por cada alumno: "))
                                total_ingreso=cantidad_alumnos*arancel_alumno
                                print("_ El ingreso total es de: $",total_ingreso)
        else:
            print("Fecha Incorrecta")
    else:
        print("Fecha Incorrecta")
else:
 print("Fecha Incorrecta")


