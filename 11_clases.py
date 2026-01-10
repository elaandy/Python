#Clases#

class UnaPersona:
    pass

print(UnaPersona)

class Persona:
    def __init__(self, name, lastname):
        self.namee = name
        self.lastnamee = lastname

persona = Persona("Anderson", "Ramirez")
print(f"{persona.lastnamee} {persona.namee}")

class PersonaDos:
    def __init__(self, name, lastname): #constructor instancia por defecto de python:
        self.nombre_completo = f"{lastname} {name}"

    def comer(self): #una clase en donde con self puedo llamar la mismos valores de la clase:
        print(f"{self.nombre_completo} esta comiendo")
persona = PersonaDos("Anderson", "Ramirez")

print (persona.nombre_completo())
persona.comer()

