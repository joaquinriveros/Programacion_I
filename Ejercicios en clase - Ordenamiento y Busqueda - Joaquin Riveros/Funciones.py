#----------------------------------------------------------------------#
# _ ORDENAMIENTO
#----------------------------------------------------------------------#
#Bubble Sort
def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

#----------------------------------------------------------------------#
#Selection Sort
def selection_sort(list1):
    n = len(list1)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if list1[j] < list1[min_index]:
                min_index = j
        
        list1[i], list1[min_index] = list1[min_index], list1[i]

#----------------------------------------------------------------------#
#Insertion Sort
def insertion_sort(list2):
    for i in range(1, len(list2)):
        key = list2[i]
        j = i - 1

        while j >= 0 and key < list2[j]:
            list2[j + 1] = list2[j]
            j -= 1
        list2[j + 1] = key

#----------------------------------------------------------------------#
#Marge Sort
def merge_sort(list3):
    if len(list3) > 1:
        middle = len(list3) // 2
        left_half = list3[:middle]
        right_half = list3[middle:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list3[k] = left_half[i]
                i += 1
            else:
                list3[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list3[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list3[k] = right_half[j]
            j += 1
            k += 1

#----------------------------------------------------------------------#
#Quick Sort
def quick_sort(list4):
    if len(list4) <= 1:
        return list4
    
    pivot = list4[len(list4) // 2]
    left = [x for x in list4 if x < pivot]
    middle = [x for x in list4 if x == pivot]
    right = [x for x in list4 if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

#----------------------------------------------------------------------#
# _ BUSQUEDA
#----------------------------------------------------------------------#
#Binaria
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 
    
    return -1 
 
#----------------------------------------------------------------------#
#Lineal
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Si el elemento no se encuentra en la lista

