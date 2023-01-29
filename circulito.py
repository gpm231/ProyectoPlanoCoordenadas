import time
import math

import Bibliotecas.plano as moduloPlano

tamañoPlano = 22

plano = moduloPlano.Plano(round(tamañoPlano*1.35), tamañoPlano) # el *1.35 es para compensar que los caracteres en un ordenador son más altos que anchos

def crearCirculo(velocidad, divisiones):
    stepAngulo = math.pi/divisiones
    angulo = 0

    while True:#angulo < 2*math.pi:
        plano.resetear()
        plano.dibujarVector("{}, {}".format(round(math.cos(angulo)*tamañoPlano*1.35), round(math.sin(angulo)*tamañoPlano)), "green") # el *1.35 por lo que pone en la línea en la que creamos el plano
        angulo += stepAngulo
        time.sleep(1/velocidad)

crearCirculo(40, 30)