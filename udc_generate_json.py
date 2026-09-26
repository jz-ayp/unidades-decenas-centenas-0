"""
Generar casos de prueba, en formato JSON, para ejercicio de calcular unidades, decenas y centenas, 
omitiendo valores en cero.
"""

import json
from random import randint

PROG = "uni_dec_cen.py"

cases = []
# Casos especiales:
# Sin centenas
cases.append((0, randint(1, 9), randint(1, 9)))
# Sin centenas ni decenas
cases.append((0, 0, randint(1, 9)))
# Sin centenas ni unidades
cases.append((0, randint(1, 9), 0))
# Sin decenas
cases.append((randint(1, 9), 0, randint(1, 9)))
# Sin decenas ni unidades
cases.append((randint(1, 9), 0, randint(1, 9)))
# Sin unidades
cases.append((randint(1, 9), randint(1, 9), 0))
# Caso general
cases.append((randint(1, 9), randint(1, 9), randint(1, 9)))

output = {}
tests = []

for i, case in enumerate(cases, start=1):
    c, d, u = case
    n = u + 10 * d + 100 * c
    
    inp = f"{n}"
    outp = f"{c}(\n|.)*{d}(\n|.)*{u}"
    name = f"Caso {i}: {n}"
    entry = {
        "name": name,
        "type": "io",
        "run": "python3 " + PROG,
        "points": 10,
        "comparison": "regex",
        "input": inp,
        "expected": outp,
        }
    tests.append(entry)
tests = {"tests": tests}

# Añadir sangrías extra para copiar en archivo de Classroom 50
clsrm50 = {"assignments": [tests]}
with open("test_cases.json", "w") as f:
    json.dump(tests, f, indent=2, ensure_ascii=False)
