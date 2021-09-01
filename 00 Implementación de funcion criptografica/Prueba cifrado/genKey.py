# Para cifrar y decifrar necesitamos una llave, que es como una comtraseña pero en un formato especial

from cryptography.fernet import Fernet

# Se genera una llave al azar cada vez que se llama a la funcion
llave = Fernet.generate_key()
# La llave generada es una cadena codificada en un objeto de bytes en base64
print(llave)
print(type(llave))

# Se debe cifrar y decifrar con la misma llave, por lo que se procede a guardarla
archivo = open('llave.key', 'wb') 
# Como la llave es un objeto de bytes, se debe abrir el archivo con el permiso "write bytes" para escribir directamente bytes
archivo.write(llave)
archivo.close()
