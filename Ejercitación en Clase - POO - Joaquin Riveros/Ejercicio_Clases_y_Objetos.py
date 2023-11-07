from Clase import Motorbike

motorbike_1 = Motorbike("blanco","AB123CD",10,2,"Kawasaki","Ninja","2023","350 km/h","500 kg")

print("Prueba de Arrancar el motor:")
motorbike_1.start() # Muestra: "Se encendió el motor"
motorbike_1.start() # Muestra: "El motor ya está encendido"

print("Prueba de Detener el motor: ")
motorbike_1.stop() # Muestra: "Se apagó el motor"
motorbike_1.stop() # Muestra: "El motor ya estaba apagado"

motorbike_1.price = "$ 15.000.000 "

print(f"El precio de la motocicleta {motorbike_1.brand} , {motorbike_1.model} es de: {motorbike_1.price}")

# Consulta desde la clase:

print(f"El precio de la motocicleta {motorbike_1.brand} , {motorbike_1.model} es de: {motorbike_1.method_price()}")

