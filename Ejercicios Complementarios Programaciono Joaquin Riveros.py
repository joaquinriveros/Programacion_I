#Ejercicios Complementarios Joaquin Riveros
#1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1=15
#2. Crea una variable llamada "numero2" asignándole un número decimal de tu elección.
numero2=5.5
#3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma=numero1+numero2
#4. Crea tres variables más, una para resta, otra para multiplicación y otra para división. Imprime estas variables.
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2
print("Los valores obtenidos son los siguientes: ")
print("suma:", suma ,"  resta:", resta ,"  multiplicacion:", multiplicacion ,"  division:", division)

print("--------------------------------------------------------------------------------------------------------------------------------------")

#5. Crea una variable llamada "nombre" y asígnale tu nombre como valor
nombre="Joaquin Riveros"
#6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el precio de un artículo ficticio
precio=1655.99
#7. Crea una variable llamada "descuento" y asígnale un valor decimal que represente el descuento aplicado al artículo.
descuento=0.35
#8. Calcular el precio final aplicando el descuento al precio original y almacena el resultado en una variable llamada "precio_final"
descuento_final=(descuento*precio/1)
precio_final=precio-descuento_final
print("El precio del producto es de: $",precio, "(pesos)")
print("El descuento que se le aplica es de un 35%")
print("El precio final del producto es de: $", precio_final, "(pesos)")
print("Cliente: ",nombre)

print("--------------------------------------------------------------------------------------------------------------------------------------")

#9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu elección. Qué sea un string.
cadena="Que entretenido estoy"
#10. Crea una nueva variable llamada "longitud". En ella, vas a almacenar la longitud en caracteres de la cadena.
longitud=len(cadena)
print("La cadena '" ,cadena, "' tiene ",longitud," caracteres")

print("--------------------------------------------------------------------------------------------------------------------------------------")

#11. Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y conviértelo en número entero.
precio2=25.56
print("La parte entera de ", precio2 ," es:", int(precio2))

print("--------------------------------------------------------------------------------------------------------------------------------------")

#12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas en una tercera variable llamada "nombre_completo"
nombre2= "Marcelo " 
apellido="Gallardo"
nombre_completo=nombre2+apellido
print("El nombre del mejor director tecnico del mundo es: ", nombre_completo)

print("--------------------------------------------------------------------------------------------------------------------------------------")

#13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad=20
incremento=edad*5
disminucion=(incremento-10*10) #Al incremento que es 100 lo disminuyo de 10 en 10, 10 veces quedandome con valor 0
print ("_ Mi edad es:", edad)
print ("_ Incremento mi edad por 5: ", incremento)
print ("_ Disminuyo mi edad en 10: ", disminucion)

print("--------------------------------------------------------------------------------------------------------------------------------------")

#14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y centímetros.
altura=1.70
calculo=(altura*4)/3
print("Altura final: ", calculo)

print("--------------------------------------------------------------------------------------------------------------------------------------")


#15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después transfórmalo todo en minúsculas.
nombre_mayusculas="JOAQUIN"
print("Mi nombre en mayusculas es: ", nombre_mayusculas)
print("Mi nombre en minusculas es: ", nombre_mayusculas.lower())

print("--------------------------------------------------------------------------------------------------------------------------------------")

#16. Con la variable con el nombre en mayúsculas, aplica un método parecido para que se transforme todo en minúsculas excepto la primera letra.
nombre_mayusculas1="JOAQUIN"
print("Mi nombre en mayusculas es: ", nombre_mayusculas1)
print("Mi nombre en minusculas es: ", nombre_mayusculas1.capitalize())