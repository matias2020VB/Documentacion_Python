# CAPITULO 5: BUCLES

# ========== INICIO DE LA PARTE 1 ============

# BREVE INTRODUCCION A LAS LISTAS

# ¿Que es una lista? -> Es un tipo de dato que permite agrupar informacion, otros datos.

# De que forma se puede plantear una lista? de la siguiente forma:

numeros = [1, 2, 3, 4 , 5, 6]  # LISTA NUMERICA 

# QUE DEBEMOS SABER DE LAS LISTAS? -> Existen posiciones de la lista ó el indice de la lista y la longitud de la lista.

# Posicion de la lista: Consiste en saber en que lugar esta ubicado cada elemento.

# Continuando el ejemplo de la lista numeros. Si queremos saber la posicion del numero "uno" en la lista.
# Su posicion seria 0 por ejemplo:

# Las posiciones de la lista van desde cero hasta la posicion LONGITUD - 1

# numeros = [posicion0, posicion1, posicion2, posicion3, posicion4, posicion5] # -> EL rango de posiciones en este caso seria del 0 al 4.

# ¿Cómo puedo acceder a un elemento de esta lista?
    # Imprimiendo por pantalla la variable numeros que es la lista como muestro a continuación:  

#print(numeros[ConLaPosicionQueRequiera]


print(numeros)
print(numeros[0])
print(numeros[3])

# PARA CONOCER LA CANTIDAD DE ELEMENTOS QUE CONTIENE LA LISTA O LA LONGITUD PODEMOS UTILIZAR LA FUNCION: len

# Continuando con el ejemplo anterior si quiero saber la longitud lo hacemos de esta manera.

#print(len(nombreDeLaLista))



print(len(numeros))


# DENTRO DE LAS LISTAS PODEMOS IMPLEMENTAR EL TIPO DE DATO STRING: 

# Podemos crear una lista con el nombre: "texto" e incluir texto (formato: STR) en nuestra lista.


text = ["juan", "Botella", "Taza", "Matias"]
print(text)
print(text[3])


# PODEMOS IMPLEMENTAR NUMEROS ENTEROS, NUMEROS FLOAT, BOOLEANOS, STRING...


text_2 = [10, "Hola", 2.5, False]
print(text_2[3])



# Un truquito: Si yo quisiera ingresar al ultimo elemento de una lista lo que podemos hacer es:

# EJEMPLO COMENTADO -> print(text([len(text -1])

# Lista N°1 -> text

# print(text[len(text) -1 ])

# Lista N° -> text_2

# print(text_2[len(text_2) -1 ])



# COMENZAMOS CON BUCLES

# Un bucle es algo que se repite. -> Lo que buscamos es repetir una instruccion que nosotros queramos.

# Tenemos FOR y WHILE.  -> Podemos repetir un seguido de instrucciones un pedacito de codigo tantas veces que nosotros queramos.
#                       -> Podemos repetir una instruccion hasta que haya una condicion que hayamos puesto.

# ¿Como es la sintáxis? por ejemplo:

for x in range(5):
    print(x)
print("Hemos terminado el bucle")

# ¿Que estamos haciendo aqui? Nosotros aqui en este bucle lo que vamos hacer es que la variable "x" se repita 5 veces.
# Empezando desde la posicion 0 hasta la posicion4

# Dentro de la funcion range podemos arrancar de la posicion que nosotros queramos. Estableciendo limites inferior y limites superior. Por ejemplo:

for x in range(1, 7):
    print(x)

# Tambien dentro de la funcion range podemos establecer un limite inf que nosotros elijamos hasta un limite superior que nosotros elijamos y con un tercer argumento
# que nos diga que iremos incrementando de dos en dos. Por ejemplo:
# Tercer argumento: Es el incremento de "x" en cada iteración. 


for x in range(2, 20, 2):
    print(x)

# Nos mostraria del 2 al 18 ya que es 20 - 2 = 18 -> 18 es la posicion final del bucle.

# Mini ejemplo, imprimir solo las vocales de una palabra

palabra = "cocodrilo"
for letra in palabra:
    if(letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print(letra)
    else:
        print("Es una consonante")

# Mini ejemplo, iterar sobre una lista

numeros = [22, 33, 44, 55]



for numero in numeros:
    print(numero)   # -> Imprimimos cada numero.
    numero += 10    # -> Actualizamos el numero sumandole 10
    print(numero)   # -> Imprimimos cada numero de nuevo

print(numeros)      # -> Afuera del bucle imprimimos la lista de los numeros para ver que le ha pasado a la lista.

# ¿Que a ocurrido?
# Tenemos como resultado:
# Aqui lo que hace es primero imprimir el primer numero (22) y luego le suma 10 y nos actualza el resultado (32).

"""
22
32
33
43
44
54
55
65
[22, 33, 44, 55]    -> Aqui lo que hace es imprimir la variable numeros ya que es una lista que no se ha modificado en absoluto."""

for indice in range(len(numeros)):
    numeros[indice] += 10
print(numeros)

# Aqui lo que hacemos es usar la funcion range para que solamente me muestre el incremento de 10 de cada elemento de la lista.

# BUCLES WHILE
# Los bucles While sirven para iterar el codigo hasta que se cumpla una condicion.
# While significa "mientras"


contador = 0
while(contador < 10):
    print(contador)
    contador += 1

# Aqui lo que estamos haciendo es: definir una variable contador con el valor cero. Luego usamos while para que la variable contador
# tenga una condicion de que sea estrictamente menor que 10 y se repita tantas veces hasta que se complete la condicion. "Sea menor a 10"
# imprimimos para ver que nos muestra y usamos la adicion de la variable contador que en este caso le sumaria uno a la variable. (+=)

# Nos muestra por pantalla.
"""
0
1
2
3
4
5
6
7
8
9
"""

# Mini ejemplito usando While -> Encontrar la primera letra a en una frase, si se encuentra se acaba el bucle.

letraEncontrada = False
letra = "a"     # -> Letra a encontrar
frase = "En este momento estoy buscando la letra a"
indice = 0      # -> El indice nos indica la posicion de la letra encontrada que es "a"

while(not(letraEncontrada)):    # Mientras no (not) tengamos una letra encontrada -> "not" lo que hace es cambiar de false a true.
    if(frase[indice] == letra): # Si en nuestra variable "frase" esta en la posicion "Indice" va a tomar el primer caracter de nuestra frase que es la letra "E" -> posicion 0
                                # indice lo que hará es ir comprobando caracter por caracter para verificar si es la leltra "a"
        letraEncontrada = True  # En caso de haber encontrado la primera "a" lo que hacemos es verificar la condicion por lo que la variable letraEncontrada se vuelve verdadera y se termina el while.
        
        print(f"Hemos encontrado la letra {letra} en la posicion {indice}!")
        
#   Mostramos por pantalla que hemos mostrado la letra incluyendo el formateo con la sintaxis "f" concatenando dentro del print las variables {letra} y {indice}
    
    else: # Si todavia no hemos encontrado esta letra
        indice += 1 # Recorrer el siguiente caracter para ver si hemos encontrado la letra "a"


