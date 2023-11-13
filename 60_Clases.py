import random
# Clases (Programación Orientada a Objetos POO)

class Book():
    '''
    Clase para trabajar con libros
    '''
    def __init__(self, titulo, autor, electronic = False):
        self.titulo = titulo
        self.autor = autor
        self.electronic = electronic
        
    
print (Book.__doc__) # Accedemos a la documentación que le hemos asignado a la clase

# Creamos un hijo de la clase
book1 = Book('El señor de los anillos', 'J.R.R Tolkien', False)
print (book1.titulo)
print (book1.autor)
print (book1.electronic)

# Creamos otro hijo de la clase
book3= Book('Juego de tronos', 'Geroge R.R. Martin', False)
print (book3.titulo)
print (book3.autor)
print (book3.electronic)

# Otra clase

class Coche():
    def __init__(self, color = '', modelo = '' ):
        self.color = color
        self.modelo = modelo
        
coche1 = Coche(color='amarillo', modelo='Renault')
print (coche1.color)
print (coche1.modelo)

# Método destructor

class Animales():
    def __init__(self, nombre, patas):
        self.nombre = nombre
        self.patas = patas
        
    def __del__ (self):
        print ('Acabamos de crear un método destructor que se encargará de eliminar basura')


perro = Animales('Toby', 4)
print (perro.nombre)
print (perro.patas)
del perro

# Métodos de una clase (de instancia, estáticos, de clase)

# Métodos de instancia:

class Rectangulo():
    def __init__(self, base = 1, height = 1, color = 'blue'):
        self.base = base
        self.height = height
        self.color = color
        
    def perimetro(self):
        return 2 * self.base + 2 * self.height 
    
    def area(self):
        return self.base * self.height
    
    def is_base_big (self, min = 5):
        if self.base > min:
            return True
        return False
    
    def __str__(self):
        return (self.base, self.height)
    
    # Métodos estáticos (@staticmethod)
    @staticmethod
    def iguales_rectangulos(rec1, rec2):
        if rec1.base == rec2.base and rec1.height == rec2.height:
            return True
        return False
    
    # Métodos de clase 
    @classmethod
    def random_rectangulo(cls):
        base = random.randrange(1, 10)
        height = random.randrange(1,10)
        return (cls, base, height)
            

rec1 = Rectangulo(5, 2, 'red')
rec2 = Rectangulo (5, 2, 'red')
rec3 = Rectangulo().random_rectangulo()
print (rec3)
print ('El resultado del perímetro es {}'.format(rec1.perimetro()))
print ('El área del rectángulo es {}'.format(rec1.area()))
print (rec1.is_base_big())
print (Rectangulo.iguales_rectangulos(rec1, rec2))







