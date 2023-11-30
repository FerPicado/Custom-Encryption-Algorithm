import os
from dotenv import load_dotenv
import string

class CustomEncryptionAlgorithm:

    def __init__(self):
        load_dotenv()
        self.key = int(os.getenv("KEY", default=7))
        self.chars = string.digits + string.ascii_letters + " " + "áéíóú"

    def encode_message(self, message):
        encoded_text = ""
        for letter in message:
            try:
                if letter in self.chars:
                    value = self.chars.index(letter) + 1
                    encrypted_value = (value * self.key) % len(self.chars)
                    encoded_text += self.chars[encrypted_value - 1]
                else:
                    encoded_text += letter
            except ValueError:
                encoded_text += letter
        return encoded_text

    def decode_message(self, encoded_text):
        decoded_text = ""
        for letter in encoded_text:
            try:
                if letter in self.chars:
                    value = self.chars.index(letter) + 1
                    decrypted_value = (value * pow(self.key, -1, len(self.chars))) % len(self.chars)
                    decoded_text += self.chars[decrypted_value - 1]
                else:
                    decoded_text += letter
            except:
                decoded_text += letter
        return decoded_text

# Uso del Custom Encryption Algorithm
encryption_algo = CustomEncryptionAlgorithm()

plain_text = "Bajo el manto estrellado, el río serpentea entre colinas silenciosas, reflejando el resplandor lunar. En el bosque, los árboles susurran historias antiguas mientras las hojas crujen bajo patas furtivas. Un faro distante proyecta destellos intermitentes sobre las aguas, guiando a los navegantes en la oscuridad. En la ciudad, las luces parpadean como luciérnagas urbanas, revelando callejones donde secretos se tejen entre sombras. En un rincón del parque, bancos desgastados cuentan las confidencias de enamorados y susurros de amigos. En esta sinfonía nocturna, el mundo se ralentiza, invitando a explorar el misterio que solo la noche revela."

cipher_text = encryption_algo.encode_message(plain_text)
print(f"Original message : {plain_text}")
print(f"Encrypted message: {cipher_text}")

decrypted_text = encryption_algo.decode_message(cipher_text)
print(f"Decrypted message: {decrypted_text}")

print(f"{plain_text == decrypted_text}")  # True / False
