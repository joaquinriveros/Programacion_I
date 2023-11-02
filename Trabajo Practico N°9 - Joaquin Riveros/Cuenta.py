"""2-Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). 
El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos."""

# @property es para los getters y los @<nombre_del_atributo>.setter para los setters.

class Account:
    def __init__(self, holder='', balance=0):
        self.__holder = holder  
        self.__balance = balance  

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, value):
        self.__holder = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    def show(self):
        print(f"Titular: {self.holder}")
        print(f"Cantidad: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("La cantidad ingresada debe ser mayor que 0.")

    def withdraw(self, amount):
        self.balance -= amount
