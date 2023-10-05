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

# Nota: con el + lo que hariamos es concatenar cadenas de textos. 
# resultado1 y resultado2 no son cadenas de texto por lo que deberiamos definir de salida que sean numeros enteros o float.
# Para transformar esto hariamos: Añadir "str", ¿Que hace en este caso? Tomar el valor numerico en este caso el resultado de la suma y el resultado de la resta
# y transformarlo en una cadena de texto para concatenarlo con otras cadenas de texto

"""¿Que pasa si no colocamos el "str"? """

# Nos diria: "TypeError: can only concatenate str (not "int") to str"





"""

Ejercicio 1: Funcion maximo -> Dados dos numeros. 
La funcion debe encontrar cual de los dos numeros es mas grande y retornarlo. 
Extra: Se deben comprobar que los argumentos de la funcion sean de tipo int o float. 
Si alguno de los dos no lo es, mostrar un mensaje de error y retornar false.
Solución: 

"""

