# x=0
# valor de incremento= 1
# condicion de salida= >= 30
# interrupcion de la ejecucion cuando x = 15
# cada vez que se ejecuta el bucle se imprime "El valor del bucle es de: ", X
# Debes saltarte las ejecuciones con el valor de x en 4, 6 y 10.
# En cada salto de ejecución, debe mostrar los valores saltados con este mensaje: 'El valor ' + x ' de x fue omitido'
# Cuando se interrumpe la ejecución del bucle, se debe mostrar un mensaje indicándolo: 'La ejecución del bucle se interrumpió cuando x era' + x.

x=int(0)
while x in range(0,30):
    x=x+1
    if x==4 or x==6 or x==10:
        print("El valor ",x," de x fue omitido")
    elif x==15:
        print("La ejecucion del bucle se interrumpio cuando x era: ",x)
        break
    else:
        print ("El valor del buccle es:", x )
x>=30

print("------------------------------------------------------------------------------------------")

# Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. 
# Deje una línea en blanco para indicar que ha finalizado la entrada de líneas
lines = []
while True:
    line = input("Ingrese una línea de texto o deje una línea en blanco para finalizar): ")

    if not line:
        break

    lines.append(line)

for line in lines:
    print(line.upper())

print("------------------------------------------------------------------------------------------")

# Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
# La bitácora de operaciones tiene la siguiente forma:
# D 100
# R 50

# D 100 significa que depositó 100 pesos
# R 50 significa que retiró 50 pesos

# Ejemplo de una entrada:
# D 200
# D 200
# R 100
# D 50
# Introducir una línea vacía indica que ha finalizado la bitácora.
# La salida de éste programa sería:
# 350

print("_-_-_-_-_-_ CUENTA BANCARIA _-_-_-_-_-_")

account = 0
deposit = 0
withdrawal = 0

while True:
    answer=str(input("_ Ingrese D si desea depositar / _ Ingrese R si desea retirar: ").upper())
    if not answer:
        break

    if answer=="D":
        deposit = int(input("D: "))
        account= account+deposit
    else:
        if answer=="R":
            withdrawal = int(input("R: "))
            account=account-withdrawal

print("Saldo en la cuenta: ", account)
print("------------------------------------------------------------------------------------------")

# Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
# finalizando cuando se reciba un cero. Imprimir la cantidad total de números primos ingresados.
# Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.

quality_prime_numbers = 0

while True:
    try:
        number = int(input("Ingrese un número mayor que 1 (o ingrese 0 para terminar): "))
        if number == 0:
            break
        elif number <= 1:
            print("El número debe ser mayor que 1.")
        else:
            is_cousin = True
            for i in range(2, number):
                if number % i == 0:
                    is_cousin = False
                    break
            if is_cousin:
                quality_prime_numbers += 1
    except ValueError:
        print("Por favor, ingrese un número válido.")

print(f"La cantidad de números primos entre los números ingresados es: {quality_prime_numbers}")

print("------------------------------------------------------------------------------------------")

# Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, 
# que sean bisiestos y múltiplos de 10. Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe 
# ser divisible por 100, excepto que también sea divisible por 400.

initial_year = int(input("_ Ingrese el año inicial: "))
final_year = int(input("_ Ingrese el año final: "))

if final_year < initial_year:
    print("El año final debe ser mayor o igual al año inicial.")
else:
    print("Años bisiestos y múltiplos de 10 entre los años ingresados:")
    for year in range(initial_year, final_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if year % 10 == 0:
                print(year)
        else:
            continue

print("------------------------------------------------------------------------------------------")
       
# Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.

for num in range(1, 21):
    if num % 2 != 0:
        continue
    print(num)

print("------------------------------------------------------------------------------------------")

# Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.

numbers_list = [5, 10, 15, 20, 25, 30, 35, 40]

for _ in range(len(numbers_list)):
    guess = int(input("_Ingresa un numero: "))
    
    if guess in numbers_list:
        print(f"El numero {guess} esta en la lista")
        break
    else:
        print("Ese número no está en la lista. Intenta de nuevo.")


print("------------------------------------------------------------------------------------------")
# Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir al usuario seleccionar una opción.
# Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).

while True:
    print("Menu de opciones:")
    print("1. Opcion 1")
    print("2. Opcion 2")
    print("3. Opcion 3")
    print("0. Salir")
    
    choice = input("Elije una opcion: ")
    
    if choice == "1":
        print("Has seleccionado la Opcion 1.")
    elif choice == "2":
        print("Has seleccionado la Opcion 2.")
    elif choice == "3":
        print("Has seleccionado la Opcion 3.")
    elif choice == "0":
        break
    else:
        print("Opcion invalida")
