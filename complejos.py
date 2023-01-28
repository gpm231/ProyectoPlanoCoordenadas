import random
import math
import time
from termcolor import colored

import Bibliotecas.plano as moduloPlano

tamañoPlano = 25

plano = moduloPlano.Plano(round(tamañoPlano*1.35), tamañoPlano) # el *1.35 es para compensar que los caracteres en un ordenador son más altos que anchos

def aFormatoI(complejo):
    complejoFormatoJ = str(complejo)
    index = complejoFormatoJ.find("j")
    return complejoFormatoJ[:index] + "i" + complejoFormatoJ[index+1:]

# Transforma el complejo en formato i (5+3i) al formato de python (5+3j)
# Saca también el conjugado y el opuesto
def representarComplejo(numComplejo):
    complejoFormatoI = str(numComplejo)
    index = complejoFormatoI.find("i")
    complejoFormatoPy = complex(complejoFormatoI[:index] + "j" + complejoFormatoI[index+1:])

    plano.resetear()

    plano.dibujarComplejo(complejoFormatoPy, "blue")
    plano.dibujarComplejo(complejoFormatoPy.conjugate(), "red")
    plano.dibujarComplejo(-complejoFormatoPy, "green")

    return complejoFormatoPy

entrada = str(input("Introduce el número complejo: "))
complejoEnFormatoPython = aFormatoI(representarComplejo(entrada))

print(colored("Número: " + str(complejoEnFormatoPython), "blue"))
print(colored("Conjugado: " + str(complejoEnFormatoPython.conjugate()), "red"))
print(colored("Opuesto: " + str(-complejoEnFormatoPython), "green"))