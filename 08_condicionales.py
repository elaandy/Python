#condicionales#

condicion = True

if condicion: #Si es verdadera la condicion se realiza
    print("se cumple")
else: #Si es falsa la condicion se realiza
    print("no cumple")

print ("funciona")

condicion = 10

if condicion == 11:
    print ("se cumple")
else:
    print("no se cumple")

print ("funcionando")

if condicion < 15 and condicion == 10:
    print("hola")

if condicion > 15:
    print("nada")
elif condicion==10:
    print("todo")

#--------------------------------#

un_string = ""

if un_string:
    print ("no es vacio")
else:
    print("es vacio")

if not un_string: #negarlo
    print ("no es vacio")
else:
    print("es vacio")
