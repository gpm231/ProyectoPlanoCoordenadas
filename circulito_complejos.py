import math
import time
from termcolor import colored

import Bibliotecas.plano as moduloPlano

tamañoPlano = 22

plano = moduloPlano.Plano(round(tamañoPlano*1.35), tamañoPlano) # el *1.35 es para compensar que los caracteres en un ordenador son más altos que anchos

def aFormatoI(complejo):
    complejoFormatoJ = str(complejo)
    index = complejoFormatoJ.find("j")
    return complejoFormatoJ[:index] + "i" + complejoFormatoJ[index+1:]


# Saca también el conjugado y el opuesto
def representarComplejo(numComplejo):
    plano.resetear()

    plano.dibujarComplejo(numComplejo, "blue", sacar=False)
    plano.dibujarComplejo(numComplejo.conjugate(), "red", sacar=False)
    plano.dibujarComplejo(-numComplejo, "green")


def crearCirculo(velocidad, divisiones):
    stepAngulo = math.pi/divisiones
    angulo = 0

    while True:#angulo < 2*math.pi:
        numero = 0+0j
        if math.sin(angulo) >= 0:
            numero = complex("{}+{}j".format(round(math.cos(angulo)*tamañoPlano*1.35), round(math.sin(angulo)*tamañoPlano))) # construye el complejo
        else:
            numero = complex("{}{}j".format(round(math.cos(angulo)*tamañoPlano*1.35), round(math.sin(angulo)*tamañoPlano))) # construye el complejo

        representarComplejo(numero)

        print(colored("Número: " + str(aFormatoI(numero)), "blue", attrs=["underline"]))
        print(colored("Conjugado: " + str(aFormatoI(numero.conjugate())), "red"))
        print(colored("Opuesto: " + str(aFormatoI(-numero)), "green"))

        angulo += stepAngulo
        time.sleep(1/velocidad)

crearCirculo(7, 30)