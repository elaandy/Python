#Tuplas#
"""
una_tupla = tuple()
otra_tupla = ()

una_tupla = (8, 11, "andy", "patch")

print(una_tupla[1])

print(una_tupla)

#una tupla tiene valores cerrados, no se puede modificar o agregar datos sin agregar otra tupla;
#se puede transformar en lista para poder modificar los datos pero no se usa es innecesario;

Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura,
y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura>
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario."""

materias_curso = ["Matematicas", "Fisica", "Quimica", "Historia", "Ingles"]
notas_curso=[]
notas_curso.append(input(f"cuanto sacaste en {materias_curso[0]} "))
notas_curso.append(input(f"cuanto sacaste en {materias_curso[1]} "))
notas_curso.append(input(f"cuanto sacaste en {materias_curso[2]} "))
notas_curso.append(input(f"cuanto sacaste en {materias_curso[3]} "))
notas_curso.append(input(f"cuanto sacaste en {materias_curso[4]} "))

print(f"Sacaste en {materias_curso[0]} {notas_curso[0]}, en {materias_curso[1]} {notas_curso[1]}, en {materias_curso[2]} {notas_curso[2]}, en {materias_curso[3]} {notas_curso[3]}, en {materias_curso[4]} {notas_curso[4]}")
