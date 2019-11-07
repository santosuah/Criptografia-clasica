class CifradoRailFence(object):

    def cifrar(self, mensaje, clave):
        # Troceo del mensaje en railes

        # Inicializar array de string
        criptogramaPorRailes = ["" for _ in range(clave)]

        # Hacer el zig-zag
        rail = 0
        bajar = False
        for caracter in mensaje:

            criptogramaPorRailes[rail] += caracter

            # Si llegamos a uno de los extremos
            # de los railes (cambiamos de sentido)
            if (rail == 0 or rail == (clave-1)):
                bajar = not bajar

            if bajar: rail += 1
            else:     rail -= 1

        # Juntamos todos las cadenas  por rail
        # de la lista en una sola
        return "".join(criptogramaPorRailes)

    def descifrar(self, criptograma, clave):
        # Fase de troceo en los railes del criptograma (indicado por la clave)

        # Inicializar array de string
        mensajePorRailes = ["" for _ in range(clave)]

        # Indice global de recorrido del criptograma
        idxCriptograma = 0

        for pasada in range(clave):

            # Hacemos una pasada por todo el criptograma
            # en forma de zig-zag
            rail = 0
            bajar = False
            for _ in criptograma:

                # Si coincide el rail actual con+
                # la fase de pasada
                if rail == pasada:
                    # Añadimos el caracter donde interseca rail-pasada
                    mensajePorRailes[rail] += criptograma[idxCriptograma]
                    # Avanzamos en el criptograma
                    idxCriptograma += 1

                # Operaciones recorrido en zig-zag
                if (rail == 0 or rail == (clave-1)):
                    bajar = not bajar

                if bajar: rail += 1
                else:     rail -= 1

        # Fase recomponer mensaje con el criptograma troceado

        # Indices consumidos en cada cadena de la lista cript2
        mensajePorRailesIdx = [0 for _ in range(clave)]
        mensajeDescifrado = ""
        rail = 0
        bajar = False

        for _ in criptograma:

            # Obtenermos el caracter de la cadena rail, y de esta el caracter siguiente
            # cuyo indice se guarda en mensajePorRailesIdx[rail]
            mensajeDescifrado += mensajePorRailes[rail][mensajePorRailesIdx[rail]]

            # Nos desplazamos en la cadena
            mensajePorRailesIdx[rail] += 1

            # Operaciones recorrido en zig-zag
            if (rail == 0 or rail == (clave-1)):
                bajar = not bajar

            if bajar: rail += 1
            else:     rail -= 1

        return mensajeDescifrado
