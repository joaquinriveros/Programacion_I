import random 
#-----------------------------------------------------------------------------------#
# Escribir una función que simule el siguiente experimento: Se tiene una rata en una
# jaula con 3 caminos, entre los cuales elige al azar (cada uno tiene la misma
# probabilidad), si elige el 1 luego de 3 minutos vuelve a la jaula, si elige el 2 luego de 5
# minutos vuelve a la jaula, en el caso de elegir el 3 luego de 7 minutos sale de la jaula.
# La rata no aprende, siempre elige entre los 3 caminos con la misma probabilidad, pero
# quiere su libertad, por lo que recorrerá los caminos hasta salir de la jaula.
# La función debe devolver el tiempo que tarda la rata en salir de la jaula.

def mouse_escape():
    choice = random.randint(1, 3)
    
    if choice == 3:
        return 7
    elif choice == 2:
        return 5 + mouse_escape()
    elif choice == 1:
        return 3 + mouse_escape()

time = mouse_escape()
print(f"La rata tardó {time} minutos en escapar de la jaula.")

#-----------------------------------------------------------------------------------#
# Escrubir una función recursiva que tome un número entero como entrada y devuelva sus 
# dígitos en orden inverso como una cadena

def f(n):
    s=str(n)
    if len(s)<=1:
        return s
    return s[-1] + f(int(s[:-1])) 