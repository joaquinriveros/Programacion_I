"""1-Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""

# @property es para los getters y los @<nombre_del_atributo>.setter para los setters.

class Person:
    def __init__(self, name='', age=0, dni=0):
        self.__name = name 
        self.__age = age  
        self.__dni = dni  

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value
        else:
            print("La edad no puede ser un valor negativo.")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        self.__dni = value

    def show(self):
        print(f"Nombre: {self.name}")
        print(f"Edad: {self.age}")
        print(f"DNI: {self.dni}")

    def isAdult(self):
        return self.age >= 18

