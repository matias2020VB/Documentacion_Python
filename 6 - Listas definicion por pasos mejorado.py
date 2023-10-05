# Capitulo 6: Listas
# Apartado 1: Repaso de conceptos basicos

# Creamos una lista llamada numeros. -->  (PASO 1)
# como accedemos a su primera posicion. "en este caso el nro 1 de la lista" --> (PASO 2)
# Guardamos la lista en una variable y citamos la primera posicion de la lista.--> (PASO 2.1)
# Si quiero saber la longitud de la lista ejecuto el comando: len --> (PASO 3)
# Podemos iterar sobre la lista. Por ejemplo utilizando un bucle for --> (PASO 4)


numeros = [1, 2, 3, 4, 5] # PASO 1
print(numeros)
primeraPosicion = numeros[1] # PASO 2 Y 2.1
longitud = len(numeros) # PASO 3
print(f"El primer valor es: {primeraPosicion}\nLa longitud de la lista es: {longitud}") # PASO 4

for num in numeros:
    print(num)

# Apartado 2: Indexado y sublistas
# Creamos una lista con elementos tipo string. --> PASO A
# En las listas podemos recurrir a el posicionamiento de cada elemento de la lista en forma negativa tambien a diferencia de arriba. --> PASO 1
# Podemos hacerlo con indices negativos. Por ejemplo si yo elijo el indice [-1] --> Corresponderia a "Crack" --> PASO 1.1
# Si yo quisiera pedir el penultimo elemento de la lista y que me lo muestre por pantalla tenemos que elejir el indice [-2] --> PASO 2


lista = ["Dale", "un", "buen", "like", "crack"] # --> PASO A

print(lista)

ultimaPosicion = lista[-1] # --> PASO 1 Y 1.1
print(ultimaPosicion)

penultimaPosicion = lista[-2] # --> PASO 2
print(penultimaPosicion)

# Sublistas
# Si yo quiero acceder a varios elementos de la lista lo que hacemos es armar un par ordenado declarando el limite inferior (Primer elemento elegido) y el limite superior (Elemento de la lista -1) --> PASO 1
# Si yo quiero acceder al primer elemento de la lista tranquilamente puedo dejar el limite inferior en cero y colocar dos puntos y declarar el limite superior. --> PASO 2
# Tambien podemos hacer lo siguiente: Elegir desde que posicion o elemento (En el ejemplo elijo la posicion 2. "buen") queremos acceder hasta recorrer toda la lista de la siguiente forma. --> PASO 3
# Podemos utilizar indices negativos o limites negativos. --> PASO 4

sublista = lista[1:4] # --> PASO 1
print(sublista)

sublista = lista[:4] # --> PASO 2
print(sublista)

sublista = lista[2:] # --> PASO 3
print(sublista)

sublista = lista[-4:-1] # --> PASO 4
print(sublista)

# Apartado 3: 
# Comprobar si una lista contiene o no un elemento. --> PASO 1
# Para comprobar que SI ESTÁ en una lista usamos el condicional if + la palabra que guardamos en la variable (palabra1) + preposicion (in: dentro) + la lista. --> PASO 2
# Para comprobar SI NO ESTÁ en una lista usamos tambien un condicional if + la palabra guardada en la variable (palabra2) + preposicion (not in: no esta dentro) + la lista. --> PASO 3

lista = ["Dale", "un", "buen", "like", "crack"] # --> PASO 1 LISTA A COMPROBAR

palabra1 = "like" # --> PALABRA A COMPROBAR

palabra2 = "melocoton" # --> PALABRA A COMPROBAR

if palabra1 in lista: # --> PASO 2.
    print("La palabra pertenece a la lista")
    
if palabra2 not in lista: # --> PASO 3.
    print("La palabra no esta en la lista")

# Apartado 4: Modificar elementos de una lista.

# Creamos una lista con lenguajes de programacion.
# Si yo quiero modificar algun elemento de la lista debemos citar la variable (lenguajes) añadirle la posicion del elemento de la lista que queremos cambiar y utilizamos en forma string (en este caso un string pero puede ser cualquier cosa) el nombre que queremos cambiarle al elemento --> PASO 1
# Tambien podemos modificar un elemento de la lisa concatenandole un nombre citando la posicion del elemento + el contenido que queremos agregarle. --> PASO 2
# Tambien podemos modificar todos los elementos de la lista debemos usar (INDICES - INDEX) Por ejemplo de la siguiente manera: --> PASO 3
# Podemos tambien agregar varios elementos en la lista: Pensando y haciendo una diferencia (4-5=1) Un elemento es el que se cambia y agrega los otros tres en este caso. "Varios" reemplaza a Kotlin, "Valores", "Botella" son agregados sin modificar a "Ruby" y a "Rust" --> PASO 4


lenguajes = ["C", "Java", "Python", "Kotlin", "JavaScript", "Ruby", "Rust"]
print(lenguajes)

lenguajes[1] = "Angular"   # --> PASO 1
print(lenguajes)

lenguajes[0] = lenguajes[0] + "++"   # --> PASO 2
print(lenguajes)

lenguajes[2:4] = ["Anaconda", "Typescript"]  # --> PASO 3
print(lenguajes)

lenguajes[4:5] = ["Varios", "Valores", "Botellas"]  # --> PASO 4
print(lenguajes)


# Apartado 5: Veremos Metodos de las listas: Para añadir elementos.

# En Python podemos utilizar metodos con las listas.
# Para ejecutar estos metodos lo hacemos de la siguiente manera: --> variableDeTipoLista.metodo()

# Podemos agregar elementos a nuestra lista en la posicion que nosotros elijamos, para eso vamos a usar indices para indicar en que posicion de la lista queremos estos elementos nuevos.
# Método Insert(): Lo que hace es insertar un elemento dentro de nuestra lista en la posicion que nosotros queramos. NO reemplaza los elementos que ya tenemos. Solo lo agrega. ---> PASO 1
# Método Append(): Este metodo lo que hace es agregar un nuevo elemento al final de la lista y lo sobreescribe. NO utilizamos INDICE ya que coloca este elemento al final de la lista. ---> PASO 2
# Método Extend(): En listas sirve para unir dos listas en una sola. ---> PASO 3 

# A continuacion creamos otra lista que la vamos hacer interactuar con nuestra lista lenguajes.
# Si yo quiero añadir la lista de frutas dentro de la lista lenguajes lo que hay que utilizar es el metodo extend

lenguajes = ["C", "Java", "Python", "Kotlin", "JavaScript", "Ruby", "Rust"]
print(lenguajes)

lenguajes.insert(1, "C++")  # ---> PASO 1
print(lenguajes)

lenguajes.append("Typescript")  # ---> PASO 2
print(lenguajes)

frutas = ["Manzana", "Pera", "Naranja"] 
lenguajes.extend(frutas)  # ---> PASO 3
print(lenguajes)
print(frutas)

# TAMBIEN PODEMOS UTILIZAR EL METODO APPEND DESDE LA 2DA LISTA QUE CREAMOS DONDE LE AÑADIREMOS TODA LA LISTA DE LENGUAJES.

frutas.append(lenguajes)
print(frutas)


# Apartado 6: Metodos de las listas para eliminar elementos.
    # Tenemos tres opciones.

# 1) Método pop(): sin especificar un indice que por predefinido lo que hace es eliminar el ultimo elemento de la lista. ---> PASO 1

# 1.1) Metodo pop(0): Especificando un indice lo que hace es eliminar el elemento correspondiente de la posicion. En este ejemplo la posicion (0) Corresponde a "Peugeot". ---> PASO 1.1
# Una nota del metodo pop que lo que hace es retornarnos el valor eliminado si guardamos el metodo en una variable. a continuacion lo mostraré. ---> PASO 1.2

# 2) Metodo remove(): Este metodo lo que hace es eliminar el elemento que nosotros le proporcionemos. En este caso elegimos "Audi" por lo que el metodo va a buscar este valor y lo borrará. ---> PASO 2

# 3) del: (Palabra reservada) Lo que podemos ver es que elimina la palabra "Volkswagen" una lista sigue siendo una lista con un solo elemento ---> PASO 3

# 4) Metodo index: Retornarnos el indice de un valor de la lista si este valor existe. Nos muestra por pantalla el valor "0" ya que la palabra "Fiat" está en esa posición.  # ---> PASO 4
# Una nota del metodo index: Nos sirve para intercambiar el valor de la lista por la posicion en la que esté este valor.

autos = ["Peugeot", "Volkswagen", "Fiat", "Audi", "BMW"]
print(autos)

autos.pop()  # ---> PASO 1
print(autos)

autos.pop(0) # ---> PASO 1.1
print(autos)

elementoEliminado = autos.pop(0) # ---> PASO 1.2
print(autos)
print(elementoEliminado)


autos.remove("Audi")  # ---> PASO 2
print(autos)

del autos[0]  # ---> PASO 3
print(autos)

indice = autos.index("Fiat")  # ---> PASO 4
print(indice)

# Apartado 7: Ejercicio.

# ENUNCIADO: Tenemos un texto donde queremos encontrar palabras clave.
# Las Palabras clave pueden ser hasta 5 y deberiamos pedirselas al usuario y guardarlas en una lista.

# Si el usuario quiere poner menos de 5 palabras clave, deberá escribir "fin"
# para terminar de introducir datos. Si el usuario introduce numeros o nada, deberemos eliminarlos de la lista antes de la busqueda.

# En otra lista, deberemos guardar el numero de veces que aparece cada palabra clave en nuestro texto. Por ejemplo, si las palabras clave son
# ordenador y portatil y aparecen 5 y 7 veces respectivamente, nuestras listas deberian ser asi:
#       -  keywords = ["ordenador", "portátil"]
#       -  ocurrencias = [5, 7]

# ----------Pista:------------
# Podemos pasar de una cadena de texto a una lista de palabras mediante
# el metodo texto.split(). Por ejemplo

#texto = "Hola, que tal"
# print(texto.split())

#texto = ['hola', 'que', 'tal']

# SOLUCION: -> Se ha propuesto esta SOLUCION en 5 pasos por favor prestar atencion a cada paso.


# Creamos las listas que vamos a usar, por el momento las crearemos vacias
    
keywords = [] # --> Lista de palabras claves.
repeticiones = [] # --> N° de veces que encontramos las palabras claves.

# PASO N°:1 
# Rellenar la lista de keywords con las palabras que ingrese el usuario. No necesariamente deben ser 5 pueden ser 4 o 3 o 2 o 1.

# Procedemos a hacer un bucle FOR.

for x in range(5):
    keyword = input("Ingresa una palabra o escribe fin para terminar: ")
    if keyword == "fin":
        break
    else:
        keywords.append(keyword)
print(keywords)

# Este condicional "FOR" tiene la funcion de pedirle una palabra al usuario o de lo contrario si quiere terminar el programa que escriba "fin"
# Luego debemos plantear una condicion de que si la palabra que escribio el usuario es fin que se interrumpa (break) el bucle y termine el programa.
# Si "fin" NO es lo que escribio el usuario directamente que esa palabra la agregue a la lista "keywords"
# Seguimoss....

# PASO N°:2
# Luego lo que debemos hacer es pensar que si el usuario INGRESA NUMEROS O DIRECTAMENTE NO ESCRIBE Y DEJA VACIO generará un problema en el programa y es que almacenará un espacio vacio en nuestra lista keywords
# Por lo que debemos evitarlo y eliminar de la lista ese espacio vacío.


posicion = 0 # --> Definimos la posicion (0) ya que el primer elemento de la lista seria la primera palabra que ingrese el usuario
while(True):
    if posicion >= len(keywords):
        break
    if keywords[posicion] == '': # --> Si lo que ingreso no es un numero ni una palabra, es un espacio vacio, automaticamente borramos el espacio con el metodo pop
        keywords.pop(posicion)
    elif keywords[posicion].isnumeric(): # --> Si es un numero automaticamente con el metodo pop lo eliminamos
        keywords.pop(posicion)
    else:
        posicion += 1
print("Lista de Keywords corregida")
print(keywords)


# NOTA 1) 
# con el metodo .isnumeric(): -> Este metodo nos devuelve una comprobacion del tipo True/False dependiendo los valores que evalue el metodo como se observa a continuacion.


texto = "22" 
"""
texto.isnumeric(): # -> True

texto = "hola"
texto.isnumeric(): # -> False"""


# NOTA 2) 

# ¿Porqué ponemos posicion +=1? Lo demostraré con un ejemplo.

# Supongamos que tenemos esta lista

# keywords = ["3", "botella"]

# Tomando como referencia el condicional while de arriba hacemos iterar el bucle

# Pasando por el primer "if" podemos observar que esa condicion no se cumple por lo que pasa a la siguiente condicion

# Esta condicion si se cumple ya que el "3" es un numero que esta en la posicion 0 de la lista, con el metodo pop lo borra y queda solamente el elemento "botella"

# -> Quedaria keywords = ["botella"]

# Suponiendo que tengamos mas elementos de la lista como por ejemplo: (Añado: "Hola", "Matias")

# keywords = ["botella", "Hola", "Matias"] -> Como podemos ver ahora en la posicion 0 le corresponde a "botella", ya no se cumpliria ninguna condicion del bucle por lo que debemos pasar al siguiente elemento de la lista para que compruebe si es un numero
# o si es un espacio vacio. Aqui es donde entra en juego: posicion += 1 -> Donde definimos que pase al siguiente elemento de la lista. Si las condiciones no se cumplen ya que es una palabra, pasa al siguiente elemnto y asi consecutivamente.

# PASO N°:3

texto = texto.split()

# Este metodo lo que hace es convertir cada palabra de un texto en una lista de palabras.
# Por ejemplo si yo tengo: -> texto = "Hola que tal" -> El metodo lo que hace es darme el siguiente formato -> texto = ["hola", "que","tal"] esto se hace para poder iterar sobre la lista
# Que pasa si no aplicamos este metodo,si no iteraramos sobre el texto lo que haria el bucle for es recorrer caracter por caracter del texto osea letra por letra de cada palabra y eso no es lo que nos interesa.

# PASO N°:4

# Ahora lo que tenemos que hacer una vez convertido el texto en una lista de palabras, debemos recorrer la lista de la siguiente forma: (Con un bucle for)

for palabra in texto:
    for keyword in keywords:
        if keyword == palabra:
            pos = keywords.index(keyword)
            repeticiones[pos] += 1
            break

# Este bucle lo que hace es agarrar la primera palabra del texto, agarramos la primera keyword de la lista de keywords

# Luego comprobamos si la keyword es igual a la palabra del texto, si es que sí, se ejecuta lo siguiente del codigo y si es que no, tomamos la siguiente keyword.    

# Una vez hayamos pasado por todas las keywords y hayamos comparado cada keyword con cada palabra del texto lo que hace el bucle es reiniciarse y pasaremos a la siguiente iteracion

# del bucle (for palabra in texto:)

# Si se cumple keyword == palabra -> Lo que tenemos que conocer es el indice o la posicion de esa keyword ¿Porqué?

# Porque tenemos que acceder a la lista de ocurrencias en la misma posicion que la lista de palabras claves.
# Por ejemplo si yo tengo la lista:

#       -  keywords = ["ordenador", "portátil"]
#       -  repeticiones = [5, 7]
# Si yo tengo "ordenador" en la primera posicion en la lista de repeticiones tengo que modificarlo para que esten en la misma posicion.
# Por lo que tomamos el indice de esa palabra clave y lo utilizamos para acceder a la posicion correspondiente de la lista de repeticiones. Entonces en esa posicion sumamos uno. (+= 1)

# ¿Porqué ponemos break?
# Porque estamos asumiendo que el usuario no ha puesto repetida la misma palabra clave por lo tanto si tenemos "Ordenador" y "Botella"
# if keyword == palabra: si esa palabra: Es ordenador no hace falta que la comparemos con botella porque ya sabemos que es otra keyword por lo tanto ponemos un break.

# PASO N°:5
#Inicializamos la lista de repeticiones

for x in range(len(keywords)):
    repeticiones.append(0)

print(repeticiones)

# RESOLUCION DE EJERCICIO CON CODIGO COMPLETO SIN ANOTACIONES! :D

texto = """Seguramente hayas notado que tu productividad ha bajado desde que trabajas desde casa.
Es muy importante que logremos teletrabajar efectivamente y de manera autorregulada.
Esto se traduce en finalizar ante nuestras tareas y evitar jornadas laborales interminables.
El primer consejo y uno de los mas importantes ya te lo he dado en el apartado anterior.
Tenemos que construir un espacio de trabajo en el que nos sintamos cómodos y dispongamos de todas las herramientas necesarias para teletrabajar.
En la medida de lo posible, es importante teletrabajar siempre en el mismo lugar.
De esta forma, nuestro cerebro asocia el sitio con la accion de trabajar y nos hará estar mas focalizados en nuestras tareas."""

keywords = [] 
repeticiones = []

for x in range(5):
    keyword = input("Ingresa una palabra o escribe fin para terminar: ")
    if keyword == "fin":
        break
    else:
        keywords.append(keyword)
print(keywords)

posicion = 0
while(True):
    if posicion >= len(keywords):
        break
    if keywords[posicion] == '': # --> Si lo que ingreso no es un numero ni una palabra, es un espacio vacio, automaticamente borramos el espacio con el metodo pop
        keywords.pop(posicion)
    elif keywords[posicion].isnumeric(): # --> Si es un numero automaticamente con el metodo pop lo eliminamos
        keywords.pop(posicion)
    else:
        posicion += 1
print("Lista de Keywords corregida")
print(keywords)

texto = texto.split()

for x in range(len(keywords)):
    repeticiones.append(0)

for palabra in texto:
    for keyword in keywords:
        if keyword == palabra:
            pos = keywords.index(keyword)
            repeticiones[pos] += 1
            break
print(repeticiones)
