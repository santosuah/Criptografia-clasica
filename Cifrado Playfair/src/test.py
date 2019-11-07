from playfair import CifradoPlayfair

def main():
    playfair = CifradoPlayfair()

    clave = "keyywoord"
    print(clave, "(Clave)")

    mensaje = "secretmessage"
    print(mensaje, "(Mensaje)")

    claveProcesada = playfair.procesarClave(clave)
    print(claveProcesada, "(Clave procesada)")

    print(playfair.limpiarAlfabeto(clave), "(Alfabeto limpio)")

    martrizCifrado = playfair.generarMatrizCifrado(claveProcesada)
    print(martrizCifrado, "(Matriz cifrado)")

    criptograma = playfair.cifrar(mensaje, clave)
    print(criptograma, "(Criptograma)")

    mensajeDescifrado = playfair.descifrar(criptograma, clave)
    print(mensajeDescifrado, "(Descifrado)")

if __name__ == "__main__":
    main()
