# Despues de guardar la llave en un archivo, despues necesitaremos leer el archivo para obtener la llave
from cryptography.fernet import Fernet

archivo = open('llave.key', 'rb') # Abrir con la opcion 'read bytes'
llave = archivo.read() # La llave es de tipo bytes
archivo.close()

print(llave)

