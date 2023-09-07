# 1)_Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
word = str(input("Please, insert a word: ")) 
for i in range(1,11,1):
    print(word)

# 2)_Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años
# que ha cumplido (desde 1 hasta su edad).
age=int(input("Insert your age: "))
for i in range(0,age,1):
    print(f"You passed by {i} year old")

# 3)_Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# todos los números impares desde 1 hasta ese número separados por comas.
list=[]
number= int(input("Insert a positive number: "))
for i in range(1,(number+1),1):
    if i % 2 != 0:
        list.append(i)    
print(list)

# 4)_Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla 
# la cuenta atrás desde ese número hasta cero separados por comas.
list=[]
positive_number=int(input("Insert a positive number: "))
if positive_number > 0:
    for i in range(positive_number,(0-1),-1):
        list.append(i)
print(list)

# 5)_Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el 
# número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la 
# inversión.
invest_money=float(input("¿How much money are you going to invest?: $ "))
annual_interest=float(input("¿How much is the annual interest?:  % "))
time_years=int(input("Insert the time (in years) : "))

annual_interest = annual_interest / 100

for i in range(1,(time_years+1),1):
    increment= invest_money * annual_interest
    capital = invest_money + increment
    print(f"{i}º year: {capital}")
    annual_interest += annual_interest

# 6)_Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo 
# rectángulo como el de más abajo, de altura el número introducido.
character = "*"
triangle = "*"
number= int(input("Please, insert an integer number: "))
for i in range(1,(number + 1),1):
    print(triangle)
    triangle=triangle + character
 
# 7)_Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
print("Multiplication tables")
for i in range(1,11,1):
    print("------------------------------")
    print(f"Table of {i}")
    for j in range(1,11,1):
        print(f"{i} x {j} = { i * j }")

# 8)_Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
# rectángulo como el de más abajo.
odd = 1
triangle=""
space=" "
number = int(input("Please, insert a number: "))
for i in range(1,(number+1),1):
    triangle = str(odd) + space + triangle 
    print(triangle)
    odd += 2

# 9)_Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
password=""
while password != "contraseña":
    password=str(input("Ingrese la contraseña: "))
    if password != "contraseña":
        print("Intente de nuevo...")
print("Bienvenido")

# 10)_Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un 
# número primo o no.
number = int(input("Insert an integer number: ")) 
if (number % 2 == 0) or (number % 3 == 0) or (number % 5 == 0) or (number % 7 == 0):
    print(f"{number} It isn´t a prime number")
else:
    print(f"{number} It´s a prime number")

# 11)_Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una 
# a una las letras de la palabra introducida empezando por la última.
word=str(input("Please, insert a word: "))
for i in word[::-1]:
    print(i)

# 12)_Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre
# por pantalla el número de veces que aparece la letra en la frase.
phrase= str(input("Please, insert a phrase: "))
letter= str(input("Now, insert a letter: "))
counter = 0
for i in phrase:
    if letter == i:
        counter = counter + 1
print(f"Your letter is {counter} times in the phrase.")

# 13)_Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que 
# el usuario escriba “salir” que terminará.
finish=""
print("Escriba 'salir' al final del código para salir... ")
print("Presione 'enter' para continuar: ")
while finish != "salir":
    word=str(input("Insert a word: "))
    letter=""
    for i in word[-3::1]:
        letter=letter+i
    print(word + " " + letter)    
    finish=input()
    
# 14)_Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles
# impares desde el primero hasta el segundo.
number_1=str(input("Ingrese el 1º numero: "))
number_2=str(input("Ingrese el 2º número: "))
list_1=[]
list_2=[]
for i in number_1:
    if int(i) % 2 ==0:
        list_1.append(i)
    else:    
        list_2.append(i)
print(f"{list_1} son números pares dentro del 1º número ingresado")    
print(f"{list_2} son números impares dentro del 1º número ingresado")    

print("----------------------------------")

list_1=[]
list_2=[]
for j in number_2:
    if int(j) % 2 ==0:
        list_1.append(j)
    else:    
        list_2.append(j)
print(f"{list_1} son números pares dentro del 2º número ingresado")    
print(f"{list_2} son números impares dentro del 2º número ingresado")    


# 15)_Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
positive_number=int(input("Insert a positive number: "))
divider=[]
for i in range(1,(positive_number+1),1):
    if positive_number % i == 0:
        divider.append(i)
print(f"The inserted number could be divided by: {divider}")

# 16)_Escriba un programa que pregunte cuántos números se van a introducir, pida esos números
# y escriba cuántos negativos ha introducido.
how_much_numbers=int(input("¿How much numbers are you going to insert?: "))
i=0
negative_counter = 0
while how_much_numbers != 0:
    i += 1
    number=float(input(f"Insert your {i} number: "))
    if number < 0:
        negative_counter = negative_counter + 1
    how_much_numbers -= 1
print(f"You introduced {negative_counter} negative numbers")    

# 17)_Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que
# aparecen en esa frase (sin repetirlas).
def vewel_counter(i):
    if i in list:
        boolean=False
    else:
        boolean=True
    return boolean

phrase= str(input("Insert a phrase: "))
list=[]
for i in phrase:
    if i== "a" or i == "e" or i == "i" or i == "o"or i == "u": 
        validator=vewel_counter(i)
        if validator == True:
            list.append(i)
print(f"The vowels in the phrase are: {list}")

# 18)_Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci.
# La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma
# de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

# Inicializamos los primeros dos números de Fibonacci
fibonacci = [0, 1]

# Generamos los siguientes 8 números de Fibonacci
for i in range(8):
    next_number = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(next_number)

# Mostramos los primeros 10 números de Fibonacci
print(fibonacci)

# 19)_Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad,
# que será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará
# una y otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere
# al objetivo. El programa deberá comprobar que las cantidades ingresadas sean positivas.
total_cuantity=float(input("Ingrese la cantidad total que desea ahorrar: $ "))
acumulated_cuantity = 0
while acumulated_cuantity < total_cuantity:
    cuantity=float(input("Ingrese la cantidad a ahorrar: $ "))
    if cuantity > 0:
        acumulated_cuantity = acumulated_cuantity + cuantity
print("Ha logrado su objetivo! ")

# 20)_Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar
# la sumatoria de todos los números ingresados.
number=None
sumatory = 0
while number != 0:
    number=float(input("Insert a number (press 0 to scape): "))
    sumatory += number
print(f"Sumatory: {sumatory}")

# 21)_Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál
# fue el mayor número ingresado.
number=None
higher = 0
while number != 0:
    number=float(input("Insert a number (press 0 to scape): "))
    if number > higher:
        higher = number
print(f"Higher number: {higher}")

# 22)_Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la
# suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1.
# Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
number=None
list=[]
counter=0
while number != -1:
    sumatory = 0
    digit = []
    number=int(input("Insert a positive number (press -1 to scape): "))
    if number == -1:
       break
    else:
      for i in str(number):
          digit.append(i)
          sumatory = sumatory + int(i)
      if number % 2 == 0:
          list.append(number)
          counter += 1
      print(f"The digits are: {digit}")
      print(f"The sumatory is: {sumatory}")
print(f"La cantidad de números pares son: {counter}")
print(f"Números pares: {list}")

# 23)_Crear un programa que permita al usuario ingresar los montos de las compras de un cliente
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución),
# cortando el ingreso de datos cuando el usuario ingrese el monto 0.
# 24)_Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto.
# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total
# de $1000, se le debe aplicar un 10% de descuento.
amount=None
cuantity=[]
sumatory = 0
while amount != 0:
    amount=int(input("Ingrese el monto de su compra (presione 0 para salir): "))
    if amount > 0:
        cuantity.append(f"${amount}")
        sumatory = sumatory + amount
    else:
        print("Error, intente de nuevo...")
print(f"Monto de las compras: {cuantity}")
if sumatory >= 1000:
    discount = sumatory * (10 / 100)
    total= sumatory - discount
print("Total a pagar: $",total)

# 25)_Dado un número entero positivo, mostrar su factorial. El factorial de un número se
# obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
# El factorial de 0 es 1.
factorial= int(input("Please, insert a positive number: "))
for i in range( factorial , 0 , -1 ):
    factorial = factorial * i
print("Factorial: ",factorial)