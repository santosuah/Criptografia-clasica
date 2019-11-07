from polybios import CifradoPolybios

def main():
	polybios = CifradoPolybios()

	mensaje = "quebuenaidealadelgriego"
	print(mensaje, "(Texto claro)")

	criptograma = polybios.cifrar(mensaje)
	print(criptograma, "(Cifrado)")

	mensaje_descifrado = polybios.descifrar(criptograma)
	print(mensaje_descifrado, "(Descifrado)")

if __name__ == "__main__":
	main()
