#   Capitulo 6

#   APARTADO 1: Repaso de conceptos basicos

#   Creamos una lista
#   Los tipos de datos de las listas pueden ser: Enteros, float, booleanos etc.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros)

#   Si yo quiero acceder a la primera posicion de la lista le indicamos el indice.
#   Empezamos a contar desde 0 en adelante.

primeraPosicion = numeros[0]

#   Quiero saber la longitud de la lista: Usamos len; Nos va a retornar los elementos que esten almacenados en la lista "numeros". Nos devuelve un entero.
#   Podemos usar el format string que nos permite concatenar los valores de las variables cuando imprimimos por pantalla para un orden mayor.

longitud = len(numeros)
print(f"El primer valor es: {primeraPosicion}\nLa longitud de la lista es: {longitud}")

#   ¿Como iteramos en una lista? Podemos usar un bucle FOR por ejemplo.

for num in numeros:
    print(num)

#   Conceptos Nuevos:
#   Apartado 2: Indexado y sublistas.

lista = ["Dale", "un","buen", "Like", "Crack"]
print(lista)

#   Dentro de python podemos encontrarnos con indices negativos que quiere decir esto: que podemos acceder al ultimo elemento de la lista colocando un indice negativo.
#   Por ejemplo: -1 -> Corresponde a la posicion donde se encuentra "Like" dentro de la lista.

ultimaPosicion = lista[-1]
print(ultimaPosicion)
ultimaPosicion = lista[-2]
print(ultimaPosicion)

#   En el caso de que yo quisiera acceder a varios elementos de la lista podria intentar hacer una sublista que contenga los valores de la lista original.
#   La nomenclatura que va entre corchetes es la siguiente: -> [LimiteInferior:LimiteSuperior] 
#  
# -> LI: Posicion del primer elemento al que quiero acceder. En este caso quiero acceder a la posicion 1 = "un"
# -> LS: Posicion del ultimo elemento al que quiero acceder. En este caso quiero acceder a la posicion 3 = "buen" ya que en este caso el limite superior es 4-1 = 3

sublista = lista [1:4]                                                                        
print(sublista)

#   ¿Que mas podemos hacer?

#   Si yo quiero ir desde el inicio de la lista hasta una posicion en concreto.
#   Si quiero empezar desde la posicion cero lo que hariamos es: No colocamos nada en el limite inferior pero si declaramos el limite superior; :4

sublista = lista[:4]
print(sublista)

#   Tambien podemos ir desde una posicion en concreto hasta el final de la lista por ejemplo desde la posicion 2. Colocamos el limite inferior que seria desde la posicion que quiero arrancar
#   Y luego en el limite superior no pongo nada ya que por definido Python lo que hace es recorrer hasta el final de la lista.

sublista = lista[2:]
print(sublista)

#   Podemos recorrer las posiciones de la lista con indices negativos por ejemplo:

sublista = lista[-4:-1]
print(sublista)

#   APARTADO 3: Comprobar si una lista contiene o no un elemento. Utilizaremos los operadores condicionales.
# Reutilizamos la lista que hicimos arriba.

lista = ["Dale", "un","buen", "Like", "Crack"]

palabra = "Like"
palabra_02 = "Melocotón"

if palabra in lista:
    print("La palabra pertenece a la lista")

if palabra_02 not in lista:
    print("La palabra no esta en la lista")

#   APARTADO 4: MODIFICAR ELEMENTOS DE UNA LISTA.

lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby", "Rust"]
print(lenguajes)                    # -> Imprimimos la lista lenguajes sin ninguna modificacion
lenguajes[1] = "Angular"            # -> Tomamos la posicion 1 de la lista y modificamos el elemento agregando un framework "Angular"   
print(lenguajes)                    # -> Imprimimos la lista y vemos que hemos cambiado el lenguaje "Java" por "Angular"
lenguajes[0] = lenguajes[0] + "++"  # -> Luego si agarramos el primer elemento de la lista "C" lo que hacemos es concatenarle (Ya que toda la lista tiene strings) "++"
print(lenguajes)                    # -> Imprimomos la lista para ver los resultados.

#   Procedemos hacer mas cositas.
#   Usaremos indices de nuevo

lenguajes[2:4] = ["Anaconda", "TypeScript"]     
# -> Aqui lo que estamos haciendo al definir limite inf y Limite sup. Estamos indicando que en la lista el elemento que esta en la posicion dos y el elemento que esta en la posicion 4 lo modificaremos con el nombre "Anaconda" y "TypeScript"
print(lenguajes)
# -> Cuando imprimimos vemos que el ultimo valor de la lista no se ha modificado. Que seria en este caso "Kotlin" ¿Xq no se ha modificado? bueno al asignarle ":4" lo que estamos haciendo es llegar al limite superior de la lista
# Entonces automaticamente lo que hace python es restarle al limite superior 1; 4-1= 3 (tres es la posicion que se modificará) en este caso "JavaScript"

#   -> Ahora a continuacion agregaremos mas elementos a nuestra lista en este caso agregaremos: "Varios", "Valores", "Botella"
#   y le asignaremos una posicion que modificaremos en la lista original. Pero veamos que sucede!!!!

lenguajes[4:5] = ["Varios", "Valores", "Botella"]

#   -> Aqui estamos indicando que en la posicion 4 en este caso "Kotlin" realizaremos una modificacion por los siguientes strings "Varios", "Valores", "Botella"

print(lenguajes) #   -> Luego imprimimos y vemos que sucede.

# -> ['C++', 'Angular', 'Anaconda', 'TypeScript', 'Varios', 'Valores', 'Botella', 'Ruby', 'Rust'] 
# Como podemos observar al nosotros indicar que en la posicion 4 cambiaremos el nombre del elemento. En este caso asignamos varios strings en la posicion 4 sin modificar o sobrescribir los siguientes elementos de la lista "Ruby" y "Rust"


#   APARTADO 5: Metodos de las listas: Añadir elementos.
#   En Python podemos utilizar métodos o funciones propias de las listas.
#   Para ejecutar estos metodos: variableDeTipoLista.metodo()

lenguajes = ["C", "Java", "Python", "JavaScript", "Kotlin", "Ruby", "Rust"]
print(lenguajes)

#   Metodo insert: Sirve para añadir un elemento a una lista
#   ¿Como añadir un elemento a la lista por medio de el metodo INSERT?
#   Al metodo insert lo que debemos pasarle como argumento es la posicion en la que yo quiero que se situe este añadido y el contenido a agregar. En este caso agregaré "C++". Se situará a la derecha de la posicion 0 ya que la que elejimos es la posicion 1.

lenguajes.insert(1, "C++")
print(lenguajes)

#   Metodo append: Lo que hace es agregar un nuevo elemento al final de la lista. No requiere posicion o indice y nos sobrescribe el ultimo elemento, crea una nueva posicion y la rellena con el valor que le indiquemos.

lenguajes.append("TypeScript")
print(lenguajes)

#   Metodo extend: Sirve para unir una lista con otra. Lo que unimos son los elementos de esta lista a la original.
#   Crearemos otra lista.

lenguajesDos = ["Vue", "Angular","React"]
lenguajes.extend(lenguajesDos)
print(lenguajes)
print(lenguajesDos)

#   APARTADO 6: Metodos de las listas: Eliminar elementos de una lista.

frutas = ["Bananas", "Manzanas", "Kiwis", "Melones", "Cerezas"]
print(frutas)

frutas.pop()    # -> Si yo utilizo el metodo pop sin pasarle ningun argumento a eliminar (Algun elemento de la lista) lo que hará es eliminar por defecto el ultimo elemento de la lista.
print(frutas)

frutas.pop(2)   # -> Si yo le paso algun indice dentro de los parentesis lo que estaré indicando es que eliminaré el elemento de la lista que le indiqué, en este caso "Kiwis"
print(frutas)

# Ejercicio de listas.

#   ENUNCIADO: Tenemos un texto dónde queremos encontrar palabras clave. 
#   Las palabras clave pueden ser hasta 5 y deberemos pedírselas al usuario 
#   y guardarlas en una lista. 

#   Si el usuario quiere poner menos de 5 palabras clave, deberá escribir 
#   "fin" para terminar de introducir datos. Si el usuario introduce 
#   números o nada, deberemos eliminarlos de la lista antes de la búsqueda.

#   En otra lista, deberemos guardar el número de veces que aparece cada 
#   palabra clave en nuestro texto. Por ejemplo, si las palabras clave son
#   ordenador y portátil y aparecen 5 y 7 veces respectivamente, nuestras listas
#   deberían ser así: 
#       -   keywords = ["ordenador", "portátil"]
#       -   ocurrencias = [5, 7]
"""
texto Seguramente hayas notado que tu productividad ha bajado desde que trabajas desde casa. 
Es muy importante que logremos teletrabajar efectivamente y de manera autorregulada. 
Esto se traduce en finalizar antes nuestras tareas y evitar jornadas laborales interminables.
El primer consejo y uno de los más importantes ya te lo he dado en el apartado anterior. 
Tenemos que construir un espacio de trabajo en el que nos sintamos cómodos y dispongamos de todas las herramientas necesarias para teletrabajar. 
En la medida de lo posible, es importante teletrabajar siempre en el mismo lugar. 
De esta forma, nuestro cerebro asocia el sitio con la acción de trabajar y nos hará estar más focalizados en nuestras tareas."""""""

#   Pista: Podemos pasar de una cadena de texto a una lista de palabras mediante
#   el método texto.split(). Por ejemplo:
"""

texto = "hola que tal"
print(texto.split())
