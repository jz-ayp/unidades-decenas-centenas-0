"""
Generar casos de prueba, en formato JSON, para ejercicio de calcular unidades, decenas y centenas, 
omitiendo valores en cero.
"""

import json
from pathlib import Path
from random import randint

PROG = "uni_dec_cen.py"

base_dir = Path(".")
tests_copy_paste = base_dir / "solution" / "test_cases_copy-paste.json"
tests_upload = base_dir / "solution" / "test_cases.json"

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
cases.append((randint(1, 9), 0, 0))
# Sin unidades
cases.append((randint(1, 9), randint(1, 9), 0))
# Caso general
for _ in range(3):
    cases.append((randint(1, 9), randint(1, 9), randint(1, 9)))
# Caso especial extra (> 999)
cases.append((83, 5, 7))

output = {}
tests = []

for i, case in enumerate(cases, start=1):
    c, d, u = case
    n = u + 10 * d + 100 * c
    
    inp = f"{n}"
    centenas = f"Centenas\\b\\D*{c}\\b\\W*" if c > 0 else ""
    decenas = f"Decenas\\b\\D*{d}\\b\\W*" if d > 0 else ""
    unidades = f"Unidades\\b\\D*{u}\\b" if u > 0 else ""

    outp = f"(?i){centenas}{decenas}{unidades}"
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
#tests = {"tests": tests}

# Añadir sangrías extra para copiar en archivo de Classroom 50
clsrm50 = {"assignments": [{"tests": tests}]}

with tests_copy_paste.open("w", encoding="utf-8") as f:
    json.dump(clsrm50, f, indent=2, ensure_ascii=False)

with tests_upload.open("w", encoding="utf-8") as f:
    json.dump(tests, f, indent=2, ensure_ascii=False)
