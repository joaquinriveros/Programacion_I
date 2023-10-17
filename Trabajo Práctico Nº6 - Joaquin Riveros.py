# 1)_Solicitar al usuario que ingrese números, estos deben guardarse en una lista.
#Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.

list_number=[]
while True:
   number=int(input('Por favor ingrese numeros en la lista , si desea terminar ingrese 0  '))
   if number == 0 :
        break
   else :
     list_number+=(number ,)

# 2)_A continuación, solicitar al usuario que ingrese un número y, 
# si el número está en la lista, eliminar su primera ocurrencia.
# Mostrar un mensaje si no es posible eliminar.

number=int(input('ingrese un numero a comparar '))
list_number.remove(number)
print(list_number)

# 3)_Imprimir la sumatoria de todos los números de la lista.

summation = 0

for elemento in list_number:
    summation += elemento

print(summation)

# 4)_Solicitar al usuario otro número y crear una lista con los elementos de la lista original, 
# que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

list1 = [5, 6, 7, 8, 10, 11, 12, 13]
list2 = []

# Solicitar al usuario un número y convertirlo a entero
number = int(input("Ingrese un número: "))

# Iterar por la lista original y agregar elementos menores al número dado a la nueva lista
for element in list1:
    if element < number:
        list2.append(element)

for i, element in enumerate(list2):
    if i == len(list2) - 1:
        print(element, end="" "\n")
    else:
        print(element, end="-")

# 5)_Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta por un número 
# de la lista original y la cantidad de veces que aparece en ella. Por ejemplo, si la lista original es [5,16,2,5,57,5,2], 
# la nueva lista contendrá: [(5,3),(16,1),(2,2),(57,1)]

list_origin = [5, 16, 2, 5, 57, 5, 2]
tuple_list = []

for number in list_origin:
    count = list_origin.count(number)
    # Verificar si la tupla ya existe en la lista
    if (number, count) not in tuple_list:
        tuple_list.append((number, count))

print(tuple_list)

# 6)_Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, 
# finalizando al ingresar 'x'. A continuación, solicitar que ingrese los nombres de los alumnos de 
# nivel secundario, finalizando al ingresar 'x'.
# a)_Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.
# b)_Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
# c)_Informar qué nombres de nivel primario no se repiten en los de nivel secundario.

primary_students = []

#pedimos al usuario que ingrese los alumnos de primaria
while True:
  student = input("Ingrese el nombre de un alumno de primaria o 'x' para finalizar: ")
  
  #validamos que si es una x no este vacio el array para finalizar
  if student == "x":
    if primary_students == []:
      print("no se puede terminar con la lista vacia")
      continue
    else:
      break

  #validamos que por lo menos ingrese un nombre y apellido 
  if len(student.split()) != 2:
    print("alumno no valido solo colocar nombre y apellido ")
    continue

  primary_students.append(student)

secundary_students = []

#pedimos al usuario que ingrese los alumnos de secundaria
while True:
  student = input("Ingrese el nombre de un alumno de secundaria o 'x' para finalizar: ")
  
  #validamos que si es una x no este vacio el array para finalizar
  if student == "x":
    if secundary_students == []:
      print("no se puede terminar con la lista vacia")
      continue
    else:
      break
  
  #validamos que por lo menos ingrese un nombre y apellido 
  if len(student.split()) != 2:
    print("alumno no valido solo colocar nombre y apellido ")
    continue
  
  secundary_students.append(student)

#creamos array para rellenar con los nombres que se repiten y los que no
repeated_students = []
secundary_students_no_repeated = secundary_students
primary_students_no_repeated = primary_students

#buscamos los nombres que se repiten y los agregamos, y eliminamos los que se repiten de las otras listas 
for i in primary_students:
  if i in secundary_students:
    repeated_students.append(i)
    primary_students_no_repeated.remove(i)
    secundary_students_no_repeated.remove(i)

#mostramos los arrays
print("\nAlumnos no repetidos de primaria: ")
for i in primary_students_no_repeated:
  print(i)

print("\nAlumnos no repetidos de secundaria: ")
for i in secundary_students_no_repeated:
  print(i)

print("\nAlumnos de repetidos: ")
for i in repeated_students:
  print(i)

print("")

# 7)_Escribir un programa que procese strings ingresados por el usuario.
# La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar
# la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados.
# Ejemplo:
# 'r':5
# '%':3
# 'a':8
# '9':1

occurrences = {}

#pedimos que ingrese 50 arrays
for i in range(50):
  sentence = input(f"{i}.Ingrese una frase: ")

  #leemos caracter por caracter y los agregamos al diccionario
  for char in sentence:
    if char in occurrences:
      occurrences[char] += 1
    else:
      occurrences[char] = 1

#mostramos el diccionario
for char, count in occurrences.items():
  print(f"{char}:{count}")

# 8)_Diez equipos de la liga inter-barrial identificados con los números 
#  1, 2, 3, 4, …, 10, participaron en un campeonato de fútbol con modalidad 
#  todos contra todos.
#  Escriba un programa que:
#   _ Lea el cuadro de goles en un arreglo de dos dimensiones.
#   _ Muestre para cada equipo la cantidad de triunfos, empates y derrotas.
#	_ Muestre la diferencia entre el total de goles marcados y el total de goles recibidos.
#	_ Determine la cantidad de puntos obtenidos por cada equipo.


print("     Goles anotados en cada encuentro     ")
print("------------------------------------------")
array= [["G" , 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1   , 0, 4, 2, 1, 0, 4, 2, 5, 3, 2 ],
        [2   , 5, 0, 3, 4, 2, 1, 2, 0, 3, 2 ],
        [3   , 0, 2, 0, 1, 2, 1, 5, 3, 2, 1 ],
        [4   , 1, 0, 2, 0, 1, 1, 2, 5, 0, 3 ],
        [5   , 1, 4, 2, 5, 0, 2, 0, 2, 1, 3 ],
        [6   , 1, 2, 1, 0, 5, 0, 1, 4, 2, 1 ],
        [7   , 5, 4, 0, 3, 4, 3, 0, 2, 1, 2 ],
        [8   , 2, 2, 1, 2, 3, 1, 5, 0, 1, 3 ],
        [9   , 4, 3, 3, 1, 2, 3, 2, 1, 0, 3 ],
        [10  , 1, 2, 6, 2, 1, 2, 1, 4, 2, 0 ]]

#----------------------------------------------------#

team_results = [["T","G","P","E"],
                [ 1,  0,  0,  0 ],
                [ 2,  0,  0,  0 ],
                [ 3,  0,  0,  0 ],
                [ 4,  0,  0,  0 ],
                [ 5,  0,  0,  0 ],
                [ 6,  0,  0,  0 ],
                [ 7,  0,  0,  0 ],
                [ 8,  0,  0,  0 ],
                [ 9,  0,  0,  0 ],
                [ 10, 0,  0,  0 ]]

#----------------------------------------------------#

goals_count  = [["T","GM","GR","DIF"],
                [ 1 ,  0,  0  ,  0  ],
                [ 2 ,  0,  0  ,  0  ],
                [ 3 ,  0,  0  ,  0  ],
                [ 4 ,  0,  0  ,  0  ],
                [ 5 ,  0,  0  ,  0  ],
                [ 6 ,  0,  0  ,  0  ],
                [ 7 ,  0,  0  ,  0  ],
                [ 8 ,  0,  0  ,  0  ],
                [ 9 ,  0,  0  ,  0  ],
                [ 10,  0,  0  ,  0  ]]

#----------------------------------------------------#

team_points = [["T","P"],
                [ 1,  0 ],
                [ 2,  0 ],
                [ 3,  0 ],
                [ 4,  0 ],
                [ 5,  0 ],
                [ 6,  0 ],
                [ 7,  0 ],
                [ 8,  0 ],
                [ 9,  0 ],
                [ 10, 0 ]]

#----------------------------------------------------#

#recorremos los resultados del array primcipal
for i in range(1,11,1):
    for j in range(1,11,1):
        #contamos la cantidad de goles ganados, perdidos y empatados
        if i == j:
            continue
        if array[i][j] == array[j][i] :
            team_results[i][3] += 1
        elif array[i][j] > array[j][i]:
            team_results[i][1] += 1
        else:
            team_results[i][2] += 1

        #sumamos el total de goles marcados y recibidos
        goals_count[i][1] += array[i][j]
        goals_count[i][2] += array[j][i]
    goals_count[i][3] += goals_count[i][1] - goals_count[i][2]

    #contamos los puntos de cada equipo
    team_points[i][1] += team_results[i][1]*3 + team_results[i][3]*1

#Mostramos todos los arrays
for i in array:
    for j in i:
        print(j, end='   ')
    print()

print("------------------------------------------")

print("RESULTADOS")
for i in team_results:
    for j in i:
        print(j, end='   ')
    print()

print("------------------------------------------")

print("COMPARACIÓN")
for i in goals_count:
    for j in i:
        print(j, end='    ')
    print()

print("------------------------------------------")

print("PUNTOS")
for i in team_points:
    for j in i:
        print(j, end='    ')
    print()
    
print("------------------------------------------")  

# 9_Escribir un programa que simule el juego clásico de Memoria (Memotest)
# utilizando matrices. El juego consiste en un tablero de cartas boca abajo y el objetivo es 
# encontrar todas las parejas de cartas iguales.

import os,time

memotest = [
    ["rojo", "verde", "azul", "amarillo"],
    ["naranja", "violeta", "negro", "blanco"],
    ["azul", "verde", "rojo", "amarillo"],
    ["negro", "blanco", "naranja", "violeta"]
]

empty_table = [
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""],
    ["", "", "", ""]
]

print("Tablero 4x4")
time.sleep(3)

while True:
    os.system("cls")

    try:
        option_1 = input("Ingrese la 1º posicion en formato (posicion 1 x posicion2): ")
        position_1, position_2 = map(int, option_1.strip().split("x"))

        if position_1 < 0 or position_1 >= 4 or position_2 < 0 or position_2 >= 4:
            print("Ingresó algún valor incorrecto, intente de nuevo...")
            time.sleep(3)
            continue

        option_2 = input("Ingrese la posición en formato (posicion 1 x posicion2): ")
        position_3, position_4 = map(int, option_2.strip().split("x"))

        if position_3 < 0 or position_3 >= 4 or position_4 < 0 or position_4 >= 4:
            print("Ingresó algún valor incorrecto, intente de nuevo...")
            time.sleep(3)
            continue

        if memotest[position_1][position_2] == memotest[position_3][position_4]:
            print("Ha encontrado un par!")
            time.sleep(2)
            empty_table[position_1][position_2] = memotest[position_1][position_2]
            empty_table[position_3][position_4] = memotest[position_3][position_4]

        if empty_table == memotest:
            os.system("cls")
            print("Ha completado el juego!")
            print(empty_table)
            time.sleep(7)
            break

    except (ValueError, TypeError, KeyError, IndexError):
        print("Hubo un error, intente de nuevo.")
        time.sleep(3)
        continue


# 10)_Teniendo una matriz cuadrada de cualquier dimensión, obtener lo siguiente:
# a)_la diagonal principal.
# b)_la diagonal inversa.

table_4x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [4, 5, 6, 7]
]

print()
print("Matriz Normal")
print()

for rows in table_4x4:
    for columns in range(0,4,1):
        print(rows[columns],end=" ")
    print()

print()
print("Diagonal Principal")
print()

principal_diagonal = []

for i in range(0,len(table_4x4),1):
    principal_diagonal.append(table_4x4[i][i])

string = ""
for diagonal_element in principal_diagonal:
    print(string , diagonal_element)
    string += "  "

print()
print("Diagonal Inversa")
print()

reverse_diagonal = []
j = 0
for i in range(len(table_4x4)-1,-1,-1):
    reverse_diagonal.append(table_4x4[j][i])
    j += 1

string = ""
for diagonal_element in reverse_diagonal:
    print(string , diagonal_element)
    string += "  "

# 11)_Escribir un programa que guarde en una variable el diccionario 
# {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},pregunte al usuario por una divisa y muestre su símbolo
#  o un mensaje de aviso si la divisa no está en el diccionario.

foreign_exchange = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

while True:
    try:
        exchange = input("Ingrese una divisa: ")
        if exchange in foreign_exchange:
            print("Simbolo de su divisa: ",foreign_exchange[exchange])
        else:
            print("Esa divisa no se encuentra en el diccionario")    
        time.sleep(3)    
        break    
    except(ValueError,TypeError,KeyError):
        print("Hubo un error, intente de nuevo..")
        continue

# 12)_Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo
# guarde en un diccionario.Después debe mostrar por pantalla el mensaje ‘<nombre> tiene <edad> 
# años, vive en <dirección> y su número de teléfono es <teléfono>’.

def phone_validator(phone_number):
    if phone_number.isnumeric() and len(phone_number) == 8:
        return True
    return False

def age_validator(age):
    if age.isnumeric():
        return True
    return False

name = input("Ingrese su nombre: ")
valid_age = False
while not valid_age:
    age_input = input("Ingrese su edad: ")
    if age_validator(age_input):
        valid_age = True
    else:
        print("La edad ingresada es incorrecta.")

address = input("Ingrese su dirección: ")
valid_phone = False
while not valid_phone:
    phone_input = input("Ingrese su número de teléfono: ")
    if phone_validator(phone_input):
        valid_phone = True
    else:
        print("El número ingresado no es válido.")

personal_information = {
    "nombre": name,
    "edad": int(age_input),
    "dirección": address,
    "teléfono": int(phone_input)
}

message = f"{personal_information['nombre']} tiene {personal_information['edad']} años, vive en {personal_information['dirección']} y su número de teléfono es {personal_information['teléfono']}."

print(message)

# 13)_Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
#  pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio 
# de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un 
# mensaje informando de ello.

fruits = {
    'manzana': 400,
    'banana': 450,
    'uva': 780,
    'pera': 360,
    'naranja': 530,
    'pomelo': 700,
    'mandarina': 460,
}

buy_fruit = input("Ingrese una fruta que desee comprar: ")
if buy_fruit not in fruits:
    print("No tenemos esa fruta.")
else:
    kg = float(input("¿Cuántos kilos quiere? "))
    price_per_kg = fruits[buy_fruit]
    total_price = price_per_kg * kg
    print(f"El precio de {kg} kilos de {buy_fruit} es: {total_price}")