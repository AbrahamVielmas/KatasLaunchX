# Calculando distancia entre planetas

tierra = float('149597870')  # km
jupiter = float('778547200')  # km


def distanciaPlanetas(valorUno, valorDos):
    distancia = valorDos - valorUno
    return distancia


distancia = distanciaPlanetas(tierra, jupiter)  # son km
distanciaMillas = distancia * float('0.621')

print(f'La distancia entre la Tierra y Jupiter es: {abs(distancia)} Km')
print(
    f'La distancia entre la Tierra y Jupiter es: {abs(distanciaMillas)} Millas')
