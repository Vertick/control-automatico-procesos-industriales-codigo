"""Configuración compartida para los tests del Lote 4."""
import sys
from pathlib import Path
import numpy as np

# Permitir import directo de funciones de los notebooks reutilizables
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
