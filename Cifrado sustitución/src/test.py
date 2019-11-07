from sustitucion import CifradoSustitucion

def main():
    sustitucion = CifradoSustitucion()

    mensaje = "el tiempo de los próximos días estará dominado por una situación de alisios"
    clave = sustitucion.generarClave()

    print(mensaje, "(Clave)")
    print(clave, "(Clave)")

    criptograma = sustitucion.cifrar(mensaje, clave)
    print(criptograma, "(Cifrado)")

    mensajeDescifrado = sustitucion.descifrar(criptograma, clave)
    print(mensajeDescifrado, "(Mensaje Descifrado)")

if __name__ == "__main__":
    main()
