#Se le pide al usuario que ingrese la fecha actual
print("___________________ Ingrese la fecha actual ___________________ ")
#Se pide al usuario que ingrese el día de la semana y la fecha
entrada = input("Ingresa el día de la semana y la fecha en formato [DIA, DD/MM]: ")

#Se divide la entrada en partes
partes = entrada.split(", ")

#Se verifica si la entrada tiene el formato correcto
if len(partes) != 2:
   print("Formato incorrecto. Debe ser [DIA, DD/MM].")
    
dia_semana = partes[0].lower()
fecha = partes[1].split("/")      
dia = int(fecha[0])
mes = int(fecha[1])

#Se determina que fecha ingreso el usuario para asi poder dirigirlo a las distintas actividades que han tenido los alumnos
if dia_semana=="lunes" or dia_semana=="martes" or dia_semana=="miércoles" or dia_semana=="jueves" or dia_semana=="viernes" :
    print("")
    if dia>=1 or dia<=31:
        print("")
        if mes>=1 and mes<=12:
            print("Fecha ingresada: " ,dia_semana,dia,"/",mes )
            if dia_semana=="lunes":
               #El dia lunes se tomo examen al nivel inicial, el usuario puede ver el porcentaje de alumnos que aprobaron y los que no
               respuesta1=str(input("Hoy se tomaron examenes al nivel incial?(Responda Si o No): "))
               if respuesta1=="Si".lower(): 
                    examenes_aprobados1=int(input("_ Ingrese el número de alumnos aprobados: "))
                    examenes_desaprobados1=int(input("_ Ingrese el número de alumnos desaprobados:"))
                    alumnos_lunes=examenes_aprobados1+examenes_desaprobados1
                    porcentaje_aprobados1=(examenes_aprobados1*100)/alumnos_lunes
                    print("- Aprobaron el ", porcentaje_aprobados1, " porciento de los alumnos en nivel inicial -")
                    porcentaje_desaprobados1=(examenes_desaprobados1*100)/30
                    print("- Y desaprobaron el ", porcentaje_desaprobados1, " porciento de los alumnos en nivel inicial -")
               else:
                   print("Hoy no se tomaron examenes")      
            else:
                #El dia martes se tomo examen al nivel intermedio, el usuario puede ver el porcentaje de alumnos que aprobaron y los que no
                if dia_semana=="martes":
                  respuesta2=str(input("Hoy se tomaron examenes al nivel intermedio?(Responda Si o No): "))
                  if respuesta2=="Si".lower():
                        examenes_aprobados2=int(input("_ Ingrese el número de alumnos aprobados: "))
                        examenes_desaprobados2=int(input("_ Ingrese el número de alumnos desaprobados: "))
                        alumnos_martes=examenes_aprobados2+examenes_desaprobados2
                        porcentaje_aprobados2=(examenes_aprobados2*100)/alumnos_martes
                        print("- Aprobaron el ", porcentaje_aprobados2, " porciento de los alumnos en nivel intermedio -")
                        porcentaje_desaprobados2=(examenes_desaprobados2*100)/alumnos_martes
                        print("- Y desaprobaron el ", porcentaje_desaprobados2, " porciento de los alumnos en nivel intermedio -")
                  else:
                      print("Hoy no se tomaron examenes")
                else:
                    #El dia miercoles se tomo examen al nivel avanzado, el usuario puede ver el porcentaje de alumnos que aprobaron y los que no
                    if dia_semana=="miércoles":
                       respuesta3=str(input("Hoy se tomaron examenes al nivel avanzado?(Responda Si o No): "))
                       if respuesta3=="Si".lower():
                            examenes_aprobados3=int(input("_ Ingrese el numero de alumnos aprobados: "))
                            examenes_desaprobados3=int(input("_ Ingrese el numero de alumnos desaprobados: "))
                            alumnos_miercoles=examenes_aprobados3+examenes_desaprobados3
                            porcentaje_aprobados3=(examenes_aprobados3*100)/alumnos_miercoles
                            print("- Aprobaron el ", porcentaje_aprobados3, " porciento de los alumnos en nivel avanzado -")
                            porcentaje_desaprobados3=(examenes_desaprobados3*100)/alumnos_miercoles
                            print("- Y desaprobaron el ", porcentaje_desaprobados3, " porciento de los alumnos en nivel avanzado -")
                       else:
                           print("Hoy no se tomaron examenes")
                    else:
                        #El dia jueves hubo practica hablada, el usuario puede ver la cantidad de alumnos que asistieron y los que no
                        if dia_semana=="jueves":
                            print("______________ Hoy hubo Practica Hablada ______________")
                            alumnos_presentes=int(input("_ Ingrese el porcentaje de alumnos que asisterieron a clases: "))
                            if alumnos_presentes>=50:
                                print("- Asistio la mayoria de los alumnos -")
                            else:
                                print("- No asistio la mayoria de los alumnos -")
                        #El dia viernes hubo ingles para viajeros, el usuario puede igresar la cantidad de alumnos que ingresaron al nuevo ciclo y puede ver el ingreso total de la institucion
                        if dia_semana=="viernes":
                            print("______________ Hoy hubo Ingles para Viajeros ______________")
                            if dia==1 or mes==1 or mes==7:
                                print("Comienzo de nuevo ciclo")
                                cantidad_alumnos=int(input("_ Ingrese la cantidad de alumnos que ingresan al nuevo ciclo: "))
                                arancel_alumno=int(input("_ Ingrese el arancel en ($) por cada alumno: "))
                                total_ingreso=cantidad_alumnos*arancel_alumno
                                print("_ El ingreso total es de: $",total_ingreso)
        else:
            print("Fecha incorrecta")
    else:
        print("Fecha incorrecta")
else:
 print("Fecha incorrecta")
