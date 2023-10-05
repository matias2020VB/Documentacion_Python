# Capitulo 6: Cadena de caracteres o Strings
# Apartado 1: Repaso de conceptos básicos

# ¿Como declaramos un string? -> Hay varias formas en las que podemo declarar un string

# 1) Usamos comillas dobles

texto = "Hola, qué tal?"
print(texto)

# 2) Usamos comillas simples

texto = 'Hola, qué tal?'
print(texto)

# Ahora que gracia tiene que podamos declarar tanto con comillas simple y con comilla dobles?

# Nos sirve para incluir tanto este caracter: -> (") ó este caracter -> (')

# dentro del texto de nuestro propio string. Por ejemplo:

comillasSimples = "El personaje dijo 'suscribite al canal' rotundamente" # -> En este caso yo puedo incluir las comillas simples dentro de mi string que no pasará nada.

# ¿Que pasaría si yo a la frase 'suscribite al canal' le pongo comillas doble?

# comillaSimples = "El personaje dijo "suscribite al canal" rotundamente" # -> En este caso produciria un error de sintaxis ya que solamente python estaria tomando la expresion erronea como finalizacion del string: 

# -> "El personaje dijo = String
# -> rotundamente" = String
# -> "suscribite al canal" = Python no lo conidera texto, python considera la finalizacion del string.                                                                                                                                                                

# Si yo quisiera poner comillas dobles xq en nuestro texto lleva comillas dobles como lo haria? A continuacion lo explico.

# Podemos optar por la siguiente forma: -> Como podemos observar no nos tira ningun error de sintaxis ya que solucionariamos el error de sintaxis que nos dijo arriba.

comillasDobles = 'El personaje dijo "Suscribite al canal" rotundamente'
print(comillasDobles)
print(comillasSimples)

# 3) Usamos comillas triples para que nos permita poner saltos de linea, sangrias o identaciones. (He borrado las comillas para comentar esta parte de codigo)

stringConFormato ="""  (Si yo coloco algo aqui, no toma en cuenta el salto de linea. Si no pongo nada si.)
======= TEXTO FORMATEADO ====== 
El texto formateado:
    1. Poner saltos de linea.
    2. Poner sangrias
y mostrarlo así por pantalla.
"""
print(stringConFormato)

# Como convertimos datos numericos a datos booleanos a un string o cadena de texto. Porque como veremos a continuacion para concatenar cadena de texto neceitaremos que los datos a concatenar sean strings
# Si nosotros tenemos a continuacion estos valores (Enteros, Decimal, Booleano)
# NOTA: Usaremos la funcion type que nos permite devolver el tipo de dato que es la variable que hayamos definido.

valorEntero = 5
valorDecimal = 3.14
valorBooleano = False
print("TIPOS DE DATOS ORIGINALES SIN MODIFICAR")
print(type(valorEntero))
print(type(valorDecimal))
print(type(valorBooleano))


# Podemos convertirlos mediante la funcion string = str

valorEntero = str(valorEntero) # --> Convertimos el valor entero en string a partir de ahora
valorDecimal = str(valorDecimal) # --> Convertimos el valor decimal en string a partir de ahora
valorBooleano = str(valorBooleano) # --> Convertimos el valor booleano en string a partir de ahora

print("TIPOS DE DATOS MODIFICADOS A STRING")
print(type(valorEntero))
print(type(valorDecimal))
print(type(valorBooleano))

# Para verificar que estos tipos de datos han sido modificados a string podemos hacer lo siguiente:
# Mostraremos los tipos de datos al inicio sin modificar y luego modificados.

# 4) Como podemos descubrir la longitud es decir cuantos caracteres estan contenidos en un string. Utilizaremos una funcion que hemos usado anteriormente llamada len.
texto = "0123456789"
print("La longitud del texto es: ")
print(len(texto))

# Como concatenar strings o varias cadenas de texto

texto1 = "1234"
texto2 = "5678"

texto3 = "los valores son: " + texto1 + texto2
print(texto3)



# Apartado 2: ¿Los strings son listas? No es del todo verdad pero podemos tratarlos como listas. Comparten ciertos aspectos similares
# Un string lo que hace es tomar cada caracter y lo almacena en la posicion de una lista. (No es exactamente una lista, es un vector o un array)

# En este apartado descubriremos que realmente los strings son arrays o vectores (similares a las listas)

# Dentro de los strings podemos utilizar por ejemplo la indexacion de la siguiente forma

texto = "0123456789"
primerCaracter = texto[0]
substring = texto[1:5]

print("El texto original es: " + texto)
print("El primer valor es: " + primerCaracter)
print("El substring: " + substring)

# Tambien podemos utilizar indices negativos, por ejemplo.

print("El ultimo caracter es: " + texto[-1])

# Tambien podemos iterar sobre strings utilizando condicionales. Por ejemplo:
print("Iteracion: ")
for num in texto:
    print("El numero actual es: " + num)

# Ejercicio (mini): Tenemos un string unicamente compuesto por numeros enteros.
# Debemos sumar su valor uno a uno y mostrar por pantalla la suma de todos los numeros.

numeros = "1238532975324"
total = 0

for numero in numeros:
    total += int(numero)
else:
    print("El valor total es: " + str(total))

# Apartado 3: Format Strings
# Nos permiten generar strings combinanado texto con otras variables de forma sencilla y legible.

# Utilizaremos 3 formas de usar format string

# 1) Sin usar format string
# Ejemplo: Le queremos decir al usuario cuantas garrafas ha comprado, que precio tiene cada garrafa y cuanto es el total que tendra que pagar.

cantidadGarrafas = 5
precio = 1.5

print("Forma Rustica: ")
print("Has comprado " + str(cantidadGarrafas) + " . Cada garrafa vale " + str(precio) + "$. En total son " + str(cantidadGarrafas*precio) + "$")


# 2) Utilizando la primera manera de format string

print("Forma Piola: ")
texto = "Has comprado {}. cada garrafa vale: {}$. En total son: {}$".format(cantidadGarrafas, precio, cantidadGarrafas*precio)
print(texto)


# 3) Version mas reciente de format string

print(f"Has comprado {cantidadGarrafas}. cada garrafa vale: {precio}$. En total son: {cantidadGarrafas*precio}$")
