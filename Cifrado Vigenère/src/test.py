from vigenere import CifradoVigenere

def main():
	vigenere = CifradoVigenere()

	mensaje = "paris vaut bien une messe"
	clave = "loup"

	print(mensaje, "(Texto en claro)")
	print(clave, "(Clave)")

	criptograma = vigenere.codificar(mensaje, clave, "cifrar")
	print(criptograma, "(Criptograma)")

	mensajeDescifrado = vigenere.codificar(criptograma, clave, "descifrar")
	print(mensajeDescifrado, "(Descifrado)")

if __name__ == "__main__":
	main()
