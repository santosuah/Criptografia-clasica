class CifradoCesar(object):

	def __init__(self):
		self.__alfabeto = "abcdefghijklmnopqrstuvwxyz"
		self.__L = len(self.__alfabeto)

	def codificar(self, mensaje, clave, modo):

		criptograma = ""
		for caracter in mensaje:

			if caracter in self.__alfabeto:

				i = self.__alfabeto.find(caracter)

				if modo == "cifrar":      i = (i + clave) % self.__L
				elif modo == "descifrar": i = (i - clave) % self.__L

				criptograma += self.__alfabeto[i]

			else:
				criptograma += caracter

		return criptograma
