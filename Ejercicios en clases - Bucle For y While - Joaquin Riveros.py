#1-	Un grupo de amigos decide organizar un juego de estrategia, para lo cual forman dos
# equipos de 6 integrantes cada uno, donde un integrante de cada equipo es el “jefe” y
# los otros 5 son sus “oficiales”. La regla más importante del juego es que sólo se
# comunicarán mediante un canal común, por lo que deben buscar la forma de ocultar el
# contenido de sus mensajes. Uno de los equipos decide utilizar un método antiguo de
# encriptación llamado “la cifra del césar”, que consiste en correr cada letra del mensaje
# –considerando la posición de cada una en el alfabeto– una determinada cantidad de
# lugares. Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” se transforma
# en “CVCSWG”. Cada día, el “jefe” del equipo debe enviar un mensaje a cada uno de sus
# oficiales. Escribir un programa que permita encriptar los 5 mensajes. El corrimiento
# (cantidad de lugares que se correrán las letras) será dado por el usuario antes de
# comenzar a encriptar. Los 5 mensajes usarán el mismo corrimiento. Nota: si el alfabeto
# termina antes de poder correr la cantidad de lugares necesarios, se vuelve a comenzar
# desde la letra “a”. Ejemplo: la palabra “EXTRA” corrida 3 lugares se convierte en
# “HAWUD”. Utilizando el alfabeto español, de 27 letras, el siguiente cálculo matemático
# permite volver a comenzar por el principio una vez que se llegó a la “z”: (índice de la
# letra a correr+corrimiento)%27 Sólo se encriptarán las letras de los mensajes, dejando
# al resto de caracteres sin modificación.
print("--------------------------------------------------")
print(".-.-.-.-.-.-.-. LA CIFRA DEL CESAR .-.-.-.-.-.-.-.")
desplazamiento = int(input("Ingrese un numero para el desplazamiento del cifrado César: "))
mensajes = []#lista vacia la cual se va a ir llenando con el bucle for y el metodo append 
i=0
for i in range(5):#Con este bucle for guardo los 5 mensajes a convertir
    mensaje = input(f"Ingresa el mensaje {i+1}: ") # A "f" lo coloco para que me tome la operacion {i+1}
    mensajes.append(mensaje) #se coloca mensajes.append(mensaje) ya que quiero ir agregandole a mi lista vacia cada mensaje que voy ingresando

print("\n__________ CONVERSION DE LOS MENSAJES __________") #El \n es un carácter que representa un salto de línea que cuando se imprime la salida siguiente se imprime en una nueva linea 
for mensaje in mensajes:#Con este bucle for lo que voy a hacer es la convertibilidad a la cifra del cesar
    mensaje_convertido = ""
    for caracter in mensaje:
        if 'a' <= caracter <= 'z':#con este if el programa ve donde esta ubicado cada caracter a convertir y si esta en minusculas o mayusculas
            nuevo_codigo = ord(caracter) + desplazamiento #La función "ord()"" busca la ubicacion Unicode del caracter
            if caracter.islower():#Este metodo de cadena me permite verificar si los caracteres ingresados estan en minusculas
                if nuevo_codigo > ord('z'):
                    nuevo_codigo -= 26
            mensaje_convertido += chr(nuevo_codigo)
        elif 'A' <= caracter <= 'Z':
            nuevo_codigo = ord(caracter) + desplazamiento
            if caracter.isupper():#Este metodo de cadena me permite verificar si los caracteres ingresados estan en mayusculas
                if nuevo_codigo > ord('Z'):
                    nuevo_codigo -= 26
            mensaje_convertido += chr(nuevo_codigo)
        else:
            mensaje_convertido += caracter
    print(mensaje_convertido)

print("--------------------------------------------------")

# Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
# 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
# Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.

digitosPares=0 #Variable en la que se va cargar la cantidad de digito pareas leidos
digitosImpares=0 #Variable en la que se va cargar la cantidad de digito impareas leidos
while True: #Usamos el Bucle While
    numero = int(input("_ Ingrese un número entero positivo (ingrese 0 para terminar): "))#solicitamos al usuario que ingrese un numero
    if numero == 0:#si es 0 el bucle se detiene
        break
    
    digitos_pares = 0 #Variable en la que se carga la cantidad de digitos pares que tiene el numero ingresado
    digitos_impares = 0 #Variable en la que se carga la cantidad de digitos impares que tiene el numero ingresado

    while numero > 0:#Bucle While el cual cuenta cuantos digitos para e impares tiene el numero
        digito = numero % 10
        if digito % 2 == 0:
            digitos_pares += 1
            digitosPares+=1
        else:
            digitos_impares += 1
            digitosImpares+=1
        numero //= 10

    print("El número tiene ",digitos_pares," dígitos pares y ",digitos_impares," dígitos impares.")

#Se imprime las cantidades de pares e impares leidos
print("_ Cantidad de digitos pares leidos es: ", digitosPares)
print("_ Cantidad de digitos impares leidos es: ", digitosImpares)


