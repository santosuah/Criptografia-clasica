class CifradoAfin(object):

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

	def codificar(self, mensaje, clave, modo):

		criptograma = ""

		if modo == "descifrar":
			aInv = self.__inversaModulo(clave[0], self.__L)

		for i in range(len(mensaje)):

			mi = self.__alfabeto.find(mensaje[i])

			if modo == "cifrar":
				ci = (clave[0] * mi + clave[1]) % self.__L
			elif modo == "descifrar":
				ci = (aInv * (mi + self.__L - clave[1])) % self.__L

			criptograma += self.__alfabeto[ci]

		return criptograma
