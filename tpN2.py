"""1)Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el 
computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años."""

edad=int(input("cuántos años tiene su computadora?: "))
if edad<=2:
    print("su computadora es nueva")
elif edad>2:
    print("su computadora es vieja")
pass

"""2)Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo."""

edad = int(input("¿Cuántos años tiene su computadora?: "))
if edad < 0:
    print("Error: No puede ingresar un número negativo.")
elif edad <= 2:
    print("Su computadora es nueva.")
else:
    print("Su computadora es vieja.")

""" 3) Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables.A continuación.
Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’."""

nombre1=str(input("ingrese el primer nombre: "))
nombre2=str(input("ingrese el segundo nombre: "))
inicial1=nombre1[0]
inicial2=nombre2[0]
if inicial1==inicial2:
    print("coincidencia")
elif inicial1!=inicial2:
    print("no hay coincidencia")
pass

"""4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, candidato C por el partido azul.
Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido].
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar ‘Opción errónea.’"""

print("elija a que candidato quiere votar: 'candidato a', 'candidato b' o 'candidato c'")
voto=input("ingrese el candidato por el que quiera votar:")
candidato=voto[10]
if voto =="candidato a":
    print("usted voto por el partido rojo")
elif voto == "candidato b":
    print("usted voto por el partido verdad")
elif voto == "candidato c":
    print("usted voto por el partido azul")
else:print("opcion errónea")

"""5-	Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, 
informarle que no se puede procesar el dato."""

#solicitar y definir letra
A=str(input("ingrese una letra:"))
A=A.lower()
c=len(A)
if c==1 : 
    if A=="a" or A=="e" or A=="i" or A=="o" or A=="u":
        print("Es vocal !!!!")
        print("___________")
else:
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("[LOS DATOS INGRESADOS NO PUEDEN SER PROCESADOS]")
    print("[POR FAVOR , INGRESE UN SOLO CARCTER]")
    print("''''''''''''''''''''''''''''''''''''''''''''''''''''''''")


"""6-Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y 
no debe ser divisible por 100 excepto que también sea divisible por 400""" 

anio = int(input("Ingrese un año: "))
print("___________________")

if anio % 4 == 0:
    if anio % 100 != 0 or anio % 400 == 0:
        print("EL AÑO INGRESADO ES BISIESTO")
        print("..............................")
    else:
        print("EL AÑO INGRESADO NO ES BISIESTO")
        print("..............................")
else:
    print("EL AÑO INGRESADO NO ES BISIESTO")
    print("..............................")

"""7-Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres."""

print("^^^^^^^^^^^^^^^^")
num1=int(input("ingrese un numero:"))

print("^^^^^^^^^^^^^^^^")
num2=int(input("ingrese un segundo numero:"))

print("^^^^^^^^^^^^^^^^")
num3=int(input("ingrese un tercer numero:"))

if num1>num2 and num3>num2 :
    print("EL NUMERO MENOR ES : " , num2)
elif num2>num1 and num3>num1:
            print("EL NUMERO MENOR ES : " , num1)
else:
    if num3<num2 and num3<num1 :
        print("EL NUMERO MENOR ES : " , num3)
    else:
        if num1==num2 and num2<num3:
            print("EL NUMERO MENOR ES : " , num2)
        elif num2==num3 and num3<num1 :
                print("EL NUMERO MENOR ES : " , num3)
        else: 
                print("EL NUMERO MENOR ES : " , num1)

"""8-Escribí un programa que solicite ingresar un nombre de usuario y una contraseña.
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla
“Usuario y contraseña correctos.  Puede ingresar a Camelot”.
Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”."""

print("_______________")
usuario=str(input("ingrese el usuario:"))
print("________________")
contrasenia=str(input("ingrese la contraseña:"))
print("________________")

if usuario=="Gwenevere" and contrasenia=="excalibur" :
    print("Usuario y contraseña correctos.  Puede ingresar a Camelot")
else:
    print("Acceso denegado")

"""9-Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, 
y muestre por pantalla el grupo que le corresponde."""

print("-----------------------------------------------------------")

print("________________ DIVISION POR GRUPOS A Y B ________________")
print("_Ingrese su nombre y sexo para saber a que grupo pertenece_")
#Se pide al usuario que ingrese su nombre y sexo
nombre=input("_Ingrese su Nombre: ").upper()
sexo=input("_Ingrese su sexo(M/F): ").upper()
#Se determina a que grupo pertenece
if sexo == 'M':
    if nombre[0] < 'N':
        grupo = 'B'
    else:
        grupo = 'A'
elif sexo == 'F':
    if nombre[0] < 'M':
        grupo = 'A'
    else:
        grupo = 'B'
else:
    grupo = 'No válido'

if grupo != 'No válido':
    print("Usted pertenece al grupo: ", grupo)
else:
    print("Sexo no válido. Por favor, ingrese 'M' o 'F'.")

print("-----------------------------------------------------------")

"""10-Escribir un programa para una empresa que tiene salas de juegos para todas las edades 
y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 
$ 500 y si es mayor de 18 años, $1000."""

print("_._._._._._._._._._._ VIDEO CLUB GAME _._._._._._._._._._._")
edad_usuario=int(input("_Ingrese su edad para saber el costo de la entrada: "))
if edad_usuario<1:
    print("La edad ingresada es incorrecta")
elif edad_usuario<=4:    
    print("Los menores a 4 años entran gratis")
elif edad_usuario>4 and edad_usuario<=18:
    print("El valor de su entrada es de : $500")
elif edad_usuario>18:
    print("El valor de su entrada es de : $1000")

print("-----------------------------------------------------------")

"""11- La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada tipo de pizza aparecen a continuación.
_Ingredientes vegetarianos: Pimiento y tofu.
_Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función
de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se
puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al
final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes
que lleva."""

print(".................. PIZZERÍA BELLA NAPOLI ..................")

desicion=str(input(" _ ¿Desea comer pizza vegetariana? ")).lower
if desicion=="si":
    print("................... PIZZAS VEGETARIANAS ...................")
    print("_ Opción A: Pizza con Pimiento")
    print("_ Opción B: Pizza con Tofu")
    desicion_pizza=str(input("¿Cuál desea comer el dia de hoy? (Opcion A/Opcion B): ")).lower()
    Pimiento="opcion a"
    Tofu="opcion b"
    if desicion_pizza==Pimiento:
        print("¡Disfrute su pizza con mozzarella, tomate y pimiento!")
    else:
        print("¡Disfrute su pizza con mozzarella, tomate y tofu!")
else:
    print("......................... PIZZAS ......................... ")
    print("_ Opción A: Pizza con Peperoni")
    print("_ Opción B: Pizza con Jamón")
    print("_ Opción C: Pizza con Salmón")
    desicion_pizza1=str(input("¿Cuál desea comer el dia de hoy? (Opcion A/Opcion B/Opcion C): ")).lower()
    Peperoni="opcion a"
    Jamón="opcion b"
    Salmón="opcion c"
    if desicion_pizza1==Peperoni:
        print("¡Disfrute su pizza con mozzarella, tomate y peperoni!")
    elif desicion_pizza1==Jamón:
        print("¡Disfrute su pizza con mozzarella, tomate y jamón!")
    elif desicion_pizza1==Salmón:
        print("¡Disfrute su pizza con mozzarella, tomate y Salmón!")

print("-----------------------------------------------------------")

"""12- Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han
pasado desde ese año o cuántos años faltan para llegar a ese año."""

año_actual=int(input("_ Ingrese el año acutal: "))
año_cualquiera=int(input("_ Ingrese un año cualquiera: "))
if año_actual<=año_actual and año_cualquiera<año_actual:
    años_de_diferencia=(año_actual-año_cualquiera)
    print("Han pasado ",años_de_diferencia," años desde ",año_cualquiera)
else:
    if año_actual==año_cualquiera:
        print("No hay diferiencia entre años, el año actual es: ",año_actual)
    else:
        años_de_diferencia1=(año_cualquiera-año_actual)
        print("Faltan ",años_de_diferencia1," años para ",año_cualquiera)

"""13)Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. 
Haciendo que el programa avise cuando se escriben valores negativos o nulos."""

def es_multiplo(mayor, menor):
    return mayor % menor == 0

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 <= 0 or num2 <= 0:
    print("Esta ingresando valores negativos o nulos.")
else:
    if num1 > num2:
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1
    
    if es_multiplo(mayor, menor):
        print(f"{mayor} es múltiplo de {menor}.")
    else:
        print(f"{mayor} no es múltiplo de {menor}.")




"""14)Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es 
x = -b / a"""

a = float(input("Ingrese el coeficiente 'a' de la ecuación: "))
b = float(input("Ingrese el coeficiente 'b' de la ecuación: "))

if a == 0:
    if b == 0:
        print("La ecuación tiene infinitas soluciones (todos los números son solución).")
    else:
        print("La ecuación no tiene solución.")
else:
    x = -b / a
    print(f"La solución de la ecuación es x = {x:.2f}")


"""15)Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. 
Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base 
y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), 
el programa tiene que pedir entonces el radio y escribir el área."""

import math

opcion = input("¿Desea calcular el área de un triángulo (T) o de un círculo (C)? ").lower()

if opcion == 't':
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area_triangulo = 0.5 * base * altura
    print(f"El área del triángulo es: {area_triangulo:.2f}")
elif opcion == 'c':
    radio = float(input("Ingrese el radio del círculo: "))
    area_circulo = math.pi * radio ** 2
    print(f"El área del círculo es: {area_circulo:.2f}")
else:
    print("Opción no válida. Por favor, seleccione 'T' para triángulo o 'C' para círculo.")


"""16)Haz una calculadora básica pida al usuario dos valores, a y b.
Según la opción que desean, realizar la operación:
Si operación es 1 entonces debemos ver el resultado de a + b
Si operación es 2 entonces debemos ver el resultado de a * b
Si operación es 3 entonces debemos ver el resultado de a - b
Si operación es 4 entonces debemos ver el resultado de a / b"""

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def restar(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        print("No se puede dividir por cero.")
        return None
    return a / b

print("Calculadora Básica")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

print("Operaciones disponibles:")
print("1. Sumar")
print("2. Multiplicar")
print("3. Restar")
print("4. Dividir")

operacion = int(input("Seleccione una operación (1/2/3/4): "))

if operacion == 1:
    resultado = sumar(a, b)
    print(f"Resultado de {a} + {b} = {resultado}")
elif operacion == 2:
    resultado = multiplicar(a, b)
    print(f"Resultado de {a} * {b} = {resultado}")
elif operacion == 3:
    resultado = restar(a, b)
    print(f"Resultado de {a} - {b} = {resultado}")
elif operacion == 4:
    resultado = dividir(a, b)
    if resultado is not None:
        print(f"Resultado de {a} / {b} = {resultado:.2f}")
else:
    print("Operación no válida. Por favor, seleccione una operación válida.")

"""17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes,
otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje."""

dia = input("Ingrese un dia de la semana: ").lower()
if dia == "lunes":
    print("Feliz comienzo de semana")
elif dia == "viernes":
    print("Se acerca el findeeeee")
elif dia == "sabado" or dia == "domingo":
    print("Feliz finde semana")
else:
    print("Dia sin funcionasignada o invalido.")

"""18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes."""

horas_mes = float(input("Ingrese las horas trabajadas al mes: "))
paga_hora = float(input("Ingrese la paga por hora: "))
if horas_mes < 48:
    print("La jornada de trabajo mínima es de 48 horas.")
else:
    print(f"La paga total es de {horas_mes*paga_hora + (horas_mes-48)*(paga_hora*0.1)}")

"""19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y 
teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento."""

lapices = int(input("Ingrese los lapices que va a comprar: "))
if lapices < 1:
    print("No puedecomprar esa cantidad")
elif lapices >= 1000:
    print(f"El total que va a pagar es de ${lapices*60-lapices*60*0.07}")
else:
    print(f"El total que va a pagar es de ${lapices*60}")

"""20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas,
es mayor o igual a 6; caso contrario saldrá desaprobado"""
notas = [
    float(input("Ingrese la primer nota: ")),
    float(input("Ingrese la segunda nota: ")),
    float(input("Ingrese la tercer nota: ")),
    float(input("Ingrese la cuarta nota: "))
]
promedio = (notas[0] + notas[1] + notas[2] + notas[3]) / 4
if promedio < 6:
    print(f"Usted está desaprobado, su promedio es de {promedio}")
else:
    print(f"Usted está aprobado, su promedio es de {promedio}")