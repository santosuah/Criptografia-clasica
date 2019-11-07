class CifradoVigenere(object):

	def __init__(self):
		self.__alfabeto = "abcdefghijklmnñopqrstuvwxyz"
		self.__L = len(self.__alfabeto)

	def codificar(self, mensaje, clave, modo):

		indiceClave = 0
		criptograma = ""

		for letra in mensaje:

			if letra in self.__alfabeto:

				mi = self.__alfabeto.find(letra)
				ki = self.__alfabeto.find(clave[indiceClave])

				if modo == "cifrar":
					ci = ((mi + ki) % self.__L)
				elif modo == "descifrar":
					if (mi - ki) >= 0: ci = (mi - ki) % self.__L
					else:              ci = (mi - ki + self.__L) % self.__L

				criptograma += self.__alfabeto[ci]
				indiceClave = (indiceClave + 1) % len(clave)

			else:
				criptograma += letra

		return criptograma
