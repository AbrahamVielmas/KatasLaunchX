# ejercicio 1
text = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. 
On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

textDividido = text.split('. ')
# print(textDividido)
palabrasbuscar = ["average", "temperature", "distance"]

for parrafo in textDividido:
    for palabra in palabrasbuscar:
        if palabra in parrafo:
            print(parrafo)
            break

for parrafo in textDividido:
    for palabra in palabrasbuscar:
        if palabra in parrafo:
            print(parrafo.replace(' C', ' Celsius'))
            break

print(f"\nSEPARADOR.\n{'*'*80}")

# ejercicio 2
planet = 'Jupiter '
gravity = 0.00143
name = 'Ganímedes'

titulo = f'la gravedad de {name}'.title()


datos = f"""{'-'*80}
Nombre del planeta: {planet}
Gravedad en {name}: {gravity * 1000} m/s2
"""

template = f"""{titulo} 
{datos} 
"""
print(template)
