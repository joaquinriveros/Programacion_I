import pytest
from Trabajo_Práctico_5_Programacion_1_Funciones import *

# 1)_

@pytest.mark.parametrize(
    "dni,result",
    [
        ("43417393", True),
        ("4341739" , True),
        ("12345" , False),
    ]
)
def test_validator(dni,result):
    assert validator(dni) == result

# 2)_

@pytest.mark.parametrize(
    "sentence,result",
    [
        ("hola mundo",5),
        ("programacion",12),
        ("",0),
    ]
)
def test_length(sentence,result):
    assert length(sentence) == result

# 3)_

@pytest.mark.parametrize(
    "completed_name,result1,result2",
    [
        ("Jose Emiliano","Jose","Emiliano"),
        ("Maria","Maria",""),
        ("","",""),
    ]
)
def test_name_validator(completed_name,result1,result2):
    assert name_validator(completed_name) == (result1,result2)

@pytest.mark.parametrize(
    "dni,result",
    [
        ("43417393","43417393"),
        ("1234567","1234567"),
        ("",False),
        ("12345",False)
    ]
)
def test_validator_dni(dni,result):
    assert validator_dni(dni) == result    

# 4)_

@pytest.mark.parametrize(
    "number1, number2, result",
    [
        (4, 2, True),
        (3, 9, True),
        (5, 10, True),
        (3, 9, True),
        (6, 5, False),
        (8, 7, False),
    ]
)
def test_is_multiple_number(number1, number2, result):
    assert is_multiple_number(number1, number2) == result

# 5)_

@pytest.mark.parametrize(
    "temp_max,temp_min,result",
    [
        (20,10,15),
        (10,10,10),
        (22,2,12),
        (30,1,15.5),
    ]
)
def test_mid_temp(temp_max,temp_min,result):
    assert mid_temp(temp_max, temp_min) == result    

@pytest.mark.parametrize(
    "middle_temp,result",
    [
        ([5,10,15],10),
        ([10,10,22],14),
        ([4,8,12],8),
        ([10,25,40],25),
    ]
)
def test_average(middle_temp,result):
    assert average(middle_temp) == result   

# 6)_

@pytest.mark.parametrize(
    "text,result",
    [
        ("Jose","J o s e "),
        ("Hola mundo","H o l a   m u n d o "),
    ]
)
def test_text_to_string(text,result):
    assert text_to_string(text) == result   

# 7)_   

@pytest.mark.parametrize(
    "list_number,result",
    [
        ([4,5,8,3,7,9,10],[3,10]),
        ([7,2,5,21,9,12,5,9],[2,21]),
    ]
)
def test_max_to_min(list_number,result):
    assert max_to_min(list_number) == result   

# 8)_

import math
@pytest.mark.parametrize(
    "radio,result1,result2",
    [
        (3,(math.pi * (3**2)),(math.pi * (2*3))),
        (9,(math.pi * (9**2)),(math.pi * (2*9))),
    ]
)
def test_area_perimeter(radio,result1,result2):
    assert area_perimeter(radio) == (result1,result2)  

# 9)_

@pytest.mark.parametrize(
    "user,password,tries,result,new_tries",
    [
        ("usuario1","asdasd",1,True,1),
        ("usuario1","asdasd",2,True,2),
        ("hacker","python",2,False,3),
    ]
)
def test_login(user,password,tries,result,new_tries):
    assert login(user,password,tries) == (result,new_tries)  
  
# 10)_

@pytest.mark.parametrize(
    "prices,result",
    [
        ({1: "1000,20%"},800),
        ({2: "1500,30%"},1050),
        ({3: "2000,10%"},1800),
        ({4: "3000,20%"},2400),
        ({5: "5000,20%"},4000),
    ]
)
def test_discount_prices(prices,result):
    assert discount_prices(prices) == (result)  

# 11)_

@pytest.mark.parametrize(
    "list1,result",
    [
        ([1,2,3,4,5],[2,4,6,8,10]),
    ]
)
def test_multiplication(list1,result):
    assert multiplication(list1) == (result)  

@pytest.mark.parametrize(
    "list1,result",
    [
        ([1,2,3,4,5],[4,16,36,64,100]),
    ]
)
def test_exponent_list(list1,result):
    assert exponent_list(list1) == (result)     

# 12)_

@pytest.mark.parametrize(
    "string,result",
    [
        ("programa",{"programa":8}),
        ("python",{"python":6}),
        ("computacion",{"computacion":11}),
    ]
)
def test_string_to_dict(string,result):
    assert string_to_dict(string) == result

# 13)_

@pytest.mark.parametrize(
    "mass,aceleration,result",
    [
        (5,9.8,49),
        (6,10,60),
        (30,9.8,294),
    ]
)
def test_module_vect(mass,aceleration,result):
    assert module_vect(mass,aceleration) == result

# 14)_

@pytest.mark.parametrize(
    "prime_number,result",
    [
        (11,True),
        (19,True),
        (29,True),
        (14,False),
        (18,False),
        (27,False),
    ]
)
def test_prime_validator(prime_number,result):
    assert prime_validator(prime_number) == result

# 15)_

@pytest.mark.parametrize(
    "number,result",
    [
        (0,1),
        (6,720),
        (4,24),
        (5,120),
    ]
)
def test_factorial_number(number,result):
    assert factorial_number(number) == result

# 16)_

@pytest.mark.parametrize(
    "number,digit,result",
    [
        (-3,4,False),
        (56,-2,False),
        (31235,3,True),
    ]
)
def test_validator_number_digit(number,digit,result):
    assert validator_number_digit(number,digit) == result

@pytest.mark.parametrize(
    "number,digit,result",
    [
        (123456765,5,2),
        (33456578,3,2),
        (12345678532,8,1),
    ]
)
def test_number_digit(number,digit,result):
    assert number_digit(number,digit) == result

# 17)_

@pytest.mark.parametrize(
    "number,digit,result",
    [
        (5,7,True),
        (19,3,True),
        (-2,8,False),
        (4,-2,False),
    ]
)
def test_validator_number_digit_2(number,digit,result):
    assert validator_number_digit_2(number,digit) == result

@pytest.mark.parametrize(
    "prime_number,digit,counter,sum_digit",
    [
        (29,2,1,11),
        (97,5,0,16),
        (31,3,1,4),
    ]
)
def test_number_digit_2(prime_number,digit,counter,sum_digit):
    assert number_digit_2(prime_number,digit) == (counter,sum_digit)

@pytest.mark.parametrize(
    "prime_number,result",
    [
        (29,29),
        (11,11)
    ]
)
def test_bigger_prime_number(prime_number,result):
    assert bigger_prime_number(prime_number) == (result)
   