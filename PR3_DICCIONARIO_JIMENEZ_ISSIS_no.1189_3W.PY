#imprime los datos de la bellisima autora 
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
print("Practica de examen no.3: Utilizando diccionarios")
#se deja una linea en blanco para mas limpieza y que se vea aun mas pipirisnais
print("")
#ahora vamos a imprimir las instrucciones para que se vea mas completo 
print("Instrucciones:")
print("Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes.")
#se imprime una linea en blanco 
print("")
#lista de asignaturas
asignaturas = ["Matematicas", "Ingles", "Quimica", "Historia"]

#diccionario para almacenar las notas
notas = {}

#preguntar la nota por cada asignatura
for asignatura in asignaturas:
    nota = input(f"¿Cuánto sacaste en {asignatura}? ")
    notas[asignatura] = nota

#mostrar las asignaturas y sus respectivas notas
for asignatura, nota in notas.items():
    print(f"En {asignatura} has sacado {nota}")
