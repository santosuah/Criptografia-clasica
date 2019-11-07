from alberti import CifradoPolialfabeticoAlberti

def main():

	alberti = CifradoPolialfabeticoAlberti()

	mensaje = "el disco de alberti es el primer cifrador polialfabetico conocido".replace(" ", "").lower()
	print(mensaje, "(Texto en claro)")

	clave = [
		('g', 10), # poner a-g y descifrar 10 caracteres
		('&', 9),  # poner a-& y descifrar 9 caracteres
		('e', 19), # poner a-e y descifrar 19 caracteres
		('a', 18)  # poner a-a y descifrar 18 caracteres
	]
	print(clave, "(Clave)")

	criptograma = alberti.codificar(mensaje, clave, "cifrar")
	print(criptograma, "(Cifrado)")

	mensaje_descifrado = alberti.codificar(criptograma, clave, "descifrar")
	print(mensaje_descifrado, "(Descifrado)")

if __name__ == "__main__":
	main()
