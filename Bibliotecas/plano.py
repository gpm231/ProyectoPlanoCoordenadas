import os
from termcolor import colored

coordenadaVacía = "  "
coordenadaLlena = "0 "

#Sacar trayectoria DESDE EL ORIGEN
def sacarTrayectoriaDO(plano, coordenadaFinal):
    coordenadasAMarcar = []

    cX = int(coordenadaFinal.split(",")[0])
    cY = int(coordenadaFinal.split(", ")[1])

    signoX = max(min(cX, 1), -1) # esto es como un math.clamp en lua
    signoY = max(min(cY, 1), -1)

    mayor = max(abs(cX), abs(cY))
    menor = min(abs(cX), abs(cY))

    if (mayor == menor) or (menor == 0) or (mayor == 0): # significa que la línea será diagonal
        for i in range(0, abs(mayor)):
            coordenadasAMarcar.append("{}, {}".format(signoX*i, signoY*i))
    else:
        ratio = abs(menor/mayor)

        #Algoritmo que coge los puntos más cercanos a la trayectoria real del vector
        if mayor == abs(cY):
            for i in range(0, abs(mayor)):
                coordenadasAMarcar.append("{}, {}".format(round(signoX*i*ratio), signoY*i))
        else:
            for i in range(0, abs(mayor)):
                coordenadasAMarcar.append("{}, {}".format(signoX*i, round(signoY*i*ratio)))

    return coordenadasAMarcar

def crearPlano(xMax, yMax):
    plano = {}

    xMax = xMax
    yMax = yMax

    #Creamos el plano
    #Cada y creamos todos los cuadrados en x y los almacenamos con su coordenada
    for iy in range(int(-yMax), int(yMax)+1):
        for ix in range(int(-xMax), int(xMax)+1):
            if ix == 0:
                if iy != 0:
                    plano["{}, {}".format(ix, iy)] = "| " # cuadrados del eje y
                else:
                    plano["{}, {}".format(ix, iy)] = "|-" # el cuadrado del centro
            elif iy == 0:
                plano["{}, {}".format(ix, iy)] = "--" # cuadrados el eje x
            else:
                plano["{}, {}".format(ix, iy)] = coordenadaVacía # el resto de cuadrados

    return plano

############################################################################################################################################

# La clase que maneja el plano
class Plano:
    def __init__(self, xMax, yMax):
        self.xMax = xMax
        self.yMax = yMax

        self.plano = crearPlano(xMax, yMax)

    #En el caso de que queramos representar varios vectores sin parar el codigo habrá que usar esta función para limpiar el plano
    def resetear(self):
        self.plano = crearPlano(self.xMax, self.yMax)

    #Dibuja el plano en la consola
    def sacar(self):
        os.system('cls') # borra la consola antes de dibujar el plano

        #Hace basicamente lo mismo que la for loop que crea el plano
        for iy in range(int(self.yMax), int(-self.yMax)-1, -1):
            string = ""

            for ix in range(int(-self.xMax), int(self.xMax)+1):
                string += self.plano["{}, {}".format(ix, iy)]

            print(string)

    #Dibuja un vector en el plano
    def dibujarVector(self, coordenadaFinal, color):
        trayectoria = sacarTrayectoriaDO(self.plano, coordenadaFinal)

        for i, coordenada in enumerate(trayectoria):
            self.plano[coordenada] = colored("0 ", color)

        self.sacar()

    #Dibujar complejo
    def dibujarComplejo(self, numComplejo, color):
        trayectoria = sacarTrayectoriaDO(self.plano, "{}, {}".format(int(numComplejo.real), int(numComplejo.imag)))

        for i, coordenada in enumerate(trayectoria):
            self.plano[coordenada] = colored("0 ", color)

        self.sacar()