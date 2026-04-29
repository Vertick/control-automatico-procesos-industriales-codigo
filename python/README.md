# Notebooks Python

Notebooks Python 3.10 organizados por capítulo del libro. Cada notebook lleva el identificador `CXX_EYY` (capítulo y ejemplo) y produce las figuras y resultados que aparecen en el texto.

## Ejecución

```bash
jupyter lab python/capXX/CXX_EYY_*.ipynb
```

O ejecutar todos los notebooks de un capítulo con `nbclient`:

```python
import nbformat
from nbclient import NotebookClient
from pathlib import Path

for nb_path in Path("python/cap09").glob("*.ipynb"):
    nb = nbformat.read(nb_path, as_version=4)
    client = NotebookClient(nb, timeout=600, kernel_name="python3")
    client.execute()
    print(f"OK {nb_path.name}")
```

## Convenciones

- Datos sintéticos generados internamente con `numpy.random.seed` para reproducibilidad.
- Figuras guardadas opcionalmente en `figures/generated/` (no incluidas por defecto en el repositorio).
- Sin rutas absolutas; sin dependencias de redes externas; sin secretos.
- Cada notebook puede ejecutarse en Google Colab / mybinder con los mismos requirements.

## Cap17 — pseudocódigo

`cap17/C17_E01_patron_asistente.md` es pseudocódigo, no código ejecutable. Documenta el patrón asistente con verificación humana sin invocar LLMs reales.
