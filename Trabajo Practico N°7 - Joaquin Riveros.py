# 1)_Escribe un programa que tome una lista de números como entrada 
# y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.

sorted_list = [2,8,5,17,40,3,72,1,32,0]

band = False
while band == False:
    band = True
    for number in range(len(sorted_list)-1):
        if sorted_list[number] > sorted_list[number+1]:
            aux = sorted_list[number]
            sorted_list[number] = sorted_list[number+1]
            sorted_list[number+1] = aux
            band = False
print (sorted_list)

# 2)_Crea un programa que tome una lista de palabras como entrada y las
# ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.

word_list = ["campera","paraguas","zapatillas","remera","pantalon"]

for i in range(0,len(word_list)):
    min = i

    for j in range(i+1,len(word_list)):

        if word_list[min] > word_list[j]:
            min = j

    aux = word_list[i]
    word_list[i] = word_list[min]
    word_list[min] = aux

print (word_list)    

# 3)_Crea una lista de diccionarios, donde cada diccionario contiene información sobre
# un libro (título, autor, año de publicación, etc.). Luego, escribe un programa que
# ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.

list_dict = [
    {"Titulo": "EL QUIJOTE", "Autor": "Miguel de Cervantes", "Año de publicación": "1605", "Puntaje": "267 puntos"},
    {"Titulo": "LA ODISEA", "Autor": "Homero", "Año de publicación": "1906-1935", "Puntaje": "148 puntos"},
    {"Titulo": "Hamlet", "Autor": "William Shakespeare", "Año de publicación": "1602", "Puntaje": "63 puntos"}

]

print()
print("Libros Desordenados:")
print()
for book in list_dict:
    print(f"Titulo: {book['Titulo']}, Autor: {book['Autor']}, Año de publicación: {book['Año de publicación']}, Puntaje: {book['Puntaje']}")
print()

# Ordenaremos la lista en base al Título

for i in range(0, len(list_dict)):
    min = i
    for j in range(i + 1, len(list_dict)):
        if list_dict[min]["Titulo"] > list_dict[j]["Titulo"]:
            min = j

    aux = list_dict[i]
    list_dict[i] = list_dict[min]
    list_dict[min] = aux

print("---------------------------------")
print()

print("Libros Ordenados:")
print()
for book in list_dict:
    print(f"Titulo: {book['Titulo']}, Autor: {book['Autor']}, Año de publicación: {book['Año de publicación']}, Puntaje: {book['Puntaje']}")
print()

# 4)_Escribe un programa que tome una lista de cadenas como entrada y las ordene
# en orden ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.

string_list = ["python", "programacion", "carrera", "software", "programa"]

print("Lista Desordenada:")
print(string_list)

for i in range(1, len(string_list)):
    key = string_list[i]
    j = i - 1
    while j >= 0 and len(string_list[j]) > len(key):
        string_list[j + 1] = string_list[j]
        j -= 1
    string_list[j + 1] = key

print("-------------------------")
print()
print("Lista Ordenada:")
print(string_list)

# 5)_Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden
# descendente en lugar de ascendente.

# Modificamos el ejercicio 1)_ y lo ordenamos de forma descendente

sorted_list = [2,8,5,17,40,3,72,1,32,0]

band = False
while band == False:
    band = True
    for number in range(len(sorted_list)-1):
        # Para ordenarlo de forma desendente cambiamos el signo mayor por el de menor:
        if sorted_list[number] < sorted_list[number+1]:
            aux = sorted_list[number]
            sorted_list[number] = sorted_list[number+1]
            sorted_list[number+1] = aux
            band = False
print (sorted_list)

# 6)_Escribe un programa que tome una lista de números enteros y ordene la lista utilizando
# el algoritmo de ordenamiento por conteo.

# Lista que deseamos ordenar
arr = [4, 2, 6, 8, 3, 7, 1]

if not arr:
    print("La lista está vacía.")
else:
    # Encuentra el valor máximo en la lista
    max_value = max(arr)

    # Crear una lista de conteo de tamaño max_value + 1 e inicializarla con ceros
    count = [0] * (max_value + 1)

    # Contar la frecuencia de cada elemento
    for num in arr:
        count[num] += 1

    # Reconstruir la lista ordenada a partir de la lista de conteo
    sorted_arr = []
    for i in range(max_value + 1):
        sorted_arr.extend([i] * count[i])

    print("Arreglo ordenado:", sorted_arr)

# 7)_Crea una lista que contenga tanto números como cadenas de caracteres. Escribe
# un programa que ordene esta lista de manera que primero estén los números ordenados
# de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente.

# Usaremos el Ordenamiento por Seleccion

# Lista con números y cadenas
my_list = [5, 'manzana', 2, 'banana', 8, 'cereza', '4', 1, 'uva']

# Separa números y cadenas en listas diferentes
numbers = [x for x in my_list if isinstance(x, int)]
strings = [x for x in my_list if isinstance(x, str)]

# Ordena la lista de números utilizando ordenamiento por selección
for i in range(len(numbers)):
    min_idx = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

# Ordena la lista de cadenas alfabéticamente utilizando ordenamiento por selección
for i in range(len(strings)):
    min_idx = i
    for j in range(i + 1, len(strings)):
        if strings[j] < strings[min_idx]:
            min_idx = j
    strings[i], strings[min_idx] = strings[min_idx], strings[i]

# Combina las listas ordenadas
my_list = numbers + strings

print("Lista ordenada:", my_list)

# 8)_Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.

# Implementación del algoritmo de Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left_half = arr[:middle]
        right_half = arr[middle:]

        # Ordenar las mitades izquierda y derecha de forma Recursiva
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # Combinar las dos mitades ordenadas
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]

print("Arreglo original:", arr)

merge_sort(arr)
print("Arreglo ordenado:", arr)