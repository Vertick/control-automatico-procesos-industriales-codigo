# Guía de instalación

## Requisitos
- Python 3.10 o superior.
- Sistema operativo: Linux, macOS o Windows.
- Espacio en disco: ~2 GB con todas las dependencias.

## Opción A — conda (recomendada)
```bash
conda env create -f environment.yml
conda activate control-libro
jupyter lab
```

## Opción B — pip + venv
```bash
python3.10 -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
jupyter lab
```

## Verificación
```bash
python -c "import numpy, scipy, matplotlib, sympy, control; print('OK')"
python -c "import sklearn, cvxpy; print('OK ML/MPC')"
```

## MATLAB / Octave
- MATLAB R2022a+ con Control System Toolbox.
- Octave 7+ con paquete `control`.
  ```octave
  pkg install -forge control
  pkg load control
  ```

## Solución de problemas comunes

- **`control` no se instala vía conda**: usar `pip install control` dentro del entorno conda.
- **`cvxpy` falla por solver**: instalar también `ecos` o `scs` (`pip install ecos scs`).
- **`paho-mqtt` no conecta**: confirmar que el broker MQTT local está activo (Mosquitto: `mosquitto -v`). Demo opcional, no necesaria para seguir el libro.
