from vernam import CifradoVernam

def main():
	vernam = CifradoVernam()

	mensaje = "cifradordevernam"
	print(mensaje, "(Texto claro)")

	claveGenerada = vernam.generarClave(len(mensaje))
	print(claveGenerada, "(Clave)")

	criptograma = vernam.codificar(mensaje, claveGenerada, "cifrar")
	print(criptograma, "(Criptograma)")

	mensaje_descifrado = vernam.codificar(criptograma, claveGenerada, "descifrar")
	print(mensaje_descifrado, "(Descifrado)")

if __name__ == "__main__":
	main()
