""""
 Descifrar archivos
 Se lee el contenido del archivo cifrado y decifrarla con el metodo decrypt() y se escribe en el archivo decifrado
"""
from cryptography.fernet import Fernet

# Obtengo la llava de un archivo
archivoKey = open('llave.key', 'rb')
llave = archivoKey.read() # llave es de tipo bytes
archivoKey.close()

# Abrir y leer el archivo para cifrarlo
with open('prueba.txt.cifrado', 'rb') as f: # Leer y cerrar de forma compacta
  contenido = f.read()

# Cifrado
fernet = Fernet(llave)
decifrado = fernet.decrypt(contenido)

# Escribir el archivo cifrado
with open('prueba.txt.decifrado', 'wb') as f:
  f.write(decifrado)