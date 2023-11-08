#  Calculadora de propina: Calcula la propina en función del monto de la factura y el porcentaje de propina.

print ('La propina ha de ser del 15%')
factura = float(input('Dime de cuanto es la factura: '))
propina = (factura * 15) / 100
print ('La propina corresponde a {} euros.'.format(propina))