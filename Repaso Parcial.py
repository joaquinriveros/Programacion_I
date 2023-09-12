# Cajero Automático:
#----------------------------------
# Crearemos un cajero automático el cual al cliente se le pedira su usuario y contraseña el cual 
# deberá validar si coincide con los datos reales: 
# Usuario: Batman
# Contraseña: BruceWaine001
# Este cajero no permitirá retirar valores decimales y mucho menos retirar valores ilógicos.
# El programa terminará cuando el cliente desee ingresar 0 para salir o ingresando 'si' al final
# mostrando un mensaje de salida:
# Mensaje: Hasta luego, señor Waine.
import os
import time
cash= 1600300250900
counter=2
user=str(input("Ingrese su usuario: ")).title()
password=str(input("Ingrese su contraseña: "))
if user != "Batman" or password != "BruceWaine001":
    for i in range(counter,0,-1):
        time.sleep(1.5)
        os.system("cls")
        print("Usuario y/o contraseña incorrecto.")
        print(f"{i} intentos restantes..")
        user=str(input("Ingrese su usuario: ")).title()
        password=str(input("Ingrese su contraseña: "))
        if i == 0:
            print("Ha agotado los intentos.")    
        if user != "Batman" or password != "BruceWaine001":
            continue
        else:
            break
    
if user == "Batman" and password == "BruceWaine001":
    print("Bienvenido. señor Waine.")
    time.sleep(2)
    while True:
        time.sleep(2)
        os.system("cls")
        print("Operaciones:")
        print("0: Salir")
        print("1: Ver saldo")
        print("2: Extraccion")
        print("3: Deposito")
        operator=int(input())
        if operator == 0:
            break
        elif operator == 1:
            print(f"Saldo disponible: $ {cash}")
        elif operator == 2:
            extract=float(input("Ingrese el monto a extraer: "))
            if float(extract) != int(extract):
                print("Incorrecto, solo números enteros..")
            else:
                if extract > cash:
                    print("Fondos insuficientes. ")
                    print(f"Saldo disponible: $ {cash}")
                elif extract < 0:
                    print("No es posible la extracción de montos negativos.")
                else:
                    cash -= extract
                    print(f"Saldo disponible: $ {cash}")
        elif operator == 3: 
            add=float(input("Ingrese el monto a depositar: "))
            if float(add) != int(add):
                print("Incorrecto, solo números enteros..")
            else:
                if add < 0:
                    print("No es posible el depósito de montos negativos.")
                else:
                    cash += add
                    print(f"Saldo disponible: $ {cash}")
        else:
            print("Incorrecto, intente de nuevo...")    
            continue    
        print("Desea salir (si / no)")
        word=str(input()).lower()
        if word == "si":
            print("Hasta luego, señor Waine")
            break
        

