#!/usr/bin/python3

version = 0.5

app_title = "Playlist v" + str(version)

print(app_title)
print("-" * len(app_title))

##############################################

def saluda ():
    print("Hola!")

def suma (num1, num2):
    return num1+num2

def despide (quien="Jacinto"):
    print("Estás despedido", quien)

def retorna_multiple ():
    uno = 1
    dos = 2

    return uno,dos

##############################################

if True:
    print("Cierto")
else:
    print("Falso")

##############################################

primero = 3
segundo = 5

if primero > segundo:
    print("El primero es mayor que el segundo")
elif primero < segundo:
    print("El segundo es mayor que el primero")
else:
    print("Ambos números son iguales")

##############################################

contador = 10

while contador > 0:
#    print(contador)
    contador -= 1

print("------")

for num in range(10): # range(INICIAL, FIN, PASOS)
#    print(num)
    pass

##############################################

personas = ["Jaimito", "Jacinto", 33, "Anselmito"]

for dato in personas:
    print(">", dato)

personaje = {
    "nombre": "Paquito",
    "edad": 33,
    "pelo": "Marrón"
}

#print("Personaje: ", personaje["nombre"])
#print("Edad: ", personaje["edad"])
#print("Pelo: ", personaje["pelo"])

for clave in personaje:
    print(">>", clave, personaje[clave])

for clave, valor in personaje.items():
    print(">>>", clave, valor)

#############################################

saluda()

resultado = suma(3, 5)

print(resultado)

despide()
despide("Ramiro")

valor1, valor2 = retorna_multiple()

print("Valores:", valor1, valor2)

#############################################

nombre = input("¿Cómo te llamas?")

print(saluda(), nombre)
