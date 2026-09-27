# Entradas
numero = int(input("Introduzca un número: "))

# Proceso
centenas = numero // 100
residuo = numero % 100
decenas = residuo // 10
unidades = residuo % 10

# Salidas
if centenas > 0:
    print(f"Centenas: {centenas}")
if decenas > 0:
    print(f"Decenas: {decenas}")
if unidades > 0:
    print(f"Unidades: {unidades}")
