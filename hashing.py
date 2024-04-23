import hashlib

def calcular_hash256(cadena):
    # Convertimos la cadena a bytes
    cadena_bytes = cadena.encode('utf-8')

    # Calculamos el hash usando SHA-256
    hash_obj = hashlib.sha256(cadena_bytes)

    # Obtenemos la representación hexadecimal del hash
    hash_hex = hash_obj.hexdigest()

    return hash_hex

def calcular_hash1(cadena):
    # Convertimos la cadena a bytes
    cadena_bytes = cadena.encode('utf-8')

    # Calculamos el hash usando SHA-256
    hash_obj = hashlib.sha1(cadena_bytes)

    # Obtenemos la representación hexadecimal del hash
    hash_hex = hash_obj.hexdigest()

    return hash_hex

# Ejemplo de uso
cadena_original = "Hola, este es un ejemplo de hashing en Python."
hash1_resultado = calcular_hash1(cadena_original)
hash256_resultado = calcular_hash256(cadena_original)
print("Cadena original:", cadena_original)
print("Hash SHA-256:",hash256_resultado)
print("Hash SHA-1:  ",hash1_resultado)
