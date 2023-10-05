class Persona:
    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
    
    def presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años, mi DNI es: {self.DNI}")
"""
ana = Persona("Ana", 26, "41285133")
ana.presentarse()
print(ana.edad)
"""
# 1ro: PROCEDEMOS A APLICAR EL CONCEPTO DE HERENCIA POR LO QUE TENEMOS QUE DEFINIR OTRA CLASE.
# 2do: Luego dentro de la clase Trabajador le corresponderemos sus metodos y atributos.

class Trabajador(Persona):
    def __init__(self, nombre, edad, DNI, sueldo, cargo, empresa):
        super().__init__(nombre, edad, DNI) # -> super: Es una referencia a la clase Persona (Clase Padre)

# Al haber agregado mas atributos a nuestra clase como: sueldo, cargo y empresa. Por lo que estamos haciendo es una combinacion de el metodo (init)
# de nuestra clase Padre (Persona) con nuestros campos especificos de la clase hijo (Trabajador)

        self.sueldo = sueldo  
        self.cargo = cargo
        self.empresa = empresa

# Aunque la clase este vacia (pass) de por si la clase trabajador esta heredando los metodos y atributos de la clase Persona.
# Al ejecutar las siguientes intancias corroboramos la herencia

# Este metodo solamente podemos utilizarlo con la clase hija (Trabajador) ya que esta clase tiene solamente el atributo de sueldo. La clase padre no la contiene.
    
    def calcularSueldoAnual(self):
        return 12*self.sueldo + 2000


# Ahora a continuacion vamos a crear otra clase para mostrar el concepto de la Herencia Jerarquica (Son varias subclases que heredan de la clase padre Persona)

class Estudiante(Persona):
    def __init__(self, nombre, edad, DNI, universidad, curso, asignatura):
        super().__init__(nombre, edad, DNI)
        self.universidad = universidad
        self.curso = curso
        self.asignatura = asignatura

    def describirse(self):
        print(f""" ¡Holaaaa! soy {self.nombre}!. Tengo {self.edad} estudio en la {self.universidad} pertenezco al curso {self.curso}! y estudio las materias {self.asignatura}
        """)
"""
trabajador = Trabajador("Juan", 24 , "1727189A", 1500, "Empleado administrativo", "Google") # -> Instancia de la clase.
trabajador.presentarse()
print(trabajador.nombre)
print(trabajador.calcularSueldoAnual())
"""
estudiante = Estudiante("Silvina", 25, "41243123", "Universidad de Mendoza",3, ("Programacion", "Calculo", "Algebra"))
estudiante.describirse()

