# -*- coding: utf-8 -*-
"""
Created on Wed May  2 23:07:42 2023

@author: Hp
"""

""" desplegamos un menú de opciones para que el usuario vea los grados de libertad
que viene incluido el robot"""
def menu(): 
    print("Bienvenido a la intrfaz de control robótico", 
          "Para asegurar el funcionamiento, mostraremos a continuacion las opciones a elegir: ",
          "1. Girar o Rotacion", "2, Elevar", "3. Estirar", "4. Detener", sep="\n")

    opcion = input("Seleccione una opción para ser ejecutada por el robot: ")
    return opcion
""" cremos los metodos para obtener los valores que desee ingresar el usuario
esto va asociado en el modelo para verificar las acciones que el usuario ingresó previamente
se ejecuten"""
def get_rotation():

    rotation=int(input('¿Cuantos grados debe rotar el robot?: '))
    #Añadimos una excepcion en caso se ingrese un valor mas alla de los 360 grados 
    #por temas de seguridad del robot
    if rotation >360 and rotation<0:
        print("El valor va mas alla de los 360 grados por favor intentelo nuevamente")
        rotation=int(input("¿Cuantos grados debe rotar el robot?: "))
        return rotation
    else:
        return rotation
def get_elevation():
    elevation=int(input('¿Cuantos grados debe elevarse el robot?: '))
    #Añadimos una excepcion para evitar que la elevacion del robot vaya mas allá de los 
    #180 grados, por temas de seguridad del robot

    if elevation >180:
        print("El valor ingresado va mas allá de los 180 grados por fvor intente nuevamente")
        elevation=int(input("¿Cuantos grados debe elevarse el robot?: "))
        return elevation
    
    else:
        return elevation
def get_length():
    length=int(input('¿Cuantos cm debe estirarse el robot?: '))
    return length
                       
#Toda la parte grafica que interactua con el usuario
