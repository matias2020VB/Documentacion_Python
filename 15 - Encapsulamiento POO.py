class Circulo:
    def __init__(self, radio):
        self.__radio = radio
        self.__pi = 3.1415

    
    def calcularPerimetro(self):
        return 2*self.__pi*self.__radio

    
    def calcularArea(self):
        return self.__pi*self.__radio**2


    def getPi(self):
        return self.__pi

    
    def setRadio(self, nuevoValor):
        if type(nuevoValor) == int or type(nuevoValor) == float:
            if nuevoValor > 0:
                self.__radio = nuevoValor
                print(f"El radio se ha modificado correctamente: {self.__radio}")
            else:
                print("Oye el radio no puede ser negativo")
        else:
            print("El radio tiene que ser un número positivo")


c1 = Circulo(2.5)
print(c1.calcularArea())
print(c1.calcularPerimetro())
print(f"La constante PI es {c1.getPi()}")
c1.setRadio(34)
c1.setRadio(-23)
c1.setRadio("holaquetal")

# atributo: __radio -> _Circulo__radio . En general _NombreDeLaClase__nombreDelAtributo


# NOTA:   1ro) Para probar el encapsulamiento lo que haremos a continaucion es colocar nuestros atributos que deben ser
#        "protegidos". La sintaxis es ._ desde dentro de la clase deberiamos poder acceder a ellos pero desde fuera no.
#
#        2do) Para hacerlos "privados" colocaremos en los atributos la sintaxis .__ por lo que fuera de la clase no podriamos acceder
#        pero si dentro de la clase.
#        Si ejecutamos y nos da este error: 
        
#        File "c:\Users\usuario\Desktop\Codics\Curso Dimas\Encapsulamiento POO.py", line 27, in <module>
#    print(f"La constante pi es {c1.__pi:.2f}")
#                                ^^^^^^^
# AttributeError: 'Circulo' object has no attribute '__pi'

#Ahora: Cuando nosotros en python definimos un metodo o un atributo que empieza con dos guiones bajos (.__) lo que hace python automaticamente

# es: Por ejemplo: Si yo defino el atributo radio (__radio) con los dos guiones bajos python transforma de forma inmediata a esta sintaxis -> _Circulo__radio -> En general _NombreDeLaClase__nombreDelAtributo O metodo.

# Si nosotros colocamos en este print: print(f"La constante pi es {c1._Circulo__pi:.2f}") con la sintaxis que transforma python y la ejecutamos!

# Podemos comprobar que nos muestra los prints que hemos planteado podemos acceder a nuestro atributo pi si existiese la encapsulacion en este caso
# no deberiamos poder acceder a nuestro atributo pi ya que es privado y estamos por fuera de la clase. 

# 19.634375000000002
# 15.707500000000001       
# La constante pi es 3.1415

# ¿Qué está ocurriendo?
#    Cuando nosotros definimos un metodo o un atributo dentro de una clase empezando por los dos guiones bajos python hace lo siguiente:
#    _Circulo__radio

#    Esto lo hace para que si nosotros en nuestro programa tenemos muchas clases que heredan de otras con algunos atributos con los mismos nombres, Python hace esto para evitar que nombres de metodos o atributos de clases distintas colisionen.
#    
