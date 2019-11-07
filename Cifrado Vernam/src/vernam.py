from random import randint

# Versión orientada a caracteres
class CifradoVernam(object):

	def __init__(self):
		self.__alfabeto = "abcdefghijklmnopqrstuvwxyz"
		self.__L = len(self.__alfabeto)

	def generarClave(self, longitudMensaje):
		clave = ""
		for _ in range(longitudMensaje):
			clave += self.__alfabeto[randint(0, self.__L-1)]
		return clave

	def codificar(self, mensaje, clave, modo):

		# E(Mi) = (Mi + Ki) mod L
		# ó D(Ci) = (Ci - Ki) mod L

		criptograma = ""

		for i in range(len(mensaje)):

			mi = self.__alfabeto.find(mensaje[i])
			ki = self.__alfabeto.find(clave[i])

			# Carácter emi encriptado con la fórmula
			if modo == "cifrar":
				ci = ((mi + ki) % self.__L)
			elif modo == "descifrar":
				ci = ((mi - ki) % self.__L)

			# Añadimos el carácter al criptograma, 
			# trasformando previamente a carácter
			criptograma += self.__alfabeto[ci]

		return criptograma
