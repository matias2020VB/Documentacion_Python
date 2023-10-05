# Capitulos 7: Metodos de Strings

# Apartado 1: Metodos find, index y count

# Los metodos find e index sirven para encontrar conjuntos de caracteres dentro de un string
# (Por ejemplo), una palabra dentro de una frase.

# Metodo Find
#En este ejemplo podemos usar el metodo index o el metodo find veamos con ambos.

# Si yo quiero validar esta variable que es realmente un correo puedo buscar un caracter como el arroba, si esta variable contiene el arroba o no.

# Método INDEX
"""
mail = "correo@gmail.com"

posicion = mail.index('@')

print(posicion)

# Método FIND

posicion = mail.find('@')
print(posicion)

# El metodo find lo que hace es que cuando no encuentra el caracter o palabra que estemos buscando automaticamente nos va a mostrar un indicador (-1) -> Que simboliza que no ha encontrado dicho caracter.

# A diferencia del metodo find, el metodo index cuando no lo encuentra nos va a largar un error al ejecutar el codigo. (Por ejemplo: substring not found)

posicion = mail.find('*') # --> Al ejecutar este metodo nos dará como resultado = -1 --> Ya que en este correo: correo@gmail.com NO encontro el caracter que nosotros pasamos.
print(posicion)

#posicion = mail.index("*") # --> Al ejecutar este metodo nos dara como resultado un error = "Substring not found" ya que en el mail no encontro el caracter que nosotros hemos pasado.
#print(posicion)

# Ahora lo siguiente, como se cual tengo que usar si realmente hacen lo mismo? Ambos me devuelven la posicion del caracter que yo quiero investigar.

# La conveniencia de usar uno u otro dependerá de que necesitamos nosotros que haga nuestro programa. Porque si nosotros queremos que el programa se siga ejecutando normalmente nosotros podemos comprobar con el -1 que realmente no ha encontrado
# el caracter que nosotros hayamos pasado y el programa seguirá ejecutandose normalmente.

# En caso de que no nos importe si el programa debe seguir ejecutandosé, con el metodo index nos largara un error y parará nuestro programa.

# Metodo COUNT:

# Devolvernos la cantidad de veces que encuentra un substring o un caracter dentro de nuestro string.

apariciones = mail.count('r')
print(f"La letra r aparece: {apariciones} veces")"""

# Apartado 2: Métodos split, replace y join

# El metodo split nos sirve para dividir un string mediante un delimitador y convertir cada division en un elemento de una lista.
"""
compra = "Chocolate, Pan, Agua, Banana, Verduras" # -> Como podemos observar yo puedo pasarle una coma para dividir palabra por palabra cuando use el metodo split 
ListaDeCompra = compra.split(', ')
print(ListaDeCompra)
print(f"En la lista de la compra tenemos: {len(ListaDeCompra)} elementos ")


compra2 = "Azucar Cafe Gaseosa Manzana Cerveza Platos Huevos" # -> Tranquilamente puedo no agregar una coma para separar palabra de cada palabra. Cuando utilizo el metodo split automaticamente cuando muestro por pantalla me lo separa el mismo metodo
ListaDeCompra2 = compra2.split()
print(ListaDeCompra2)
print(f"En la lista de la compra 2 tenemos: {len(ListaDeCompra2)} elementos ")


# El metodo replace nos sirve para reemplazar un substring por otro.

compraGuiones = compra.replace(', ', ' - ' )
print(compraGuiones)

compra2 = compra.replace(', ', ' ' )
print(compra2)


# El método join nos sirve para unir una lista de strings en un unico string mediante un caracter determinado.

compra = " ".join(ListaDeCompra)
print(compra)"""

# EJERCICIO: Tenemos unas descripciones de algunos productos.
# En ellas se incluye el precio de cada producto. Debemos encontrar el precio en $ y mostrarlo por pantalla.
# El precio puede tener: 0,1 o 2 decimales y siempre va seguido del simbolo $. Por ejemplo.

#   -   9.99$
#   -   10$
#   -   10.5$



# BONUS: Deberemos modificar las descripciones para que el precio se muestre en dolares.
# La conversion es: 1$ = 1.21 USD. No hace falta modificar la variable original de la descripcion, podemos retornar una copia con el precio convertido

# SOLUCION: 

des1 = "Este bolso de cuero de la marca: Miguel Cors tiene un precio de 199.99€. Es una oferta especial."
des2 = "Las botas de la marca: Nique valen 89€. Nunca han estado tan rebajadas."
des3 = "¡Tenemos el bambú en oferta! Cómpralo ahora por 1.2€ el kg ¡No la dejes pasar!"

# Podemos armar una funcion

def findPriceAndReplace(txt):
    txtList = txt.split()
    pos = -1
    indx = -1
    conversion = 1.21
    for palabra in txtList:
        pos = palabra.find("€")
        if pos != -1:
            indx = txtList.index(palabra)
            break
    precio = txtList[indx]
    precio = precio.split('€')[0]
    txtList[indx] = str(float(precio)*conversion) + '$'
    newDesc = " ".join(txtList)
    return precio, newDesc

precio, newDesc = findPriceAndReplace(des1)
print(precio)
print(newDesc)
precio, newDesc = findPriceAndReplace(des2)
print(precio)
print(newDesc)
precio, newDesc = findPriceAndReplace(des3)
print(precio)
print(newDesc)