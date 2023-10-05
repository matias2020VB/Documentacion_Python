# Capitulo 2: Variables, Tipos de datos y operadores aritmeticos
"""
    VARIABLES : ¿Que son?

Las variables son un lugar en la memoria de nuestro ordenador donde vamos a guardar una informacion en concreto. 
Esa informacion la vamos a poder leer y modificar a lo largo del proceso.

    TIPOS DE DATOS: ¿Que son?
Los tipos de datos son diferente informacion que podemos almacenar en una varible, como por ejemplo:
    a) Numeros enteros
    b) Numeros decimales
"""
numero_entero = 1
print(numero_entero)

numero_decimal = 2.46
print(numero_decimal)

numero_entero = numero_entero + 2
print(numero_entero)

numero = numero_entero + numero_decimal
print(numero)

numero_entero += 2 # Toma el valor actual de numero entero y le sumas dos
print(numero_entero)

var_num = 20
var_num = var_num - 10
print(var_num)

var = 10 
var = var / var_num
print(var)

numero = 2/2+3 
print(numero)

factor = 2*3
print(factor)
factor = numero_entero*numero_decimal
print(factor)

potencia = 2**3
modulo = 11%2
print(potencia)
print(modulo)

#TIPOS DE DATOS: Texto
texto = "Esta es una frase"
print(texto)

texto = "texto 'entre comillas' guay"
textt = 'texto "Entre comillas" guay'
text = 'texto entre comilla simple'
txt = 'Hola'
print(texto)
print(text)
print(textt)
print(txt)


texto_con_formato = """ Esto es un texto
    con formato

"""
print(texto_con_formato)







