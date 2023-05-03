#Creamos la clase modelo que en este caso se llama Robot
class Robot:

    #Creamos e instanciamos los atributos
    def __init__(self):
        self.rotation = 0
        self.elevation = 0
        self.length = 0
        

    #Creamos los metodos
    def move_rotation(self, rotation): # aqui definimos los grados de rotación que se movera el robot
        self.newrotation=rotation
        self.rotation=self.newrotation + self.rotation
        if self.rotation >360: #se añade la excepcion de los 360 grados por seguridad del robot
            print("Límite de grados alcanzado: volviendo a posicion original . . .")
            self.rotation = 0
        else:   
            print(f"El robot está moviéndose {self.rotation} grados.")
    
    def move_elevation(self, elevation):  # se define cuantos grados se eleverá el robot
        self.newelevation=elevation
        self.elevation = self.newelevation + self.elevation
        if self.elevation >180: # se añade la exceocion de 180 grados mas allá de este valor podria romper el robot
            print("Limite de grados alcanzado, volviendo a posicion original . . .")
            self.elevation=0
        else:
            print(f"El robot está elevándose {self.elevation} grados.")

    def move_length(self, length): #se define los cm que se movera el robot
        self.newlength=length
        self.length=self.newlength + self.length
        # no se añade excepcion dado que no se conoce el rango de alcance del robot en cuestión
        print(f"El robot está estirándose {self.length} cm.")

    def stop_movement(self):
        print("Deteniendo movimientos.", "Volviendo a posición inicial", sep="\n")
        
        
        
