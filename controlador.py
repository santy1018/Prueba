# -*- coding: utf-8 -*-
"""
Created on Tue May  2 22:40:12 2023

@author: Hp
"""

"""Importamos nuestros módulos creados con anterioridad para que el controlador las una"""
from Robot import Robot
from vista import menu, get_rotation, get_elevation, get_length

class Controlador:
    def __init__(self):
        self.robot = Robot()

    def run(self):
        while True:
            opcion = menu()
            if opcion == "1":
                self.robot.move_rotation(get_rotation()) # se invoca al metodo de mover rotación
                
            elif opcion == "2":
                self.robot.move_elevation(get_elevation()) # se invoca al metodo de mover la elevación
            elif opcion == "3":
                self.robot.move_length(get_length()) # se invoca al metdo de estiramiento
            elif opcion == "4":
                self.robot.stop_movement() #se invoca al metodo de detener movimiento
                break #rompemos el bucle a la vez que se devuelve el robot a la posicion original
            else:
                print("Opción inválida. Intente nuevamente.")
                # añadimos esta excepcion por si algun usuario no ingresa correctamente la opción

