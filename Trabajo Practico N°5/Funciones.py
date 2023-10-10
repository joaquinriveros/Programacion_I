import math,time,os

# 1)_

def validator(dni):
    if len(dni)== 7 or len(dni) == 8 :
        return True
    else:
        return False
    
# 2)_

def length(sentence):
    words = sentence.split()
    # Verificamos si la lista de palabras está vacía
    if not words:  
        return 0
    last_word = len(words[-1])
    return last_word    

# 3)_

def name_validator(completed_name):
    name1 , name2 = "" , ""
    name_parts = completed_name.split()
    
    if len(name_parts) == 1:
        name1 = name_parts[0]
    elif len(name_parts) == 2 and all(part.isalpha() for part in name_parts):
        name1, name2 = name_parts[0], name_parts[1]
    return name1, name2

def validator_dni(dni):
    if len(dni) in [7, 8] and dni.isdigit():
        return dni
    else:
        return False

def validator_dni2():
    dni_verified = ""
    while not dni_verified:
        os.system("cls")
        print("Incorrecto, intente de nuevo..")
        dni_verified = input("Ingrese correctamente el DNI: ")
        if len(dni_verified) in [7, 8] and dni_verified.isdigit():
            return dni_verified

# 4)_

def is_multiple_number(number1, number2):

    if multiple_number(number1,number2) == 0:
        print(f"{number1} es múltiplo de {number2}")
    elif multiple_number(number2,number1) == 0:
        print(f"{number2} es múltiplo de {number1}")
    else:
        print("No son múltiplos entre sí...")

    return multiple_number(number1, number2)  or multiple_number(number2, number1)  

def multiple_number(number,divisor):
    return number % divisor == 0

# 5)_

def mid_temp(temp_max, temp_min):
    middle_temp = (temp_max + temp_min) / 2
    return middle_temp

def average(middle_temp):
    counter = 0
    average_temp = 0

    for temp in middle_temp:
        average_temp += temp
        counter += 1

    average_temp /= counter
    return average_temp

# 6)_

def text_to_string (text):
    new_text = ""
    for letter in text:
        new_text += letter + " "
    return new_text

# 7)_

def max_to_min (list_number):
    min_number = list_number[0]
    max_number = list_number[0]
    for i in list_number:
        if min_number >= i:
            min_number = i
        if max_number <= i:
            max_number = i
    new_list = [min_number,max_number]        
    return new_list

# 8)_

import math

def area_perimeter(radio):
    area = math.pi * radio ** 2
    perimeter = math.pi * 2 * radio
    print(f"Area: {area:.2f}; Perímetro: {perimeter:.2f}")

    return area,perimeter

# 9)_

def login(user, password, tries):
    new_tries = tries
    if user == "usuario1" and password == "asdasd":
        return True, new_tries
    else:
        new_tries += 1
        return False, new_tries

# 10)_

def discount_prices(prices):
    new_price = 0
    for price_values in prices.values():
       
        price_values = price_values.strip("%")
        price_values = price_values.split(",")

        price = int(price_values[0])
        discount = int(price_values[1])
        
        price_with_discount = price - (price * (discount / 100))
        new_price += price_with_discount

    return new_price

# 11)_

def multiplication (list1):
    new_list = []
    for number in list1:
        new_list.append(number * 2)
    return new_list

def exponent_list (list1):
    new_list = multiplication(list1)
    final_list = []
    for number in new_list:
        final_list.append(number ** 2)
    return final_list    

# 12)_

def string_to_dict (string):

    string = string.strip()
    string = string.split(" ")
    
    # string_dict = {word: len(word) for word in string} 

    string_dict = {}
    for word in string:
        string_dict [word] = len(word)

    return string_dict 

# 13)_

def module_vect (mass,aceleration):
    force = mass *aceleration
    return force

# 14)_

def prime_validator (prime_number):
    if (prime_number % 2 != 0) and (prime_number % 3 != 0) and (prime_number % 5 != 0) and (prime_number % 7 != 0):
        return True
    else:
        return False
    
# 15)_

def factorial_number(number):
    factorial = 1
    if number == 0:
        return 1
    else:
        while number != 0:
            factorial *= number
            number -= 1
        return factorial

def main_factorial(number,counter):
    new_counter = counter
    if number >= 0:
            factorial = factorial_number(number)
            print(f"El Factorial del número {number} es: {factorial}")
            new_counter += 1
    else:
        print("Por favor ingrese un número positivo o nulo..")
        return False,new_counter
    operator = input("Desea continuar? SI/NO: ").upper()
    if operator == "NO":
        print("La cantidad de números leídos en total es/son: {}".format(new_counter))
        print("Hasta luego.")
        time.sleep(3)
        os.system("cls")
        return True,new_counter
    else:
        return False,new_counter
    
# 16)_

def number_digit(number, digit):
    number_str = str(number)
    digit_str = str(digit)
    counter = 0
    for digit_in_number in number_str:
        if digit_in_number == digit_str:
            counter += 1
    return counter

def validator_number_digit(number,digit):
    if number >= 0 and digit >= 0 and digit <= 9:
        return True
    else:
        return False

# 17)_

def bigger_prime_number(prime_number):
    bigger_number = 0
    if prime_number > bigger_number:
        bigger_number = prime_number
    return bigger_number    

def number_digit_2 (prime_number,digit):
    prime_number = str(prime_number)
    digit = str(digit)
    sum_digit = 0
    counter = 0
    for digit_in_number in prime_number:
        sum_digit += int(digit_in_number)
        if digit == digit_in_number:
            counter += 1
    return counter,sum_digit

def validator_number_digit_2(number,digit):
    if number >= 0 and (digit >= 0 and digit <= 9):
        return True
    else:
        return False
 