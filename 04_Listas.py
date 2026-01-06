#listas#

otra_lista = [99, 88, "andy", 1.73]
mi_lista = [22, 33, 44, 55, 66, 77, 88, 99]

print(otra_lista[2])

print(mi_lista.count(22))#contar cuantas veces se repite el dato en la lista

otra_lista.append("Patch")
mi_lista.insert(2, "andy")#insertar en una posicion de la lista en concreto
print(mi_lista, otra_lista)
mi_lista.pop(1)#eliminar elemento de la lista
otra_lista[0]="rrr"#remplazar el valor
otra_lista.reverse()#la ordena al reves la lista
print(mi_lista, otra_lista)