from Funciones import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, binary_search, linear_search
#Elaborar una función que realice cada ordenamiento y búsqueda vistos en la presentación.
#----------------------------------------------------------------------#
# _ ORDENAMIENTO
#----------------------------------------------------------------------#
#Bubble Sort

list = [1, 34, 5, 125, 22, 11, 99]
bubble_sort(list)

print("Ordenamiento Bubble Sort:")
for number in list:
    print(number, end=" ")
    

#----------------------------------------------------------------------#
#Selection Sort

list1 = [1, 34, 5, 125, 22, 11, 99]
selection_sort(list1)
print()
print("Ordenamiento Selection Sort:")
for number1 in list1:
    print(number1, end=" ")

#----------------------------------------------------------------------#
#Insertion Sort

list2 = [1, 34, 5, 125, 22, 11, 99]
insertion_sort(list2)
print()
print("Ordenamiento Insertion Sort:")
for number2 in list2:
    print(number2, end=" ")

#----------------------------------------------------------------------#
#Marge Sort

list3 = [1, 34, 5, 125, 22, 11, 99]
merge_sort(list3)
print()
print("Ordenamiento Merge Sort:")
for number3 in list3:
    print(number3, end=" ")

#----------------------------------------------------------------------#
#Quick Sort

list4 = [1, 34, 5, 125, 22, 11, 99]
quick=quick_sort(list4)
print()
print("Ordenamiento Quick Sort:")
for number4 in quick:
    print(number4, end=" ")

#----------------------------------------------------------------------#
# _ BUSQUEDA
#----------------------------------------------------------------------#
#Binaria

print()
print("Busqueda Binaria:")
list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target =int(input("_ Ingrese el numero que desea buscar: "))
result = binary_search(list5, target)
if result != -1:
    print(f"El elemento {target} se encuentra en la posición {result}.")
else:
    print(f"El elemento {target} no se encuentra en la lista.")

#----------------------------------------------------------------------#
#Lineal

print("Busqueda Lineal:")
list6 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target1 =int(input("_ Ingrese el numero que desea buscar: "))
result1 = linear_search(list6, target1)
if result1 != -1:
    print(f"El elemento {target1} se encuentra en la posición {result1}.")
else:
    print(f"El elemento {target1} no se encuentra en la lista.")
