class Camiseta:
# El metodo init (Constructor de la clase) se encarga de iniciar o construir un objeto. self: es una referencia que hace al objeto que estamos creando de la clase.
# Para crear objetos con los mismos valores o atributos tenemos que pasarle como argumento los atributos que hemos definido. -> (self): -> (self, marca, precio, talla, color):    
    def __init__(self, talle, color, precio, marca): 
        self.talle = talle
        self.color = color
        self.precio = precio
        self.marca = marca
        self.rebajada = False
    
#METODO 1
    def aplicarDescuento(self, porcentaje): # ¿Porque indicamos self como argumento?
        self.precio = self.precio - self.precio*porcentaje/100
        if porcentaje < 100:
            self.rebajada = True

#METODO 2 
    def infoProducto(self):
        info =  f"Descripcion de la camiseta: \nTalle: {self.talle}\nColor: {self.color}\nPrecio: {self.precio:.2f}$\nMarca: {self.marca}\n"
        if self.rebajada:
            info += "Este producto está rebajado."
        return info
# Como crear un objeto de esta clase camiseta.
# Definimos una variable llamada camiseta
camiseta = Camiseta("L", "Verde", 19.99, "Gucci")
camisetaAdidas = Camiseta("XL", "Azul", 29.99, "Adidas")

camisetaAdidas.aplicarDescuento(50)
camiseta.aplicarDescuento(20)
print(camiseta.infoProducto())

print(" ----------------------- ")

print(camisetaAdidas.infoProducto())

