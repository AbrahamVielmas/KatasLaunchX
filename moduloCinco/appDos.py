# aplicacion para trabajar con numeros y entradas de usuario

convercionMilla = float('0.621')

planetaUno = float(input('Distancia del sol primer planeta: '))
planetaDos = float(input('Distancia del sol segundo planeta: '))

distancia = planetaDos - planetaUno

print(f'La distancia en km es: {abs(distancia)}')
print(f'La distancia en Millas es: {abs(distancia * convercionMilla)}')
