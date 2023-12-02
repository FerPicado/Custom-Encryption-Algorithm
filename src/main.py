import os
from dotenv import load_dotenv
import string

class CustomEncryptionAlgorithm:

    def __init__(self):
        load_dotenv()
        self.key = int(os.getenv("KEY", default=5))
        self.chars = string.digits + string.ascii_letters + " " + "áéíóú"

    def encode_msg(self, message):
        encoded_txt = ""
        for letter in message:
            try:
                if letter in self.chars:
                    value = self.chars.index(letter) + 1
                    encrypted_value = (value * self.key) % len(self.chars)
                    encoded_txt += self.chars[encrypted_value - 1]
                else:
                    encoded_txt += letter
            except ValueError:
                encoded_txt += letter
        return encoded_txt

    def decode_msg(self, encoded_txt):
        decoded_txt = ""
        for letter in encoded_txt:
            try:
                if letter in self.chars:
                    value = self.chars.index(letter) + 1
                    decrypted_value = (value * pow(self.key, -1, len(self.chars))) % len(self.chars)
                    decoded_txt += self.chars[decrypted_value - 1]
                else:
                    decoded_txt += letter
            except:
                decoded_txt += letter
        return decoded_txt

# Uso del Custom Encryption Algorithm
encryption_algo = CustomEncryptionAlgorithm()

msg_txt = "Bajo el manto estrellado, el río serpentea entre colinas silenciosas, reflejando el resplandor lunar. En el bosque, los árboles susurran historias antiguas mientras las hojas crujen bajo patas furtivas. Un faro distante proyecta destellos intermitentes sobre las aguas, guiando a los navegantes en la oscuridad. En la ciudad, las luces parpadean como luciérnagas urbanas, revelando callejones donde secretos se tejen entre sombras. En un rincón del parque, bancos desgastados cuentan las confidencias de enamorados y susurros de amigos. En esta sinfonía nocturna, el mundo se ralentiza, invitando a explorar el misterio que solo la noche revela."

cipher_txt = encryption_algo.encode_msg(msg_txt)
print(f"Original message : {msg_txt}")
print(f"Encrypted message: {cipher_txt}")

decrypted_txt = encryption_algo.decode_msg(cipher_txt)
print(f"Decrypted message: {decrypted_txt}")

print(f"{msg_txt == decrypted_txt}")  # True / False
