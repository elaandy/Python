#Diccionario#

un_diccionario = dict()

un_diccionario = {"Nombre": "Andy", "Apodo":"Patch", "altura":1.73, 1:"Angelica"}

print(un_diccionario)

otro_diccionario = {"Nombre": "Andy", "Apodo":"Patch", "altura":1.73, 1:{"Angelica", "Maria", "Martinez", "Velandia"}} #Dato asociado a un Valor

print(otro_diccionario[1])

un_diccionario["almuerzo"] = "Arroz paisa", "Arroz con pollo" #agregar un nuevo dato al diccionario
del un_diccionario["Nombre"]  #Eliminar un dato del diccionario


print(un_diccionario.items())
print(un_diccionario.keys())
print(un_diccionario.values())

#Crear diccionario con datos pero sin valores
un_diccionario = dict.fromkeys(otro_diccionario)
print (un_diccionario)

#Crear diccionario con datos pero todos con valores predeterminados que yo le ponga
un_diccionario = dict.fromkeys(otro_diccionario, ("Angelica", "Maria"))
print (un_diccionario)