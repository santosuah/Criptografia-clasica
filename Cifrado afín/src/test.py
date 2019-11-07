from afin import CifradoAfin

def main():
	afin = CifradoAfin()

	mensaje = "no hay mal que por bien o venga".replace(" ", "").lower()
	print(mensaje, "(Texto en claro)")

	clave = (5,8)
	print(clave, "(Clave)")

	criptograma = afin.codificar(mensaje, clave, "cifrar")
	print(criptograma, "(Criptograma)")

	mensaje_descifrado = afin.codificar(criptograma, clave, "descifrar")
	print(mensaje_descifrado, "(Descifrado)")

if __name__ == "__main__":
	main()
