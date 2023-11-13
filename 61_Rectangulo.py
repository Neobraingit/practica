
class Rectangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return self.base * self.altura
    
rec1 = Rectangulo(5, 2)
print ('El área del rectángulo es {}'.format(rec1.area()))