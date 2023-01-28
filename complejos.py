import random
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

# Transforma el complejo en formato i (5+3i) al formato de python (5+3j)
# Saca también el conjugado y el opuesto
def representarComplejo(numComplejo):
    complejoFormatoI = str(numComplejo)
    index = complejoFormatoI.find("i")
    complejoFormatoPy = complex(complejoFormatoI[:index] + "j" + complejoFormatoI[index+1:])

    if complejoFormatoPy.imag < 0:
        complejoFormatoPy = complex(str(round(complejoFormatoPy.real*1.35)) + str(complejoFormatoPy.imag) + "j")
    else:
        complejoFormatoPy = complex(str(round(complejoFormatoPy.real*1.35)) + "+" + str(complejoFormatoPy.imag) + "j")

    plano.resetear()

    plano.dibujarComplejo(complejoFormatoPy, "blue")
    plano.dibujarComplejo(complejoFormatoPy.conjugate(), "red")
    plano.dibujarComplejo(-complejoFormatoPy, "green")

    return complejoFormatoPy

entrada = str(input("Introduce el número complejo: "))
complejoEnFormatoPython = representarComplejo(entrada)

print(colored("Número: " + str(aFormatoI(complejoEnFormatoPython)), "blue", attrs=["underline"]))
print(colored("Conjugado: " + str(aFormatoI(complejoEnFormatoPython.conjugate())), "red"))
print(colored("Opuesto: " + str(aFormatoI(-complejoEnFormatoPython)), "green"))