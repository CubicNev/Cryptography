""""
 Cifrar y descifrar archivos
 Es similar a las cadenas, se debe leer un archivo con el permiso "read bytes", nos va a sar un dato de tipo byte que puede ir directo al metodo encryp()

"""
from cryptography.fernet import Fernet

# Obtengo la llava de un archivo
archivoKey = open('llave.key', 'rb')
llave = archivoKey.read() # llave es de tipo bytes
archivoKey.close()

# Abrir y leer el archivo para cifrarlo
with open('prueba.txt', 'rb') as f: # Leer y cerrar de forma compacta
  contenido = f.read()

# Cifrado
fernet = Fernet(llave)
cifrado = fernet.encrypt(contenido)

# Escribir el archivo cifrado
with open('prueba.txt.cifrado', 'wb') as f:
  f.write(cifrado)