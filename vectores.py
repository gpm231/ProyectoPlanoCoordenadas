import random
import math
import time

import Bibliotecas.plano as moduloPlano

tamañoPlano = 22

plano = moduloPlano.Plano(round(tamañoPlano*1.35), tamañoPlano) # el *1.35 es para compensar que los caracteres en un ordenador son más altos que anchos

#while True:
    #plano.resetear()
    #plano.dibujarVector("{}, {}".format(random.randrange(-plano.xMax, plano.xMax), random.randrange(-plano.yMax, plano.yMax)), "red")
    #time.sleep(0.2)
#plano.dibujarVector("{}, {}".format(0, -16))

#entrada = str(input("Introduce el vector: "))
#while (str(input()) != "stop"):
    #plano.dibujarVector(entrada)
    #entrada = str(input("Introduce el vector: "))

entrada = str(input("Introduce el vector: "))
plano.dibujarVector(entrada, "red")