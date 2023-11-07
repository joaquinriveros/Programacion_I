# Crea una clase vacía llamada "motocicleta".

# Todas las motocicletas del concesionario son nuevas. Por lo tanto, vamos a añadir un
# atributo de clase para especificar ese valor siempre en todas las motos.
# Ahora, crea el método __init__ vacío, con el que le daremos unos valores a las nuevas
# instancias.

# Añade los siguientes parámetros al __init__:

# o color.
# o matricula.
# o combustible_litros.
# o numero_ruedas.
# o marca.
# o modelo.
# o fecha_fabricacion.
# o velocidad_punta.
# o peso.

# Añade otro atributo de clase. Este va a ser "motor".
# Lo utilizaremos con un valor
# booleano para especificar si el motor está en marcha o detenido. True, en marcha.
# False, detenido. Por defecto, quiero que todos los motores vengan detenidos.
# Crea dos métodos inteligentes, arrancar y detener que representarán estas dos
# acciones con las motocicletas. Estos deben ser capaces de informar en la consola de
# las siguientes cosas.

# o Método arrancar():
#  Si el motor está detenido, se indica que el motor ha arrancado.
#  Si el motor está ya en marcha y se intenta arrancar de nuevo, se indica
# que el motor ya estaba en marcha.

# o Método detener():
#  Si el motor está en marcha, se indica que el motor se ha detenido.
#  Si el motor está ya detenido, y se intenta detener de nuevo, se indica
# que el motor ya estaba detenido.

# Instancia una motocicleta. La mayoría de argumentos son libres, pero quiero que
# algunos, tengan los siguientes valores:
# o combustible litros = 10
# o numero_ruedas = 2

# Prueba los dos métodos de arranque y detención con una o dos motocicletas. Haz las
# pruebas que quieras.

# El concesionario ya tiene precio para una de las motocicletas. Añade, desde fuera de la
# clase, este nuevo atributo con un valor para uno de los dos objetos.

# Prof. Cinthia Rigoni – Programación I

# Imprime el valor que acabas de añadir desde fuera de la clase con una frase como
# esta:

# "El precio de la motocicleta 'x (marca y modelo)' es de 'x_precio' $."

# Ahora, quiero que añadas una forma de consultar el precio desde la clase con un
# método (lo mismo, que en el ejercicio 11, pero con un método).
# Llama al nuevo método con las dos motocicletas. ¿Qué ocurre con una de ellas?

class Motorbike:
    new_bike = True
    engine = False
    
    def __init__(self,color,plate,fuel_lts,wheels,brand,model,fabrication_date,max_speed,weight):
        self.color = color
        self.plate = plate
        self.fuel_lts = fuel_lts
        self.wheels= wheels
        self.brand= brand
        self.model = model
        self.fabrication_date = fabrication_date
        self.max_speed = max_speed
        self.weight = weight

    def start(self):
        if self.engine == False:
            print("Se encendió el motor")
            self.engine = True
        else:
            print("El motor ya está encendido")

    def stop(self): 
        if self.engine == True:
            print("Se apagó el motor")
            self.engine = False
        else:
            print("El motor ya estaba apagado")

    def method_price(self):
        return self.price      
