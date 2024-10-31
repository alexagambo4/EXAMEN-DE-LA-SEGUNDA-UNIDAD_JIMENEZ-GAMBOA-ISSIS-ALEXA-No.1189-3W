#imprime los datos de la guapisisimisima autora 
print("Jimenez Gamboa Issis Alexa")
print("no.1189")
print("3W")
#imprime una linea en blanco para que se vea mas limpio el programa 
print("")
#imprime la fecha actual para que se vea mas nais el programita 
from datetime import date 
#obtener fecha actual 
fecha_actual = date.today()
#imprime la fecha 
print("Fecha:", fecha_actual)

#imprime el titulo del programa 
print("Practica de examen no.4: Utilizando funciones")
#se deja una linea en blanco para mas limpieza y que se vea aun mas pipirisnais
print("")
#ahora vamos a imprimir las instrucciones para que se vea mas completo 
print("Instrucciones: Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.")
#crear un diccionario para almacenar la información del usuario
usuario = {}

#preguntar al usuario por su información
usuario['nombre'] = input("¿Cuál es tu nombre? ")
usuario['edad'] = input("¿Cuál es tu edad? ")
usuario['direccion'] = input("¿Cuál es tu dirección? ")
usuario['telefono'] = input("¿Cuál es tu número de teléfono? ")

#mostrar la información del usuario
print(f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su número de teléfono es {usuario['telefono']}.")
