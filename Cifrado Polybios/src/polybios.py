class CifradoPolybios(object):

	def __init__(self):
		self.__alfabeto = "abcdefghijlmnopqrstuvwxyz"
		self.__L = 5 # 5x5

	def __buscarEnMatriz(self, caracter):
		idx = self.__alfabeto.find(caracter)
		return (idx // self.__L + 1, idx % self.__L + 1)

	def cifrar(self, mensaje):
		criptograma = ""
		for caracter in mensaje:
			i, j = self.__buscarEnMatriz(caracter)
			criptograma += str(i) + str(j)
		return criptograma

	def descifrar(self, criptograma):
		mensaje = ""
		for i in range(1, len(criptograma), 2):
			n = int(criptograma[i-1] + criptograma[i])
			mensaje += self.__alfabeto[self.__L * ((n//10)-1) + ((n%10)-1)]
		return mensaje
