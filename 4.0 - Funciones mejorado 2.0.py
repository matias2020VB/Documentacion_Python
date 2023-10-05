#   Capitulo 4: Funciones
#   Definicion de las funciones

def saludar():
    
    print("Hola ¿como estas?")

saludar()
saludar()
saludar()

#   Funciones con argumentos
def saludarDos(nombre):
    print(" Hola" + nombre + " ¿Que tal? ")

saludarDos(" Matute ")
saludarDos(" Silvi ")

#   Funciones con retorno

def suma(a, b):
    resultado = a + b #Variable local: Significa que es una variable que solo existe dentro de la funcion
    return resultado

valor = suma(10, 5)
print(valor)

valor_1 = suma(23, 12)
print(valor)

valor_2 = suma(13, 423)
print(valor)


def sumaDos(a, b):
    return a + b

valor = sumaDos(10, 5)
print(valor)


# En esta función lo que se trata de evaluar es la condicion de si dos numeros son iguales
# En el caso de que estos numeros sean iguales nos retornara un booleano: True, y si son distintos False

def sonIguales(num1, num2):
    return num1 == num2

verdad = sonIguales(3,3)
if(verdad): # Los if evaluan un booleano por lo que yo no necesito hacer: if(verdad == True): (esta forma es correcta) pero en este caso
            # directamente la variable "verdad" ya es un booleano; Un IF solamente quiere una variable o argumento que sea True or False
    
    print("Son iguales")
else:
    print("No son iguales")

print(verdad)
verdad = sonIguales(3,5)
print(verdad)

#   Funciones con argumentos con valor por defecto

def saludarPorDefecto(nombre = " Matute,"):
    print("Hola" + nombre + " Que tal?")

#saludarPorDefecto()
#saludarPorDefecto(" Silvina")

#   Funciones que retornan varios valores

def sumaYResta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta # Otra forma que podemos retornar esta suma y resta es directamente en el return colocar: return a+b, a-b

resultado1, resultado2 = sumaYResta(10, 5)
print("Los resultados son:\nSuma: " + str(resultado1) +"\nResta: " + str(resultado2))

# Nota: con el (+) lo que hariamos es concatenar cadenas de textos. 
# resultado1 y resultado2 no son cadenas de texto por lo que deberiamos definir de salida que sean numeros enteros o float.
# Para transformar esto hariamos: Añadir "str", ¿Que hace en este caso? Tomar el valor numerico en este caso el resultado de la suma y el resultado de la resta
# y transformarlo en una cadena de texto para concatenarlo con otras cadenas de texto

# ¿Que pasa si no colocamos el "str"? 

# Nos diria: "TypeError: can only concatenate str (not "int") to str"
#             "Solo podemos concatenar string con string, no con enteros."

"""
Ejercicio 1: Funcion maximo -> Dados dos numeros. 
La funcion debe encontrar cual de los dos numeros es mas grande y retornarlo. 
Extra: Se deben comprobar que los argumentos de la funcion sean de tipo int o float. 
Si alguno de los dos no lo es, mostrar un mensaje de error y retornar false.
"""
# Solución N°1.

num1 = int(input("Ingrese un numero que usted mas quiera:"))
num2 = int(input("Ingrese otro numero que usted mas quiera:"))

if num1 == num2:
    print("No hay un numero maximo, ambos numeros son iguales.")
if num1 > num2:
    print("El numero 1 es mayor.")
if num2 > num1:
    print("El numero 2 es mayor.")


#Solucion N°2

def maximo(num1, num2):
    if((type(num1) == int or type(num1) == float) and (type(num2) == int or type(num2) == float)):
        if num1 == num2:
            print("No hay numero maximo, son iguales.")
            return num1
        if num1 > num2:
            return num1
        elif(num1 < num2):
            return num2
    else:
        print("ERROR: el argumento debe ser tipo entero o de tipo float")
        return False

num = maximo(3, 10)
if (type(num) != bool):
    print("El numero es: " + str(num))

"""Este codigo de abajo es para probar si se le da como argumento un strin como lo es "rojo" y que me dice el programa creado anteriormente"""
#num = maximo(3, "rojo")
#if (type(num) != bool):
#    print("El numero es: " + str(num))



# Ejercicio N°:2

# Mini calculadora. Pedirle al usuario una operacion y dos numeros.
# Las operaciones pueden ser suma, resta, potencia. Si introduce una operacion diferente
# a estas, mostrar un mensaje de error. Si la operacion es correcta, mostrar el resultado.

def calculadora():
    operacion = input("¿Que operacion quieres realizar? Las opciones son:\n -Suma\n -Resta\n -Potencia\n")
    if(not(operacion == "Suma" or operacion == "Resta" or operacion == "Potencia")):
        print("ERROR: La operacion no es correcta. Las opciones son:\n-Suma\n-Resta\n-Potencia\n")
        return
    num1 = float(input("Número 1: "))
    num2 = float(input("Número 2: "))
    if(operacion == "Suma"):
        print(num1 + num2)
    elif(operacion == "Resta"):
        print(num1 - num2)
    elif(operacion == "Potencia"):
        print(num1 ** num2)
    else:
        print("ERROR: La operacion no es correcta. Las opciones son:\n-Suma\n-Resta\n-Potencia\n")

calculadora()
