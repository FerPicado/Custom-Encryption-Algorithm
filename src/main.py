import os
from dotenv import load_dotenv
import string

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def encode_message(message):
    key = int(os.getenv("KEY", default=7))  # Obtener la clave de la variable de entorno o usar 7 por defecto
    chars = string.digits + string.ascii_letters + "áéíóú" # Abecedario personalizado
    encoded_text = ""
    for letter in message:
        try:
            if letter in chars:
                value = chars.index(letter) + 1
                encrypted_value = (value * key) % len(chars)
                encoded_text += chars[encrypted_value - 1]
            else:
                encoded_text += letter
        except ValueError:
            encoded_text += letter
    return encoded_text

def decode_message(encoded_text):
    key = int(os.getenv("KEY", default=7))  # Obtener la clave de la variable de entorno o usar 7 por defecto
    chars = string.digits + string.ascii_letters + "áéíóú"  # Abecedario personalizado
    decoded_text = ""
    for letter in encoded_text:
        try:
            if letter in chars:
                value = chars.index(letter) + 1
                decrypted_value = (value * pow(key, -1, len(chars))) % len(chars)
                decoded_text += chars[decrypted_value - 1]
            else:
                decoded_text += letter
        except:
            decoded_text += letter
    return decoded_text

plain_text = "Bajo el manto estrellado, el río serpentea entre colinas silenciosas, reflejando el resplandor lunar. En el bosque, los árboles susurran historias antiguas mientras las hojas crujen bajo patas furtivas. Un faro distante proyecta destellos intermitentes sobre las aguas, guiando a los navegantes en la oscuridad. En la ciudad, las luces parpadean como luciérnagas urbanas, revelando callejones donde secretos se tejen entre sombras. En un rincón del parque, bancos desgastados cuentan las confidencias de enamorados y susurros de amigos. En esta sinfonía nocturna, el mundo se ralentiza, invitando a explorar el misterio que solo la noche revela."

# Encriptar el texto proporcionado
cipher_text = encode_message(plain_text)
print(f"Original message : {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Desencriptar el texto encriptado
decrypted_text = decode_message(cipher_text)
print(f"Decrypted message: {decrypted_text}")

# Verificar si el texto desencriptado coincide con el texto original
print(f"{plain_text == decrypted_text}") # True / False