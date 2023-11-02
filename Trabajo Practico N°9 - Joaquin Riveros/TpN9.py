from Persona import Person
from Cuenta import Account
from Triangulo import Triangle
from Agenda import Agenda

"""1-Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad."""

person1 = Person("Maximiliano", 23, 44746407)
print("Datos de la persona:")
person1.show()
print(f"¿Es mayor de edad? {person1.isAdult()}\n")


"""2-Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""

account1 = Account("Valentin", 1000.0)
print("Datos de la cuenta:")
account1.show()
account1.deposit(500)
account1.withdraw(200)
print("Saldo después de operaciones:")
account1.show()

"""3-Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, 
imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno)."""

triangle1 = Triangle(3, 4, 5)
print("\nTriángulo:")
print(f"Lado con tamaño mayor: {triangle1.largest_side()}")
print(f"Tipo de triángulo: {triangle1.triangle_type()}")

"""4-Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
Además deberá mostrar un menú con las siguientes opciones:
Añadir contacto
Lista de contactos
Buscar contacto
Editar contacto
Cerrar agenda"""

agenda = Agenda()
agenda.add_contact("Maximo", "2613436698", "maxi@gmail.com")
agenda.add_contact("Jose", "2634756325", "josef258@gmail.com")
agenda.add_contact("Joaquin", "2613354836", "joakocarp@gmail.com")

while True:
    print("\nMenú de la Agenda:")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    option = input("Selecciona una opción (1/2/3/4/5): ")

    if option == "1":
        name = input("Nombre: ")
        phone = input("Telefono: ")
        email = input("Email: ")
        agenda.add_contact(name, phone, email)
    elif option == "2":
        agenda.list_contacts()
    elif option == "3":
        name = input("Nombre del contacto a buscar:  ")
        agenda.find_contact(name)
    elif option == "4":
        name = input("Nombre del contacto a editar: ")
        new_phone = input("Nuevo teléfono: ")
        new_email = input("Nuevo email: ")
        agenda.edit_contact(name, new_phone, new_email)
    elif option == "5":
        print("Agenda cerrada.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
