from cesar import CifradoCesar

def main():

	cesar = CifradoCesar()
	clave = 12
	print(clave, "(Clave)")

	# Eliminar los espacios en blancos
	mensaje = "Vamos a la calle a preguntar a taxistas sobre anecdotas de su oficio".lower()
	print(mensaje, "(Mensaje)")

	criptograma = cesar.codificar(mensaje, clave, "cifrar")
	print(criptograma, "(Criptograma)")

	mensajeDescifrado = cesar.codificar(criptograma, clave, "descifrar")
	print(mensajeDescifrado, "(Descifrado)")

if __name__ == "__main__":
	main()
