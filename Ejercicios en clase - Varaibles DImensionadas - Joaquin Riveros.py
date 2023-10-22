
#-----------------------------------------------------------------------------------#
# Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas 
# con la siguiente forma: (nombre, dni, destino). Por ejemplo:
# [(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, ‘Mendoza’)]
# Además en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejemplo:
# [(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, ‘Argentina’)]
# Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
#   - Agregar pasajeros a la lista de viajeros.
#   - Agregar ciudades a la lista de ciudades.
#   - Dado el DNI de un pasajero, ver a qué ciudad viaja.
#   - Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
#   - Dado el DNI de un pasajero, ver a qué país viaja.
#   - Dado un país, mostrar cuántos pasajeros viajan a ese país.
#   - Salir del programa.


#   - Agregar pasajeros a la lista de viajeros.
def add_traveler():
    while True:
        traveler_name = input("Ingrese su nombres y apellido: ")
        traveler_name_cut = traveler_name.split()
        if len(traveler_name_cut) == 2:
            break
    while True:
        traveler_dni = input("Ingrese su DNI(8 o 7 digitos sin punto): ")
        if traveler_dni.isdigit() and (len(traveler_dni) == 8 or len(traveler_dni) == 7):
            traveler_dni = int(traveler_dni) 
            break
    while True:
        traveler_city = input("Ingrese el nombre de la ciudad: ")
        if traveler_city.isdigit() == False:
            break
    return (traveler_name.title(),traveler_dni,traveler_city.title())


#   - Agregar ciudades a la lista de ciudades.
def add_city ():
    while True:
        intro_city = input("Ingrese el nombre de la ciudad: ")
        if intro_city.isdigit() == False:
            break
    while True:
        intro_country = input("Ingrese el nombre del pais: ")
        if intro_country.isdigit() == False:
            break
    return (intro_city.title(),intro_country.title())


#   - Dado el DNI de un pasajero, ver a qué ciudad viaja.
def serch_city(travelers):
    while True:
        traveler_dni = input("Ingrese el DNI abuscar (8 o 7 digitos sin punto): ")
        if traveler_dni.isdigit() and (len(traveler_dni) == 8 or len(traveler_dni) == 7):
            traveler_dni = int(traveler_dni) 
            break
    for i in travelers:
        if traveler_dni in i:
            return i[2]
    return "No esta registrado el dni"


#   - Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
def go_to_that_city(travelers):
    while True:
        traveler_city = input("Ingrese el nombre de la ciudad: ")
        if traveler_city.isdigit() == False:
            break
        
    total_travelers = 0    
    
    for i in travelers:
        if traveler_city.title() in i:
            total_travelers += 1
    return total_travelers


#   - Dado el DNI de un pasajero, ver a qué país viaja.
def get_country(citys,travelers):
    traveler_city = serch_city(travelers)
    for i in citys:
        if traveler_city in i:
            return i[1]
    return "No hay ningun pais asignado o viajero con ese dni"


#   - Dado un país, mostrar cuántos pasajeros viajan a ese país.
def go_to_that_country(citys,travelers):
    count = 0
    while True: 
        found = False
        intro_country = input("Ingrese un pais: ").title()
        for i in citys:
            if intro_country in i:
                found = True
                break 
        if found == False:
            print("¡No esta regitrado el pais introducido!")
        else:
            break
    for i in travelers:
        for j in citys:
            if i[2] in j:
                if intro_country in j:
                    count += 1
                    break
    return count           

travelers = []
citys = []

while True:
    print("")
    print("TRAVELERS")
    print("1- Agregar pasajero")    
    print("2- Agregar ciudad")    
    print("3- Ver ciudad por dni")
    print("4- Cantidad de pasajeros por ciudad")
    print("5- Ver pais por DNI")
    print("6- Cantidad de pasajeros por pais")
    print("7- salir")

    opt = input("Ingrese una opcion: ")
    
    if opt == "1":
        travelers.append(add_traveler())
    elif opt == "2":
        citys.append(add_city())
    elif opt == "3":
        print(serch_city(travelers))
    elif opt == "4":
        print(go_to_that_city(travelers))
    elif opt == "5":
        print(get_country(citys,travelers))
    elif opt == "6":
        print(go_to_that_country(citys,travelers))
    elif opt == "7":
        print("Fin del programa")
        break
    else:
        print("Opcion no valida")

    

#-----------------------------------------------------------------------------------#
# Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual
# contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
# [(‘Nuria Costa’, 5, 1234.5,’Calle 1 – 456’), (‘Jorge Russo’, 7, 3999, ‘Calle 2 – 741’)]
# Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y
# retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada cliente
# puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura que
# contenga cada domicilio una sola vez.

def obtener_domicilios_factura(compras):
    domicilios = {} 

    for compra in compras:
        cliente, _, _, domicilio = compra  
        domicilios[cliente] = domicilio  

    return list(domicilios.values())  


compras = [('Joaquin Riveros', 6, 5362.5, 'Calle 1 - 102'), ('Maximo Aguilera ', 4, 6842, 'Calle 2 - 018' )]
domicilios_factura = obtener_domicilios_factura(compras)
print("DOMICILIOS")
print()
print(domicilios_factura)

#-----------------------------------------------------------------------------------#
# Crear un programa para gestionar datos de los socios de un club, permitiendo:
# - Cargar información de los socios en un diccionario para acceder por número de socio. Los datos a almacenar
# son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). El programa debe iniciar
# con los datos de los socios fundadores ya cargados:
# o Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
# o Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
# o Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
# - Informar cantidad de socios del club.
# - Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
# - Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad
# ingresaron el 14/03/2018.
# - Solicitar el nombre y apellido de un socio y darle de baja (eliminarlo del listado)
# - Imprimir el listado de socios completo.

# Datos iniciales de socios fundadores
socios = {
    1: {"nombre": "Amanda Núñez", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True},
    2: {"nombre": "Bárbara Molina", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True},
    3: {"nombre": "Lautaro Campos", "fecha_ingreso": "17/03/2009", "cuota_al_dia": True}
}

# Función para contar la cantidad de socios
def contar_socios(socios):
    return len(socios)

# Función para registrar el pago de todas las cuotas de un socio
def pagar_cuotas(socio_numero):
    if socio_numero in socios:
        socios[socio_numero]["cuota_al_dia"] = True
        print(f"Las cuotas de {socios[socio_numero]['nombre']} han sido registradas como pagadas.")
    else:
        print("Número de socio no encontrado.")

# Función para modificar la fecha de ingreso
def modificar_fecha_ingreso(fecha_antigua, fecha_nueva):
    for numero_socio, socio in socios.items():
        if socio["fecha_ingreso"] == fecha_antigua:
            socio["fecha_ingreso"] = fecha_nueva

# Función para dar de baja a un socio
def dar_de_baja(nombre_apellido):
    for numero_socio, socio in list(socios.items()):
        if socio["nombre"] == nombre_apellido:
            del socios[numero_socio]
            print(f"{nombre_apellido} ha sido dado de baja.")
            return
    print(f"Socio {nombre_apellido} no encontrado.")

# Función para imprimir el listado completo de socios
def imprimir_listado(socios):
    print("Listado de socios:")
    for numero_socio, socio in socios.items():
        print(f"Socio n°{numero_socio}, {socio['nombre']}, ingresó: {socio['fecha_ingreso']}, cuota al día: {socio['cuota_al_dia']}")

# Main loop
while True:
    print("\nGestión de Socios de Club\n")
    print("1. Informar cantidad de socios")
    print("2. Registrar pago de cuotas")
    print("3. Modificar fecha de ingreso")
    print("4. Dar de baja a un socio")
    print("5. Imprimir listado de socios")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print(f"La cantidad de socios en el club es: {contar_socios(socios)}")
    elif opcion == "2":
        numero_socio = int(input("Ingrese el número de socio que ha pagado todas las cuotas adeudadas: "))
        pagar_cuotas(numero_socio)
    elif opcion == "3":
        fecha_antigua = "13/03/2018"
        fecha_nueva = "14/03/2018"
        modificar_fecha_ingreso(fecha_antigua, fecha_nueva)
        print(f"La fecha de ingreso ha sido modificada para todos los socios que ingresaron el {fecha_antigua}.")
    elif opcion == "4":
        nombre_apellido = input("Ingrese el nombre y apellido del socio que desea dar de baja: ")
        dar_de_baja(nombre_apellido)
    elif opcion == "5":
        imprimir_listado(socios)
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")