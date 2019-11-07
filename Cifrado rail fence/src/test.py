from railfence import CifradoRailFence

def main():
    railFence = CifradoRailFence()

    mensaje = "we are discovered flee at once".replace(" ", "").lower()
    print(mensaje, "(Mensaje)")

    # 2 <= clave <= len(mensaje)
    clave = 3
    print(clave, "(Clave)")

    criptograma = railFence.cifrar(mensaje,clave)
    print(criptograma, "(Criptograma)")

    mensajeDescifrado = railFence.descifrar(criptograma,clave)
    print(mensajeDescifrado, "(Descifrado)")

if __name__ == "__main__":
    main()
