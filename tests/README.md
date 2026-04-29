# Tests

Suite pytest mínima que valida los algoritmos clave del libro:

| Test | Cubre |
|---|---|
| `test_imports.py` | Importaciones reproducibles (numpy, scipy, matplotlib, sympy, control). |
| `test_core_models.py` | Modelos canónicos (FOPDT, segundo orden, integrador). |
| `test_cusum.py` | Algoritmo CUSUM para detección de drift. |
| `test_datasets_exist.py` | Estructura de datos sintéticos. |
| `test_fopdt_fit.py` | Ajuste FOPDT recupera parámetros conocidos. |
| `test_pid_antiwindup.py` | PID con antiwindup reduce sobreoscilación. |
| `test_sensibilities.py` | Identidad S+T=1 a baja frecuencia. |
| `test_sintonias.py` | Coherencia entre Z-N, Lambda y SIMC. |

## Ejecutar

```bash
pip install pytest
pytest -v
```

Resultado esperado: ~45 tests passing, 2 skipped (cvxpy, paho.mqtt — opcionales).
