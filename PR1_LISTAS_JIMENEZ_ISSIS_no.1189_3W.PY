#imprime los datos de la guapisima e inteligente autora 
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
print("Practica de examen no.1: Utilizando listas")
#se deja una linea en blanco para mas limpieza y que se vea aun mas pipirisnais
print("")
#ahora vamos a imprimir las instrucciones para que se vea mas completo 
print("Instrucciones:")
print("Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.")
#imprime una linea en blanco 
print("")
#listas de las materias 
materias = ["matematicas", "quimica", "ingles", "historia"]
#preguntamos las calificaciones y eliminamos las aprobadas
for materias in materias[:]:
#creamos una copia 
    nota = int(input(f"Ingresa tu calificación para {materias}:"))
    if nota >= 6:
        materias.removesuffix(materias)
#aqui se mostraran las materias que se deben repetir 
print("Debes repetir las siguientes materias:")
for materias in materias:
    print(materias)
