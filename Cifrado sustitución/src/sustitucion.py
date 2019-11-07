from random import shuffle
from sys import exit

class CifradoSustitucion(object):

    def __init__(self):
        self.__alfabeto = "abcdefghijklmnñopqrstuvwxyz"
        self.__L = len(self.__alfabeto)

    def generarClave(self):
        clave = list(self.__alfabeto)
        shuffle(clave)
        return "".join(clave)

    def __esValidaClave(self, clave):
        for letra in self.__alfabeto:
            if letra not in clave: return False
        return True

    def __codificar(self, mensaje, clave, modo):

        if not self.__esValidaClave(clave):
            exit("Clave: " + clave + " no es válida")

        criptograma = ""

        if modo == "cifrar":
            origen = clave
            destino = self.__alfabeto
        elif modo == "descifrar":
            origen = self.__alfabeto
            destino = clave

        for letra in mensaje:

            letra = letra.lower()

            if letra in self.__alfabeto:
                i = origen.find(letra)
                criptograma += destino[i]

            else:
                criptograma += letra

        return criptograma

    def cifrar(self, mensaje, clave):
        return self.__codificar(mensaje, clave, "cifrar")

    def descifrar(self, criptograma, clave):
        return self.__codificar(criptograma, clave, "descifrar")
