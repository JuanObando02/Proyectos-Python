import hashlib

def encontrar_colision_sha1():
    # Cadena original
    cadena1 = "Hola, este es un ejemplo de colisión en SHA-1"

    # Primer valor hash SHA-1
    hash1 = hashlib.sha1(cadena1.encode()).hexdigest()

    # Encontrar una cadena que produzca el mismo hash
    contador = 0
    while True:
        cadena2 = "Otra cadena con diferentes caracteres para buscar una colisión " + str(contador)
        hash2 = hashlib.sha1(cadena2.encode()).hexdigest()

        if hash1 == hash2:
            return cadena1, cadena2, hash1

        contador += 1

# Encontrar una colisión SHA-1
cadena1, cadena2, hash_colision = encontrar_colision_sha1()

# Mostrar las cadenas y el hash colisionado
print("Cadena 1:", cadena1)
print("Hash SHA-1 Cadena 1:", hashlib.sha1(cadena1.encode()).hexdigest())
print("\nCadena 2:", cadena2)
print("Hash SHA-1 Cadena 2:", hashlib.sha1(cadena2.encode()).hexdigest())
print("\nHash Colisionado:", hash_colision)

