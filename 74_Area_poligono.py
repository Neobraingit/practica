
'''
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
 '''
 
def area(poligono):
     base = float(input('Define el área: '))
     altura = float(input('Define la altura: '))
     
     
     area = base * altura
     
     print ('El área del {} es de {} cm'.format(poligono, area))
     
     
area('Cuadrado')
     