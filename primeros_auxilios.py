import sys

resp_est = input("Responde a estímulos?, si o no ")
while resp_est != "si" and resp_est != "no":
    resp_est = input("Error, responde con si o no: ")
    break
resp = input("Respira?, si o no ")
while resp != "si" and resp != "no":
    resp_est = input("Error, responde con si o no: ")
    break
sign_vida = input("¿Se siente vivo?, si o no ")
while sign_vida != "si" and sign_vida != "no":
    resp_est = input("Error, responde con si o no: ")
    break
amb_lleg = input("Llegó ambulancia?, si o no ")
while amb_lleg != "si" and amb_lleg != "no":
    resp_est = input("Error, responde con si o no: ")
    break

if  resp_est == "si":
    print("Valorar la necesidad de llevar a hospital más cercano")
    print("Fin de algoritmo")
    exit()
else:
    print("Abrir la vía aérea")
if resp == "si":
    print("Permitirle posición de suficiente ventilación")
    print("Fin de algoritmo")
    exit()
else:
    print("Administrar 5 ventilaciones y llamar a ambulancia")
if sign_vida == "si":
    print("Reevaluar a la espera de la ambulancia")
else:
    print("Administrar compresiones toráccicas hasta que llegue ambulancia")
if sign_vida == "si" and amb_lleg == "si":
    print("Enviar en ambulancia")
    print("Fin de algoritmo")
    exit()
elif sign_vida == "si" and amb_lleg == "no":
    print("Continuar con tratamiento de compresiones toráccicas hasta que llegue ambulancia")
else:
    print("Paciente sin estado vital a la espera de traslado")
    print("Fin de algoritmo")
    exit()