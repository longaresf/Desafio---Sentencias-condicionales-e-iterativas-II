import string
import getpass

contador:int = 0
alphabeto = string.ascii_lowercase
password = getpass.getpass("Ingrese su contraseña: ")


for char in password:
    for charter in alphabeto:
        contador += 1
        if char == charter:
            break

print(f"La contraseña {password} fue forzada en {contador} intentos")