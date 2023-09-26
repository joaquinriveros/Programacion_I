#Crea un juego interactivo del ahorcado en Python. El juego debe seleccionar una palabra al
#azar de una lista de palabras predefinidas y permitir que el jugador adivine la palabra letra por
#letra. El jugador tiene un número limitado de intentos antes de perder el juego.

#Requisitos:
# _ Define una lista de palabras que el programa pueda elegir al azar para que el jugador
# adivine. Puedes usar palabras relacionadas con la programación, tecnología o
# cualquier tema que te guste.
# _ El programa debe seleccionar una palabra al azar de la lista para cada partida.
# _ El juego debe mostrar el estado actual de la palabra oculta con guiones bajos (_) que
# representan las letras no adivinadas y las letras adivinadas deben mostrarse en su
# lugar correspondiente.
# _ El jugador debe poder ingresar una letra adivinada en cada turno.
# _ El programa debe verificar si la letra adivinada está en la palabra secreta y actualizar el
#   tablero en consecuencia.
# _ El jugador tiene un número limitado de intentos (por ejemplo, 6) antes de perder el
# juego.
# _ Muestra mensajes informativos al jugador, como "Adivinaste una letra correctamente"
# o "Letra incorrecta, te quedan X intentos".
# _ El juego debe terminar cuando el jugador adivina todas las letras o se quedan sin
# intentos.
# _ Proporciona un mensaje de victoria si el jugador adivina la palabra y un mensaje de
# derrota si se quedan sin intentos.

#Consideraciones adicionales:
# _ Puedes utilizar funciones para organizar tu código de manera efectiva.
# _ Agrega comentarios para explicar el funcionamiento de tu código.

import random 

#EL programa elije una palabra al azar
words_list=["javascript","java","python","html"]
chosen_word=random.choice(words_list)

# Función para mostrar la palabra oculta con letras adivinadas
def mostrar_palabra(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            result += "_"
    return result

# Función principal del juego
secret_word = chosen_word
attempts = 6  
guessed_letters = []
game_over = False

print("_.-_.-_.-_.-_.- AHORCADO -._-._-._-._-._")
    
while not game_over:
    current_word = mostrar_palabra(secret_word, guessed_letters)
    print("\nPalabra:", current_word)
    letter = input("Ingresa una letra: ").lower()
    
    #Se verifica que la letra ingresada no sea la misma
    if letter in guessed_letters:
        print("Esa letra ya fue adivinada")
    #Se verifica que la letra ingresada se encuentre en la palabra elegida    
    elif letter in secret_word:
        guessed_letters.append(letter)
        print("¡Excelente! Adivinaste una letra")
    #Si la letra no se encuentra en la palabra elegida tira error y muestra los intentis    
    else:
        guessed_letters.append(letter)
        attempts -= 1
        print("Incorrecto. Te quedan {} intentos.".format(attempts))

    #Si finaliza los intentos pierde el usuario
    if attempts == 0:
        print("\n¡Perdiste! La palabra correcta era '{}'.".format(secret_word))
        game_over = True
    
    #Si acierta todas las letras de la palabra gana 
    if "_" not in mostrar_palabra(secret_word, guessed_letters):
        print("\n¡Ganaste! La palabra es '{}'.".format(secret_word))
        game_over = True


