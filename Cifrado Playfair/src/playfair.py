from copy import deepcopy
from collections import OrderedDict
from re import escape, sub

class CifradoPlayfair(object):

    def __init__(self):
        self.__alfabeto = "abcdefghiklmnopqrstuvwxyz"
        # Caracter especial procesado mensaje
        self.__caracterEspecial = "x"
        self.__L = len(self.__alfabeto)
        self.__ANCHO = 5

    # Quitar letras repetidas consecutivas
    # y asegurarse una longitud par
    def procesarMensaje(self, mensaje):

        # Copiamos mensaje
        mensajeCopia = deepcopy(mensaje)
        mensajeProcesado = ""

        longitudMensajeCopia = len(mensajeCopia)

        # Añadimos un caracter especial si
        # la longitud del mensaje es impar
        # (imprescindible que sea par)
        if (longitudMensajeCopia % 2) != 0:
            mensajeCopia += self.__caracterEspecial
            longitudMensajeCopia += 1

        # Iteramos el mensaje copia de dos en dos caracteres
        i = 0
        while (i < longitudMensajeCopia):

            m1 = mensajeCopia[i]
            m2 = mensajeCopia[i+1]

            # Si los dos caracteres contiguos son iguales
            if m1 == m2:

                # Añadimos una letra aleatoria enmedio
                mensajeProcesado += m1 + self.__caracterEspecial
                # Retornamos una posición (ya que sino obviamos m2)
                i -= 1

                # Correción parte final mensaje (para que sea la longitud par en todo momento)
                # sino produce una excepción
                esImpar = (longitudMensajeCopia-i) % 2 != 0
                existeAsteriscoFinal = mensajeCopia[longitudMensajeCopia-1] == self.__caracterEspecial

                # Si la longitud del mensaje es impar
                if esImpar:
                    # Y tiene * al final
                    if existeAsteriscoFinal:
                        # Lo eliminanos y disminuimos la longitud del mensaje
                        mensajeCopia = mensajeCopia[:-1]
                        longitudMensajeCopia -= 1
                    # Si no tiene *
                    else:
                        # Añadimos el asterisco
                        mensajeCopia += self.__caracterEspecial
                        longitudMensajeCopia += 1

            # sino, mantenenos el par de caracteres originales
            else:
                mensajeProcesado += m1 + m2

            i += 2

        return mensajeProcesado

    # Quitar letras repetidas de la clave
    def procesarClave(self, clave):
        return "".join(OrderedDict.fromkeys(clave))

    # Elimina las letras que aparecen en la clave
    # de el alfabeto inicial
    def limpiarAlfabeto(self, clave):
        rx = "[" + escape(clave) + "]"
        return sub(rx, "", self.__alfabeto)

    # Genera la matriz 5X5 de cifrado
    def generarMatrizCifrado(self, claveProcesada):
        return claveProcesada + self.limpiarAlfabeto(claveProcesada)

    # Busca una letra en la matriz y devuelve la posición (i,j)
    def buscarEnMatriz(self, caracter, matrizCifrado):
        i = matrizCifrado.find(caracter)
        return (i // self.__ANCHO, i % self.__ANCHO)

    # Obtiene el caracterer de la matriz de cifrado
    # indicando la fila y columna
    def matrizCifrado(self, matriz, i, j):
        return matriz[self.__ANCHO * i + j]

    # Metodo de apoyo para cifrar y descifrar
    def codificar(self, mensaje, matriz, modo):

        criptograma = ""
        sustraer = 1 if modo == "cifrar" else -1
        for i in range(0, len(mensaje), 2):

            i1, j1 = self.buscarEnMatriz(mensaje[i], matriz)
            i2, j2 = self.buscarEnMatriz(mensaje[i+1], matriz)

            # Si los caracteres estan en la misma fila
            # movemos entre columnas
            if i1 == i2:
                j1 = (j1 + sustraer) % self.__L
                j2 = (j2 + sustraer) % self.__L

            # Si los caracteres estan en la misma columna
            # avanzamos en filas
            elif j1 == j2:
                i1 = (i1 + sustraer) % self.__L
                i2 = (i2 + sustraer) % self.__L

            # Sino, en distintas filas y columnas
            else:
                j1, j2 = j2, j1

            criptograma += self.matrizCifrado(matriz, i1, j1) + self.matrizCifrado(matriz, i2, j2)

        return criptograma

    def cifrar(self, mensaje, clave):

        # Procesamos el mensaje
        mensajeProcesado = self.procesarMensaje(mensaje)

        # Procesamos la clave
        claveProcesada = self.procesarClave(clave)

        # Generamos la matriz de cifrado
        matrizCifrado = self.generarMatrizCifrado(claveProcesada)

        # Ciframos el mensaje
        return self.codificar(mensajeProcesado, matrizCifrado, "cifrar")

    def descifrar(self, criptograma, clave):

        # Procesamos la clave
        claveProcesada = self.procesarClave(clave)

        # Generamos la matriz de cifrado
        matrizCifrado = self.generarMatrizCifrado(claveProcesada)

        # Desciframos el criptograma
        return self.codificar(criptograma, matrizCifrado, "descifrar")
