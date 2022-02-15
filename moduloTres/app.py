# ejercicio 1
# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.
velocidad_asteroide = 49
if velocidad_asteroide > 25:
    print('Cuidado se acerca un asteroide!!!')
else:
    print('Tranquilos estamos todos a salvo.')

# ejercicio 2
# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False
velocidad_asteroide_dos = 19
if velocidad_asteroide_dos > 20:
    print('Voltea arriba talvez veaz un asteroide!')
elif velocidad_asteroide_dos == 20:
    print('Voltea arriba talvez veaz un asteroide!')
else:
    print('Nada nuevo, todo normal.')

# ejercicio tres
# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar
velocidad_asteroide_tres = 25  # kh/s
tamaño_asteroide = 25  # metros
if velocidad_asteroide_tres > 25 and tamaño_asteroide > 25:
    print('Emergencia, un asteroide muy peligroso se aproxima!')
elif velocidad_asteroide_tres >= 20:
    print('Emergencia, un asteroide muy peligroso se aproxima!')
elif tamaño_asteroide < 25:
    print('Sin peligro evidente.')
else:
    print('Sin peligto evidente')
