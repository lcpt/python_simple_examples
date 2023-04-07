import pyparsing
cStr= '"Casco de seguridad con atalaje provisto de 6 puntos de anclaje, para uso normal y eléctrico hasta 440 V", "Casco de seguridad con arnés de cabeza ajustable por medio de rueda dentada, para uso normal y eléctrico hasta 440 V.", "Conjunto formado por casco con atalaje provisto de 6 puntos de anclaje + protectores de oídos acoplables. Según UNE-EN 458, UNE-EN 352", "Casco de seguridad dieléctrico con pantalla para protección de descargas eléctricas (amortizable en 5 usos)", "Casco de seguridad sin ventilar para trabajos verticales, con visera corta para facilitar la visión hacia arriba. Incluye barboquejo de 4 puntos de sujeción. Fabricado en polietileno de alta densidad (PEHD) con resistencia a temperaturas de hasta -30ºC y una resistencia eléctrica de hasta 1000 V. Peso: 375 g. Colores: Blanco y amarillo. Según UNE-EN 397, UNE-EN 50365"'
items= pyparsing.commaSeparatedList.parseString(cStr).asList()
tmp= list()
for item in items:
    tmp.append(item[1:-1])

print(tmp)
