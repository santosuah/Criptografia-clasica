from copy import deepcopy

class CifradoPolialfabeticoAlberti(object):

	def __init__(self):
		self.__discoExterior = "abcdefgilmnopqrstvxz1234"
		self.__discoInterior = "gklnprtuz&xysomqihfdbace"
		self.__L = len(self.__discoExterior)

	# Encriptar mensaje con la clave compuesta por fases
	def codificar(self, mensaje, clave, modo):

		criptograma = ""
		indiceMensaje = 0

		# Por cada fase en la clave
		for fase in clave:

			# Buscar la posición del caracter dentro del disco interno
			# como un desplazamiento
			d = self.__discoInterior.find(fase[0])

			# Desencriptamos con ese disco rotado el numero de caracteres selccionado
			for _ in range(fase[1]):

				if modo == "cifrar":
					mi = self.__discoExterior.find(mensaje[indiceMensaje])
					cmi = (mi + d) % self.__L
					criptograma += self.__discoInterior[cmi]

				elif modo == "descifrar":
					mi = self.__discoInterior.find(mensaje[indiceMensaje])
					cmi = (mi - d) % self.__L
					criptograma += self.__discoExterior[cmi]

				indiceMensaje += 1

		return criptograma
