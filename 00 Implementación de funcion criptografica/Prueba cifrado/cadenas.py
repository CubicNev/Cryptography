# Cifrar y descifrar cadenas
from cryptography.fernet import Fernet

# Obtengo la llava de un archivo
archivoKey = open('llave.key', 'rb')
llave = archivoKey.read() # llave es de tipo bytes
archivoKey.close()

# Mensaje a cifrar
msj = "Ciframe plox!"
encMsj = msj.encode() # Se convierte el mensaje a bytes

# Cifrado 
f = Fernet(llave) # Se crea un objeto Fernet y se le pasa la llave
cifrado = f.encrypt(encMsj) # EL metodo regresa el mensaje cifrado
print(cifrado)

# Decifrado
# Se llama a la lllave de nuevo por demostracion
archivoKey = open('llave.key', 'rb')
llave2 = archivoKey.read() # llave es de tipo bytes
archivoKey.close()
# Se llama a otro objeto fernet pasandole la llave
f2 = Fernet(llave2)
decifrado = f2.decrypt(cifrado) # Devuelve el mensaje decifrado en modo de bytes
print(decifrado)

# Decodificando el mensaje
msj_o = decifrado.decode()
print(msj_o)