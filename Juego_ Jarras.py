from random import random, shuffle
import pandas as pd
import numpy as np

'''
2) Implementar un juego donde constas de 2 jarras, de capacidad 5 y 3 litros respectivamente, y debes colocar 4 litros en la jarra de 5L.
Las opciones posibles son:
* Llenar la jarra de 3 litros
* Llenar la jarra de 5 litros
* Vaciar la jarra de 3 litros
* Vaciar la jarra de 5 litros
* Verter el contenido de la jarra de 3 litros en la de 5 litros
* Verter el contenido de la jarra de 5 litros en la de 3 litros
'''

espacio_lleno = '|***|'
espacio_vacio = '|   |'

# 1. Crear las jarras analíticamente (Crear la clase)
class Jarra: 
    def __init__(self,capacidad:int):   # Parámetro
        # Propiedades del objeto
        self.litros = []            # Atributo = representación visual de la cantidad de litros
        self.cantLitros = 0
        self.capacidad = capacidad
    
        for i in range(capacidad):  # Modificador de un atributo -> litros 
            self.litros.append('|   |')

    # Acciones que se pueden aplicar a las propiedade del objeto 
    def visualizar(self):       # Método de la clase para visualizar 
        for i in self.litros: 
            print(i)
        print('TTTTT\n')

    def vaciar(self):           # Método de la clase para vaciar la jarra 
        for i in range(self.capacidad):
            self.litros.pop()
        for i in range(self.capacidad):
            self.litros.append('|   |')
        self.cantLitros = 0

    def llenar(self):           # Método de la clase para llenar la jarra 
        for i in range(self.capacidad):
            self.litros.pop()
        for i in range(self.capacidad):
            self.litros.append('|***|')
        self.cantLitros = self.capacidad

    def verter(self, otraJarra):           # Método de la clase para verter el contenido 
        DispOtraJarra = otraJarra.capacidad - otraJarra.cantLitros

        # Version David
        if self.cantLitros > DispOtraJarra: 
            otraJarra.llenar()
            self.cantLitros -= DispOtraJarra
            for i in range(DispOtraJarra):
                self.litros.pop()
            for i in range(DispOtraJarra):
                self.litros.insert(0, '|   |')
        elif self.cantLitros <= DispOtraJarra: 
            otraJarra.cantLitros += self.cantLitros
            self.vaciar()
            for i in range(self.cantLitros):
                otraJarra.litros.pop()
            for i in range(self.cantLitros):
                otraJarra.litros.insert(0, '|***|')

# 1.1 Instanciamos el objeto 

Jarra5ltr = Jarra(5)
Jarra3ltr = Jarra(3)

# 2. Crear un menú

# * Llenar la jarra de 3 litros
# * Llenar la jarra de 5 litros
# * Vaciar la jarra de 3 litros
# * Vaciar la jarra de 5 litros
# * Verter el contenido de la jarra de 3 litros en la de 5 litros
# * Verter el contenido de la jarra de 5 litros en la de 3 litros

print("Menú:")
print("1. Llenar la jarra de 3 litros")
print("2. Llenar la jarra de 5 litros")
print("3. Vaciar la jarra de 3 litros")
print("4. Vaciar la jarra de 5 litros")
print("5. Verter el contenido de la jarra de 3 litros en la de 5 litros")
print("6. Verter el contenido de la jarra de 5 litros en la de 3 litros")
print("7. Salir")

opcion = int(input("Selecciona la acción que deseas hacer: "))

while opcion != 7:
    if opcion == 1: 
        Jarra3ltr.llenar()
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
    elif opcion == 2: 
        Jarra5ltr.llenar()
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
    elif opcion == 3: 
        Jarra3ltr.vaciar()
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
    elif opcion == 4: 
        Jarra5ltr.vaciar()
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
    elif opcion == 5: 
        Jarra3ltr.verter(otraJarra=Jarra5ltr)
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
    elif opcion == 6: 
        Jarra5ltr.verter(otraJarra=Jarra3ltr)
        Jarra3ltr.visualizar()
        Jarra5ltr.visualizar()
    print("1. Llenar la jarra de 3 litros")
    print("2. Llenar la jarra de 5 litros")
    print("3. Vaciar la jarra de 3 litros")
    print("4. Vaciar la jarra de 5 litros")
    print("5. Verter el contenido de la jarra de 3 litros en la de 5 litros")
    print("6. Verter el contenido de la jarra de 5 litros en la de 3 litros")
    print("7. Salir")
    opcion = int(input("Selecciona la acción que deseas hacer: "))


# 3. Imprimir el resultado 







# Jarra de 5 litros con 2 de contenido 
# print('|  |\n|  |\n|  |\n|**|\n|**|\nTTTT')