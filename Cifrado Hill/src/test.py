import numpy as np
from hill import CifradoHill

def main():

	hill = CifradoHill()

   # Clave
	clave = np.matrix([[3,3],[2,5]])
	print(clave, "(Clave)")

	# Mensaje
	mensaje = "helpme"
	print(mensaje, "(Mensaje)")

	# Criptograma
	criptograma = hill.cifrar(mensaje, clave)
	print(criptograma, "(Criptograma)")

	# Mensaje descifrado
	mesanjeDescifrado = hill.descifrar(criptograma, clave)
	print(mesanjeDescifrado, "(Mensaje descifrado)")

if __name__ == "__main__":
	main()
