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
print("Practica de examen no.2: Utilizando diccionarios")
#se deja una linea en blanco para mas limpieza y que se vea aun mas pipirisnais
print("")
#ahora vamos a imprimir las instrucciones para que se vea mas completo 
print("Instrucciones:")
print("Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.")
#se imprime una linea en blanco 
print("")
#creamos un diccionario
creditos = {"Historia": 5,"Quimica": 3,"Matematicas": 6,"Ingles": 4}
#se mostraran los creditos por materia 
creditos_total = 0
for materia, credito in creditos.items():
    print(f"{materia} tiene {credito} creditos")
    creditos_total += credito
#se imprime una linea en blanco para que se vea mas impio el resultado 
print("")
#muestra el total de los creditos 
print(f"Su total de creditos en el semestre es:{creditos_total}")