#  ======= INICIO DE LA PARTE 2 ========

#   Break, continue, pass

#   Break (Es una instruccion que consiste en decir que el bucle que hemos propuesto ha terminado; a diferencia del continue, éste si sale del bucle)

frase = "En este momento estoy buscando la letra a"
letra = "y"

for caracter in frase:
    if(caracter == letra):
        print(f"letra {letra} encontrada en la posicion {frase.index(caracter)}!!") # Usamos el metodo index (indice) que nos especificará en que posicion se encuentra dicha letra en la frase propuesta por nosotros.
        print(caracter)
        break
    else:
        print("No hemos encontrado nada de momento.")
    print(caracter)


# Cuantas veces aparece la letra A en la frase.

#   Continue:   Es una instruccion que te envia a la siguiente iteración pero sin salir del bucle. 
#               Si colocamos mas lineas de codigo debajo del continue lo que va a pasar es que ese codigo no se ejecute.

frase = "Hola Ana"
letra = "a"
count = 0

for caracter in frase:
    if(caracter == letra):
        count += 1
        print(f"Letra encontrada {count} veces")
        continue
        print("Hola que tal")   # En esta linea lo que esta ocurriendo ademas de tener un continue en la linea de arriba. si ejecutamos no nos lo imprime ya que se saltea la iteracion}
    print("No hemos encontrado nada")

#   Pass: Es una instruccion que no hace nada. dejar vacío.

lista = [ 0, 10, 20, 25]
for jose in lista:
    if(jose == 10):
        pass
    print(f"El valor de Jose es: {jose}")



#   Else: En este caso Else lo que hace es que una vez se haya terminado todas las iteraciones posibles que me imprima "La frase tiene {count 'tantos caracteres de la frase' caracteres}"
# Vamos a contar todos los caracteres de una frase.

frase = "Todos los caracteres de una frase"
count = 0
for caracter in frase:
    count += 1
else:
    print(f"La frase tiene {count} caracteres")



#Ejercicio: El usuario debe adivinar un numero entre 0 y 10.
#El programa deberá pedir que el usuario introduzca un numero
#y debe decir si ha acertado, si el numero a adivinar es menor o mayor que el ha introducido.

numero_correcto = 6

def numero_comprobando(numero_correcto):
    num = int(input("Oye, adivina el número :3: "))
    if num == numero_correcto:
        print("has adivinado el numero correctamente, te has ganado un cafecito!!! :D ")
        return True
    elif num > numero_correcto:
        print("Oye no has adivinado el numero, prueba con un numero mas pequeño :( ")
        return False
    elif num < numero_correcto:
        print("Oye no has adivinado el numero, prueba con un numero mas grande por favor, no te des por vencido.")
        return False

#   A continuacion plantearemos un while ya que necesitamos que el usuario pueda jugar tantas veces sea necesario para adivinar el numero correcto.
#   Si no ponemos el while le estaremos dando una sola oportunidad para adivinar el numero correcto
#   Si ponemos while(True) -> Estaremos diciendo que se ejecute todas las veces necesarias, infinitamente digamos, haaaasta que se encuentre con un break.
#   Colocamos un booleano para comprobar que sea True. -> Una vez comprobemos que el numero sea correcto (True) -> pondremos un Break para finalizar el programa.


while(True): 
    if(numero_comprobando(numero_correcto)): #  -> Esta funcion me devuelve un booleano (True) ya que se esta verificando la condición de que el numero que ingreso el usuario es correcto.
        break

#   De que otras formas podemos hacer este bucle while?
#   A continuacion veremos como.. podriamos hacer:

    while(True):
#   Planteamos una variable
        retorno = numero_comprobando(numero_correcto)
        if(retorno == True):



# Otra forma de hacer el while tambien puede ser la siguiente.

            """
        while(not(numero_comprobando(numero_correcto))):
        pass
    else:
        print("Fin del juego, gracias por jugar")
"""

#   En el while lo que hacemos es plantear; Mientras no haya acertado el numero correcto voy a seguir ejecutando esta funcion.
#   ponemos Pass porque no hay nada mas que hacer.

#   Ambas opciones son correctas, dejar la que mas se amolde a la situación.
