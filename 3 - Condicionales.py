#   Capitulo 3: Booleanos, condicionales y entrada de datos por el usuario.

# Entrada de datos por el usuario. Identificacion del tipo de datos.

age = input("Escribe tu edad: ")
type_date = type(age)
print(age)
print(type_date)

# Booleanos, IF (Guarda solamente los valores que son verdaderos o falsos)

verdadero = True
falso = False

if(verdadero == True): # Condicion que se tiene que cumplir o no. (==) -> Comparar.
    print("Soy verdadero!")

if (falso == True): # Si yo imprimo por pantalla esta condicion no me la va a mostrar por terminal ya que no es cierta la condicion. false no es igual que true.
    print("Son iguales")

if(falso == False):
    print("Si soy falso!")



# Operadores de comparacion, ELIF, ELSE.

age = int(input("Dime tu edad por favor: ")) # Como le vamos a pedir la edad al usuario para que tenga coherencia vamos a definir que la edad es un valor entero.

if (age >= 18):
    print(" Eres mayor de edad, podes pasar!! ")
elif(age < 0):
    print("Oye, esto es imposible")
elif(age < 14):
    print("Oye, eres muy pequeño")
else:
    print(" Eres menor de edad, no puedes pasar!! ")




# Operadores Logicos and. or, not
""" 
Nos sirven para comprobar varias expresiones a la vez por ejemplo si una persona entra a nuestro club si tiene mas de 18 años
y a la vez es menor de 35 años.
"""

age = int(input("Dime tu edad por favor: "))
if (type(age) == int):
    if(age > 120 or age < 0):
        print("Esto es imposible")
    elif(age >= 18 and age < 40):
        print("Puedes entrar a mi club")
    elif(age < 18 or age > 15):
        print("Todavia eres menor, no puedes entrar")
    else:
        print("No ha sucedido ninguna de las condiciones")
else:
    print("Oye, la edad debe ser un numero entero")
if(not(age <= 18)):
    print("Puedes entrar")




# EJERCICIO: 
# 1) Comprobar si el usuario introduce un numero, si no es un numero indicar que debe introducir un entero. 
# 2) Si es un numero, deberemos comprobar si es o no PAR y notificarselo al usuario.

numero = (input("Dame un numero"))
if(not(numero.isdigit())):
    print("El numero ingresado no es un numero")
elif numero %2 == 0 and numero == int(numero):
    print("el numero es par")
else:
    print("El numero es impar")




num = input("Dime un numero: ")
if(not(num.isdigit())):
    print("Los datos son incorrectos. Debe ser un número")
else:
    num = int(num)
    if(num%2 == 0):
        print("es par")
    else:
        print("es impar")

"""
num = input("Introduce un número entero: ")
def comprobar_numero():
    if not num.isdigit():
        print("Debes introducir un número entero.")
    else:
        num = int(num)
        if num % 2 == 0:
            print(f"El número {num} es par.")
        else:
            print(f"El número {num} es impar.")
"""

