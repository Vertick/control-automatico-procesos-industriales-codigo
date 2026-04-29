"""Verifica que las dependencias declaradas son importables.

Si este test falla, la instalación del entorno está incompleta. No usa
imports tardíos ni `try/except`: la idea es que un fallo señale
inequívocamente la dependencia ausente.
"""
import importlib
import pytest


CORE = ["numpy", "scipy", "matplotlib", "sympy", "control"]
ML   = ["sklearn"]
OPTIONAL = ["cvxpy", "paho.mqtt"]   # documentadas como opcionales


@pytest.mark.parametrize("mod", CORE)
def test_core_import(mod):
    importlib.import_module(mod)


@pytest.mark.parametrize("mod", ML)
def test_ml_import(mod):
    """sklearn es obligatorio sólo para C15-C16."""
    importlib.import_module(mod)


@pytest.mark.parametrize("mod", OPTIONAL)
def test_optional_imports_dont_break_collection(mod):
    """Las dependencias opcionales pueden faltar; este test sólo
    documenta su carácter no obligatorio sin hacer fallar el suite."""
    try:
        importlib.import_module(mod)
    except ImportError:
        pytest.skip(f"opcional no instalado: {mod}")
