# Se usa una constraseña para crear la llave

import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

entrada = "secreto"  # Para pruebas
pswrd = entrada.encode()  # Convierte la contraseña ingresada a bytes

# Salt necesario para algoritmo creado a parte con el metodo os.urandom(16)
salt = b'q\xa2\xb82\xab\xf7\x8f]\xc7\xd4d\x95OE\x02d'

# Parametros base para el objeto kdf
kdf = PBKDF2HMAC(algorithm=hashes.SHA256,
                 length=32,
                 salt=salt,
                 iterations=100000,
                 backend=default_backend())

# Par obtener la llave la contraseña se pasa a kdf.derive y se codifica usando base64
key = base64.urlsafe_b64encode(
    kdf.derive(pswrd))  # Solo se puede usar kdf una vez
print(key)
