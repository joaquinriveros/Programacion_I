"""1)Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces."""

word=input("Ingrese una palabra: ")
for i in range(10):
    print(word)

"""2)Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad)."""

year=int(input("Ingrese su edad: "))
for i in range(1, year+1):
    print(f"Has cumplido {i} años")

"""3)Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares
desde 1 hasta ese número separados por comas."""

number=int(input("Ingrese un numero entero: "))
for i in range(1, number+ 1, 2):
    print(i, end=", ")

"""4)Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""

number = int(input("Ingrese un numero entero: "))
for i in range(number, -1, -1):
    if i == 0:
        print(i)
    else:
        print(i, end=", ")

"""5)Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y 
muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión."""

amount_invested = float(input("Ingrese la cantidad a invertir: "))
annual_interest = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
years = int(input("Ingrese el número de años de la inversión: "))

# Calcula el capital obtenido cada año
for year in range(1, years + 1):
    capital_obtained = amount_invested * (1 + (annual_interest / 100))**year
    print(f"Año {year}: Capital obtenido = {capital_obtained}")

"""6-Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
rectángulo, de altura el número introducido."""

number_height=int(input("_ Ingrese un numero de altura: "))

for i in range(0,number_height+1):
    right_triangle="*"*i
    print(right_triangle) 

print("---------------------------------------------------------------------")

"""7-Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10."""      

print(".-.-.-.-.-.-.-. TABLAS DE MULTIPLICAR(1 AL 10) .-.-.-.-.-.-.-.")
for i in range(1,11):
    for j in range(1,11):
        result=i*j
        print(i,"x",j,"=",result)
    
print("---------------------------------------------------------------------")

"""8-Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
como el de más abajo."""

#Se le pide al usuario que ingrese un numero.
triangle_height=int(input("_ Ingrese la altura de su triangulo:"))

#Bucle for que va a iterar de 1 a 6
for i in range(1, triangle_height + 1):
    # Bucle for interno para imprimir números en cada fila
    for j in range(2 * i - 1, 0, -2):  #Comienza por el valor tomado por i, y luego retrocede de 2 en 2
        print(j, end=" ")#Se imprime el valor de `j` seguido de un espacio en blanco, para formar la parte de números de cada fila
    print()  #Se salta de línea para pasar a la siguiente fila

print("---------------------------------------------------------------------")

"""9-Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña
hasta que introduzca la contraseña correcta."""

print("_ - _ - _ - _ - _ SAMSUNG PAGE _ - _ - _ - _ - _")#Relleno para que se vea estetico el programa
user_1=str(input("_ Cree un usuario Samsung: ")) #Relleno para que se vea estetico el programa
password_1=str(input("_ Cree una contraseña samsung: "))#Se le pide al Usuario que cree una contraseña
password=str("")#Variale que sirve para la verificacion 
user=str("")#Relleno para que se vea estetico el programa
while user!= user_1:#Relleno para que se vea estetico el programa
    user=str(input("_ Ingrese su nombre de usuario: "))#Relleno para que se vea estetico el programa
    if user!= user_1:#Relleno para que se vea estetico el programa
        print("Usuario incorrecto")#Relleno para que se vea estetico el programa
user==user_1#Relleno para que se vea estetico el programa

while password!=password_1:#Bucle While donde el programa va a leer si la contraseña ingresada e igual a la creada y almacenada en la variable user_1
    password=str(input("_ Ingrese su contraseña: "))#Se le pide al usuario que ingrese una contraseña
    if password!=password_1:#Si contaseña es inconrrecta el programa muesttra Contraseña Incorretca 
        print("Contraseña incorrecta")
password==password_1
print("!!!BIENVENIDO AL SISTEMA!!!")#Relleno para que se vea estetico el programa

print("---------------------------------------------------------------------")

"""10-Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no."""

number_cousin=int(input("_ Ingrese un numero para saber si es primo o no: ")) #Se le pide al usuario que ingrese un numero
    
while number_cousin>1:
    
    if number_cousin <= 1: #Si el numero ingresado es igual a 1 no es primo
        print("El numero ingresado no es primo")  
        break
    elif number_cousin == 2: #Si el numero ingresado es igual a 2 es un numero primo especial
        print("El numero 2 es un numero primo especial")
        break   
    elif number_cousin % 2 == 0: #Si el numero ingresado es divisible por 2 con resto 0 no es primo ya que los números pares mayores que 2 no son primos
        print("El numero ingresado no es primo")
        break
    else:
        print("El numero ingresado es primo")  
        break
for divider in range(3, int(number_cousin**0.5) + 1, 2): #Se comprueba la divisibilidad desde 3 hasta la raíz cuadrada de 'number_cousin'
    if number_cousin % divider == 0:
        print("El numero ingresado no es primo")
        break
    else:
        print("El numero ingresado es primo")
        break

"""11-Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras 
de la palabra introducida empezando por la última."""

word=str(input("ingrese la palabra que quiere invertir: "))
inverted_word=word[::-1]
print(inverted_word)

"""12-Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla 
el número de veces que aparece la letra en la frase."""

sentence=str(input("ingrese la frase que desee: "))
character=str(input("ingrese la letra que desea para poder contar cuantas veces se repite en la frase: "))
character_count=0
for letter in sentence :
    if letter == character :
        character_count = character_count+1
        pass
print(character_count)

"""13-Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba 
“salir” que terminará."""

while True:
    entry = input("Escribe algo ('salir' para terminar): ")
    if entry.lower() == "salir":
        print("¡Hasta luego!")
        break
    else:
        print(entry)

"""14-Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares 
desde el primero hasta el segundo"""

number1=int(input("ingrese el primer numero: "))
number2=int(input("ingrese el segundo numero: "))
print(f"Números pares entre {number1} y {number2}:")
for numbers in range(number1, number2 + 1):
    if numbers % 2 == 0:
        print(numbers)
print(f"Números impares entre {number1} y {number2}:")
for numbers in range(number1, number2 + 1):
    if numbers % 2 != 0:
        print(numbers)

"""15-Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores."""

print("escriba un número del que quiera saber sus divisores: ")
number=int(input())
print("divisores del número ",number)
for dividers in range(1,number+1):
    if number%dividers==0:
        print(dividers)

"""16-Escriba un programa que pregunte cuántos números se van a introducir, pida esos números y 
escriba cuántos negativos ha introducido."""

aux=int(input("ingrese cuantos numeros va a introducir:"))
aux2=0
negative=0
while aux2<aux :
    number=int(input(" ingrese el numero: "))
    if number<0 :
        negative+=1
    aux2+=1
print("se han ingresado " , negative ," numeros negativos")

"""17-Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase 
(sin repetirlas)."""

phrase=input("ingrese una frase:  ")
phrase=phrase.lower()
vocal=set()
for i in range(len(phrase)):
    if phrase[i]=="a" or phrase[i]=="e" or phrase[i]=="i" or phrase[i]=="o" or phrase[i]=="u" :
        vocal.add(phrase[i])
print("Las vocales ingresadas son " , ', '.join(vocal) , ' ' )     


"""18-Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza 
con los números 0 y 1 y, a partir de éstos,cada elemento es la suma de los dos 
números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…"""

print("la secuencia de fibonacci es: ")
#Inicializamos los primeros dos números de la secuencia
a, b = 0, 1
# Mostramos los primeros 10 números de la secuencia
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b

"""19-Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, 
que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y otra vez 
las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo.
El programa deberá comprobar que las cantidades ingresadas sean positivas."""

ultimate_savings=int(input("ingrese los ahorros que quiere juntar:"))
savings=0
while savings < ultimate_savings:
    saving_tem=int(input("ingrese dinero a ahorrar: "))
    if saving_tem >0 : 
        savings= savings + saving_tem
    else : print(" El numero ingresado no es valido , porfavor ingrese un numero positivo")
print(" ")
print("ALCANZO SU META !, Sus ahorros son :" , savings)

"""20-Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria 
de todos los números ingresados."""

print("Empecemos a sumar !")
num=1
number=0
while num<0 or num>0:
    num=int(input("inrese un numero para salir ingrese 0:"))
    number+= num
print("La suma de todos los numeros es : " , number)

"""21-Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. 
Informar cuál fue el mayor número ingresado."""

def serch_bigger ():
    number = int(input("Ingrese un numero o 0 para finalizar: "))
    bigger_number = number
    while number != 0:
        if bigger_number < number:
            bigger_number = number
        number = int(input("Ingrese un numero o 0 para finalizar: "))


    print(f"El numero mas grande ingresado fue: {bigger_number}")

serch_bigger()

"""22-Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los 
dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, 
mostrar cuántos de los números ingresados por el usuario fueron números pares."""

def summation_and_pair():
    number = int(input("Ingrese un numero positivo o -1 para finalizar: "))
    summation = 0
    pairs = 0
    while number != -1 :

        for i in str(number):
            summation += int(i) 
        if number % 2 == 0:
            pairs+=1

        print(f"La sumatoria de los digitos de {number} es de {summation}")
        number = int(input("Ingrese un numero positivo o -1 para finalizar: "))
        summation = 0
    
    print(f"Ingresó {pairs} numeros pares.")
summation_and_pair()

"""23-Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de 
datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0."""

def shoppingV1():
    number = int(input("Ingrese un monto de compra o 0 para finalizar: $")) 
    total = 0
    while number != 0 :
        total += number 
        number = int(input("Ingrese un monto de compra o 0 para finalizar: $")) 
    print(f"El total es de ${total}.")

shoppingV1()

"""24-Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, 
informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% 
de descuento."""

def shoppingV2():
    number = int(input("Ingrese un monto de compra o 0 para finalizar: $")) 
    total = 0
    while number != 0 :
        if number<0:
            print("¡No se cuentan los montos negativos!")
        total += number 
        number = int(input("Ingrese un monto de compra o 0 para finalizar: $")) 
    if total >1000 :
        total -= total*0.1
        print(f"El total es de ${total} con un 10% de desguento agregado.")
    else:
        print(f"El total a pagar es de ${total}")
    
shoppingV2()

"""25-Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando 
todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1."""

def factorial ():
    total = 1
    counter=0
    number = int(input("Ingrese un numero entero positivo: ")) 
    while number<0:
        print("El numero ingresado no es valido")
        number = int(input("Ingrese un numero entero positivo: "))
    if number >0:
        while counter != number:
            counter+=1
            total*=counter
    print(f"El factorial de {number} es {total}")
        
    
        
factorial()