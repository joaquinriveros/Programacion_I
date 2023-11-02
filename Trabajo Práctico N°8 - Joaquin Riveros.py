# 1)_Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene

def f(n):
    s=str(n)
    return len(s)
    
while True:
    try:
        n=int(input("ingrese un valor positivo: "))
        if n:   
            result = f(n)
            break
    except(ValueError,TypeError,KeyError):
        print("hubo un error")
        continue
print(result)

# 2)_Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b

def f(n,b):
    if n % b == 0 :
        return True
    else: 
        return False    
        
while True:
    try:
        b=int(input("ingrese un numero: "))
        n=int(input("ingrese un numero que crea que es potencia del primero: "))
        break
    except(ValueError,KeyError,TypeError):
        print("hubo un error")
        continue
        
if f(n,b) == True:
    print("n es potencia de b")
else:
    print("n no es potencia de b")

# 3)_Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista
# con las posiciones en donde se encuentra b dentro de a.

def find_all_occurrences(a, b, start=0, occurrences=None):
    if occurrences is None:
        occurrences = []

    # Busca la siguiente ocurrencia de b en a a partir de la posición 'start'
    index = a.find(b, start)

    # Si no se encuentra más ninguna ocurrencia, termina la recursión y devuelve las posiciones encontradas
    if index == -1:
        return occurrences

    # Agrega la posición de la ocurrencia actual a la lista de posiciones
    occurrences.append(index)

    # Llama a la función recursivamente para buscar la siguiente ocurrencia a partir de la siguiente posición
    return find_all_occurrences(a, b, index + 1, occurrences)

# Ejemplo de uso
a = "abracadabra"
b = "a"
positions = find_all_occurrences(a, b)
print("Posiciones de '{}' en '{}': {}".format(b, a, positions))
     
# 4)_Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen
# la paridad del numero natural dado, conociendo solo que:
# •	1 es impar.
# •	Si un número es impar, su antecesor es par; y viceversa.
     
def even(n):
    if n == 0:
        return True  # El cero se considera un número par
    else:
        return odd(n - 1)

def odd(n):
    if n == 0:
        return False  # El cero se considera un número par
    else:
        return even(n - 1)

# Ejemplo de uso
number = 6

if even(number):
    print(f"{number} es un número par.")
else:
    print(f"{number} es un número impar.")


# 5)_Escribir una función recursiva que encuentre el mayor elemento de una lista.

def find_largest(lst):
  if len(lst) == 1:
    return lst[0]
  else:
    first_element = lst[0]
    rest_of_list = lst[1:]
    largest_in_rest = find_largest(rest_of_list)
    return first_element if first_element > largest_in_rest else largest_in_rest

elements = [1, 1, 3, 3, 3, 3, 7, 7]
largest = find_largest(elements)
print(f"El elemento mas grande es: {largest}")

# 6)_Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces.
# Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])

def repeat_elements(elems,times):
  elem_duplicate = []
  for i in range(0,times):
    elem_duplicate.append(elems[0])
      
  if len(elems) == 1 :
    return elem_duplicate
  else:
    return elem_duplicate + repeat_elements(elems[1:],times) 

elements_returned = repeat_elements([1, 3, 3, 7], 4)
print(elements_returned)    
    
# 7)_Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente sumatoria:
# K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
# El programa debe pedir al usuario que ingrese un número n, y un número d,
# Luego debe calcular el valor de K(n, p) usando una función recursiva,
# Debe imprimir el resultado de K(n, p)

def K(n,p):

    if n == 1:
        return p
    else:
        return p*n + K(n-1,p)

while True:
    try:
        number_n = int(input("Ingrese un numero positivo: "))
        number_d = int(input("Ingrese otro numero positivo: "))
        if number_n >= 0 and number_d >= 0:
            result = K(number_n,number_d)
            break
        else:
            print("Ingrese numeros possitivos..")
            continue    

    except(ValueError,TypeError,KeyError):
        print("Hubo un error, intente de nuevo")
        continue

print("Resultado de la sumatoria de productos: ",result)

# 8)_El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente
# manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila
# se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes
# del triángulo son todos unos. Cualquier otro valor se calcula sumando los dos valores contiguos
# de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el valor que se
# encuentra en la fila n y la columna k.

def pascal(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)

# Ejemplo de uso
n = 4  # Fila 4
k = 2  # Columna 2
resultado = pascal(n, k)
print(f'El valor en la fila {n} y columna {k} es: {resultado}')

# 9)_ Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, 
# y un número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres 
# dados (permitiendo caracteres repetidos).

def combinations(listt, k):
    def prefix_combinations(prefix):
        if len(prefix) == k:
            print(prefix)
            return
        for character in listt:
            prefix_combinations(prefix + character)
    
    if k <= 0 or not listt:
        return
    
    prefix_combinations("")

caracteres = ["A", "B", "C","D"]
k = 3
combinations(caracteres, k)

# 10)_La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 
# (210 mm de ancho y 297 mm de largo). 
# Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las siguientes medidas,
# digamos la A(N+1), 
# se definen doblando al medio la hoja A(N). Siempre se miden en milímetros con números enteros:
# entonces la hoja A1 mide 594 mm de ancho (y no 594.5) 
# por 841 mm de largo.

# Escribí una función recursiva medidas_hoja_A(N) que para una entrada N mayor que cero, devuelva
# el ancho y el largo de la hoja A(N) calculada 
# recursivamente a partir de las medidas de la hoja A(N−1), usando la hoja A0 como caso base. 
# La función debe devolver el ancho y el largo -en ese orden- en una tupla.

def measurements_sheet_A(N):
    # Caso base A0
    if N == 0:
        return (841, 1189)
    else:
        # Calcula las medidas de la hoja A(N) recursivamente a partir de A(N-1).
        width_previous, long_previous = measurements_sheet_A(N - 1)
        width_current = long_previous // 2  # '//' Se utiliza para la división entera.
        long_current = width_previous
        return (width_current, long_current)

try:
    N = int(input("Ingresa un número entre 0-10: "))
    if 0 <= N <= 10:
        width, long = measurements_sheet_A(N)
        print(f"A{N}: {width} x {long} mm")
    else:
        print("El número ingresado debe estar entre 0 y 10.")
except ValueError:
    print("Ingresa un número válido.")

