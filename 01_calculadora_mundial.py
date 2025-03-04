#Pequeña calculadora de fechas.

import datetime
now = datetime.datetime.now()
nextdate = now - datetime.datetime(2026, 6, 11)
print("Para el inicio del próximo mundial faltan:" , nextdate)
# Calcular la diferencia entre dos fechas.