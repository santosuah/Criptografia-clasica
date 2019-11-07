import numpy as np
from copy import deepcopy

class CifradoHill(object):

	def __init__(self):
		self.__alfabeto = "abcdefghijklmnopqrstuvwxyz"
		self.__L = len(self.__alfabeto)

	def __mcd(self, a, b):
		while a != 0:
			a, b = b % a, a
		return b

	def __inversaModulo(self, n, modulo):

		if self.__mcd(n, modulo) != 1: return None

		u1, u2, u3 = 1, 0, n
		v1, v2, v3 = 0, 1, modulo

		while v3 != 0:
			q = u3 // v3
			v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

		return u1 % modulo

	def __inversaMatrizModular(self, matriz):

		# Calcular determinante matriz
		determinante = int(np.linalg.det(matriz))

		# Ajunta de la matriz multiplcandolo inversa * determinante
		adjunta = np.round((determinante * matriz.I) % self.__L, decimals=1)

		# Devolvemos la inversa del determinta * adjunta modular
		return np.int_((self.__inversaModulo(determinante, self.__L) * adjunta) % self.__L)

	def __codificar(self, mensaje, clave):

		mensajeCodificado = ""
		d = len(clave)

		# Iteramos el mensaje con saltos d
		for i in range(0, len(mensaje), d):

			# Trozeamos el mensaje en matrices
			# de tamaño dx1
			m = []
			for j in range(i, i+d):
				m.append([self.__alfabeto.find(mensaje[j])])

			# Transformamos a matriz la lista
			m = np.matrix(m)

			# Multiplicamos la matriz por la clave modular
			m = (clave * m) % self.__L

			# Volvemos transformar las listas
			m = m.tolist()

			# Por cada numero la matriz, lo transformamos en caracter
			# y lo añadimos al mensaje codificado
			for fila in m:
				for e in fila:
					mensajeCodificado += self.__alfabeto[e]

		return mensajeCodificado

	def cifrar(self, mensaje, clave):

		mensajeCopia = deepcopy(mensaje)
		congruencia = len(mensaje) % len(clave)

		# si el tamaño no se ajusta se añade caracteres
		if (congruencia != 0):
			for _ in range(congruencia):
				mensajeCopia += "x"

		return self.__codificar(mensajeCopia, clave)

	def descifrar(self, criptograma, clave):

		# Calculamos la inversa de la clave
		claveInversa = self.__inversaMatrizModular(clave)
		print(claveInversa, "(Clave inversa)")

		return self.__codificar(criptograma, claveInversa)
