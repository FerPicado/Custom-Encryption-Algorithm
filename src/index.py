# from cryptography.fernet import Fernet

# # Función para cifrar con Cifrado César
# def cifrar_cesar(mensaje, adelantar=3):
#     cipher = ""
#     for letra in mensaje:
#         cipher += chr(ord(letra) + adelantar)
#     return cipher

# # Función para descifrar con Cifrado César
# def descifrar_cesar(cipher, adelantar=3):
#     mensaje = ""
#     for letra in cipher:
#         mensaje += chr(ord(letra) - adelantar)
#     return mensaje

# # Función para cifrar con Cifrado Simétrico (Fernet)
# def cifrar_simetrico(mensaje, clave):
#     cipher_suite = Fernet(clave)
#     cipher_text = cipher_suite.encrypt(mensaje.encode())
#     return cipher_text

# # Función para descifrar con Cifrado Simétrico (Fernet)
# def descifrar_simetrico(cipher_text, clave):
#     cipher_suite = Fernet(clave)
#     mensaje = cipher_suite.decrypt(cipher_text).decode()
#     return mensaje

# if __name__ == "__main__":
#     print("\t   -------------------------")
#     print("\t  | * CIFRADO CÉSAR Y SIMÉTRICO * |")
#     print("\t   -------------------------")

#     # Solicitar al usuario que ingrese un mensaje
#     mensaje = input("Ingrese el Mensaje: ")

#     # Clave para cifrado simétrico
#     clave_simetrica = Fernet.generate_key()

#     print("\n-------------------------------")

#     # Cifrar el mensaje con Cifrado César
#     cipher_cesar = cifrar_cesar(mensaje)
#     print("Cifrado con Cifrado César:", cipher_cesar)

#     # Cifrar el mensaje con Cifrado Simétrico
#     cipher_simetrico = cifrar_simetrico(mensaje, clave_simetrica)
#     print("Cifrado con Cifrado Simétrico:", cipher_simetrico)

#     print("-------------------------------")

#     # Descifrar el texto cifrado con Cifrado César
#     descifrado_cesar = descifrar_cesar(cipher_cesar)
#     print("Descifrado con Cifrado César:", descifrado_cesar)

#     # Descifrar el texto cifrado con Cifrado Simétrico
#     descifrado_simetrico = descifrar_simetrico(cipher_simetrico, clave_simetrica)
#     print("Descifrado con Cifrado Simétrico:", descifrado_simetrico)

#     print("-------------------------------")

import random

# Función para cifrar con Cifrado César
def cifrar_cesar(mensaje, adelantar=3):
    cipher = ""
    for letra in mensaje:
        if letra.isalpha():
            offset = ord('a') if letra.islower() else ord('A')
            cipher += chr((ord(letra) - offset + adelantar) % 26 + offset)
        else:
            cipher += letra
    return cipher

# Función para descifrar con Cifrado César
def descifrar_cesar(cipher, adelantar=3):
    return cifrar_cesar(cipher, -adelantar)

# Función para cifrar con Cifrado Simétrico
def cifrar_simetrico(mensaje, clave):
    random.seed(clave)
    return ''.join([chr((ord(letra) + random.randint(0, 255)) % 256) for letra in mensaje])

# Función para descifrar con Cifrado Simétrico
def descifrar_simetrico(cipher, clave):
    random.seed(clave)
    return ''.join([chr((ord(letra) - random.randint(0, 255)) % 256) for letra in cipher])

if __name__ == "__main__":
    print("\t   -------------------------")
    print("\t  | * CIFRADO CÉSAR Y SIMÉTRICO * |")
    print("\t   -------------------------")

    # Solicitar al usuario que ingrese un mensaje
    mensaje = input("Ingrese el Mensaje: ")

    # Clave para cifrado simétrico (puedes elegir cualquier número)
    clave_simetrica = 42

    print("\n-------------------------------")

    # Cifrar el mensaje con Cifrado César
    cipher_cesar = cifrar_cesar(mensaje)
    print("Cifrado con Cifrado César:", cipher_cesar)

    # Cifrar el mensaje con Cifrado Simétrico
    cipher_simetrico = cifrar_simetrico(mensaje, clave_simetrica)
    print("Cifrado con Cifrado Simétrico:", cipher_simetrico)

    print("-------------------------------")

    # Descifrar el texto cifrado con Cifrado César
    descifrado_cesar = descifrar_cesar(cipher_cesar)
    print("Descifrado con Cifrado César:", descifrado_cesar)

    # Descifrar el texto cifrado con Cifrado Simétrico
    descifrado_simetrico = descifrar_simetrico(cipher_simetrico, clave_simetrica)
    print("Descifrado con Cifrado Simétrico:", descifrado_simetrico)

    print("--------------Hola-----------------")