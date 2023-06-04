# Fernet
!pip install cryptography

#Lorem ipsum
!pip install lorem-text

# Fernet
from cryptography.fernet import Fernet

import time

from lorem_text import lorem

def generar_lorem(num_palabras):
    texto = lorem.words(num_palabras)
    return texto

"""##1. Leer un archivo con el texto del mensaje a cifrar."""

inicio = time.time()

mensaje = generar_lorem(10).encode()

fin = time.time()

duracion = fin - inicio

print("Tiempo de ejecución:", duracion*1000, "milisegundos")

"""##2. Generar e imprimir la(las) claves de cifrado y/o descifrado."""

inicio = time.time()

clave = Fernet.generate_key()
f = Fernet(clave)
print('Clave',clave)

fin = time.time()

duracion = fin - inicio

print("Tiempo de ejecución:", duracion*1000, "milisegundos")

"""##3. Cifrar e imprimir el texto."""

inicio = time.time()

texto_encriptado = f.encrypt(mensaje)
print('Texto encriptado:',texto_encriptado.decode())

fin = time.time()

duracion = fin - inicio

print("Tiempo de ejecución:", duracion*1000, "milisegundos")

"""##4. Descifrar e imprimir el texto."""

inicio = time.time()

desencriptado = f.decrypt(texto_encriptado)
print('Texto desencriptado:',desencriptado.decode())

fin = time.time()

duracion = fin - inicio

print("Tiempo de ejecución:", duracion*1000, "milisegundos")