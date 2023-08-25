print("----------------------------------------------------------------------------------------------------")

"""1.	Calcular el perímetro y área de un rectángulo dada su base y su altura."""
print("__Calculo del perímetro y área de un rectángulo__")
base=float(input("ingrese el valor de la base del rectangulo "))
altura=float(input("ingrese el valor de la altura "))
print("el area del rectangulo es: ",base*altura)
print("el perimetro del rectangulo es:",(base*2)+(altura*2))

print("----------------------------------------------------------------------------------------------------")

"""2.Dados los catetos de un triángulo rectángulo, calcular su hipotenusa."""

print("_Calculo de la hipotenusa de un triangulo rectangulo_")
cat1=float(input("diga el primer cateto:"))
cat2=float(input("diga el segundo cateto:"))
hipo=(cat1**2 + cat2**2 )**(1/2)
print("El valor de la hipotenusa es:",hipo)

print("----------------------------------------------------------------------------------------------------")

"""3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos."""
print("_Suma,resta,division y multiplicacion de dos numeros_")
num1=float(input("Ingrese un numero:"))
num2=float(input("Ingrese un segundo numero:"))
suma= num1 + num2
resta=num1-num2
divicion=num1/num2
multiplicacion=num1* num2

print("El valor de la suma de los dos números es: ",suma)
print("El valor de la resta de los dos números es: ",resta)
print("El valor de la divición de los dos números es: ",divicion)
print("El valor de la multiplicación de los dos números es: ",multiplicacion)

print("----------------------------------------------------------------------------------------------------")

"""4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:"""
print("_Convertidor de un valor dado en grados Fahrenheit a grados Celsius_")
grados_f=float(input("Ingrese los grados Fahrenheit:"))
grados_c=(grados_f-32)*5/9
print(f"El valor de grados Fahrenheit {grados_f} convertido en grados Celcius es:{grados_c} ")

print("----------------------------------------------------------------------------------------------------")

"""5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

a)	A = input(nombre, “¿Cuál es tu canción favorita?”)"""
#input() debe recibir un solo argumento, que es el mensaje que se mostrará al usuario. En este caso le esta pasando dos argumentos y uno de ellos no esta definido. 
#Solución:
nombre= input("Nombre:")
A=input(f"Hola {nombre.title()}, Cual es tu canción favorita? :") 
print(f"{nombre.title()} tu canción favorita es: {A}")

"""b)	precio = input(“Precio: “)
total = precio + (precio * 0.1)"""
#Se nesesita de un conversor numerico , sino de otra manera fallara y le falto imprimir el resultado
precio = float(input("Precio: "))
total = precio + (precio * 0.1)
print(f"El precio total es: {total}")

"""c)	edad = int(input(“Edad: “))
print(tu edad es, edad)"""
#el problema se debe a la falta de comillas.
edad = int(input("Edad: "))
print("Tu edad es", edad)

"""d)	edad = int(input(“Edad": “))
print(“Veamos si tu edad es 18…”, edad=18)"""
#En este caso se comete el error de intentar definir una variable dentro de print , lo cual print no acepta argumentoss con asignación como en una función normal.
#Solución : se pueden usar operadores de comparación para verificar si la edad es igual a 18.
edad = int(input("Edad: "))
print("Veamos si tu edad es 18…", end=" ") #end=" ", se utiliza para que no haya un salto de línea después del mensaje principal, permitiendo que el mensaje condicional se muestre en la misma línea.
if edad == 18:
    print("¡Tu edad es 18!")
else:
    print("Tu edad no es 18.")

print("----------------------------------------------------------------------------------------------------")

"""6.	Calcular la media de tres números pedidos por teclado."""
print("_Calculo de la media de tres números_")
numero1=int(input("Ingrese un numero entero: "))
numero2=int(input("Ingrese otro numero entero: "))
numero3=int(input("Ingrese otro numero entero: "))
promedio=int((numero1+numero2+numero3)/3)
print("El promedio final es de: ",promedio)

print("----------------------------------------------------------------------------------------------------")


"""7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
Por ejemplo: 1000 minutos son 16 horas y 40 minutos."""
print("_Ingrese un numero y vealo en formato de minutos y horas_")
cantidad_minutos=int(input("Ingrese una cantidad de minutos: "))
horas=cantidad_minutos//60
minutos=cantidad_minutos%60
if cantidad_minutos<60:
    print("", cantidad_minutos, " minutos")
else:
    if cantidad_minutos==60: 
        cantidad_minutos=1
        print(cantidad_minutos," hora")
    else:
        if cantidad_minutos>60:
            print(horas," horas y ",minutos, "minutos" )

print("----------------------------------------------------------------------------------------------------")

"""8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes 
y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones."""
print("_Calculo de Sueldo_")
sueldo_base=int(input("Ingrese su sueldo: "))
ventas_por_mes=int(input("Ingrese las ventas realizadas por mes: "))
porcentaje=(sueldo_base*10)/100
aumento_porventas=int(porcentaje*ventas_por_mes)
total=aumento_porventas+sueldo_base
print("Obtendra: $",sueldo_base, " por mes mas un aumento del 10% por venta al mes ")
print("Aumento: $", aumento_porventas)
print("Obentra un total de: $",total," al mes")

print("----------------------------------------------------------------------------------------------------")

"""9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra."""
print("________________TIENDA________________")
print("!!! 15% DE DESUENTO CON TU COMPRA¡¡¡")
producto=int(input("Ingrese el valor de su producto: "))
porcentaje_producto=int((producto*15)/100)
descuento=producto-porcentaje_producto
print("El precio del producto es: $",producto)
print("Descuento de un 15%: $",porcentaje_producto)
print("Precio final con descuento aplicado: $", descuento)

print("----------------------------------------------------------------------------------------------------")

"""10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
•	    55% del promedio de sus tres calificaciones parciales.
•	    30% de la calificación del examen final.
•	    15% de la calificación de un trabajo final."""

parcial1 = float(input("Ingrese la calificación del parcial 1: "))
parcial2 = float(input("Ingrese la calificación del parcial 2: "))
parcial3 = float(input("Ingrese la calificación del parcial 3: "))

print("----------------------------------------------------------------------------------------------------")

"""11.	Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo)."""
promedio_parciales= (parcial1 + parcial2 + parcial3)/3

examen_final= float(input("Ingrese la calificación del examen final: "))

trabajo_final= float(input("Ingrese la calificación del trabajo final: "))

nota_final= (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)
    
print("La calificación final en la materia de Algoritmos es: ",nota_final)

print("----------------------------------------------------------------------------------------------------")

"""12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica."""
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

distancia = abs(num1 - num2)

print("La distancia entre",num1,"y",num2,"es:",distancia)

print("----------------------------------------------------------------------------------------------------")

"""13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32."""
import math
num = float(input("Ingrese un número: "))

raiz_cuadrada = math.sqrt(num)
raiz_cubica = num ** (1/3)

print("La raíz cuadrada de",num,"es:",raiz_cuadrada)
print("La raíz cúbica de",num,"es:",raiz_cubica)

#Otra forma
""" num = float(input("Ingrese un número: "))

raiz_cuadrada = num ** (1/2)
raiz_cubica = num ** (1/3)

print("La raíz cuadrada de",num,"es:",raiz_cuadrada)
print("La raíz cúbica de",num,"es:",raiz_cubica)"""

print("----------------------------------------------------------------------------------------------------")

"""14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie
los valores de ambas variables y muestre cuanto valen al final las dos variables."""
# Solicitar al usuario que ingrese los valores de las variables A y B.
A = float(input("Ingrese el valor de la variable A: "))
B = float(input("Ingrese el valor de la variable B: "))

# Intercambiar los valores utilizando una variable auxiliar.
c = A
A = B
B = c

# Mostrar los valores intercambiados
print(f"Después del intercambio, el valor de A es: {A}")
print(f"Después del intercambio, el valor de B es:{B}")

print("----------------------------------------------------------------------------------------------------")

"""15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B."""
def calcular_hora_llegada(HH, MM, SS, T):

    partida_en_segundos = HH * 3600 + MM * 60 + SS
    llegada_en_segundos = partida_en_segundos + T


    llegada_horas = llegada_en_segundos // 3600
    llegada_minutos = (llegada_en_segundos % 3600) // 60
    llegada_segundos = llegada_en_segundos % 60

    return f"{llegada_horas:02d}:{llegada_minutos:02d}:{llegada_segundos:02d}"

HH = int(input("Hora de partida (HH): "))
MM = int(input("Minutos de partida (MM): "))
SS = int(input("Segundos de partida (SS): "))
T = int(input("Tiempo de viaje en segundos (T): "))
hora_llegada= calcular_hora_llegada(HH,MM,SS,T)
print("Hora de llegada:",hora_llegada)

print("----------------------------------------------------------------------------------------------------")

"""16.	Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales."""
def obtener_iniciales(nombre, apellido1, apellido2):
    inicial_nombre = nombre[0]
    inicial_apellido1 = apellido1[0]
    inicial_apellido2 = apellido2[0]
    
    iniciales = inicial_nombre + inicial_apellido1 + inicial_apellido2
    return iniciales

nombre = input("Ingrese el nombre: ")
apellido1 = input("Ingrese el primer apellido: ")
apellido2 = input("Ingrese el segundo apellido: ")

iniciales = obtener_iniciales(nombre, apellido1, apellido2)
print("Las iniciales son:",iniciales)

print("----------------------------------------------------------------------------------------------------")

"""17.	Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada usuario.
A continuación mostrar por pantalla: “Ahora estás en la matrix, [nombre del usuario]”."""
usuario = input("Ingrese su nombre: ")
print("Ahora estás en la matrix,",usuario)

print("----------------------------------------------------------------------------------------------------")

"""18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. A ese valor,
sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en pantalla el monto final a pagar."""
costo = float(input("ingrese el costo de la cena: "))
costo += costo*0.062+costo*0.1
print(f"El costo mas la propina y concepto de servicio es de ${costo}")

print("----------------------------------------------------------------------------------------------------")


"""19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar cada uno de ellos en una variable numérica (en total, tres variables diferentes). Finalmente, mostrar la fecha en formato dd/mm/aaaa."""
anio_nacimiento = int(input("ingrese el año de nacimineto: "))
mes_nacimiento = int(input("ingrese el mes de nacimineto: "))
dia_nacimiento = int(input("ingrese el dia de nacimineto: "))
print(f"Su fecha de nacimiento es {dia_nacimiento}/{mes_nacimiento}/{anio_nacimiento}")

print("----------------------------------------------------------------------------------------------------")


"""20.	Hacer otra versión del programa, pero esta vez almacenado todo en una única variable con formato DDMMAAA."""
fecha_nacimiento = input("Ingrese su fecha de nacimiento completando con ceros en formato DDMMAAAA: ")

print(f"Su fecha de nacimiento es {fecha_nacimiento[0:2]}/{fecha_nacimiento[2:4]}/{fecha_nacimiento[4:8]}")

print("----------------------------------------------------------------------------------------------------")

"""21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible, qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
Hacer un programa que solicite los datos necesarios y luego informe la cantidad de tanques de combustible necesarios."""

km_por_1l = float(input("ingrese kilometros por litro: "))
capacidad = float(input("ingrese capacidad del tanque en litros: "))
distancia = float(input("ingrese distancia del recorrido: "))

tanques_necesarios = int(distancia / km_por_1l/capacidad)+1
print(f"usted va a necesitar {tanques_necesarios} tanques para alcansar su destino")

print("----------------------------------------------------------------------------------------------------")
