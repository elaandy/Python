#Variables;
"""
mango = "Delicoso"

print(mango)

una_variable = "Mi primera Variable"
print(una_variable)

variable_entera = 3
print(variable_entera)

variable_extrema = 2 - 7j #Operaciones algebraicas;
print(variable_extrema)

convertidor_variable = str(variable_entera)
    
#prueba de poner varias variables en un print; 
#Cibcatebación de variables;

print(variable_extrema, variable_entera, una_variable)

print(type(convertidor_variable))

#Funciones del sistema;

print(len(una_variable)) #cuenta los carecteres;

print("Hola como estas?:", variable_extrema)

#variables de una sola linea;

nombre, apellido, apodo, juego_fav = "Anderson", "Ramirez", "Andy", "lol"

print("Mi nombres es", nombre, apellido, "pero me dicen", apodo, "mi juego favorito es", juego_fav) #Se puede hacer pero puede ser mala practica;

# Inputs agregar datos;

nombre_user = input("Cual es tu nombre")
edad_user = input("Cual es tu edad")

print("Hola", nombre_user, "eres joven para tener", edad_user, "años" )


def walter_Blanco_lochupa(num1, num2):
    return("amor mio el resultado es", num1-num2 )

print(walter_Blanco_lochupa(8,2))

def area(perimetro):
    return"El area del circulo es", (perimetro*perimetro)*3.14159

print(area(5))

Escribir una función que calcule el total de una factura tras 
aplicarle el IVA. La función debe recibir la cantidad sin IVA y 
el porcentaje de IVA a aplicar, y devolver el total de la factura. 
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%."""

def aplicarIva(Valor_factura, iva):
    if isinstance(Valor_factura, int) and isinstance(iva, int):
       if iva==0:
          iva=0.19
          return f"el valor total de la factura con iva es de: {Valor_factura*iva+Valor_factura} el valor sin iva es de: {Valor_factura} el iva del 19% es de: {Valor_factura*iva}"
       else:
          iva=iva/100
          return f"el valor total de la factura con iva es de: {Valor_factura*iva+Valor_factura} el valor sin iva es de: {Valor_factura} el iva del {100*iva} % es de:{Valor_factura*iva}"
    else:
       return "Escriba bien sapo perro"
    
print(aplicarIva(15000,20))