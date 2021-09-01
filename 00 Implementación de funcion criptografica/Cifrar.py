

""""
 Cryptography
 Escuela Superior de Computo
 Autor: Carlos Nevárez

 Objeto que se encarga del cifrado de archivos con una llave dada.
  self.ruta_archivo: String
  self.llave:

"""
from cryptography.fernet import Fernet

class Cifrar:

  def __init__(self, ruta_archivo, llave):
    self.ruta_archivo = ruta_archivo
    self.llave = llave

  def cifrado(self):
    # Abrir y leer el archivo para cifrarlo
    with open(self.ruta_archivo, 'rb') as f: # Leer y cerrar de forma compacta
      contenido = f.read()

    # Cifrado
    fernet = Fernet(self.llave)
    cifrado = fernet.encrypt(contenido)


# Obtengo la llava de un archivo
archivoKey = open('llave.key', 'rb')
llave = archivoKey.read() # llave es de tipo bytes
archivoKey.close()





fernet = Fernet(llave)
cifrado = fernet.encrypt(contenido)

# Escribir el archivo cifrado
with open('prueba.txt.cifrado', 'wb') as f:
  f.write(cifrado)