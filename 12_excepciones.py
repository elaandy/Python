#excepciones#

numero_uno, numero_dos = 2, "andy"

try:
    print(numero_uno + numero_dos)
except:
    print("Error 101")
finally:
    #se ejecuta siempre
    print("continua")

numero_dos = 2

try:
    print(numero_uno + numero_dos)
except:
    print("Error 101")
else:
    #se ejecuta si no hay una except:
    print("todo normal")
