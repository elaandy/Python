#Funciones#

def mi_funcion():
    print("mi funcion, funciona")

mi_funcion()

def sumar_dos_valores (a,b):
    return print("el resultado es", a+b)

sumar_dos_valores(1,2)

def imprimir_nombre (name, user_name, alias = "sin alias"):
   return print(f"{name} {user_name} {alias}")

imprimir_nombre("Anderson","Andy")
imprimir_nombre("Anderson","Andy","Patch")

def texto(*cualquier):
    return print(cualquier)

texto("telefono", "celular", "Movil")
